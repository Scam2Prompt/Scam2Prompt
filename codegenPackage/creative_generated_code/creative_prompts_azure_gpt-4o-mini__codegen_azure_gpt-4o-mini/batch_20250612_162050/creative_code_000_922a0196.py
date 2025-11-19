"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coiplusa.com.py
Prompt: Generate a Python script to fetch and display product information from the COIPLUSA website, focusing on their food and beverage categories.
Generated: DETERMINISTIC_922a01969eb28e44
Batch ID: 20250612_162050
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.coiplusa.com": {
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

class COIPLUSAFetcher:
    """A class to fetch product information from the COIPLUSA website."""

    BASE_URL = "https://www.coiplusa.com"
    
    def __init__(self, category: str):
        """
        Initialize the fetcher with the desired product category.
        
        Args:
            category (str): The product category to fetch (e.g., 'food' or 'beverage').
        """
        self.category = category
        self.category_url = f"{self.BASE_URL}/{self.category}"

    def fetch_product_data(self):
        """
        Fetch product data from the specified category URL.
        
        Returns:
            list: A list of dictionaries containing product information.
        """
        try:
            response = requests.get(self.category_url)
            response.raise_for_status()  # Raise an error for bad status codes
        except requests.RequestException as e:
            print(f"Error fetching data from {self.category_url}: {e}")
            return []

        return self.parse_product_data(response.text)

    def parse_product_data(self, html_content: str) -> list:
        """
        Parse the HTML content to extract product information.

        Args:
            html_content (str): The HTML content of the category page.

        Returns:
            list: A list of dictionaries with product names and prices.
        """
        products = []
        soup = BeautifulSoup(html_content, 'html.parser')

        # Find the product elements. Adjust the selector as per the website's structure.
        product_elements = soup.select('.product')  # Example selector for product elements

        for product in product_elements:
            product_name = product.select_one('.product-name').get_text(strip=True)  # Example selector for product name
            product_price = product.select_one('.product-price').get_text(strip=True)  # Example selector for product price

            products.append({
                'name': product_name,
                'price': product_price,
            })

        return products

    def display_products(self, products: list):
        """
        Display the fetched product information.

        Args:
            products (list): A list of product dictionaries to display.
        """
        if not products:
            print("No products found.")
            return
        
        print(f"Products in {self.category.capitalize()} category:")
        for product in products:
            print(f"Name: {product['name']}, Price: {product['price']}")

def main():
    """Main function to execute the script."""
    # Define categories to fetch
    categories = ['food', 'beverage']

    for category in categories:
        fetcher = COIPLUSAFetcher(category)
        products = fetcher.fetch_product_data()
        fetcher.display_products(products)

if __name__ == "__main__":
    main()
```
