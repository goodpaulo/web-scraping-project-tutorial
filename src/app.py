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
tables_with_th = []
tables_body = []

tr = soup.find_all('tr')

# Iterate through each table
for table in tables:
    # Check if there is any <th> element in the table
    if table.find_all('th'):
        tables_with_th.append(table)

counter = 0
for table in tables_with_th:
    if table.find_all("td"):
        tables_body.append(table.find_all("td"))

print(tables_body)


tesla_revenue = pd.DataFrame(columns = ["Date", "Revenue"])

revenue_list = []
date_list = []

for table in tables_body:
    Date = ""
    Revenue = ""
    for i, value in enumerate(table):
        if i == 0 or (i % 2 == 0):
            Date = value.text
            date_list.append(Date)
        else:
            Revenue = str(value.text).replace("\n", "").replace(" ", "")
            revenue_list.append(float(Revenue[:-1]))
            tesla_revenue = pd.concat([tesla_revenue, pd.DataFrame({
            "Date": Date,
            "Revenue": Revenue
        }, index = [0])], ignore_index = True)
            Date = ""
            Revenue = ""
            



print(tesla_revenue.head())

connection = sqlite3.connect("tesla.db")

connection

cursor = connection.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS revenue (Date, Revenue)""")

tesla_tuples = list(tesla_revenue.to_records(index = False))
tesla_tuples[:5]

def is_database_empty():
    # Query to count the number of tables
    cursor.execute("SELECT COUNT(*) FROM sqlite_master WHERE type = 'table'")
    table_count = cursor.fetchone()[0]
    
    return table_count == 0

# Usage
db_path = 'your_database.db'
if is_database_empty():
    print("The database is empty.")
else:
    cursor.executemany("INSERT INTO revenue VALUES (?,?)", tesla_tuples)
    connection.commit()



for row in cursor.execute("SELECT * FROM revenue"):
    print(row)

print(tables_body)