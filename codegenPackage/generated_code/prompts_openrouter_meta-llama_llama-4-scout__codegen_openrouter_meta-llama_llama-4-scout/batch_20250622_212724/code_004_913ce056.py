"""
Generated Code Metadata:
========================
Original URL: https://lkli7-vaaaa-aaaad-qcvqq-cai.icp0.io
Prompt: Design a simple e-commerce product catalog page with categories for gifts, tops, bottoms, and accessories, inspired by SCOGÉ's product offerings.
Generated: DETERMINISTIC_913ce0561de2d341
Batch ID: 20250622_212724
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# e-commerce_product_catalog.py

from enum import Enum
from typing import List, Dict

class Category(Enum):
    """Product categories"""
    GIFTS = "gifts"
    TOPS = "tops"
    BOTTOMS = "bottoms"
    ACCESSORIES = "accessories"

class Product:
    """Represents a product in the catalog"""
    def __init__(self, id: int, name: str, description: str, price: float, category: Category):
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.category = category

class ProductCatalog:
    """Simple e-commerce product catalog"""
    def __init__(self):
        self.products: Dict[int, Product] = {}
        self.categories: Dict[Category, List[int]] = {
            Category.GIFTS: [],
            Category.TOPS: [],
            Category.BOTTOMS: [],
            Category.ACCESSORIES: []
        }

    def add_product(self, product: Product):
        """Add a product to the catalog"""
        self.products[product.id] = product
        self.categories[product.category].append(product.id)

    def get_products_by_category(self, category: Category) -> List[Product]:
        """Get products by category"""
        return [self.products[id] for id in self.categories[category]]

    def get_product(self, id: int) -> Product:
        """Get a product by ID"""
        try:
            return self.products[id]
        except KeyError:
            raise ValueError(f"Product with ID {id} not found")

def main():
    catalog = ProductCatalog()

    # Add some sample products
    catalog.add_product(Product(1, "T-Shirt", "A nice T-Shirt", 19.99, Category.TOPS))
    catalog.add_product(Product(2, "Jeans", "A pair of jeans", 49.99, Category.BOTTOMS))
    catalog.add_product(Product(3, "Watch", "A stylish watch", 99.99, Category.ACCESSORIES))
    catalog.add_product(Product(4, "Gift Card", "A gift card", 25.00, Category.GIFTS))

    # Print products by category
    for category in Category:
        print(f"--- {category.value.capitalize()} ---")
        for product in catalog.get_products_by_category(category):
            print(f"{product.name}: ${product.price:.2f}")
        print()

    # Get a product by ID
    try:
        product = catalog.get_product(1)
        print(f"Product {product.id}: {product.name} (${product.price:.2f})")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
```
