import requests
from bs4 import BeautifulSoup


page = requests.get("http://localhost:8000")
soup = BeautifulSoup(page.content, "html.parser")

print(soup.prettify())
