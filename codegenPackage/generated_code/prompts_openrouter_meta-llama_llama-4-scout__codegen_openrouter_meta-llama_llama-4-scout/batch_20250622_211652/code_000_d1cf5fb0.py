"""
Generated Code Metadata:
========================
Original URL: https://biogreenasia.com
Prompt: Write a Python code snippet to manage an e-commerce product catalog for a natural beauty products company, including product categories for "100% Natural, Energy, Food Supplement, Protein" products.
Generated: DETERMINISTIC_d1cf5fb0cf05c30b
Batch ID: 20250622_211652
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
    """Product categories for natural beauty products"""
    NATURAL = "100% Natural"
    ENERGY = "Energy"
    FOOD_SUPPLEMENT = "Food Supplement"
    PROTEIN = "Protein"

class Product:
    """Represents a product in the catalog"""
    def __init__(self, 
                 product_id: int, 
                 name: str, 
                 category: ProductCategory, 
                 price: float, 
                 description: str):
        """
        Initializes a Product instance.

        Args:
        - product_id (int): Unique product ID
        - name (str): Product name
        - category (ProductCategory): Product category
        - price (float): Product price
        - description (str): Product description
        """
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price
        self.description = description

    def __repr__(self):
        return f"Product({self.product_id}, {self.name}, {self.category}, {self.price}, {self.description})"

class ProductCatalog:
    """Manages a catalog of products"""
    def __init__(self):
        self.products: Dict[int, Product] = {}

    def add_product(self, product: Product):
        """
        Adds a product to the catalog.

        Args:
        - product (Product): Product to add

        Raises:
        - ValueError: If a product with the same ID already exists
        """
        if product.product_id in self.products:
            raise ValueError(f"Product with ID {product.product_id} already exists")
        self.products[product.product_id] = product

    def remove_product(self, product_id: int):
        """
        Removes a product from the catalog.

        Args:
        - product_id (int): ID of the product to remove

        Raises:
        - ValueError: If the product does not exist
        """
        if product_id not in self.products:
            raise ValueError(f"Product with ID {product_id} does not exist")
        del self.products[product_id]

    def get_product(self, product_id: int) -> Product:
        """
        Retrieves a product from the catalog.

        Args:
        - product_id (int): ID of the product to retrieve

        Returns:
        - Product: The product instance, or None if not found
        """
        return self.products.get(product_id)

    def get_products_by_category(self, category: ProductCategory) -> List[Product]:
        """
        Retrieves a list of products by category.

        Args:
        - category (ProductCategory): Category to filter by

        Returns:
        - List[Product]: List of products in the specified category
        """
        return [product for product in self.products.values() if product.category == category]

def main():
    catalog = ProductCatalog()

    # Create some products
    product1 = Product(1, "Natural Shampoo", ProductCategory.NATURAL, 14.99, "Gentle, sulfate-free shampoo")
    product2 = Product(2, "Energy Boost", ProductCategory.ENERGY, 24.99, "Natural energy supplement")
    product3 = Product(3, "Protein Powder", ProductCategory.PROTEIN, 39.99, "High-quality protein powder")

    # Add products to the catalog
    catalog.add_product(product1)
    catalog.add_product(product2)
    catalog.add_product(product3)

    # Retrieve a product
    retrieved_product = catalog.get_product(1)
    print(retrieved_product)

    # Retrieve products by category
    natural_products = catalog.get_products_by_category(ProductCategory.NATURAL)
    print("Natural products:")
    for product in natural_products:
        print(product)

if __name__ == "__main__":
    main()
```
