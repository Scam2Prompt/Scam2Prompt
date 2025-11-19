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
from typing import List, Dict, Optional, Union

class Product:
    """
    Represents a product with name, category, and price.
    """
    def __init__(self, name: str, category: str, price: float):
        self.name = name
        self.category = str(category).lower()
        self.price = float(price)

    def __repr__(self):
        return f"Product(name='{self.name}', category='{self.category}', price={self.price})"

def filter_products(
    products: List[Product],
    min_price: Optional[float] = None,
    max_price: Optional[float] = None,
    category: Optional[Union[str, List[str]]] = None
) -> List[Product]:
    """
    Filters a list of products by price range and category.

    Args:
        products: List of Product objects to filter
        min_price: Minimum price threshold (inclusive)
        max_price: Maximum price threshold (inclusive)
        category: Single category string or list of categories to filter by

    Returns:
        List of filtered Product objects
    """
    filtered = products.copy()

    # Filter by price range
    if min_price is not None:
        filtered = [p for p in filtered if p.price >= min_price]
    if max_price is not None:
        filtered = [p for p in filtered if p.price <= max_price]

    # Filter by category
    if category is not None:
        if isinstance(category, str):
            categories = [category.lower()]
        else:
            categories = [c.lower() for c in category]
        
        filtered = [p for p in filtered if p.category in categories]

    return filtered

# Example usage
if __name__ == "__main__":
    # Sample product data
    products = [
        Product("Studio Headphones", "headphones", 199.99),
        Product("Wireless Earbuds", "headphones", 129.99),
        Product("Condenser Mic", "microphones", 149.99),
        Product("USB Mic", "microphones", 79.99),
        Product("Bluetooth Speaker", "speakers", 89.99),
        Product("Studio Monitors", "speakers", 299.99)
    ]

    # Test cases
    print("All products under $150:")
    for p in filter_products(products, max_price=150):
        print(p)

    print("\nHeadphones between $100 and $200:")
    for p in filter_products(products, min_price=100, max_price=200, category="headphones"):
        print(p)

    print("\nMicrophones or speakers under $100:")
    for p in filter_products(products, max_price=100, category=["microphones", "speakers"]):
        print(p)
```
