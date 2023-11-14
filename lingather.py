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
        print(f"{pathname} not found.\n")
    else:
        try:
            with open(pathname, 'r') as config:
                print(f"{name} - ({pathname})")
                for line in config:
                    print(f"{filename}>>> {line.strip()}")
                print('\n')
        except PermissionError as e:
            print(f"{name} - {pathname}")
            print(e, '\n')


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
print_config("MYSQL CONFIGURATION", "/etc/mysql/my.cnf")
print_config("UFW CONFIGURATION", "/etc/ufw/ufw.conf")
print_config("UFW (SYSCTL) CONFIGURATION", "/etc/ufw/sysctl.conf")
print_config("SECURITY ACCESS CONFIGURATION", "/etc/security.access.conf")
print_config("SHELLS", "/etc/shells")
print_config("PAM_SEPERMIT (SELINUX)", "/etc/security/sepermit.conf")
print_config("CA CERTIFICATES CONFIGURATION", "/etc/ca-certificates.conf")
print_config("ACCESS CONFIGURATION", "/etc/security/access.conf")
print_config("GATED CONFIGURATION", "/etc/gated.conf")
print_config("RPC", "/etc/rpc")
print_config("PSAD", "/etc/psad/psad.conf")
print_config("MYSQL (DEBIAN) CONFIGURATION", "/etc/mysql/debian.cnf")
print_config("CHKROOTKIT CONFIGURATION", "/etc/chkrootkit.conf")
print_config("LOGROTATE CONFIGURATION", "/etc/logrotate.conf")
print_config("RKHUNTER CONFIGURATION", "/etc/rkhunter.conf")
print_config("SAMBA CONFIGURATION", "/etc/samba/smb.conf")
print_config("LDAP CONFIGURATION", "/etc/ldap/ldap.conf")
print_config("OPENLDAP CONFIGURATION", "/etc/openldap/openldap.conf")
print_config("CUPS CONFIGURATION", "/etc/cups/cups.conf")
print_config("XAMP HTTPD CONFIGURATION", "/etc/opt/lampp/etc/httpd.conf")
print_config("SYSCTL CONFIGURATION", "/etc/sysctl.conf")
print_config("PROXYCHAINS CONFIGURATION", "/etc/proxychains4.conf")
print_config("CUPS SNMP CONFIGURATION", "/etc/cups/snmp.conf")
print_config("SENDMAIL CONFIGURATION", "/etc/mail/sendmail.conf")
print_config("SNMP CONFIGURATION", "/etc/snmp/snmp.conf")