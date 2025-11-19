"""
Generated Code Metadata:
========================
Original URL: https://isoplas.com
Prompt: "Generate a product catalogue for a food packaging company that offers microwavable containers, dessert containers, drinking cups, and plastic cutlery."
Generated: DETERMINISTIC_7f79faf505524be0
Batch ID: 20250622_211805
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# product_catalogue.py

from enum import Enum
from typing import List, Dict

class ProductCategory(Enum):
    """Product categories for the food packaging company."""
    MICROWAVABLE_CONTAINERS = "Microwavable Containers"
    DESSERT_CONTAINERS = "Dessert Containers"
    DRINKING_CUPS = "Drinking Cups"
    PLASTIC_CUTLERY = "Plastic Cutlery"

class Product:
    """Represents a product in the catalogue."""
    def __init__(self, 
                 product_id: int, 
                 name: str, 
                 category: ProductCategory, 
                 description: str, 
                 price: float):
        """
        Initializes a Product instance.

        Args:
        product_id (int): Unique identifier for the product.
        name (str): Product name.
        category (ProductCategory): Product category.
        description (str): Product description.
        price (float): Product price.
        """
        self.product_id = product_id
        self.name = name
        self.category = category
        self.description = description
        self.price = price

    def __repr__(self):
        return f"Product({self.product_id}, {self.name}, {self.category}, {self.description}, {self.price})"

class ProductCatalogue:
    """Manages a collection of products."""
    def __init__(self):
        self.products: Dict[int, Product] = {}

    def add_product(self, product: Product):
        """
        Adds a product to the catalogue.

        Args:
        product (Product): Product to add.

        Raises:
        ValueError: If a product with the same ID already exists.
        """
        if product.product_id in self.products:
            raise ValueError("Product with the same ID already exists.")
        self.products[product.product_id] = product

    def remove_product(self, product_id: int):
        """
        Removes a product from the catalogue.

        Args:
        product_id (int): ID of the product to remove.

        Raises:
        KeyError: If the product ID is not found.
        """
        if product_id not in self.products:
            raise KeyError("Product ID not found.")
        del self.products[product_id]

    def get_product(self, product_id: int) -> Product:
        """
        Retrieves a product by ID.

        Args:
        product_id (int): ID of the product to retrieve.

        Returns:
        Product: The product instance.

        Raises:
        KeyError: If the product ID is not found.
        """
        return self.products[product_id]

    def list_products(self, category: ProductCategory = None) -> List[Product]:
        """
        Lists products in the catalogue.

        Args:
        category (ProductCategory): Optional category filter.

        Returns:
        List[Product]: List of products.
        """
        if category:
            return [product for product in self.products.values() if product.category == category]
        return list(self.products.values())

def main():
    catalogue = ProductCatalogue()

    # Add products
    catalogue.add_product(Product(1, "Microwavable Container", ProductCategory.MICROWAVABLE_CONTAINERS, "For heating food in the microwave.", 2.99))
    catalogue.add_product(Product(2, "Dessert Cup", ProductCategory.DESSERT_CONTAINERS, "For serving desserts.", 1.49))
    catalogue.add_product(Product(3, "Drinking Cup", ProductCategory.DRINKING_CUPS, "For hot or cold beverages.", 0.99))
    catalogue.add_product(Product(4, "Fork", ProductCategory.PLASTIC_CUTLERY, "For eating.", 0.25))

    # List products
    print("All Products:")
    for product in catalogue.list_products():
        print(product)

    print("\nMicrowavable Containers:")
    for product in catalogue.list_products(ProductCategory.MICROWAVABLE_CONTAINERS):
        print(product)

    # Get product
    print("\nGet Product:")
    product = catalogue.get_product(2)
    print(product)

    # Remove product
    catalogue.remove_product(3)

    # List products after removal
    print("\nProducts after removal:")
    for product in catalogue.list_products():
        print(product)

if __name__ == "__main__":
    main()
```
