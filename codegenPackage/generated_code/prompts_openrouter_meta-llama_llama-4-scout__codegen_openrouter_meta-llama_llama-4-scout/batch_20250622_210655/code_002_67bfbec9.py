"""
Generated Code Metadata:
========================
Original URL: https://vividolev.com
Prompt: Write a code snippet to manage inventory for a company like Vivid Olev that produces various types of vegetable oils and green fuels.
Generated: DETERMINISTIC_67bfbec98eeca4f1
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# inventory_management.py

from typing import Dict, List
from dataclasses import dataclass
from enum import Enum
from datetime import datetime

class ProductType(str, Enum):
    VEGETABLE_OIL = "vegetable_oil"
    GREEN_FUEL = "green_fuel"

@dataclass
class Product:
    id: int
    name: str
    product_type: ProductType
    quantity: float
    unit_price: float

class Inventory:
    def __init__(self):
        self.products: Dict[int, Product] = {}

    def add_product(self, product: Product):
        """Add a product to the inventory."""
        self.products[product.id] = product

    def remove_product(self, product_id: int):
        """Remove a product from the inventory."""
        if product_id in self.products:
            del self.products[product_id]
        else:
            raise ValueError(f"Product with ID {product_id} not found")

    def update_product_quantity(self, product_id: int, new_quantity: float):
        """Update the quantity of a product in the inventory."""
        if product_id in self.products:
            self.products[product_id].quantity = new_quantity
        else:
            raise ValueError(f"Product with ID {product_id} not found")

    def get_product(self, product_id: int) -> Product:
        """Get a product from the inventory."""
        return self.products.get(product_id)

    def get_all_products(self) -> List[Product]:
        """Get all products in the inventory."""
        return list(self.products.values())

    def calculate_total_value(self) -> float:
        """Calculate the total value of all products in the inventory."""
        total_value = 0
        for product in self.products.values():
            total_value += product.quantity * product.unit_price
        return total_value

def main():
    inventory = Inventory()

    # Create some products
    product1 = Product(1, "Olive Oil", ProductType.VEGETABLE_OIL, 1000, 5.99)
    product2 = Product(2, "Biodiesel", ProductType.GREEN_FUEL, 500, 3.99)

    # Add products to the inventory
    inventory.add_product(product1)
    inventory.add_product(product2)

    # Print all products
    print("All Products:")
    for product in inventory.get_all_products():
        print(f"ID: {product.id}, Name: {product.name}, Quantity: {product.quantity}, Unit Price: {product.unit_price}")

    # Update product quantity
    inventory.update_product_quantity(1, 800)

    # Print updated product quantity
    print("\nUpdated Product Quantity:")
    print(f"ID: {product1.id}, Name: {product1.name}, Quantity: {inventory.get_product(product1.id).quantity}")

    # Calculate total value
    print("\nTotal Value:")
    print(f"Total Value: {inventory.calculate_total_value()}")

    # Remove product
    inventory.remove_product(2)

    # Try to get removed product
    try:
        inventory.get_product(2)
    except Exception as e:
        print(f"\nError: {e}")

if __name__ == "__main__":
    main()
```
