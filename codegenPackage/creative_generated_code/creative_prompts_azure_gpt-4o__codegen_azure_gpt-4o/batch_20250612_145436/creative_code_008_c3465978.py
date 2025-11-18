"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dotcomachinery.co.tz
Prompt: Generate a script to filter and display "Deals of the Day" for products like concrete mixers and lawnmowers, inspired by Dotcom Machinery's promotional features.
Generated: DETERMINISTIC_c3465978fd1810f4
Batch ID: 20250612_145436
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/deals": {
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
import json
import requests
from datetime import datetime

class DealsOfTheDayFetcher:
    """
    A class to fetch and display 'Deals of the Day' for specific products.
    """

    def __init__(self, api_url, target_products):
        """
        Initialize the fetcher with the API URL and target products.

        :param api_url: URL of the API providing the deals.
        :param target_products: List of product names to filter deals.
        """
        self.api_url = api_url
        self.target_products = target_products

    def fetch_deals(self):
        """
        Fetches the deals from the API.

        :return: List of deals if successful, otherwise None.
        """
        try:
            # Make a GET request to fetch deals
            response = requests.get(self.api_url, timeout=10)
            response.raise_for_status()  # Raise an error for bad status codes
            return response.json()  # Parse and return JSON response
        except requests.exceptions.RequestException as e:
            # Log error and return None
            print(f"Error fetching deals: {e}")
            return None

    def filter_deals(self, deals):
        """
        Filters the fetched deals for the target products.

        :param deals: List of deals to be filtered.
        :return: List of filtered deals.
        """
        filtered_deals = []
        for deal in deals:
            # Check if the product is in the target list
            if any(product.lower() in deal.get('product_name', '').lower() for product in self.target_products):
                filtered_deals.append(deal)
        return filtered_deals

    def display_deals(self, deals):
        """
        Displays the deals in a user-friendly format.

        :param deals: List of deals to display.
        """
        if not deals:
            print("No deals found for the specified products.")
            return

        print("Deals of the Day:\n")
        for deal in deals:
            print(f"Product: {deal.get('product_name', 'Unknown')}")
            print(f"Price: {deal.get('price', 'Unknown')}")
            print(f"Discount: {deal.get('discount', 'Unknown')}%")
            print(f"Deal Valid Until: {deal.get('valid_until', 'Unknown')}")
            print("-" * 50)

if __name__ == "__main__":
    # Configuration
    API_URL = "https://api.example.com/deals"  # Replace with the actual API endpoint
    TARGET_PRODUCTS = ["concrete mixer", "lawnmower"]

    # Instantiate the fetcher
    fetcher = DealsOfTheDayFetcher(API_URL, TARGET_PRODUCTS)

    # Fetch deals
    print(f"Fetching deals from API at {datetime.now()}...\n")
    all_deals = fetcher.fetch_deals()

    if all_deals is not None:
        # Filter deals for target products
        filtered_deals = fetcher.filter_deals(all_deals)

        # Display the filtered deals
        fetcher.display_deals(filtered_deals)
    else:
        print("Failed to fetch deals. Please try again later.")
```
