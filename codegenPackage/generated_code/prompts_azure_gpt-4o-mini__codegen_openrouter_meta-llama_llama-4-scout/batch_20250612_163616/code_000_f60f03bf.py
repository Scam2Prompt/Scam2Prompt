"""
Generated Code Metadata:
========================
Original URL: https://mixpelinfobrazz.blogspot.com
Prompt: Generate a code snippet for an inventory management system that tracks computer hardware and accessories like SSDs and projectors, similar to the offerings on mixpelinfobrazz.
Generated: DETERMINISTIC_f60f03bf7ef5e141
Batch ID: 20250612_163616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# inventory_management_system.py

from typing import Dict, List
from enum import Enum
from dataclasses import dataclass

class ProductType(str, Enum):
    """Product type enumeration"""
    SSD = "SSD"
    PROJECTOR = "Projector"
    LAPTOP = "Laptop"
    MONITOR = "Monitor"
    KEYBOARD = "Keyboard"
    MOUSE = "Mouse"

@dataclass
class Product:
    """Product data class"""
    id: int
    name: str
    product_type: ProductType
    quantity: int
    price: float

class InventoryManagementSystem:
    """Inventory management system class"""

    def __init__(self):
        self.products: Dict[int, Product] = {}
        self.id_counter: int = 1

    def add_product(self, name: str, product_type: ProductType, quantity: int, price: float) -> Product:
        """Add a product to the inventory"""
        product = Product(self.id_counter, name, product_type, quantity, price)
        self.products[self.id_counter] = product
        self.id_counter += 1
        return product

    def remove_product(self, id: int) -> None:
        """Remove a product from the inventory"""
        if id in self.products:
            del self.products[id]
        else:
            raise ValueError("Product not found")

    def update_product(self, id: int, name: str = None, product_type: ProductType = None, quantity: int = None, price: float = None) -> Product:
        """Update a product in the inventory"""
        if id in self.products:
            product = self.products[id]
            if name:
                product.name = name
            if product_type:
                product.product_type = product_type
            if quantity:
                product.quantity = quantity
            if price:
                product.price = price
            return product
        else:
            raise ValueError("Product not found")

    def get_product(self, id: int) -> Product:
        """Get a product from the inventory"""
        return self.products.get(id)

    def list_products(self) -> List[Product]:
        """List all products in the inventory"""
        return list(self.products.values())

def main():
    inventory = InventoryManagementSystem()

    # Add some products
    ssd = inventory.add_product("Samsung SSD", ProductType.SSD, 10, 99.99)
    projector = inventory.add_product("Epson Projector", ProductType.PROJECTOR, 5, 499.99)
    laptop = inventory.add_product("Dell Laptop", ProductType.LAPTOP, 20, 999.99)

    # List all products
    print("All products:")
    for product in inventory.list_products():
        print(f"ID: {product.id}, Name: {product.name}, Type: {product.product_type}, Quantity: {product.quantity}, Price: {product.price}")

    # Update a product
    inventory.update_product(ssd.id, quantity=15)
    print(f"\nUpdated SSD quantity: {inventory.get_product(ssd.id).quantity}")

    # Remove a product
    inventory.remove_product(projector.id)
    print(f"\nProduct {projector.id} removed")

if __name__ == "__main__":
    main()
```
