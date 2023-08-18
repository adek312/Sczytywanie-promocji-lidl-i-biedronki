######  BIEDRONKA   #########
from bs4 import BeautifulSoup
import requests
import itertools

html_text = requests.get('https://www.biedronka.pl/pl/biedronkowe-oszczednosci-17-08').text
soup = BeautifulSoup(html_text, 'lxml')
products = soup.find_all('div', id='container')



for product in products:
    item = product.find_all("h4", class_='tile-name')
    pln = product.find_all("span", class_="pln")
    gr = product.find_all("span", class_="gr")
    jaka = product.find_all("span", class_="product-promo-text")
    for (items, plns, grs, jakas) in zip(item,pln,gr,jaka):
        print(f"Produkt: {items.text}")
        print(f"Cena: {plns.text}, ", end="")
        print(f"{grs.text}")
        print(f"Typ promocji:{jakas.text}")