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
    if "not found" in command.stderr.decode().strip():
        return interfaces()
    else:
        return command


def routes(): return subprocess.run(["netstat -rn"], shell=True, capture_output=True)
def netstat(): return subprocess.run(["netstat -anpt"], shell=True, capture_output=True)
def processes(): return subprocess.run(["ps aux"], shell=True, capture_output=True)
def environment(): return subprocess.run(["env"], shell=True, capture_output=True)


print(f"""CURRENT SYSTEM INFORMATION
Distribution: {distribution().stdout.decode().strip()}
{uname().sysname} {uname().nodename} {uname().release} {uname().version} {uname().machine}
""")

print(f"""CURRENT USER INFORMATION
Username: {whoami()}
Groups: {user_groups().gr_name} ({os.getgid()})
""")

print(f"""NETWORK INFORMATION
{interfaces_ifconfig().stdout.decode().strip()}
""")

print(f"""ROUTES
{routes().stdout.decode().strip()}
""")

print(f"""NETSTAT
{netstat().stdout.decode().strip()}
""")

print(f"""RUNNING PROCESSES
{processes().stdout.decode().strip()}
""")

print(f"""ENVIRONMENT
{environment().stdout.decode().strip()}
""")
