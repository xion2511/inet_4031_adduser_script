#!/usr/bin/python3
# INET4031 – create-users2.py
# Interactive version of the user creation script
# This version allows the user to choose between a “dry-run” (testing mode)
# and a “normal” run that actually creates accounts.
# The dry-run option helps verify logic and prevent accidental user creation.

import os
import re
import sys

# Helper function that decides whether to actually run the command
# or just print it, based on whether the dry-run mode is enabled.
def run_or_print(cmd: str, dry: bool):
    if dry:
        # If dry-run mode is active, print what would have run
        print(f"[DRY RUN] {cmd}")
    else:
        # Otherwise, execute the command normally
        os.system(cmd)

def main():
    # Ask the user if they want to run this script in “dry-run” mode.
    # Dry-run mode allows testing the code without modifying the system.
    ans = input("Would you like to run this in dry-run mode? (Y/N): ").strip().lower()
    dry_run = (ans == 'y')  # True if 'Y', False if 'N'

    # The script reads each line of the input file (create-users.input)
    for raw in sys.stdin:
        line = raw.rstrip("\n")

        # Lines that begin with "#" are comments and should be skipped.
        # This uses regex to check if a line starts with "#".
        is_comment = re.match(r"^\s*#", line) is not None

        # Each valid input line should contain exactly 5 fields separated by colons.
        fields = line.strip().split(":")
        malformed = (len(fields) != 5)

        # If we’re in dry-run mode, we display messages instead of taking real action.
        if dry_run:
            if is_comment:
                print(f"[DRY RUN] Skipping commented line: {line}")
                continue
            if malformed:
                print(f"[DRY RUN] ERROR: Line has missing/extra fields and will be skipped: {line}")
                continue
        else:
            # In normal mode, skip malformed or commented lines silently (no prints)
            if is_comment or malformed:
                continue

        # Extract the expected five fields
        username = fields[0]
        password = fields[1]
        last_name = fields[2]
        first_name = fields[3]
        groups = fields[4].split(",")

        # Combine first and last names for the GECOS field
        gecos = f"{first_name} {last_name}"

        # Create the user account
        print(f"==> Creating account for {username}...")
        cmd = f"/usr/sbin/adduser --disabled-password --gecos '{gecos}' {username}"
        run_or_print(cmd, dry_run)

        # Set the user's password
        print(f"==> Setting the password for {username}...")
        cmd = f"/bin/echo -ne '{password}\\n{password}\\n' | /usr/bin/sudo /usr/bin/passwd {username}"
        run_or_print(cmd, dry_run)

        # Add the user to any listed groups, unless it’s marked with “-”
        for grp in groups:
            if grp.strip() == '-' or grp.strip() == '':
                continue
            print(f"==> Assigning {username} to the {grp} group...")
            cmd = f"/usr/sbin/adduser {username} {grp}"
            run_or_print(cmd, dry_run)

if __name__ == "__main__":
    main()

