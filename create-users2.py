#!/usr/bin/python3
# INET4031 – create-users2.py
# Interactive dry-run vs normal run version

import os
import re
import sys

def run_or_print(cmd: str, dry: bool):
    if dry:
        print(f"[DRY RUN] {cmd}")
    else:
        os.system(cmd)

def main():
    # 1) Prompt for dry-run
    ans = input("Would you like to run this in dry-run mode? (Y/N): ").strip().lower()
    dry_run = (ans == 'y')

    for raw in sys.stdin:
        line = raw.rstrip("\n")

        # detect comment lines (start with '#')
        is_comment = re.match(r"^\s*#", line) is not None

        # split fields (colon-delimited)
        fields = line.strip().split(":")

        # Validate record: exactly 5 fields required
        malformed = (len(fields) != 5)

        # 4 & 5) DRY RUN: print messages for invalid or skipped lines
        if dry_run:
            if is_comment:
                print(f"[DRY RUN] Skipping commented line: {line}")
                continue
            if malformed:
                print(f"[DRY RUN] ERROR: Line has missing/extra fields and will be skipped: {line}")
                continue
        else:
            # 7 & 8) NORMAL RUN: do NOT print errors or “skipped” messages—just skip
            if is_comment or malformed:
                continue

        # Safe to unpack now
        username  = fields[0]
        password  = fields[1]
        last_name = fields[2]
        first_name= fields[3]
        groups    = fields[4].split(",")

        # Build GECOS as "First Last"
        gecos = f"{first_name} {last_name}"

        # Create account
        print(f"==> Creating account for {username}...")
        cmd = f"/usr/sbin/adduser --disabled-password --gecos '{gecos}' {username}"
        run_or_print(cmd, dry_run)

        # Set password
        print(f"==> Setting the password for {username}...")
        # Uses passwd with echo feeding two lines (password + confirm)
        cmd = f"/bin/echo -ne '{password}\\n{password}\\n' | /usr/bin/sudo /usr/bin/passwd {username}"
        run_or_print(cmd, dry_run)

        # Group assignments (skip '-' = no groups)
        for grp in groups:
            if grp.strip() == '-' or grp.strip() == '':
                continue
            print(f"==> Assigning {username} to the {grp} group...")
            cmd = f"/usr/sbin/adduser {username} {grp}"
            run_or_print(cmd, dry_run)

if __name__ == "__main__":
    main()

