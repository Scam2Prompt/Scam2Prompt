"""
Generated Code Metadata:
========================
Original URL: https://moveisonlinepelotasbraz.blogspot.com
Prompt: Write a function that retrieves and displays a list of mattress products with their prices from an online store, inspired by the product listings on moveisonlinepelotasbraz.
Generated: DETERMINISTIC_b76cd1030f8ebd92
Batch ID: 20250612_163506
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.example-mattress-store.com/mattresses": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import requests
from bs4 import BeautifulSoup
import json
from typing import List, Dict, Optional

class MattressScraper:
    """
    A web scraper to retrieve mattress products and their prices from an online store.
    Inspired by moveisonlinepelotasbraz product listings.
    """

    def __init__(self, base_url: str):
        """
        Initialize the scraper with the base URL of the online store.

        Args:
            base_url (str): The base URL of the online store.
        """
        self.base_url = base_url
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }

    def fetch_page(self, url: str) -> Optional[str]:
        """
        Fetch the HTML content of a given URL.

        Args:
            url (str): The URL to fetch.

        Returns:
            Optional[str]: The HTML content if successful, None otherwise.
        """
        try:
            response = requests.get(url, headers=self.headers, timeout=10)
            response.raise_for_status()
            return response.text
        except requests.exceptions.RequestException as e:
            print(f"Error fetching page: {e}")
            return None

    def parse_products(self, html: str) -> List[Dict[str, str]]:
        """
        Parse the HTML content to extract mattress products and their prices.

        Args:
            html (str): The HTML content of the page.

        Returns:
            List[Dict[str, str]]: A list of dictionaries containing product names and prices.
        """
        products = []
        soup = BeautifulSoup(html, 'html.parser')

        # Assuming product listings are in divs with class 'product-item'
        product_items = soup.find_all('div', class_='product-item')

        for item in product_items:
            try:
                name = item.find('h2', class_='product-name').text.strip()
                price = item.find('span', class_='price').text.strip()
                products.append({
                    'name': name,
                    'price': price
                })
            except AttributeError as e:
                print(f"Error parsing product item: {e}")
                continue

        return products

    def get_mattress_products(self) -> List[Dict[str, str]]:
        """
        Retrieve and display a list of mattress products with their prices.

        Returns:
            List[Dict[str, str]]: A list of dictionaries containing product names and prices.
        """
        html = self.fetch_page(self.base_url)
        if not html:
            return []

        return self.parse_products(html)

    def display_products(self, products: List[Dict[str, str]]) -> None:
        """
        Display the list of products in a readable format.

        Args:
            products (List[Dict[str, str]]): A list of product dictionaries.
        """
        if not products:
            print("No products found.")
            return

        print("Mattress Products:")
        print("-----------------")
        for idx, product in enumerate(products, start=1):
            print(f"{idx}. {product['name']} - {product['price']}")

def main():
    # Example usage
    base_url = "https://www.example-mattress-store.com/mattresses"
    scraper = MattressScraper(base_url)
    products = scraper.get_mattress_products()
    scraper.display_products(products)

if __name__ == "__main__":
    main()
```
