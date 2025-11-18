"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ebrasilbrazz.blogspot.com
Prompt: Generate an API integration script for an e-commerce platform to display crafting products like "Bulbo rosa para Letra luminosa Heidi Swapp" and sort them by "Mais Vendidos" as per the sorting options on the ebrasilbrazz site.
Generated: DETERMINISTIC_4910470e4558174a
Batch ID: 20250612_154949
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.ebrasilbrazz.com": {
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
import logging
from typing import List, Dict, Optional

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ECommerceAPI:
    """
    A class to integrate with the e-commerce platform API for fetching crafting products
    and sorting them by 'Mais Vendidos'.
    """

    def __init__(self, base_url: str, api_key: str):
        """
        Initialize the API client with the base URL and authentication key.

        :param base_url: The base URL of the e-commerce API.
        :param api_key: The API key for authentication.
        """
        self.base_url = base_url
        self.api_key = api_key

    def get_crafting_products(self) -> List[Dict]:
        """
        Fetch crafting products from the e-commerce platform.

        :return: A list of crafting products.
        """
        endpoint = f"{self.base_url}/products"
        headers = {"Authorization": f"Bearer {self.api_key}"}
        params = {"category": "crafting"}  # Assuming 'crafting' is the category for crafting products.

        try:
            response = requests.get(endpoint, headers=headers, params=params)
            response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx).
            return response.json().get("data", [])
        except requests.exceptions.RequestException as e:
            logging.error(f"Error fetching crafting products: {e}")
            return []

    def sort_products_by_popularity(self, products: List[Dict]) -> List[Dict]:
        """
        Sort a list of products by 'Mais Vendidos'.

        :param products: A list of products.
        :return: The sorted list of products.
        """
        # Assuming 'sales_count' is the field representing popularity or sales number.
        return sorted(products, key=lambda x: x.get("sales_count", 0), reverse=True)

    def display_products(self, sorted_products: List[Dict]):
        """
        Display the crafting products in a user-friendly way.

        :param sorted_products: A list of sorted crafting products.
        """
        print("Crafting Products Sorted by Mais Vendidos:")
        for product in sorted_products:
            name = product.get("name", "Unknown Product")
            sales_count = product.get("sales_count", "N/A")
            print(f"- {name} (Sales: {sales_count})")


def main():
    """
    Main function to execute the API integration process.
    """
    # Replace these with actual values for production use.
    BASE_URL = "https://api.ebrasilbrazz.com"  # Example base URL.
    API_KEY = "your_api_key_here"  # Replace with a valid API key.

    try:
        # Initialize the API client.
        api_client = ECommerceAPI(base_url=BASE_URL, api_key=API_KEY)

        # Fetch crafting products.
        crafting_products = api_client.get_crafting_products()

        if not crafting_products:
            logging.warning("No crafting products found.")
            return

        # Sort products by 'Mais Vendidos'.
        sorted_products = api_client.sort_products_by_popularity(crafting_products)

        # Display the sorted products.
        api_client.display_products(sorted_products)

    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
