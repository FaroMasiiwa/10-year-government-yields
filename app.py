#Imports

import requests
from bs4 import BeautifulSoup
import csv
import  re


url = 'https://markets.ft.com/data/bonds/government-bonds-spreads'

response = requests.get(url)
content = response.content

soup = BeautifulSoup(content, "html.parser")



table = soup.find('tbody')


data =[]

print(type(data))
for row in table.findAll('tr'):
    if len(re.split(r'(\d\.\d+)',row.text.split('%')[0],0)) == 0:
       continue
    else:
       res = re.split(r'(\d\.\d+)',row.text.split('%')[0],0)

    print(res[1])
    
    
    







# Open a file for writing in CSV format
with open('data.csv', '+a', newline='') as csvfile:
  writer = csv.writer(csvfile)
  
  # Write the data as separate rows
  for row in data:
    writer.writerow(row.split('+'))

print("CSV file created successfully!")




