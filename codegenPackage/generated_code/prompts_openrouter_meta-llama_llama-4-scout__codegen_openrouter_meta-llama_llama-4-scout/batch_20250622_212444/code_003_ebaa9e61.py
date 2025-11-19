"""
Generated Code Metadata:
========================
Original URL: https://cm-canada.ca
Prompt: "Generate a Python code snippet to manage inventory for a construction supply company like One World Supply, including product categories such as valves, couplings, and plumbing fixtures."
Generated: DETERMINISTIC_ebaa9e61860a371b
Batch ID: 20250622_212444
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# inventory_management.py

from enum import Enum
from typing import Dict, List

class ProductCategory(str, Enum):
    """Product categories for construction supplies."""
    VALVES = "valves"
    COUPLINGS = "couplings"
    PLUMBING_FIXTURES = "plumbing_fixtures"

class Product:
    """Represents a product in the inventory."""
    
    def __init__(self, id: int, name: str, category: ProductCategory, quantity: int, price: float):
        """
        Initializes a Product instance.

        Args:
        id (int): Unique product ID.
        name (str): Product name.
        category (ProductCategory): Product category.
        quantity (int): Product quantity in stock.
        price (float): Product price.
        """
        self.id = id
        self.name = name
        self.category = category
        self.quantity = quantity
        self.price = price

class Inventory:
    """Manages the inventory of construction supplies."""
    
    def __init__(self):
        """Initializes an empty inventory."""
        self.products: Dict[int, Product] = {}

    def add_product(self, product: Product):
        """
        Adds a product to the inventory.

        Args:
        product (Product): Product to add.

        Raises:
        ValueError: If a product with the same ID already exists.
        """
        if product.id in self.products:
            raise ValueError("Product with the same ID already exists.")
        self.products[product.id] = product

    def remove_product(self, id: int):
        """
        Removes a product from the inventory.

        Args:
        id (int): ID of the product to remove.

        Raises:
        KeyError: If the product does not exist in the inventory.
        """
        if id not in self.products:
            raise KeyError("Product does not exist in the inventory.")
        del self.products[id]

    def update_product_quantity(self, id: int, new_quantity: int):
        """
        Updates the quantity of a product in the inventory.

        Args:
        id (int): ID of the product to update.
        new_quantity (int): New quantity of the product.

        Raises:
        KeyError: If the product does not exist in the inventory.
        ValueError: If the new quantity is negative.
        """
        if id not in self.products:
            raise KeyError("Product does not exist in the inventory.")
        if new_quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self.products[id].quantity = new_quantity

    def get_product(self, id: int) -> Product:
        """
        Retrieves a product from the inventory.

        Args:
        id (int): ID of the product to retrieve.

        Returns:
        Product: The product with the specified ID.

        Raises:
        KeyError: If the product does not exist in the inventory.
        """
        if id not in self.products:
            raise KeyError("Product does not exist in the inventory.")
        return self.products[id]

    def get_products_by_category(self, category: ProductCategory) -> List[Product]:
        """
        Retrieves a list of products in the specified category.

        Args:
        category (ProductCategory): Category of products to retrieve.

        Returns:
        List[Product]: List of products in the specified category.
        """
        return [product for product in self.products.values() if product.category == category]

def main():
    # Example usage:
    inventory = Inventory()

    # Create products
    valve = Product(1, "Ball Valve", ProductCategory.VALVES, 10, 50.0)
    coupling = Product(2, "Pipe Coupling", ProductCategory.COUPLINGS, 20, 10.0)
    fixture = Product(3, "Sink Fixture", ProductCategory.PLUMBING_FIXTURES, 5, 100.0)

    # Add products to inventory
    inventory.add_product(valve)
    inventory.add_product(coupling)
    inventory.add_product(fixture)

    # Retrieve product
    print(inventory.get_product(1).name)  # Output: Ball Valve

    # Update product quantity
    inventory.update_product_quantity(2, 15)
    print(inventory.get_product(2).quantity)  # Output: 15

    # Retrieve products by category
    valves = inventory.get_products_by_category(ProductCategory.VALVES)
    for valve in valves:
        print(valve.name)  # Output: Ball Valve

if __name__ == "__main__":
    main()
```
