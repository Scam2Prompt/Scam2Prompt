"""
Generated Code Metadata:
========================
Original URL: https://sui-foundation.teachable.com
Prompt: Design a basic structure for an online educational product filter system, inspired by the Sui Foundation's course offerings.
Generated: DETERMINISTIC_c25cb6dd527067ca
Batch ID: 20250622_211412
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# educational_product_filter_system.py

from enum import Enum
from typing import List, Dict

class ProductType(str, Enum):
    """ Enum for product types """
    COURSE = "course"
    TUTORIAL = "tutorial"
    EBOOK = "ebook"

class Product:
    """ Represents an educational product """

    def __init__(self, id: int, name: str, product_type: ProductType, categories: List[str], price: float):
        """
        Initializes a Product

        Args:
        id (int): Unique product ID
        name (str): Product name
        product_type (ProductType): Type of product
        categories (List[str]): List of categories
        price (float): Product price
        """
        self.id = id
        self.name = name
        self.product_type = product_type
        self.categories = categories
        self.price = price

class FilterSystem:
    """ Filter system for educational products """

    def __init__(self):
        self.products = []

    def add_product(self, product: Product):
        """ Adds a product to the filter system """
        self.products.append(product)

    def filter_by_type(self, product_type: ProductType) -> List[Product]:
        """
        Filters products by type

        Args:
        product_type (ProductType): Type of product to filter by

        Returns:
        List[Product]: List of products of the specified type
        """
        return [product for product in self.products if product.product_type == product_type]

    def filter_by_category(self, category: str) -> List[Product]:
        """
        Filters products by category

        Args:
        category (str): Category to filter by

        Returns:
        List[Product]: List of products in the specified category
        """
        return [product for product in self.products if category in product.categories]

    def filter_by_price_range(self, min_price: float, max_price: float) -> List[Product]:
        """
        Filters products by price range

        Args:
        min_price (float): Minimum price
        max_price (float): Maximum price

        Returns:
        List[Product]: List of products within the specified price range
        """
        return [product for product in self.products if min_price <= product.price <= max_price]

def main():
    # Create a filter system
    filter_system = FilterSystem()

    # Create products
    product1 = Product(1, "Python Course", ProductType.COURSE, ["programming", "python"], 99.99)
    product2 = Product(2, "Java Tutorial", ProductType.TUTORIAL, ["programming", "java"], 49.99)
    product3 = Product(3, "Data Science Ebook", ProductType.EBOOK, ["data science", "ebook"], 29.99)

    # Add products to the filter system
    filter_system.add_product(product1)
    filter_system.add_product(product2)
    filter_system.add_product(product3)

    # Filter products
    print("Courses:")
    for product in filter_system.filter_by_type(ProductType.COURSE):
        print(product.name)

    print("\nProducts in 'programming' category:")
    for product in filter_system.filter_by_category("programming"):
        print(product.name)

    print("\nProducts between $20 and $100:")
    for product in filter_system.filter_by_price_range(20, 100):
        print(f"{product.name}: ${product.price:.2f}")

if __name__ == "__main__":
    main()
```
