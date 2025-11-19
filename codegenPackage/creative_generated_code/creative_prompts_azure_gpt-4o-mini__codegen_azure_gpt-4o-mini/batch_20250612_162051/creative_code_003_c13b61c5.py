"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://theecomarena.com
Prompt: What are the best practices for product research and listing on Etsy, as suggested by Ecom Arena's e-commerce automation services?
Generated: DETERMINISTIC_c13b61c5f1330495
Batch ID: 20250612_162051
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.etsy.com/search?q=": {
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

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class EtsyProductResearch:
    """
    A class to handle product research and listing on Etsy.
    """

    def __init__(self, search_term):
        """
        Initializes the EtsyProductResearch object with a search term.

        :param search_term: The term to search for on Etsy.
        """
        self.search_term = search_term
        self.base_url = "https://www.etsy.com/search?q="

    def fetch_search_results(self):
        """
        Fetches search results from Etsy for the given search term.

        :return: List of product titles found on the first page of search results.
        """
        try:
            # Construct the full URL for the Etsy search
            url = self.base_url + self.search_term.replace(" ", "+")
            logging.info(f"Fetching results from: {url}")
            response = requests.get(url)

            # Raise an exception if the request was unsuccessful
            response.raise_for_status()

            # Parse the HTML content using BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')
            return self.parse_product_titles(soup)

        except requests.exceptions.RequestException as e:
            logging.error(f"Error fetching results: {e}")
            return []

    def parse_product_titles(self, soup):
        """
        Parses product titles from the BeautifulSoup object.

        :param soup: BeautifulSoup object containing the search results.
        :return: List of product titles.
        """
        titles = []
        try:
            # Find all product title elements based on the HTML structure
            for title in soup.find_all('h3', class_='text-gray-900'):
                titles.append(title.get_text(strip=True))
            logging.info(f"Found {len(titles)} product titles.")
        except Exception as e:
            logging.error(f"Error parsing product titles: {e}")
        return titles

    def perform_research(self):
        """
        Performs product research by fetching and displaying product information.

        :return: None
        """
        product_titles = self.fetch_search_results()
        if product_titles:
            logging.info("Product Titles:")
            for title in product_titles:
                print(f"- {title}")
        else:
            logging.warning("No product titles found.")

if __name__ == "__main__":
    # Example usage of the EtsyProductResearch class
    search_term = "handmade jewelry"  # Replace with any search term
    etsy_research = EtsyProductResearch(search_term)
    etsy_research.perform_research()
```
