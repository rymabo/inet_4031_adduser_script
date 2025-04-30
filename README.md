# User creating automation script

## Description
This python script (create-users.py) automates the process of creating user accounts on an Ubuntu system. It reads user account information from an input file ('create-users.input) and uses system commands to add users, set passwords, and assign them to groups. This is useful for sysadmins managing many users across multiple systems.

## How it works
# This script expects an input file with the following format: username:password:last_name:first_name:group1,group2
