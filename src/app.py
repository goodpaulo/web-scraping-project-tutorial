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
tables_with_date_header = []

for table in tables:
    # Find all th elements in the thead of the current table
    if table.find('thead') is not None:
        headers = table.find('thead').find_all('th')
    print(headers)
    
    # Check if any header contains the text "Date"
    if any(header.get_text(strip=True) == "Date" for header in headers):
        tables_with_date_header.append(table)

for table in tables:
    if (header.get_text(strip = True) == "Date" for header in headers):
        print(table)

# Print or process the tables with the header "Date"
#for table in tables_with_date_header:
    #print(table.prettify())

price = soup.find("td", class_="text-right")
date = soup.find("td")
tables_with_th = []

# Iterate through each table
for table in tables:
    # Check if there is any <th> element in the table
    if table.find_all('th'):
        tables_with_th.append(table)

# Print or process the tables with <th> elements
for table in tables_with_th:
    print(table.prettify())
#gfg = soup.find_all(lambda tag: tag.name == "strong" and text in tag.text)

tesla_revenue = pd.DataFrame(columns = ["Date", "Revenue"])

for index, table in enumerate(tables):
    if ("Date" in str(table)):
        table_index = index
        break

#for

print(table_index)