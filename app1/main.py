#!/usr/bin/python3
import sys

from helper import create_threads
from helper import get_ips_from_file
from helper import is_ips_valid
from helper import check_ips_reachable
from ssh_connection import ssh_connection

# Read IPs file
ips_file = input("Enter IP file path and name (e.g. D:\MyApps\myfile.txt): ")
print("Reading IPs from '{}' \n".format(ips_file))

try:
    ips = get_ips_from_file(ips_file)
    is_ips_valid(ips)
    check_ips_reachable(ips)
except KeyboardInterrupt:
    print("Program aborted \n")
    sys.exit()

create_threads(ips, ssh_connection)
