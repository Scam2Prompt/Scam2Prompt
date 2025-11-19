"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.lattechocolate.com.ar
Prompt: Generate a Python script that interacts with the Latte Chocolate online store API to retrieve product details and check stock availability for specific chocolate items.
Generated: DETERMINISTIC_8de4ab1e6044bdd9
Batch ID: 20250612_162710
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.lattechocolate.com/v1": {
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

class LatteChocolateAPI:
    """
    A class to interact with the Latte Chocolate online store API.
    Provides functionality to retrieve product details and check stock availability.
    """

    def __init__(self, base_url, api_key):
        """
        Initializes the API client.

        :param base_url: The base URL of the Latte Chocolate API.
        :param api_key: The API key for authentication.
        """
        self.base_url = base_url
        self.headers = {"Authorization": f"Bearer {api_key}"}

    def get_product_details(self, product_id):
        """
        Retrieves details for a specific product.

        :param product_id: The ID of the product.
        :return: A dictionary containing product details, or None if an error occurs.
        """
        endpoint = f"{self.base_url}/products/{product_id}"
        try:
            response = requests.get(endpoint, headers=self.headers)
            response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching product details: {e}")
            return None

    def check_stock_availability(self, product_id):
        """
        Checks stock availability for a specific product.

        :param product_id: The ID of the product.
        :return: A string indicating stock status or None if an error occurs.
        """
        product_details = self.get_product_details(product_id)
        if product_details is None:
            return None

        # Assuming the API response includes a 'stock' key with stock count
        stock = product_details.get("stock", None)
        if stock is None:
            print("Stock information is not available for this product.")
            return None

        return "In Stock" if stock > 0 else "Out of Stock"


def main():
    """
    Main function to interact with the Latte Chocolate API.
    Retrieves product information and checks stock availability.
    """
    # Replace with the actual base URL and API key
    API_BASE_URL = "https://api.lattechocolate.com/v1"
    API_KEY = "your_api_key_here"

    # Example product IDs
    product_ids = ["12345", "67890"]

    # Initialize the API client
    api_client = LatteChocolateAPI(API_BASE_URL, API_KEY)

    # Fetch and display product information and stock status
    for product_id in product_ids:
        print(f"Fetching details for product ID: {product_id}")
        product_details = api_client.get_product_details(product_id)

        if product_details:
            print("Product Details:")
            print(product_details)
            stock_status = api_client.check_stock_availability(product_id)
            print(f"Stock Status: {stock_status}")
        print("-" * 50)


if __name__ == "__main__":
    main()
```
