# INET4031 Add Users Script and User List

## Program Description
The Create Users Script is a Python automation tool that helps system administrators easily add multiple users to a Linux system. Instead of manually typing commands to create users, set passwords, and assign groups, this script automates the same process using an input file. It reads the user details, verifies that each line is valid, and executes the appropriate Linux commands to create each account. Normally, administrators would use commands like `adduser`, `passwd`, and `adduser <user> <group>` repeatedly for each account. This program performs those same commands automatically, saving time and reducing the chance of manual errors. It’s an efficient way to manage bulk account creation on a system.

## Program User Operation
This program reads data from a user-provided input file line by line. Each line represents one user and contains their username, password, first and last name, and group information. The script checks for missing data and skips any invalid or commented lines (those beginning with `#`). After reading each valid line, it creates the account, sets the password, and assigns the user to one or more groups. The program also prints confirmation messages for every action so the user can see what’s happening. This section starts with a general overview, followed by detailed subsections explaining how the input file works, how to execute the program, and how to perform a “dry run.”

### Input File Format
The input file contains user data separated by colons (:), with each field representing: 1) Username, 2) Password, 3) Last Name, 4) First Name, and 5) Group(s). Each line corresponds to one user entry that the script will read and process. Example:
