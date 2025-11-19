"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://maker-rewards.com
Prompt: Generate a Python code snippet to scrape product details from Snapdeal, focusing on categories like men's fashion, electronics, and home decor.
Generated: DETERMINISTIC_8cf932d198e7a2b3
Batch ID: 20250612_160156
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.snapdeal.com": {
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

class SnapdealScraper:
    """A class to scrape product details from Snapdeal for specific categories."""

    BASE_URL = "https://www.snapdeal.com"

    def __init__(self, categories):
        """
        Initialize the scraper with the desired categories.

        :param categories: List of categories to scrape from Snapdeal.
        """
        self.categories = categories

    def fetch_category_url(self, category):
        """
        Construct the URL for the given category.

        :param category: The category to fetch.
        :return: The category URL.
        """
        return f"{self.BASE_URL}/products/{category.replace(' ', '-')}-fashion"

    def scrape_product_details(self):
        """
        Scrape product details from each category and return results.

        :return: A list of dictionaries containing product details.
        """
        products = []
        for category in self.categories:
            url = self.fetch_category_url(category)
            response = self.make_request(url)

            if response:
                soup = BeautifulSoup(response.text, 'html.parser')
                product_cards = soup.find_all('div', class_='product-tuple-listing')

                for card in product_cards:
                    product = self.extract_product_info(card)
                    if product:
                        products.append(product)

        return products

    def make_request(self, url):
        """
        Make an HTTP GET request to the given URL.

        :param url: The URL to request.
        :return: The response object or None if an error occurs.
        """
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an HTTPError for bad responses
            return response
        except requests.exceptions.RequestException as e:
            print(f"Error fetching {url}: {e}")
            return None

    def extract_product_info(self, card):
        """
        Extract product information from a product card.

        :param card: The BeautifulSoup object representing a product card.
        :return: A dictionary with product details or None if not found.
        """
        try:
            title = card.find('p', class_='product-title').text.strip()
            price = card.find('span', class_='lfloat product-price').text.strip()
            link = card.find('a', class_='dp-widget-link')['href']

            return {
                'title': title,
                'price': price,
                'link': link
            }
        except AttributeError as e:
            print(f"Error extracting product info: {e}")
            return None


if __name__ == "__main__":
    # Define categories to scrape
    categories_to_scrape = ["Men's Fashion", "Electronics", "Home Decor"]

    # Instantiate the scraper and fetch product details
    scraper = SnapdealScraper(categories_to_scrape)
    product_details = scraper.scrape_product_details()

    # Print the scraped product details
    for product in product_details:
        print(product)
```
