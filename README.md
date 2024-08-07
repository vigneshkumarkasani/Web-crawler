
# Web Crawler

A simple web crawler built with Python that explores and retrieves pages from a given starting URL. This crawler follows links within the website, respecting basic crawling limits.

## Features

- **Crawls Web Pages**: Automatically retrieves and processes linked pages starting from a specified URL.
- **Recursion**: Follows links to a specified depth or number of pages.
- **Link Validation**: Ensures that only valid URLs are processed.

## Requirements

- Python 3.x
- `requests` library
- `beautifulsoup4` library

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/web-crawler.git
   cd web-crawler
   ```

2. **Install Dependencies**

   You can use `pip` to install the required libraries. It's recommended to use a virtual environment for Python projects.

   ```bash
   pip install requests beautifulsoup4
   ```

## Usage

1. **Run the Crawler**

   To start crawling, execute the script and provide the starting URL when prompted.

   ```bash
   python crawler.py
   ```

2. **Input**

   You will be prompted to enter the starting URL for the crawler.

   ```text
   Enter the starting URL: http://example.com
   ```

## Example

When you run the script, it will print out the URLs it is crawling and the total number of pages crawled:

```text
Crawling http://example.com...
Crawling http://example.com/page1...
Crawling http://example.com/page2...
Crawled 5 pages.
```

## Code Overview

- `is_valid(url)`: Checks if the URL is valid and well-formed.
- `get_all_links(url)`: Retrieves all links from the given URL, returning only valid URLs.
- `crawl(url, max_pages=100, visited=None)`: Recursively crawls the website, starting from the given URL, until the `max_pages` limit is reached or all links are visited.

## Notes

- This script does not handle request errors or HTTP status codes other than 200. Consider adding error handling for production use.
- The crawler is basic and does not respect `robots.txt`. Use it responsibly and consider implementing `robots.txt` checking if you intend to use it on various websites.

---

Feel free to adjust the content to better fit your project’s specifics or to add any additional information you deem necessary.
