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
from typing import List, Dict

class Product:
    """
    A class to represent a digital glasses product.
    """

    def __init__(self, name: str, price: float, usage_time: int):
        self.name = name
        self.price = price
        self.usage_time = usage_time

    def to_dict(self) -> Dict:
        """Convert the product to a dictionary."""
        return {
            "name": self.name,
            "price": self.price,
            "usage_time": self.usage_time
        }


def load_products(file_path: str) -> List[Product]:
    """
    Load products from a JSON file.
    
    Args:
        file_path (str): The path to the JSON file containing products.

    Returns:
        List[Product]: A list of Product objects.
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return [Product(**item) for item in data]
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return []
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON from the file.")
        return []


def filter_products(products: List[Product], min_price: float, max_price: float, max_usage_time: int) -> List[Product]:
    """
    Filter products based on price range and maximum usage time.

    Args:
        products (List[Product]): The list of products to filter.
        min_price (float): The minimum price for filtering.
        max_price (float): The maximum price for filtering.
        max_usage_time (int): The maximum usage time for filtering.

    Returns:
        List[Product]: The filtered list of Product objects.
    """
    filtered = []
    
    for product in products:
        if min_price <= product.price <= max_price and product.usage_time <= max_usage_time:
            filtered.append(product)
    
    return filtered


def main(file_path: str, min_price: float, max_price: float, max_usage_time: int):
    """
    Main function to load, filter, and display products.

    Args:
        file_path (str): The path to the JSON file with products.
        min_price (float): The minimum price for filtering.
        max_price (float): The maximum price for filtering.
        max_usage_time (int): The maximum usage time for filtering.
    """
    # Load products from the file
    products = load_products(file_path)

    # Filter the products based on user-defined criteria
    filtered_products = filter_products(products, min_price, max_price, max_usage_time)

    # Display filtered products
    if filtered_products:
        print("Filtered Products:")
        for product in filtered_products:
            print(product.to_dict())
    else:
        print("No products match the filter criteria.")


if __name__ == "__main__":
    # Example usage
    main("products.json", min_price=100.0, max_price=500.0, max_usage_time=8)
```

**Note:** The `products.json` file should exist in the same directory as this script, containing a JSON array of product objects with `name`, `price`, and `usage_time` fields.
