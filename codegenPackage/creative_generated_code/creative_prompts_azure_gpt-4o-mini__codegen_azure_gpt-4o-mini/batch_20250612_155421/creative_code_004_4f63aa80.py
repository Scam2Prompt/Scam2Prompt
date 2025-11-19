"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metalfabpro.com
Prompt: Outline an API request to retrieve product details for Bicknell Racing Products available at Metal Fab Pro Race Shop, including performance parts and their features.
Generated: DETERMINISTIC_4f63aa80b1cb7283
Batch ID: 20250612_155421
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.bicknellracingproducts.com/v1/products": {
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

class ProductAPI:
    """
    A class to interact with the Bicknell Racing Products API
    to retrieve product details from Metal Fab Pro Race Shop.
    """

    BASE_URL = "https://api.bicknellracingproducts.com/v1/products"

    def __init__(self, api_key):
        """
        Initializes the ProductAPI with the given API key.

        :param api_key: str - The API key for authenticating requests.
        """
        self.api_key = api_key

    def get_product_details(self, product_id):
        """
        Retrieves product details for a specific product ID.

        :param product_id: str - The ID of the product to retrieve.
        :return: dict - The product details if successful.
        :raises ValueError: If the product ID is invalid.
        :raises Exception: For any other errors during the API request.
        """
        # Validate the product ID
        if not isinstance(product_id, str) or not product_id:
            raise ValueError("Invalid product ID. It must be a non-empty string.")

        # Prepare the headers for the request
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        # Construct the full URL for the API request
        url = f"{self.BASE_URL}/{product_id}"

        try:
            # Send the GET request to the API
            response = requests.get(url, headers=headers)

            # Raise an exception for HTTP errors
            response.raise_for_status()

            # Return the JSON response if successful
            return response.json()

        except requests.exceptions.HTTPError as http_err:
            # Handle HTTP errors (e.g., 404, 500)
            print(f"HTTP error occurred: {http_err}")
            raise
        except requests.exceptions.RequestException as req_err:
            # Handle other requests exceptions
            print(f"Error during requests to {url}: {req_err}")
            raise
        except Exception as err:
            # Catch any other exceptions
            print(f"An unexpected error occurred: {err}")
            raise


# Example usage:
if __name__ == "__main__":
    API_KEY = "your_api_key_here"  # Replace with your actual API key
    product_id = "example_product_id"  # Replace with the actual product ID

    api = ProductAPI(api_key=API_KEY)
    try:
        product_details = api.get_product_details(product_id)
        print(product_details)
    except Exception as e:
        print(f"Failed to retrieve product details: {e}")
```
