#!/usr/bin/python3

# INET 4031
# Ryan Bondoc
# Data Created
# Date Last Modified

# os is used to run system commands addusr passwd etc
# re is used to identify comment lines
# sys is used to read lines from input

import os
import re
import sys

def main():
	for line in sys.stdin:
		print("Reading line:", repr(line))

		# skip lines that start with #
		match = re.match("^#", line)

		# remove extra white space and split the line by : into 5 expected fields
		fields = line.strip().split(':')

		# if the line is a comment or doesnt have exactly 5 fields then skip
		if match or len(fields) != 5:
			continue

		# extract user details from fields
		username = fields[0]
		password = fields[1]

		# gecos is a string with the users full name and other info
		gecos = "%s %s,,," % (fields[3], fields[2])

		# split the group field into a list of groups
		groups = fields[4].split(',')

		# print message to show account creation is starting
		print("==> Creating account for %s,,," % (username))

		#construct the adduser command with disabled password and gecos info
		cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos, username)

		# run the command
		# print cmd
		os.system(cmd)

		#print  message to show password is set
		print("==> Setting the password for %s,,," % (username))

		# set password using echo and passwd pipes through sudo
		cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password, password, username)

		# run the command
		# print cmd
		os.system(cmd)

		#for each group the user should be in
		for group in groups:
		# if the group is not - assign user to group
			if group != '-':
				print("==> Assigning %s to the %s group..." % (username, group))
				cmd = "/usr/sbin/adduser %s %s" % (username, group)

				# run commmand
				# print cmd
				os.system(cmd)
# run main function when the script is executed
if __name__ == '__main__':
	main()
