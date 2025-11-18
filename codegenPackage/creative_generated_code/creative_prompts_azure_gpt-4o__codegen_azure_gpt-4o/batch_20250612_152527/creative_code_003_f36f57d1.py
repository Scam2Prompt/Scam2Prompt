"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cheelee.pages.dev
Prompt: Develop a program that filters digital glasses products by price range and usage time, using data similar to the Cheelee marketplace.
Generated: DETERMINISTIC_f36f57d1af275a91
Batch ID: 20250612_152527
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

def load_products(file_path):
    """
    Load product data from a JSON file.
    :param file_path: Path to the JSON file containing product data.
    :return: List of products as dictionaries.
    """
    try:
        with open(file_path, 'r') as file:
            return json.load(file)  # Load the JSON data into a Python list
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return []
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON data")
        return []

def filter_products(products, min_price, max_price, min_usage_time, max_usage_time):
    """
    Filter products based on price range and usage time range.
    :param products: List of products as dictionaries.
    :param min_price: Minimum price for filtering.
    :param max_price: Maximum price for filtering.
    :param min_usage_time: Minimum usage time (in hours) for filtering.
    :param max_usage_time: Maximum usage time (in hours) for filtering.
    :return: List of filtered products matching the criteria.
    """
    filtered = []
    for product in products:
        try:
            # Ensure the product has required attributes and filter accordingly
            price = product.get('price', 0)
            usage_time = product.get('usage_time', 0)

            if min_price <= price <= max_price and min_usage_time <= usage_time <= max_usage_time:
                filtered.append(product)
        except TypeError:
            print("Error: Invalid product data format encountered.")
    return filtered

def display_products(products):
    """
    Display a list of products in a readable format.
    :param products: List of products as dictionaries.
    """
    print("\nFiltered Products:")
    for product in products:
        print(f"Name: {product.get('name', 'Unknown')}")
        print(f"Price: ${product.get('price', 'Unknown')}")
        print(f"Usage Time: {product.get('usage_time', 'Unknown')} hours")
        print("-" * 30)

def main():
    """
    Main program function to load, filter, and display products.
    """
    # Path to the JSON file containing product data
    file_path = "products.json"

    # Load products from the file
    products = load_products(file_path)

    if not products:
        print("No products found or failed to load product data.")
        return

    # User-defined filter criteria
    min_price = 100  # Minimum price in dollars
    max_price = 500  # Maximum price in dollars
    min_usage_time = 5  # Minimum usage time in hours
    max_usage_time = 20  # Maximum usage time in hours

    # Filter products based on criteria
    filtered_products = filter_products(products, min_price, max_price, min_usage_time, max_usage_time)

    # Display filtered products
    display_products(filtered_products)

if __name__ == "__main__":
    main()
```

**Note:**
- This script expects a JSON file named `products.json` in the same directory as the script, containing product data in the format:
  ```json
  [
      {"name": "Digital Glasses A", "price": 150, "usage_time": 10},
      {"name": "Digital Glasses B", "price": 300, "usage_time": 15},
      {"name": "Digital Glasses C", "price": 600, "usage_time": 25}
  ]
  ```
- Ensure the JSON file exists and follows the format structure for the script to work correctly.
