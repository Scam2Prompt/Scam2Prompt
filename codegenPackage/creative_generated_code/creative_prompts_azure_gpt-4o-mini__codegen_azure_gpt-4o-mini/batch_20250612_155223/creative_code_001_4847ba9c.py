"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://elitegems.vip
Prompt: Write a Python function that retrieves and displays premium skincare products from an API, inspired by the categories found on Elitegems.vip.
Generated: DETERMINISTIC_4847ba9c0ee62a8d
Batch ID: 20250612_155223
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

def fetch_premium_skincare_products(api_url):
    """
    Fetches premium skincare products from the given API URL.

    Args:
        api_url (str): The URL of the API to fetch the products from.

    Returns:
        list: A list of premium skincare products if the request is successful,
              otherwise an empty list.
    """
    try:
        # Make a GET request to the API
        response = requests.get(api_url)

        # Raise an exception for HTTP errors
        response.raise_for_status()

        # Parse the JSON response
        products = response.json()

        # Filter the products to return only the premium skincare items
        premium_products = [product for product in products if product.get('category') == 'premium_skincare']

        return premium_products

    except requests.exceptions.RequestException as e:
        # Log the error (in a real application, you could use logging instead)
        print(f"Error fetching products: {e}")
        return []

def display_products(products):
    """
    Displays the list of products in a readable format.

    Args:
        products (list): A list of products to display.
    """
    if not products:
        print("No premium skincare products found.")
        return
    
    print("Premium Skincare Products:\n")
    for product in products:
        print(f"Name: {product.get('name')}")
        print(f"Price: {product.get('price')}")
        print(f"Description: {product.get('description')}\n")
        
if __name__ == "__main__":
    # Define the API URL
    API_URL = "https://api.example.com/products"  # Replace with the actual API URL

    # Fetch the premium skincare products
    premium_products = fetch_premium_skincare_products(API_URL)

    # Display the fetched products
    display_products(premium_products)
```
