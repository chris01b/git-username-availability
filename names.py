import argparse
import requests

parser = argparse.ArgumentParser(description='Check availible Github usernames')
parser.add_argument('usernames', help='username to check')
parser.add_argument('--source','-s', action='store_true', help='check usernames from file')
args = parser.parse_args()

reserved = [line.rstrip('\n') for line in open("reserved-usernames.txt")]

def isUp(username):
	statusCode = requests.get('https://api.github.com/users/' + username).status_code
	if username in reserved:
			print("Taken")
	elif statusCode == 404:
		print("Available")
	elif statusCode == 200:
		print("Taken")
	elif statusCode != 404 or 200:
		raise ValueError("Unexpected statuscode")

if args.source:
	content = [line.rstrip('\n') for line in open(args.usernames)]
	for username in content:
		print(username.upper() + ":")
		isUp(username)
		print("")
else:
	isUp(args.usernames)