"""
Generated Code Metadata:
========================
Original URL: https://homefoodsghana.com
Prompt: Write a Python code snippet to manage inventory for a company like Homefoods that produces various food products, including seasonings and ready-to-eat meals.
Generated: DETERMINISTIC_c68455710de66750
Batch ID: 20250622_211659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# inventory_manager.py

from typing import Dict, List
from dataclasses import dataclass
from enum import Enum

class ProductType(str, Enum):
    """Product type enumeration."""
    SEASONING = "seasoning"
    READY_TO_EAT = "ready_to_eat"

@dataclass
class Product:
    """Product data class."""
    id: int
    name: str
    product_type: ProductType
    quantity: int
    price: float

class Inventory:
    """Inventory management class."""
    def __init__(self):
        self.products: Dict[int, Product] = {}

    def add_product(self, product: Product):
        """Add a product to the inventory."""
        if product.id in self.products:
            raise ValueError(f"Product with ID {product.id} already exists.")
        self.products[product.id] = product

    def remove_product(self, product_id: int):
        """Remove a product from the inventory."""
        if product_id not in self.products:
            raise ValueError(f"Product with ID {product_id} does not exist.")
        del self.products[product_id]

    def update_quantity(self, product_id: int, new_quantity: int):
        """Update the quantity of a product in the inventory."""
        if product_id not in self.products:
            raise ValueError(f"Product with ID {product_id} does not exist.")
        if new_quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self.products[product_id].quantity = new_quantity

    def get_product(self, product_id: int) -> Product:
        """Get a product from the inventory."""
        try:
            return self.products[product_id]
        except KeyError:
            raise ValueError(f"Product with ID {product_id} does not exist.")

    def list_products(self) -> List[Product]:
        """List all products in the inventory."""
        return list(self.products.values())

def main():
    # Create an inventory
    inventory = Inventory()

    # Create products
    seasoning = Product(1, "Seasoning", ProductType.SEASONING, 100, 2.99)
    ready_to_eat = Product(2, "Ready-to-Eat Meal", ProductType.READY_TO_EAT, 50, 5.99)

    # Add products to the inventory
    inventory.add_product(seasoning)
    inventory.add_product(ready_to_eat)

    # List products
    print("Products:")
    for product in inventory.list_products():
        print(f"ID: {product.id}, Name: {product.name}, Type: {product.product_type.value}, Quantity: {product.quantity}, Price: ${product.price:.2f}")

    # Update quantity
    inventory.update_quantity(1, 80)

    # Get product
    print("\nUpdated Seasoning Quantity:")
    print(inventory.get_product(1).quantity)

    # Remove product
    inventory.remove_product(2)

    # Try to get removed product
    try:
        inventory.get_product(2)
    except ValueError as e:
        print(f"\nError: {e}")

if __name__ == "__main__":
    main()
```
