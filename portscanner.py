#!/usr/bin/python3

import socket
import sys
import time

usage="python3 pscan.py <TARGET> <START_PORT> <END_PORT>"

if(len(sys.argv) != 4):
    print(usage)
    sys.exit()

try:
    target = socket.gethostbyname(sys.argv[1])
except socket.gaierror:
    print("name resolution error")
    sys.exit()

start_port=int(sys.argv[2])
end_port=int(sys.argv[3])

for port in range(start_port,end_port+1):
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    if not s.connect_ex((target,port)):
        print("Port",port,"is OPEN")