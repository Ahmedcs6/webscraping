import requests
from requests.sessions import Session
from bs4 import BeautifulSoup
import csv
session = requests.Session()
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:139.0) Gecko/20100101 Firefox/139.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5"
}
def scraper(url, headers, session, f):
    re = session.get(url,headers=headers)
    if(re.status_code != 200):
        print("Error: ", re.status_code)
        return
    soup = BeautifulSoup(re.content, 'html.parser')
    books = soup.find_all('li', class_='col-xs-6 col-sm-4 col-md-3 col-lg-3')
    titles = []
    prices = []
    status = []
    for book in books:
        titles.append(book.h3.a['title'])
        prices.append(book.find('p', class_='price_color').get_text())
        status.append(book.find('p', class_='instock availability').get_text().strip())
    for i in range(len(titles)):
        f.writerow([titles[i], prices[i], status[i]])
    print(url , " Done!")
with open("books.csv", "w", encoding="utf-8", newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Price", "Status"])
    for i in range(1, 51):
        scraper(f"http://books.toscrape.com/catalogue/page-{i}.html", headers, session, writer)
