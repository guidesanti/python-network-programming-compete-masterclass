import threading
import sys
import os.path
import subprocess


# Create threads
def create_threads(ips, function):
    threads = []

    for ip in ips:
        th = threading.Thread(target=function, args=(ip,))  # args is a tuple with a single element
        th.start()
        threads.append(th)

    for th in threads:
        th.join()


# Check IP address file and content validity
# Return the IPs within the file as a list
def get_ips_from_file(ips_file_path):
    # Check if the file exists
    if os.path.isfile(ips_file_path):
        print("IP file is valid\n")
    else:
        print("File {} does not exist!\n", ips_file_path)
        sys.exit()

    # Open IP file and read the IP list
    ip_file = open(ips_file_path, "r")
    ip_file.seek(0)
    ips = ip_file.readlines()
    ip_file.close()

    return ips


# Check IP octets
def is_ips_valid(ips):
    for ip in ips:
        ip = ip.rstrip("\n")
        octets = ip.split(".")
        if (len(octets) == 4) and (1 <= int(octets[0]) <= 223) and (int(octets[0]) != 127) and (
                int(octets[0]) != 169 or int(octets[1]) != 254) and (
                0 <= int(octets[1]) <= 255 and 0 <= int(octets[2]) <= 255 and 0 <= int(octets[3]) <= 255):
            continue
        else:
            print("There was an invalid IP address in the file: {}\n", format(ip))
            sys.exit()


# Check IPs reachability
def check_ips_reachable(ips):
    for ip in ips:
        ip = ip.rstrip("\n")

        ping_reply = subprocess.call("ping %s -c 2" % ip, shell=True, stdout=subprocess.DEVNULL,
                                     stderr=subprocess.DEVNULL)

        if ping_reply == 0:
            print("{} is reachable\n".format(ip))
            continue
        else:
            print("{} is not reachable, check connectivity and try again.\n".format(ip))
            sys.exit()
