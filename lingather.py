#!/usr/bin/python3
import subprocess
import os
import grp
import pathlib


def print_config(name: str, path: str) -> None:
    pathname = pathlib.Path(path)
    filename = pathlib.Path(path).name
    if not pathlib.Path.exists(pathname):
        print(f"{name} - {pathname}")
        print(f"{path} not found.")
    else:
        with open(path, 'r') as config:
            print(f"{name} - ({pathname})")
            for line in config:
                print(f"{filename}>>> {line.strip()}")
            print('\n')


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

# APACHE CONFIGURATION
print_config("APACHE2 CONFIGURATION", "/etc/apache2/apache2.conf")
print_config("APACHE2 PORTS CONFIGURATION", "/etc/apache2/ports.conf")
print_config("NGINX CONFIGURATION", "/etc/nginx/nginx.conf")
print_config("SNORT CONFIGURATION", "/etc/snort/snort.conf")