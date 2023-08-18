########    LIDL    ##########

from bs4 import BeautifulSoup
import requests
import itertools

URL = requests.get("https://www.lidl.pl/q/query/wyprzedaz").text
soup = BeautifulSoup(URL, 'lxml')
products = soup.find_all('section',class_='s-content')

for product in products:
    item = product.find_all('h2', class_='grid-box__headline grid-box__text--dense')
    price = product.find_all('div', class_="m-price__price m-price__price--small")
    for (items, prices) in zip(item, price):
        print(f"Produkt: {items.text.strip()}")
        print(f"Cena: {prices.text.strip()}")