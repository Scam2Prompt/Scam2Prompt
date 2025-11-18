"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://doubles.sellpass.io
Prompt: Generate a Python script to automate the creation of a customizable Sellpass storefront for selling digital products like software keys and subscriptions.
Generated: DETERMINISTIC_9f4009a26f7a6d83
Batch ID: 20250612_154250
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.sellpass.io/v1/": {
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

class SellpassStorefront:
    """
    A class to automate the creation of a Sellpass storefront for selling digital products.
    """

    def __init__(self, api_key):
        """
        Initializes the SellpassStorefront with the provided API key.

        :param api_key: The API key for authenticating with the Sellpass API.
        """
        self.api_key = api_key
        self.base_url = 'https://api.sellpass.io/v1/'

    def create_storefront(self, storefront_data):
        """
        Creates a new storefront using the provided data.

        :param storefront_data: A dictionary containing the storefront configuration.
        :return: The response from the Sellpass API after creating the storefront.
        :raises Exception: If the API request fails.
        """
        endpoint = f"{self.base_url}storefronts"
        headers = {'Authorization': f'Bearer {self.api_key}', 'Content-Type': 'application/json'}

        try:
            response = requests.post(endpoint, headers=headers, data=json.dumps(storefront_data))
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Return the JSON response if successful
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            raise
        except Exception as err:
            print(f"An error occurred: {err}")
            raise

    def create_product(self, storefront_id, product_data):
        """
        Creates a new product in the specified storefront.

        :param storefront_id: The ID of the storefront where the product will be added.
        :param product_data: A dictionary containing the product configuration.
        :return: The response from the Sellpass API after creating the product.
        :raises Exception: If the API request fails.
        """
        endpoint = f"{self.base_url}storefronts/{storefront_id}/products"
        headers = {'Authorization': f'Bearer {self.api_key}', 'Content-Type': 'application/json'}

        try:
            response = requests.post(endpoint, headers=headers, data=json.dumps(product_data))
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            raise
        except Exception as err:
            print(f"An error occurred: {err}")
            raise

def main():
    """
    Main function to run the script and create a Sellpass storefront and products.
    """
    api_key = 'YOUR_SELLPASS_API_KEY'  # Replace with your Sellpass API key
    storefront_data = {
        'name': 'My Digital Store',
        'description': 'A store for selling digital products like software keys and subscriptions.',
        'currency': 'USD',
        'custom_domain': 'mydigitalstore.com'
    }

    product_data = {
        'name': 'Awesome Software Key',
        'description': 'Unlock the full version of Awesome Software.',
        'price': 19.99,
        'type': 'digital',
        'sku': 'AWESOME-KEY-001'
    }

    try:
        # Create a Sellpass storefront
        storefront = SellpassStorefront(api_key)
        created_storefront = storefront.create_storefront(storefront_data)
        print(f"Storefront created successfully: {created_storefront}")

        # Create a product in the created storefront
        storefront_id = created_storefront['id']  # Extract the storefront ID
        created_product = storefront.create_product(storefront_id, product_data)
        print(f"Product created successfully: {created_product}")

    except Exception as e:
        print(f"An error occurred during the storefront/product creation process: {e}")

if __name__ == "__main__":
    main()
```
