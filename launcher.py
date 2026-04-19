import requests
import json
from base64 import b64encode
from pathlib import Path

headers = {
    'Content-Type': 'application/json',
}

json_data = {
    'token': '',
    'content': '',
}

file = Path("token.json").read_text()

print("Checking if token is saved...")

if "token" in file:
	print("It appears you've already inputted your token! Moving on...")
else:
	print("No token found...")
	print("Enter token here:")
	key = input()
	print("Token is: " + key)
	json_data.update({"token": key})

filename = "token.json"
with open(filename, "w") as f:
	f.write(json.dumps(json_data))

def check_status_length(message):
	length = len(message)
	if length > 500:
		return "Status must be under 500 characters."
	else:
		return "Successfully submitted your post."

print("Enter content here:")
message = input()
print("Content is: " + message)
json_data.update({"content": message})
response = requests.post('https://hjonk.me/api/token/post/create/', headers=headers, json=json_data)
print(response.status_code)


