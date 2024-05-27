import requests
from bs4 import BeautifulSoup
import time
import pandas as pd

url = 'https://jiji.co.ke/cars?period&price_min=500000&price_max=1000000'
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')

content = soup.find_all('div', class_ = 'b-list-advert__gallery__item js-advert-list-item')

forSaleCars = []

for car in content:
    name = car.find('div', class_ ="b-advert-title-inner qa-advert-title b-advert-title-inner--div") .text.strip()
    price = car.find('div', class_ = 'qa-advert-price').text.strip()
    spec = car.find('div', class_ = 'b-list-advert-base__item-attr').text.strip()
    transmission = car.find_all('div', class_ = 'b-list-advert-base__item-attr') [1] .text.strip()

    car_info = {
        'name' : name,
        'price': price,
        'spec': spec,
        'transmission': transmission
    }
    forSaleCars.append(car_info)
print('Cars for Sale found:', len(forSaleCars))
time.sleep(2)
      
df = pd.DataFrame(forSaleCars)
print(df.head())

df.to_csv('CarsforSale.csv')


