"""
Generated Code Metadata:
========================
Original URL: https://cafelc.com
Prompt: Write a function to filter a list of products (e.g., speakers, microphones, headphones) by price range and category, simulating the functionality of an e-commerce search feature.
Generated: DETERMINISTIC_fe1bfe8ea94cf247
Batch ID: 20250612_154927
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
    """Class representing a product with a name, category, and price."""
    
    def __init__(self, name: str, category: str, price: float):
        self.name = name
        self.category = category
        self.price = price

    def __repr__(self) -> str:
        return f"Product(name={self.name}, category={self.category}, price={self.price})"

def filter_products(products: List[Product], min_price: float, max_price: float, category: str) -> List[Product]:
    """
    Filters a list of products by price range and category.

    Args:
        products (List[Product]): The list of products to filter.
        min_price (float): The minimum price for the filter.
        max_price (float): The maximum price for the filter.
        category (str): The category to filter by.

    Returns:
        List[Product]: A list of products that match the criteria.

    Raises:
        ValueError: If min_price is greater than max_price.
    """
    
    # Validate price range
    if min_price > max_price:
        raise ValueError("Minimum price cannot be greater than maximum price.")

    # Filter products based on price range and category
    filtered_products = [
        product for product in products
        if min_price <= product.price <= max_price and product.category.lower() == category.lower()
    ]
    
    return filtered_products

# Example usage
if __name__ == "__main__":
    # Sample product list
    products = [
        Product("Bluetooth Speaker", "speakers", 49.99),
        Product("Wired Headphones", "headphones", 29.99),
        Product("USB Microphone", "microphones", 89.99),
        Product("Wireless Headphones", "headphones", 199.99),
        Product("Portable Speaker", "speakers", 79.99),
    ]

    try:
        # Filter products in the price range of 30 to 80 and category 'headphones'
        filtered = filter_products(products, 30, 80, "headphones")
        print("Filtered Products:", filtered)
    except ValueError as e:
        print("Error:", e)
```
