import requests
from requests.sessions import Session
from bs4 import BeautifulSoup
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
    quotes = soup.find_all('div', class_='quote')
    for quote in quotes:
        text = quote.find('span', class_='text').get_text()
        author = quote.find('small', class_='author').get_text()
        f.write(f'{text} - {author} \n')
    print(url , " Done!")
with open("quotes.txt", "w", encoding="utf-8") as f:
    for i in range(1, 11):
        scraper(f"http://quotes.toscrape.com/page/{i}/", headers, session, f)
