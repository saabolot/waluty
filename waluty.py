import requests
import csv

response = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
data = response.json()
data2 = data[0]['rates']

column=list((data2[0]).keys()) 

with open('waluty.csv', 'w', newline='') as output_file:
    fc = csv.DictWriter(output_file, fieldnames=column)
    fc.writeheader()
    fc.writerows(data2)
