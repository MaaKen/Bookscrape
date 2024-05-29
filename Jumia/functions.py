import requests
from bs4 import BeautifulSoup

def get_price(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    price = soup.find('div', class_ = 'prc').text.strip()
    return price

print(get_price('https://www.jumia.co.ke/mlp-black-friday-h-entertainment-center/complete-home-theater-systems/?sort=lowest-price&page=2#catalog-listing'))
