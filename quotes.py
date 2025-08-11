import requests
from bs4 import BeautifulSoup

def scrape_quotes():
    """Generator that scrapes quotes from quotes.toscrape.com."""
    url = "http://quotes.toscrape.com/page/{}/"
    page = 1
    
    while True:
        res = requests.get(url.format(page))
        if res.status_code != 200:
            break

        soup = BeautifulSoup(res.text, "html.parser")
        quotes = soup.select(".quote")

        if not quotes:
            break

        for quote in quotes:
            text = quote.find("span", class_="text").get_text()
            author = quote.find("small", class_="author").get_text()
            yield {"quote": text, "author": author}

        page += 1
