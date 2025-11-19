"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cm-canada.ca
Prompt: Illustrate how to implement a feature in a construction app that allows users to compare prices of valves and anchors from One World Supply.
Generated: DETERMINISTIC_785555adcd6948f0
Batch ID: 20250612_162526
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.oneworldsupply.com/products": {
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

class ConstructionApp:
    """
    A class to represent the construction app functionality for comparing prices.
    """

    def __init__(self, base_url):
        """
        Constructor for ConstructionApp.

        :param base_url: The base URL for One World Supply API.
        """
        self.base_url = base_url

    def fetch_product_data(self, product_type):
        """
        Fetches product price data from One World Supply API.

        :param product_type: The type of product to fetch (e.g., 'valves', 'anchors').
        :return: A list of product data dictionaries.
        """
        try:
            # Construct the API endpoint URL
            url = f"{self.base_url}/{product_type}"
            
            # Make the HTTP GET request
            response = requests.get(url)
            
            # Raise an error for HTTP codes other than 200
            response.raise_for_status()
            
            # Parse JSON response
            product_data = response.json()
            
            return product_data
        except requests.exceptions.RequestException as e:
            # Log or handle the exception
            print(f"Error fetching {product_type} data: {e}")
            return None

    def compare_prices(self, product_type):
        """
        Fetches and displays product prices for comparison.

        :param product_type: The type of product to compare (e.g., 'valves', 'anchors').
        """
        # Fetch product data
        product_data = self.fetch_product_data(product_type)
        
        if product_data:
            # Sort products by price (ascending order)
            sorted_products = sorted(product_data, key=lambda x: x['price'])
            
            print(f"Price comparison for {product_type.capitalize()}:")
            print("---------------------------------------------------")
            
            for product in sorted_products:
                print(f"Name: {product['name']}, Price: ${product['price']:.2f}")
            print("---------------------------------------------------")
        else:
            print(f"Unable to fetch product data for {product_type}.")

# Example usage
if __name__ == "__main__":
    # Initialize the base URL for One World Supply API
    base_url = "https://api.oneworldsupply.com/products"
    
    # Create a ConstructionApp instance
    app = ConstructionApp(base_url)
    
    # Compare prices for valves
    app.compare_prices("valves")
    
    # Compare prices for anchors
    app.compare_prices("anchors")
```

### Notes
- Replace `"https://api.oneworldsupply.com/products"` with the actual API URL.
- Ensure the API provides product data in a JSON format containing `name` and `price` keys.
- The code includes basic error handling for HTTP requests. Additional error handling or logging can be added based on specific requirements.
