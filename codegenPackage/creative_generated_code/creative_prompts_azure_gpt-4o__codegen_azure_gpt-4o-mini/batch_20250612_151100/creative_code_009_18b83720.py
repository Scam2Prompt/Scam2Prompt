"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://teamelevenx1.com
Prompt: Develop a Python script to fetch and display exclusive app-only products using an API similar to "ayuwin apk."
Generated: DETERMINISTIC_18b83720ddb8714d
Batch ID: 20250612_151100
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/products": {
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

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class AppOnlyProductsFetcher:
    def __init__(self, api_url):
        """
        Initializes the fetcher with the API URL.

        :param api_url: str - The base URL of the API to fetch products from.
        """
        self.api_url = api_url

    def fetch_products(self):
        """
        Fetches exclusive app-only products from the API.

        :return: list - A list of exclusive products or an empty list if an error occurs.
        """
        try:
            logging.info("Fetching exclusive app-only products from the API.")
            response = requests.get(self.api_url)

            # Check if the request was successful
            response.raise_for_status()

            data = response.json()
            if 'products' in data:
                exclusive_products = [product for product in data['products'] if product.get('exclusive')]
                logging.info(f"Found {len(exclusive_products)} exclusive products.")
                return exclusive_products
            else:
                logging.warning("No 'products' key found in the response.")
                return []

        except requests.exceptions.HTTPError as http_err:
            logging.error(f"HTTP error occurred: {http_err}")
        except requests.exceptions.ConnectionError as conn_err:
            logging.error(f"Connection error occurred: {conn_err}")
        except requests.exceptions.Timeout as timeout_err:
            logging.error(f"Timeout error occurred: {timeout_err}")
        except requests.exceptions.RequestException as req_err:
            logging.error(f"An error occurred: {req_err}")
        except Exception as e:
            logging.error(f"An unexpected error occurred: {e}")

        return []

    def display_products(self, products):
        """
        Displays the exclusive products in a user-friendly format.

        :param products: list - A list of exclusive products to be displayed.
        """
        if not products:
            logging.info("No exclusive products to display.")
            print("No exclusive products found.")
            return

        print("Exclusive App-Only Products:")
        for product in products:
            print(f"- {product.get('name', 'Unknown Product')} (Price: {product.get('price', 'N/A')})")

if __name__ == "__main__":
    # Replace with the actual API URL
    api_url = "https://api.example.com/products"

    fetcher = AppOnlyProductsFetcher(api_url)
    exclusive_products = fetcher.fetch_products()
    fetcher.display_products(exclusive_products)
```
