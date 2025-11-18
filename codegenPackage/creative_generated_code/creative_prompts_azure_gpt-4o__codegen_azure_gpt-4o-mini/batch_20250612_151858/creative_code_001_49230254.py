"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vertivvpp.dev.stp.prmcdn.io
Prompt: Recommend APIs or libraries that can help implement product selectors and configurators similar to those described in Vertiv's Partner Program.
Generated: DETERMINISTIC_4923025427297942
Batch ID: 20250612_151858
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.vertiv.com/partner": {
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

class ProductSelector:
    """
    A class to handle product selection and configuration using external APIs.
    """

    def __init__(self, api_url):
        """
        Initializes the ProductSelector with the given API URL.

        Args:
            api_url (str): The base URL for the product API.
        """
        self.api_url = api_url

    def fetch_products(self):
        """
        Fetches the list of available products from the API.

        Returns:
            list: A list of products if successful, else an empty list.
        """
        try:
            response = requests.get(f"{self.api_url}/products")
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Return the JSON response as a list
        except requests.RequestException as e:
            print(f"Error fetching products: {e}")
            return []

    def configure_product(self, product_id, configuration):
        """
        Configures a specific product with the given configuration.

        Args:
            product_id (str): The ID of the product to configure.
            configuration (dict): The configuration options for the product.

        Returns:
            dict: The configured product details if successful, else None.
        """
        try:
            response = requests.post(f"{self.api_url}/products/{product_id}/configure", json=configuration)
            response.raise_for_status()
            return response.json()  # Return the configured product details
        except requests.RequestException as e:
            print(f"Error configuring product {product_id}: {e}")
            return None

# Example usage
if __name__ == "__main__":
    # Define the API URL for the product service
    api_url = "https://api.vertiv.com/partner"  # Replace with the actual API URL
    product_selector = ProductSelector(api_url)

    # Fetch available products
    products = product_selector.fetch_products()
    if products:
        print(f"Available products: {products}")

    # Example configuration (make sure to replace with actual product id and config)
    example_product_id = "12345"  # Replace with an actual product ID
    example_configuration = {
        "option1": "value1",
        "option2": "value2"
    }
    
    configured_product = product_selector.configure_product(example_product_id, example_configuration)
    if configured_product:
        print(f"Configured product details: {configured_product}")
```
