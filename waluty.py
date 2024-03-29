from optparse import Values
import requests
import csv

response = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
data = response.json()
data2 = data[0]['rates']

column=list((data2[0]).keys()) 

with open('waluty.csv', 'w', newline='') as output_file:
    fc = csv.DictWriter(output_file, delimiter =';' , fieldnames=column)
    fc.writeheader()
    fc.writerows(data2)


kody=[]
kursy=[]
with open("waluty.csv", "r") as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=';')
    for lines in csv_reader:
        kody.append(lines['code'])
        kursy.append(lines['bid'])

waluty_dict = dict(zip(kody, kursy))
print(kody)
symbol = str(input('Wybierz z powyszych symbol waluty do przeliczenia: '))
ilosc = float(input('Podaj ilość waluty do przeliczenia: '))

if symbol in waluty_dict:
    print(f"Wartość sprzedawanej waluty to: ", round((float(waluty_dict[symbol])*ilosc), 2))
else:
    print("nieprawidłowy symbol waluty")
