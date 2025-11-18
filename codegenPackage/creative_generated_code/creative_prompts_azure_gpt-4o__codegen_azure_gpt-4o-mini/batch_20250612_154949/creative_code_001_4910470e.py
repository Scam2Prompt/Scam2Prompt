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
  "https://api.ebrasiabrazz.com/products": {
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
import json

class ECommerceAPI:
    """
    A class to interact with the e-commerce API to fetch and sort crafting products.
    """

    BASE_URL = "https://api.ebrasiabrazz.com/products"  # Base URL for the e-commerce platform API

    def __init__(self):
        """
        Initializes the ECommerceAPI instance.
        """
        self.session = requests.Session()  # Create a session for persistent HTTP connections

    def fetch_products(self, query, sort_by="Mais Vendidos"):
        """
        Fetches products from the e-commerce API based on the provided query and sorting option.

        Parameters:
            query (str): The search term for the products.
            sort_by (str): The sorting option for the products (default is "Mais Vendidos").

        Returns:
            list: A list of sorted products.
        """
        try:
            # Construct the API request parameters
            params = {
                'search': query,
                'sort': sort_by
            }

            # Make the API GET request
            response = self.session.get(self.BASE_URL, params=params)
            response.raise_for_status()  # Raise an exception for HTTP error responses

            # Parse the JSON response
            products = response.json()

            # Return the sorted products
            return products.get('data', [])

        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")  # Log HTTP errors
        except json.JSONDecodeError as json_err:
            print(f"JSON decode error: {json_err}")  # Log JSON decode errors
        except Exception as err:
            print(f"An error occurred: {err}")  # Log any other errors

        return []  # Return an empty list if there was an error

    def display_products(self, products):
        """
        Displays the list of products in a formatted manner.

        Parameters:
            products (list): A list of products to display.
        """
        if not products:
            print("No products found.")
            return

        print(f"{'Product Name':<40} {'Price':<10} {'Sold Count':<10}")
        print("=" * 70)

        # Iterate over the products and print their details
        for product in products:
            name = product.get('name', 'N/A')
            price = product.get('price', 'N/A')
            sold_count = product.get('sold_count', 'N/A')
            print(f"{name:<40} {price:<10} {sold_count:<10}")

if __name__ == "__main__":
    # Instantiate the ECommerceAPI class
    api = ECommerceAPI()

    # Fetch and display crafting products
    crafting_products = api.fetch_products("Bulbo rosa para Letra luminosa Heidi Swapp")
    api.display_products(crafting_products)
```
