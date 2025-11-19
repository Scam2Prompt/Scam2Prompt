"""
Generated Code Metadata:
========================
Original URL: https://lunaroz.ro
Prompt: Write a Python function to retrieve and display the latest products from an online store, inspired by the product listings on Loredana Manea's website.
Generated: DETERMINISTIC_142f2e50783668a2
Batch ID: 20250612_161616
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/latest-products": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import requests
from typing import List, Dict

class Product:
    """Class to represent a product."""
    def __init__(self, name: str, price: float, description: str, image_url: str):
        self.name = name
        self.price = price
        self.description = description
        self.image_url = image_url

    def __str__(self):
        return f"{self.name} - ${self.price:.2f}\n{self.description}\nImage: {self.image_url}"

def fetch_latest_products(api_url: str) -> List[Product]:
    """
    Fetch the latest products from the online store API.

    Args:
        api_url (str): The URL of the API endpoint to fetch products from.

    Returns:
        List[Product]: A list of Product objects.

    Raises:
        ValueError: If the response from the API is not valid.
        requests.RequestException: If there is an error during the API request.
    """
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an error for bad responses (4xx and 5xx)

        products_data = response.json()  # Parse the JSON response

        # Validate the response structure
        if not isinstance(products_data, list):
            raise ValueError("Invalid response format: Expected a list of products.")

        products = []
        for item in products_data:
            # Extract product details
            name = item.get('name')
            price = item.get('price')
            description = item.get('description', 'No description available.')
            image_url = item.get('image_url', '')

            # Validate product details
            if name is None or price is None:
                raise ValueError("Product data is missing required fields.")

            products.append(Product(name, float(price), description, image_url))

        return products

    except requests.RequestException as e:
        print(f"Error fetching products: {e}")
        return []
    except ValueError as e:
        print(f"Data validation error: {e}")
        return []

def display_products(products: List[Product]) -> None:
    """
    Display the list of products.

    Args:
        products (List[Product]): The list of Product objects to display.
    """
    if not products:
        print("No products available.")
        return

    for product in products:
        print(product)
        print("-" * 40)  # Separator for better readability

if __name__ == "__main__":
    API_URL = "https://api.example.com/latest-products"  # Replace with the actual API URL
    latest_products = fetch_latest_products(API_URL)
    display_products(latest_products)
```
