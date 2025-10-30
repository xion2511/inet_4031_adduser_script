#!/usr/bin/python3
# INET4031 – Managing Access
# Author: Ethan Xiong
# Created: 2025-10-30
# Last Modified: 2025-10-30
#
# Program summary:
# Reads colon-delimited user records from standard input and (1) creates the
# account, (2) sets the password, and (3) assigns the account to one or more
# groups. Lines beginning with "#" are treated as comments and skipped. Lines
# that do not contain exactly five fields are also skipped to avoid bad input.

import os   # Run OS commands like adduser/passwd and group assignment via os.system()
import re   # Use regular expressions to detect commented lines (e.g., lines starting with '#')
import sys  # Access sys.stdin so the script can read the input file via shell redirection

def main():
    for line in sys.stdin:
        # This regular expression looks for a '#' at the very start of the line.
        # If present, the line is considered a comment so the record should be ignored.
        match = re.match(r"^\s*#", line)

        # Split the incoming record on ':' because the input file is colon-delimited.
        fields = line.strip().split(':')

        # Skip processing if the line is a comment OR the record is malformed.
        # We expect exactly five fields: username, password, last, first, groups.
        # If len(fields) != 5, continuing prevents index errors later in the script.
        if match or len(fields) != 5:
            continue

        # Pull out each field into named variables for clarity and easier use below.
        # The GECOS field in /etc/passwd typically stores human-friendly info
        # such as "First Last", so we build that from the input.
        username = fields[0]
        password = fields[1]
        gecos = "%s %s" % (fields[3], fields[2])   # first + last -> "First Last"

        # The groups column itself can contain a comma-separated sublist.
        # Split it so we can iterate and add the user to multiple groups.
        groups = fields[4].split(',')

        # --- Account creation step ---
        # Print for visibility (and to support “dry run”); the cmd variable then holds
        # the exact command we would execute to create the user without an initial password.
        print("==> Creating account for %s..." % (username))
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos, username)
        # In dry-run: keep os.system(cmd) commented. In real-run: uncomment it.
        # print(cmd)
        os.system(cmd)

        # --- Password set step ---
        # Print a status line, then build the command that sets the password.
        # The echo pipeline feeds the password twice to passwd to satisfy confirmation.
        print("==> Setting the password for %s..." % (username))
        cmd = "/bin/echo -ne '%s\n%s\n' | /usr/bin/sudo /usr/bin/passwd %s" % (password, password, username)
        # print(cmd)
        os.system(cmd)

        # --- Group membership step ---
        # Iterate each target group. A lone '-' means “no groups” so we skip it.
        for group in groups:
            # If group is '-', nothing to do for this user.
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username, group))
                cmd = "/usr/sbin/adduser %s %s" % (username, group)
                # print(cmd)
                os.system(cmd)

if __name__ == "__main__":
    main()
