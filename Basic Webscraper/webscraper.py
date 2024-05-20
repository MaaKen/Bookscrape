import requests
from bs4 import BeautifulSoup

book_list =[]

for x in range(1,51):
    print(x)
    url = f'https://books.toscrape.com/catalogue/page-{x}.html'

    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    article = soup.find_all ('article', class_ = 'product_pod')

    for book in article:
        title = book.find_all ('a')[1]['title']
        price = book.find ('p', class_ = 'price_color').text[2:]
        inStock = book.find ('p', class_ = 'instock availability').text.strip()
        books = {
            'title': title,
            'price': price,
            'inStock': inStock
        }
        book_list.append(books)

print(len(book_list))
