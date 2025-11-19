"""
Generated Code Metadata:
========================
Original URL: https://baliauthenticcoffeeandgallery.com
Prompt: "Generate a product catalog for an e-commerce site selling Balinese crafts and coffee, including categories for paintings, hoodies, and tote bags."
Generated: DETERMINISTIC_86b614b77c066560
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# product_catalog.py

from enum import Enum
from typing import List, Dict

class ProductCategory(str, Enum):
    """Product categories"""
    PAINTINGS = "paintings"
    HOODIES = "hoodies"
    TOTE_BAGS = "tote_bags"

class Product:
    """Represents a product in the catalog"""
    def __init__(self, id: int, name: str, description: str, price: float, category: ProductCategory):
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.category = category

    def __repr__(self):
        return f"Product(id={self.id}, name='{self.name}', description='{self.description}', price={self.price}, category='{self.category.value}')"

class ProductCatalog:
    """Manages a collection of products"""
    def __init__(self):
        self.products: Dict[int, Product] = {}
        self.categories: Dict[ProductCategory, List[Product]] = {
            ProductCategory.PAINTINGS: [],
            ProductCategory.HOODIES: [],
            ProductCategory.TOTE_BAGS: []
        }

    def add_product(self, product: Product):
        """Add a product to the catalog"""
        if product.id in self.products:
            raise ValueError(f"Product with ID {product.id} already exists")
        self.products[product.id] = product
        self.categories[product.category].append(product)

    def get_product(self, id: int) -> Product:
        """Retrieve a product by ID"""
        try:
            return self.products[id]
        except KeyError:
            raise ValueError(f"Product with ID {id} not found")

    def get_products_by_category(self, category: ProductCategory) -> List[Product]:
        """Retrieve products by category"""
        return self.categories[category]

def main():
    catalog = ProductCatalog()

    # Add some sample products
    catalog.add_product(Product(1, "Beautiful Beach Painting", "A vibrant painting of a Balinese beach", 99.99, ProductCategory.PAINTINGS))
    catalog.add_product(Product(2, "Balinese Coffee Hoodie", "A cozy hoodie with a design inspired by Balinese coffee culture", 49.99, ProductCategory.HOODIES))
    catalog.add_product(Product(3, "Handwoven Tote Bag", "A sturdy tote bag made from natural fibers", 29.99, ProductCategory.TOTE_BAGS))
    catalog.add_product(Product(4, "Sunset over Ubud", "A stunning painting of a sunset over Ubud", 149.99, ProductCategory.PAINTINGS))

    # Print products by category
    for category in ProductCategory:
        print(f"Category: {category.value}")
        for product in catalog.get_products_by_category(category):
            print(product)
        print()

if __name__ == "__main__":
    main()
```
