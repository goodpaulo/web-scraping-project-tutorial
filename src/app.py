import os
from bs4 import BeautifulSoup
import requests
import time
import sqlite3
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

url = "https://ycharts.com/companies/TSLA/revenues"

response = requests.get(url, time.sleep(1))

if response.status_code != 200:
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    request = requests.get(url, headers = headers)
    time.sleep(10)
    response = request.text

soup = BeautifulSoup(response,"html.parser")

tables = soup.find_all("table")

#tesla_tables = 
print(tables)

price = soup.find("td", class_="text-right")
date = soup.find("td")

#gfg = soup.find_all(lambda tag: tag.name == "strong" and text in tag.text)

tesla_revenue = pd.DataFrame(columns = ["Date", "Revenue"])

for index, table in enumerate(tables):
    if ("Date" in str(table)):
        table_index = index
        break

#for

print(table_index)