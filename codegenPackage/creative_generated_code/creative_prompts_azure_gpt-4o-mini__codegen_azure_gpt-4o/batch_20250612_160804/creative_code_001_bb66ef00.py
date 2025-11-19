"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://demo-8g2.pages.dev
Prompt: Write a function to filter products by size (Large, Medium, Small) in a shopping cart application, inspired by the filtering options available on the T-Shirt Store.
Generated: DETERMINISTIC_bb66ef00f1bc0632
Batch ID: 20250612_160804
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# shopping_cart.py

from typing import List, Dict

# Define the Product class
class Product:
    def __init__(self, name: str, size: str, price: float):
        """
        Initializes a Product instance.

        :param name: Name of the product
        :param size: Size of the product ('Large', 'Medium', 'Small')
        :param price: Price of the product
        """
        self.name = name
        self.size = size
        self.price = price

    def __repr__(self):
        """
        String representation of the Product instance.
        """
        return f"Product(name='{self.name}', size='{self.size}', price={self.price})"

# Define the function to filter products by size
def filter_products_by_size(products: List[Product], size: str) -> List[Product]:
    """
    Filters the list of products by the specified size.

    :param products: A list of Product instances to filter
    :param size: The size to filter by ('Large', 'Medium', 'Small')
    :return: A list of products matching the specified size
    """
    # Validate input size
    valid_sizes = {'Large', 'Medium', 'Small'}
    if size not in valid_sizes:
        raise ValueError(f"Invalid size '{size}'. Size must be one of {valid_sizes}.")

    # Filter products based on size
    filtered_products = [product for product in products if product.size == size]

    return filtered_products

# Example usage (uncomment the lines below to test the functionality)
# if __name__ == "__main__":
#     # Create a list of sample products
#     sample_products = [
#         Product("T-Shirt 1", "Large", 19.99),
#         Product("T-Shirt 2", "Medium", 15.99),
#         Product("T-Shirt 3", "Small", 12.99),
#         Product("T-Shirt 4", "Large", 25.99),
#         Product("T-Shirt 5", "Medium", 18.99),
#     ]
#
#     # Filter products by size
#     try:
#         large_products = filter_products_by_size(sample_products, "Large")
#         print("Large Products:", large_products)
#     except ValueError as e:
#         print("Error:", e)
```

This code defines a `Product` class and a `filter_products_by_size` function, adhering to best practices, with type hints, comments, and error handling.
