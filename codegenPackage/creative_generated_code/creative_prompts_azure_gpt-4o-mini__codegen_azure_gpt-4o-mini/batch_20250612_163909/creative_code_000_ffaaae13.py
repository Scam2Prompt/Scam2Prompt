"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gprobolsa.com
Prompt: Write a Python script that generates a list of eco-friendly promotional products, specifically focusing on reusable bags, as described by Grupo ProBolsa.
Generated: DETERMINISTIC_ffaaae13bda855f9
Batch ID: 20250612_163909
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.probolsa.com/products": {
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
from typing import List, Dict

class EcoFriendlyProducts:
    """
    A class to handle the retrieval and storage of eco-friendly promotional products.
    """

    def __init__(self, api_url: str):
        """
        Initializes the EcoFriendlyProducts with the given API URL.
        
        Args:
            api_url (str): The URL of the API to fetch eco-friendly products from.
        """
        self.api_url = api_url
        self.products = []

    def fetch_products(self) -> None:
        """
        Fetches eco-friendly promotional products from the specified API URL.
        Handles any potential request errors.
        """
        try:
            response = requests.get(self.api_url)
            response.raise_for_status()  # Raise an error for bad responses (4xx and 5xx)
            self.products = response.json()
            print("Products fetched successfully.")
        except requests.exceptions.RequestException as e:
            print(f"Error fetching products: {e}")
            self.products = []  # Reset products to an empty list on error

    def filter_reusable_bags(self) -> List[Dict]:
        """
        Filters the fetched products to return only reusable bags.
        
        Returns:
            List[Dict]: A list of reusable bag products.
        """
        reusable_bags = [
            product for product in self.products
            if 'reusable bag' in product.get('description', '').lower()
        ]
        return reusable_bags

    def display_products(self, products: List[Dict]) -> None:
        """
        Displays the list of products in a readable format.
        
        Args:
            products (List[Dict]): The list of products to display.
        """
        if not products:
            print("No reusable bags found.")
            return
        
        print("Reusable Bags:")
        for product in products:
            print(f"- {product.get('name')} | Price: {product.get('price')} | Eco-friendly: {product.get('eco_friendly')}")


def main():
    """
    Main function to execute the eco-friendly products script.
    """
    # URL of the API providing eco-friendly promotional products
    api_url = "https://api.probolsa.com/products"  # Example URL, replace with actual URL

    # Create an instance of EcoFriendlyProducts
    eco_friendly_products = EcoFriendlyProducts(api_url)

    # Fetch and filter products
    eco_friendly_products.fetch_products()
    reusable_bags = eco_friendly_products.filter_reusable_bags()

    # Display the reusable bags
    eco_friendly_products.display_products(reusable_bags)


if __name__ == "__main__":
    main()
```
