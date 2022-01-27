import time

import paramiko
import os
import sys


# Get credentials file and verify if exists
credentials_file_path = input("Enter credentials file path and name (e.g. ./myfile.txt): ")
if os.path.isfile(credentials_file_path):
    print("Username/password file '{}' is valid\n".format(credentials_file_path))
else:
    print("File {} does not exist :( Please check and try again.\n".format(credentials_file_path))
    sys.exit()


# Get commands file and verify if exists
commands_file_path = input("Enter commands file path and name (e.g. ./myfile.txt): ")
if os.path.isfile(credentials_file_path):
    print("Commands file '{}' is valid\n".format(commands_file_path))
else:
    print("File {} does not exist :( Please check and try again.\n".format(commands_file_path))
    sys.exit()


# Open SSH connection
def ssh_connection(ip):
    global credentials_file_path
    global commands_file_path

    try:
        # Get credentials (username and password)
        credentials_file = open(credentials_file_path, 'r')
        credentials_file.seek(0)
        username = credentials_file.readlines()[0].split(",")[0].rstrip("\n")
        print("Username: {}".format(username))
        credentials_file.seek(0)
        password = credentials_file.readlines()[0].split(",")[1].rstrip("\n")
        print("Password: {}".format(password))
        credentials_file.close()

        # Get commands
        commands_file = open(commands_file_path, "r")
        commands_file.seek(0)
        commands = commands_file.readlines()
        commands_file.close()
        print("Commands: {}", commands)

        # Create SSH session
        session = paramiko.SSHClient()
        session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        session.connect(ip.rstrip("\n"), username=username, password=password)

        # Creating SSH connection
        connection = session.invoke_shell()
        for command in commands:
            print("Sending command: {}\n".format(command))
            connection.send(command + "\n")
            time.sleep(2)

        router_output = connection.recv(65535)
        print(str(router_output) + "\n")

        # Close SSH connection
        session.close()
    except paramiko.AuthenticationException:
        print("Invalid credentials\n")
