"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://newhomepoocoin.blogspot.com
Prompt: Create an API request to fetch details about "sapato social" and "tenis de esporte" from the Vanusa Sapato Infantil website.
Generated: DETERMINISTIC_b5a5b3cc427fc1d9
Batch ID: 20250612_162812
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.vanusasapato.com.br/api": {
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

class VanusaSapatoAPI:
    """Class to fetch product details from the Vanusa Sapato Infantil website."""

    BASE_URL = "https://www.vanusasapato.com.br/api"  # Base URL of the API

    def __init__(self):
        """Initialize the API client."""
        pass

    def fetch_product_details(self, product_name):
        """
        Fetch product details from the API.

        Args:
            product_name (str): The name of the product to search for.

        Returns:
            dict: A dictionary containing product details, or None if an error occurred.
        """
        try:
            # Send a GET request to the API with the product name as a query parameter
            response = requests.get(f"{self.BASE_URL}/products", params={"search": product_name})

            # Raise an exception if the request was unsuccessful
            response.raise_for_status()

            # Parse and return the JSON response
            return response.json()

        except requests.exceptions.RequestException as e:
            # Handle any request-related errors
            print(f"An error occurred while fetching product details: {e}")
            return None

def main():
    """Main function to fetch and display product details for 'sapato social' and 'tenis de esporte'."""
    api_client = VanusaSapatoAPI()

    products_to_fetch = ["sapato social", "tenis de esporte"]
    
    for product in products_to_fetch:
        print(f"Fetching details for: {product}")
        details = api_client.fetch_product_details(product)
        
        if details:
            print(f"Details for {product}: {details}")
        else:
            print(f"No details found for {product} or an error occurred.")

if __name__ == "__main__":
    main()
```
