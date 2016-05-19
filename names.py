import argparse
import requests

parser = argparse.ArgumentParser(description='Check availible Github usernames.')
parser.add_argument('usernames')
parser.add_argument('--source','-s', action='store_true')
args = parser.parse_args()

def isUp(username):
	statusCode = requests.get('https://api.github.com/users/' + username).status_code
	if statusCode == 404:
		code = False
		print("Available")
	elif statusCode == 200:
		code = True
		print("Taken")
	elif statusCode != 404 or 200:
		raise ValueError("Unexpected statuscode")
	return code

if args.source:
	content = [line.rstrip('\n') for line in open(args.usernames)]
	for username in content:
		isUp(username)
else:
	isUp(args.usernames)