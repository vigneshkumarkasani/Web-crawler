import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

def is_valid(url):
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)

def get_all_links(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    links = [urljoin(url, a['href']) for a in soup.find_all('a', href=True)]
    return [link for link in links if is_valid(link)]

def crawl(url, max_pages=100, visited=None):
    if visited is None:
        visited = set()

    visited.add(url)
    print(f"Crawling {url}...")

    for link in get_all_links(url):
        if link not in visited and max_pages > 0:
            crawl(link, max_pages - 1, visited)

    print(f"Crawled {len(visited)} pages.")

if __name__ == "__main__":
    start_url = input("Enter the starting URL: ")
    crawl(start_url)

