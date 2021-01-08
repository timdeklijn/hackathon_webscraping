import requests
from bs4 import BeautifulSoup
import pandas as pd


page = requests.get("http://localhost:8000")
soup = BeautifulSoup(page.content, "html.parser")

table = soup.find("table", {"class": "age-table"})
df = pd.read_html(str(table))[0]
print(df.head())
