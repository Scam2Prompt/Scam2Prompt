"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rewards-steth.com
Prompt: Write code to extract and categorize product information from the "해외뽐뿌" section, focusing on electronics and gadgets.
Generated: DETERMINISTIC_f36cc7876a822343
Batch ID: 20250612_153527
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.example.com/heoibaempompu": {
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
import json
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

class ProductScraper:
    """A class to scrape and categorize product information from the 해외뽐뿌 section."""

    def __init__(self, url):
        """Initialize the scraper with the target URL."""
        self.url = url
        self.products = []

    def fetch_page(self):
        """Fetch the HTML content of the target URL.

        Returns:
            str: HTML content of the page.
        """
        try:
            response = requests.get(self.url)
            response.raise_for_status()  # Raise an error for bad requests
            return response.text
        except requests.RequestException as e:
            logging.error(f"Failed to fetch page: {e}")
            return None

    def parse_products(self, html):
        """Parse product information from HTML content.

        Args:
            html (str): HTML content of the page.
        """
        soup = BeautifulSoup(html, 'html.parser')

        # Find all product items in the designated section
        product_items = soup.find_all('div', class_='product-item')  # Adjust the class as needed

        for item in product_items:
            try:
                title = item.find('h2', class_='product-title').text.strip()
                price = item.find('span', class_='product-price').text.strip()
                link = item.find('a', class_='product-link')['href']

                # Append product info as a dictionary
                self.products.append({
                    'title': title,
                    'price': price,
                    'link': link
                })
            except AttributeError as e:
                logging.warning(f"Failed to extract data from item: {e}")

    def categorize_products(self):
        """Categorize products based on predefined criteria."""
        categorized = {'electronics': [], 'gadgets': []}

        for product in self.products:
            if 'electronics' in product['title'].lower():
                categorized['electronics'].append(product)
            elif 'gadget' in product['title'].lower():
                categorized['gadgets'].append(product)

        return categorized

    def save_to_json(self, data, filename='products.json'):
        """Save categorized product data to a JSON file.

        Args:
            data (dict): The data to save.
            filename (str): The name of the file to save data in.
        """
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
            logging.info(f"Data saved to {filename}")
        except IOError as e:
            logging.error(f"Failed to save data to file: {e}")

    def run(self):
        """Execute the product scraping and categorization process."""
        html = self.fetch_page()
        if html:
            self.parse_products(html)
            categorized_data = self.categorize_products()
            self.save_to_json(categorized_data)

if __name__ == "__main__":
    # URL of the 해외뽐뿌 section for electronics and gadgets
    url = 'https://www.example.com/heoibaempompu'  # Replace with the actual URL
    scraper = ProductScraper(url)
    scraper.run()
```
