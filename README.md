# INET4031 Add Users Script and User List

## Program Description
The **Create Users Script** is an automated Python program designed to simplify the process of adding multiple users to a Linux system. Instead of manually typing long commands to create each user, set passwords, and assign groups, this program does all of that automatically based on data from a formatted input file.  

Normally, a system administrator would have to run commands such as `adduser`, `passwd`, and `adduser <user> <group>` repeatedly for every new account. This script automates those same commands, saving time and minimizing human error. It reads a list of user details, processes each valid line, and executes the appropriate commands to create the users, set their passwords, and place them into their assigned groups.

---

## Program User Operation
After reading this section, the user should understand how to prepare the input file, run the script, and verify the output. The script should be executed in two stages: a **dry run** for testing, and a **live run** for actual system updates.

When running, the program reads the input file line by line. It skips lines that begin with a `#` (comments) or lines that don’t contain enough data fields. For valid entries, it creates the account, sets the password, and assigns the user to one or more groups. The script also prints progress messages to the terminal so the user can easily follow what actions are being taken.

---

### Input File Format
The input file must contain one user per line, with each field separated by colons (`:`).  
Each line includes the following five fields in order:
