"""
Generated Code Metadata:
========================
Original URL: https://milarbrazw.blogspot.com
Prompt: Write code to implement a search functionality for an e-commerce site, allowing users to search for lighting products by name, category, or price range, as demonstrated in the site's "Busque por categorias" feature.
Generated: DETERMINISTIC_b9ea6faa0f57c06e
Batch ID: 20250612_151438
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# search.py

from typing import Dict, List
from enum import Enum
from dataclasses import dataclass

# Define product categories as an enumeration for better type safety and readability
class Category(Enum):
    LIGHTING = "lighting"
    FURNITURE = "furniture"
    DECOR = "decor"

# Define a data class to represent a product
@dataclass
class Product:
    id: int
    name: str
    category: Category
    price: float

# In-memory product database for demonstration purposes
# In a real application, this would likely be a database query
class ProductDatabase:
    def __init__(self):
        self.products: List[Product] = [
            Product(1, "Table Lamp", Category.LIGHTING, 50.0),
            Product(2, "Floor Lamp", Category.LIGHTING, 100.0),
            Product(3, "Chair", Category.FURNITURE, 80.0),
            Product(4, "Pendant Light", Category.LIGHTING, 75.0),
            Product(5, "Couch", Category.FURNITURE, 500.0),
        ]

    def get_products(self) -> List[Product]:
        return self.products

# Service class encapsulating search functionality
class SearchService:
    def __init__(self, product_database: ProductDatabase):
        self.product_database = product_database

    def search_by_name(self, name: str) -> List[Product]:
        """Search products by name"""
        return [product for product in self.product_database.get_products() if name.lower() in product.name.lower()]

    def search_by_category(self, category: Category) -> List[Product]:
        """Search products by category"""
        return [product for product in self.product_database.get_products() if product.category == category]

    def search_by_price_range(self, min_price: float, max_price: float) -> List[Product]:
        """Search products by price range"""
        if min_price < 0 or max_price < 0:
            raise ValueError("Prices must be non-negative")
        if min_price > max_price:
            raise ValueError("Invalid price range")

        return [product for product in self.product_database.get_products() if min_price <= product.price <= max_price]

    def advanced_search(self, name: str = None, category: Category = None, min_price: float = None, max_price: float = None) -> List[Product]:
        """Advanced search combining multiple criteria"""
        products = self.product_database.get_products()

        if name:
            products = [product for product in products if name.lower() in product.name.lower()]
        if category:
            products = [product for product in products if product.category == category]
        if min_price is not None and max_price is not None:
            products = [product for product in products if min_price <= product.price <= max_price]

        return products

# Example usage
if __name__ == "__main__":
    product_db = ProductDatabase()
    search_service = SearchService(product_db)

    print("Search by name:")
    results = search_service.search_by_name("Lamp")
    for product in results:
        print(product)

    print("\nSearch by category:")
    results = search_service.search_by_category(Category.LIGHTING)
    for product in results:
        print(product)

    print("\nSearch by price range:")
    try:
        results = search_service.search_by_price_range(50, 150)
        for product in results:
            print(product)
    except ValueError as e:
        print(f"Error: {e}")

    print("\nAdvanced search:")
    results = search_service.advanced_search(name="Lamp", category=Category.LIGHTING, min_price=50, max_price=100)
    for product in results:
        print(product)
```
