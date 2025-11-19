"""
Generated Code Metadata:
========================
Original URL: https://www.eclat.com.tr
Prompt: Write a Python code snippet to manage an e-commerce inventory system for a beauty store like Eclat, including products such as nail polish, nail art supplies, and eyelash extensions.
Generated: DETERMINISTIC_e362bc32664413e7
Batch ID: 20250622_205955
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# e-commerce_inventory_system.py

from typing import Dict, List
from enum import Enum
from dataclasses import dataclass

class ProductType(str, Enum):
    """Product types"""
    NAIL_POLISH = "nail_polish"
    NAIL_ART_SUPPLIES = "nail_art_supplies"
    EYELASH_EXTENSIONS = "eyelash_extensions"

@dataclass
class Product:
    """Product data class"""
    id: int
    name: str
    product_type: ProductType
    price: float
    quantity: int

class InventorySystem:
    """E-commerce inventory system"""

    def __init__(self):
        self.products: Dict[int, Product] = {}
        self.product_id_counter: int = 1

    def add_product(self, name: str, product_type: ProductType, price: float, quantity: int) -> Product:
        """Add a product to the inventory"""
        if price <= 0:
            raise ValueError("Price must be greater than zero")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")

        product = Product(self.product_id_counter, name, product_type, price, quantity)
        self.products[self.product_id_counter] = product
        self.product_id_counter += 1
        return product

    def update_product(self, product_id: int, name: str = None, price: float = None, quantity: int = None) -> Product:
        """Update a product in the inventory"""
        if product_id not in self.products:
            raise ValueError("Product not found")

        product = self.products[product_id]
        if name:
            product.name = name
        if price:
            if price <= 0:
                raise ValueError("Price must be greater than zero")
            product.price = price
        if quantity:
            if quantity < 0:
                raise ValueError("Quantity cannot be negative")
            product.quantity = quantity
        return product

    def delete_product(self, product_id: int) -> None:
        """Delete a product from the inventory"""
        if product_id not in self.products:
            raise ValueError("Product not found")
        del self.products[product_id]

    def get_product(self, product_id: int) -> Product:
        """Get a product from the inventory"""
        return self.products.get(product_id)

    def list_products(self) -> List[Product]:
        """List all products in the inventory"""
        return list(self.products.values())

def main():
    # Create an instance of the inventory system
    inventory = InventorySystem()

    # Add some products
    nail_polish = inventory.add_product("Red Nail Polish", ProductType.NAIL_POLISH, 10.99, 100)
    nail_art_supplies = inventory.add_product("Nail Art Brushes", ProductType.NAIL_ART_SUPPLIES, 5.99, 50)
    eyelash_extensions = inventory.add_product("Eyelash Extensions", ProductType.EYELASH_EXTENSIONS, 19.99, 20)

    # List all products
    print("Products:")
    for product in inventory.list_products():
        print(f"ID: {product.id}, Name: {product.name}, Type: {product.product_type}, Price: ${product.price:.2f}, Quantity: {product.quantity}")

    # Update a product
    updated_nail_polish = inventory.update_product(nail_polish.id, price=11.99)
    print(f"\nUpdated {updated_nail_polish.name} price to ${updated_nail_polish.price:.2f}")

    # Delete a product
    inventory.delete_product(nail_art_supplies.id)
    print(f"\nDeleted {nail_art_supplies.name}")

    # Try to get a deleted product
    try:
        inventory.get_product(nail_art_supplies.id)
    except Exception as e:
        print(f"\nError: {e}")

if __name__ == "__main__":
    main()
```
