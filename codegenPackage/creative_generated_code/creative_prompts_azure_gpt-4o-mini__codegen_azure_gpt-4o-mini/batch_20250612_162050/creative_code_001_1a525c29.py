"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thedigitalage.co.nz
Prompt: Write a Python script that utilizes SEO best practices to optimize a website for better search engine rankings, as outlined by The Digital Age.
Generated: DETERMINISTIC_1a525c294f51d9a7
Batch ID: 20250612_162050
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://example.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import requests
from bs4 import BeautifulSoup
import logging
from urllib.parse import urlparse, urljoin

# Configure logging for error tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SEOOptimizer:
    """
    A class to optimize a website for better search engine rankings.
    """

    def __init__(self, base_url):
        """
        Initializes the SEOOptimizer with a base URL.

        :param base_url: The URL of the website to optimize.
        """
        self.base_url = base_url
        self.visited_urls = set()

    def fetch_page(self, url):
        """
        Fetches the HTML content of a page.

        :param url: The URL of the page to fetch.
        :return: The HTML content of the page, or None if an error occurs.
        """
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for bad responses
            return response.text
        except requests.RequestException as e:
            logging.error(f'Error fetching {url}: {e}')
            return None

    def parse_content(self, html):
        """
        Parses the HTML content to extract SEO-relevant data.

        :param html: The HTML content to parse.
        :return: A dictionary containing SEO data.
        """
        soup = BeautifulSoup(html, 'html.parser')
        
        # Extract title, description, and keywords
        title = soup.title.string if soup.title else "No title found"
        description = self.get_meta_content(soup, 'description')
        keywords = self.get_meta_content(soup, 'keywords')

        return {
            'title': title,
            'description': description,
            'keywords': keywords
        }

    def get_meta_content(self, soup, name):
        """
        Retrieves the content of a meta tag by name.

        :param soup: The BeautifulSoup object.
        :param name: The name of the meta tag to find.
        :return: The content of the meta tag, or None if not found.
        """
        meta_tag = soup.find('meta', attrs={'name': name})
        return meta_tag['content'] if meta_tag else None

    def optimize_page(self, url):
        """
        Optimizes the content of a page for SEO.

        :param url: The URL of the page to optimize.
        """
        # Fetch page content
        html = self.fetch_page(url)
        if html:
            # Parse content for SEO data
            seo_data = self.parse_content(html)
            logging.info(f"SEO Data for {url}: {seo_data}")

            # Here you would add more optimization logic, e.g., checking for keywords, etc.

    def crawl_site(self):
        """
        Crawls the website starting from the base URL and optimizes each page.
        """
        self.visited_urls.add(self.base_url)
        self.optimize_page(self.base_url)

        # Here we would find and crawl internal links - for simplicity, let's assume we've done that.

if __name__ == '__main__':
    # The base URL of the website to optimize
    BASE_URL = 'https://example.com'

    # Create an SEO optimizer instance and start the optimization process
    seo_optimizer = SEOOptimizer(BASE_URL)
    seo_optimizer.crawl_site()
```
