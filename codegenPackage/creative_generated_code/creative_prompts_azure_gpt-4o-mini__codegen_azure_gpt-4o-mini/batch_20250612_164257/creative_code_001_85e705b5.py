"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://malkeenz.com
Prompt: Write a Python function that interacts with an API to fetch product details for moissanite jewelry, similar to those offered by Malkeenz, including attributes like price, material, and available sizes.
Generated: DETERMINISTIC_85e705b51a1ef940
Batch ID: 20250612_164257
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

class MoissaniteJewelryAPI:
    BASE_URL = "https://api.example.com/products"  # Replace with the actual API endpoint

    def __init__(self, api_key):
        """
        Initialize the API client with the provided API key.

        :param api_key: str - The API key for authentication.
        """
        self.headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }

    def fetch_product_details(self, product_id):
        """
        Fetch the details of a specific moissanite jewelry product by ID.

        :param product_id: str - The ID of the product to retrieve.
        :return: dict - The product details including price, material, and available sizes.
        :raises ValueError: If the product ID is invalid.
        :raises Exception: If an error occurs during the API request.
        """
        if not isinstance(product_id, str) or not product_id.strip():
            raise ValueError("Invalid product ID. It must be a non-empty string.")

        url = f"{self.BASE_URL}/{product_id}"
        
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()  # Raises an error for 4xx/5xx responses
            product_data = response.json()  # Parse the JSON response
            
            # Return relevant product attributes
            return {
                "price": product_data.get("price"),
                "material": product_data.get("material"),
                "available_sizes": product_data.get("available_sizes"),
            }
        except requests.exceptions.HTTPError as http_err:
            # Handle HTTP errors (e.g., 404, 500)
            print(f"HTTP error occurred: {http_err}")
            raise
        except requests.exceptions.RequestException as req_err:
            # Handle other request-related errors
            print(f"Request error occurred: {req_err}")
            raise
        except ValueError as json_err:
            # Handle JSON decoding errors
            print(f"JSON decoding error: {json_err}")
            raise

# Example usage:
# api_key = "your_api_key_here"
# jewelry_api = MoissaniteJewelryAPI(api_key)
# try:
#     product_details = jewelry_api.fetch_product_details("12345")
#     print(product_details)
# except Exception as e:
#     print(f"An error occurred: {e}")
```
