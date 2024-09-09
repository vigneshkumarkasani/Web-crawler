import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

def is_valid(url):
    """Check if the URL is valid."""
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)

def get_all_links(url):
    """Extract and validate all links from a given URL."""
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        soup = BeautifulSoup(response.text, 'html.parser')
        links = [urljoin(url, a['href']) for a in soup.find_all('a', href=True)]
        return [link for link in links if is_valid(link)]
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return []

def crawl(url, max_pages=100, visited=None):
    """Crawl the web starting from the given URL."""
    if visited is None:
        visited = set()

    if max_pages <= 0:
        return

    visited.add(url)
    print(f"Crawling {url}...")

    links = get_all_links(url)
    print(f"Found {len(links)} links on {url}.")

    for link in links:
        if link not in visited:
            crawl(link, max_pages - 1, visited)

    print(f"Crawled {len(visited)} pages.")

if __name__ == "__main__":
    start_url = input("Enter the starting URL: ")
    crawl(start_url)
