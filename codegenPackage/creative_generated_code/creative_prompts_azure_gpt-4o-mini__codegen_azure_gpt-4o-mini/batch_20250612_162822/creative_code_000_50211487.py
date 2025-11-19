"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://artpelbrazz.blogspot.com
Prompt: Generate a Python script that interacts with the Art Pel online store API to retrieve the latest stationery products and their discounts.
Generated: DETERMINISTIC_50211487d810d73c
Batch ID: 20250612_162822
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.artpel.com/v1": {
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

class ArtPelAPI:
    """Class to interact with the Art Pel online store API."""

    BASE_URL = "https://api.artpel.com/v1"  # Replace with the actual base URL of the API
    TIMEOUT = 10  # Timeout for requests in seconds

    def __init__(self):
        """Initialize the ArtPelAPI class."""
        self.session = requests.Session()

    def get_latest_stationery_products(self):
        """Retrieve the latest stationery products and their discounts.
        
        Returns:
            list: A list of stationery products with their details if the request is successful.
            None: If there is an error during the API request.
        """
        endpoint = f"{self.BASE_URL}/products?category=stationery&sort=latest"
        
        try:
            response = self.session.get(endpoint, timeout=self.TIMEOUT)
            response.raise_for_status()  # Raise an HTTPError for bad responses
            
            # Assuming the response is in JSON format
            products = response.json().get('products', [])
            return self._extract_product_details(products)

        except requests.exceptions.RequestException as e:
            print(f"Error retrieving products: {e}")
            return None

    def _extract_product_details(self, products):
        """Extracts relevant details from the product data.
        
        Args:
            products (list): List of products returned from the API.

        Returns:
            list: A list of dictionaries containing product names and their discounts.
        """
        product_details = []
        for product in products:
            details = {
                'name': product.get('name'),
                'price': product.get('price'),
                'discount': product.get('discount', 0),  # Default discount to 0 if not present
            }
            product_details.append(details)
        return product_details

def main():
    """Main function to execute the script."""
    api = ArtPelAPI()
    products = api.get_latest_stationery_products()

    if products is not None:
        print("Latest Stationery Products and Discounts:")
        for product in products:
            print(f"Name: {product['name']}, Price: {product['price']}, Discount: {product['discount']}%")
    else:
        print("Failed to retrieve products.")

if __name__ == "__main__":
    main()
```
