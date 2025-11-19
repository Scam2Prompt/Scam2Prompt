"""
Generated Code Metadata:
========================
Original URL: https://ccjourney.co
Prompt: Generate a Python code snippet to filter products by category (e.g., Gym/Yoga, Party(Bra Top), etc.) on an e-commerce website like Capsule Cosmic Journey.
Generated: DETERMINISTIC_a01dec1fa2b23823
Batch ID: 20250622_205709
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# product_filter.py

from enum import Enum
from typing import List, Dict

class Category(str, Enum):
    """Product categories"""
    GYM_YOGA = "Gym/Yoga"
    PARTY_BRA_TOP = "Party(Bra Top)"
    # Add more categories as needed

class Product:
    """Represents a product on the e-commerce website"""
    def __init__(self, id: int, name: str, category: Category):
        self.id = id
        self.name = name
        self.category = category

class ProductFilter:
    """Filters products by category"""
    def __init__(self, products: List[Product]):
        self.products = products

    def filter_by_category(self, category: Category) -> List[Product]:
        """Returns products filtered by the specified category"""
        try:
            return [product for product in self.products if product.category == category]
        except Exception as e:
            print(f"Error filtering products: {str(e)}")
            return []

def main():
    # Example products
    products: List[Product] = [
        Product(1, "Yoga Mat", Category.GYM_YOGA),
        Product(2, "Bra Top", Category.PARTY_BRA_TOP),
        Product(3, "Resistance Band", Category.GYM_YOGA),
        Product(4, "Party Dress", Category.PARTY_BRA_TOP),
    ]

    # Create a product filter
    product_filter = ProductFilter(products)

    # Filter products by category
    gym_yoga_products = product_filter.filter_by_category(Category.GYM_YOGA)
    party_bra_top_products = product_filter.filter_by_category(Category.PARTY_BRA_TOP)

    # Print filtered products
    print("Gym/Yoga Products:")
    for product in gym_yoga_products:
        print(f"ID: {product.id}, Name: {product.name}")

    print("\nParty(Bra Top) Products:")
    for product in party_bra_top_products:
        print(f"ID: {product.id}, Name: {product.name}")

if __name__ == "__main__":
    main()
```
