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
	#Ask User if they want to do a dry run
	dry_run_input = input("Would you like to run in dry-run mode? (Y/N): ").strip().lower()
	dry_run = dry_run_input == 'y'


	print("\nStarting script... Dry-run mode is", "ON" if dry_run else "OFF")

	for line in sys.stdin:
		match = re.match("^#", line)
		fields = line.strip().split(':')

		if match or len(fields) !=5:
			if dry_run:
				print("Skipped line (comment or invalid):", line.strip())
			continue

		username = fields[0]
		password = fields[1]
		gecos = "%s %s ,,," % (fields[3], fields[2])
		groups = fields[4].split(',')

		print(f"\n==> Creating account for {username}...")

		cmd = f"/usr/sbin/adduser --disabled-password --gecos '{gecos}' {username}"
		if dry_run:
			print("[Dry-Run] Would run:", cmd)
		else:
			os.system(cmd)

		for group in groups:
			if group != '-':
				print(f"==> Assigning {username} to group {group}...")
				cmd = f"/usr/sbin/adduser {username} {group}"
				if dry_run:
					print("[Dry-Run] Would run:", cmd)
				else:
					os.system(cmd)




# run main function when the script is executed
if __name__ == '__main__':
	main()
