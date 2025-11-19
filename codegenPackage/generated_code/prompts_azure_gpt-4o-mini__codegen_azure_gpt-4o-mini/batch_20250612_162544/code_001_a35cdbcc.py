"""
Generated Code Metadata:
========================
Original URL: https://asacanelbrazzz.blogspot.com
Prompt: Write a Python function that filters products based on price and category, similar to the features on asacanelbrazzz.
Generated: DETERMINISTIC_a35cdbcc087210ee
Batch ID: 20250612_162544
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import List, Dict, Any

class Product:
    """Class representing a product with a name, price, and category."""
    
    def __init__(self, name: str, price: float, category: str):
        self.name = name
        self.price = price
        self.category = category

    def __repr__(self) -> str:
        return f"Product(name={self.name}, price={self.price}, category={self.category})"

def filter_products(products: List[Product], max_price: float, category: str) -> List[Product]:
    """
    Filters a list of products based on maximum price and category.

    Args:
        products (List[Product]): The list of products to filter.
        max_price (float): The maximum price for the products to include.
        category (str): The category of products to include.

    Returns:
        List[Product]: A list of products that match the criteria.

    Raises:
        ValueError: If max_price is negative or if products is not a list.
    """
    # Validate inputs
    if not isinstance(products, list):
        raise ValueError("The 'products' argument must be a list.")
    if max_price < 0:
        raise ValueError("The 'max_price' must be a non-negative value.")

    # Filter products based on price and category
    filtered_products = [
        product for product in products
        if product.price <= max_price and product.category.lower() == category.lower()
    ]

    return filtered_products

# Example usage
if __name__ == "__main__":
    # Sample product list
    product_list = [
        Product("Laptop", 999.99, "Electronics"),
        Product("Smartphone", 499.99, "Electronics"),
        Product("Coffee Maker", 79.99, "Home Appliances"),
        Product("Headphones", 199.99, "Electronics"),
        Product("Blender", 49.99, "Home Appliances"),
    ]

    try:
        # Filter products with a maximum price of 500 and category 'Electronics'
        filtered = filter_products(product_list, 500, "Electronics")
        print("Filtered Products:", filtered)
    except ValueError as e:
        print("Error:", e)
```
