# INET4031 Add Users Script and User List

## Program Description
The Create Users Script is a Python automation tool that helps system administrators easily add multiple users to a Linux system. Instead of manually typing commands to create users, set passwords, and assign groups, this script automates the same process using an input file. It reads the user details, verifies that each line is valid, and executes the appropriate Linux commands to create each account. Normally, administrators would use commands like `adduser`, `passwd`, and `adduser <user> <group>` repeatedly for each account. This program performs those same commands automatically, saving time and reducing the chance of manual errors. It’s an efficient way to manage bulk account creation on a system.

## Program User Operation
This program reads data from a user-provided input file line by line. Each line represents one user and contains their username, password, first and last name, and group information. The script checks for missing data and skips any invalid or commented lines (those beginning with `#`). After reading each valid line, it creates the account, sets the password, and assigns the user to one or more groups. The program also prints confirmation messages for every action so the user can see what’s happening. This section starts with a general overview, followed by detailed subsections explaining how the input file works, how to execute the program, and how to perform a “dry run.”

### Input File Format
The input file contains user data separated by colons (:), with each field representing: 1) Username, 2) Password, 3) Last Name, 4) First Name, and 5) Group(s). Each line corresponds to one user entry that the script will read and process. Example:

### Command execution: 
The command execution process is straightforward and mirrors typical Linux system administration tasks. Once the script has been made executable using chmod +x create-users.py, it can be run by redirecting input from the create-users.input file with the command ./create-users.py < create-users.input. This tells the program to read user data from the input file and process it line by line. Each valid entry triggers commands to create a new user, set their password, and assign them to the appropriate group or groups. If administrative privileges are required, the script can be run with sudo to ensure it has the necessary permissions. Throughout execution, the program prints clear status messages to confirm which users are being created and what actions are being performed, allowing the administrator to monitor progress in real time.

### Dry Run:
During a dry run, the program prints messages showing what commands would have been executed if it were a live run. This is used to verify that the logic and formatting of the input file are correct. Once the dry run output looks good, the user can remove the comment symbols to enable full execution and perform real user creation.

