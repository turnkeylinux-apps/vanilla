#!/usr/bin/python3
"""Set Vanilla admin password and email

Option:
    --pass=     unless provided, will ask interactively
    --email=    unless provided, will ask interactively

"""

import re
import sys
import getopt
from libinithooks import inithooks_cache
import subprocess
from subprocess import PIPE
from os.path import *

from libinithooks.dialog_wrapper import Dialog
from mysqlconf import MySQL

def usage(s=None):
    if s:
        print("Error:", s, file=sys.stderr)
    print("Syntax: %s [options]" % sys.argv[0], file=sys.stderr)
    print(__doc__, file=sys.stderr)
    sys.exit(1)

def main():
    try:
        opts, args = getopt.gnu_getopt(sys.argv[1:], "h",
                                       ['help', 'pass=', 'email='])
    except getopt.GetoptError as e:
        usage(e)

    password = ""
    email = ""
    for opt, val in opts:
        if opt in ('-h', '--help'):
            usage()
        elif opt == '--pass':
            password = val
        elif opt == '--email':
            email = val

    if not password:
        d = Dialog('TurnKey Linux - First boot configuration')
        password = d.get_password(
            "Vanilla Password",
            "Enter new password for the Vanilla 'admin' account.")

    if not email:
        if 'd' not in locals():
            d = Dialog('TurnKey Linux - First boot configuration')

        email = d.get_email(
            "Vanilla Email",
            "Enter email address for the Vanilla 'admin' account.",
            "admin@example.com")

    inithooks_cache.write('APP_EMAIL', email)

    command = ["php", join(dirname(__file__), 'vanilla_pass.php'), password]
    p = subprocess.Popen(command, stdin=PIPE, stdout=PIPE, shell=False)
    stdout, stderr = p.communicate()
    if stderr:
        fatal(stderr)

    cryptpass = stdout.strip()

    m = MySQL()
    m.execute('UPDATE vanilla.GDN_User SET Password=%s WHERE Name=\"admin\";', (cryptpass,))
    m.execute('UPDATE vanilla.GDN_User SET Email=%s WHERE Name=\"admin\";', (email,))

    CONFIG="/var/www/vanilla/conf/config.php"
    with open(CONFIG, 'r') as fob:
        old = fob.read()
    new = re.sub("\['SupportAddress.*;", "['SupportAddress'] = '%s';" % email, old)
    with open(CONFIG, 'w') as fob:
        fob.write(new)

if __name__ == "__main__":
    main()

