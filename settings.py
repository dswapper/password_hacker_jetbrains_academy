import sys
import os

BUFF_SIZE = 2048

args = sys.argv
hostname = args[1].strip()
port = int(args[2].strip())

with open('logins.txt') as f:
    login_base = f.readlines()

for i in range(len(login_base)):
    login_base[i] = login_base[i].strip()
