"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://asacanelbrazzz.blogspot.com
Prompt: Write a Python function that filters products based on price and category, similar to the features on asacanelbrazzz.
Generated: DETERMINISTIC_a35cdbcc087210ee
Batch ID: 20250612_162544
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from typing import List, Dict

class Product:
    """Represents a product with a name, price, and category."""
    
    def __init__(self, name: str, price: float, category: str):
        self.name = name
        self.price = price
        self.category = category

    def __repr__(self):
        return f"Product(name={self.name}, price={self.price}, category={self.category})"

def filter_products(products: List[Product], min_price: float, max_price: float, category: str) -> List[Product]:
    """
    Filters products based on price range and category.

    Args:
        products (List[Product]): A list of Product objects to filter.
        min_price (float): The minimum price for filtering.
        max_price (float): The maximum price for filtering.
        category (str): The category to filter products by.

    Returns:
        List[Product]: A list of filtered Product objects.

    Raises:
        ValueError: If min_price is greater than max_price.
    """
    
    # Validate input
    if min_price > max_price:
        raise ValueError("min_price cannot be greater than max_price")

    # Filter products based on the given criteria
    filtered_products = [
        product for product in products
        if min_price <= product.price <= max_price and product.category == category
    ]
    
    return filtered_products

# Example usage
if __name__ == "__main__":
    # Sample product list
    products = [
        Product("Laptop", 999.99, "Electronics"),
        Product("Smartphone", 499.99, "Electronics"),
        Product("Chair", 89.99, "Furniture"),
        Product("Table", 199.99, "Furniture"),
        Product("Headphones", 29.99, "Accessories"),
    ]
    
    try:
        # Filter products in the "Electronics" category between $100 and $1000
        filtered = filter_products(products, 100, 1000, "Electronics")
        print("Filtered Products:", filtered)
    except ValueError as e:
        print(f"Error: {e}")
```
