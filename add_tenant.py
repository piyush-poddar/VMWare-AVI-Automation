import requests

session = requests.Session()
login = session.post("https://35.200.176.139/login", verify=False, data={'username': '', 'password': ''})
print(login.status_code)

csrf_token = session.cookies.get("csrftoken")

headers = {
    "Content-Type": "application/json",
    "X-Avi-Version": "30.2.3",
    "X-CSRFToken": csrf_token,
    "Referer": "https://35.200.176.139/"
    }

payload = {
    "name": "your_name",
}

post_tenant = session.post("https://35.200.176.139/api/tenant", headers=headers, json=payload, verify=False)
print(post_tenant.status_code)
print(post_tenant.json())