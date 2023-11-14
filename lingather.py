#!/usr/bin/python3
import subprocess
import os
import grp


def distribution(): return subprocess.run(["cat /etc/*issue"], shell=True, capture_output=True)
def whoami(): return os.getlogin()
def user_groups(): return grp.getgrgid(os.getgid())
def uname(): return os.uname()
def interfaces(): return subprocess.run(["ip a"], shell=True, capture_output=True)


def interfaces_ifconfig():
    command = subprocess.run(["ifconfig"], shell=True, capture_output=True)
    if "command not found" in command.stderr.decode().strip():
        return interfaces()
    else:
        return command.stdout.decode().strip()


def routes(): return subprocess.run(["route"], shell=True, capture_output=True)

print(f"""CURRENT SYSTEM INFORMATION
Distribution: {distribution().stdout.decode().strip()}
Uname: {uname().sysname} {uname().nodename} {uname().release} {uname().version} {uname().machine}
""")

print(f"""NETWORK INFORMATION
{interfaces().stdout.decode().strip()}

ROUTES
{routes().stdout.decode().strip()}
""")

print(f"""CURRENT USER INFORMATION
Username: {whoami()}
Groups: {user_groups().gr_name} ({os.getgid()})
""")

print(interfaces_ifconfig())
