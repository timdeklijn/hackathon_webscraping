import requests

html = requests.get("http://localhost:8000")

print("*" * 80)
print("status code:\n", html.status_code)
print("*" * 80)
print("text:\n", html.text)
print("*" * 80)
print("content    :\n", html.content)
print("*" * 80)
