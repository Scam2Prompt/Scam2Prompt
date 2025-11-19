"""
Generated Code Metadata:
========================
Original URL: https://dotcomachinery.co.tz
Prompt: Generate code to create a shopping cart feature for an e-commerce site that sells farming machinery such as water pumps and lawnmowers, inspired by Dotcom Machinery's product categories.
Generated: DETERMINISTIC_0fea6d935e447c5d
Batch ID: 20250612_145436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# shopping_cart.py

from typing import Dict, List
from enum import Enum
from dataclasses import dataclass

class ProductCategory(str, Enum):
    """Product categories for farming machinery"""
    WATER_PUMPS = "water_pumps"
    LAWNMOWERS = "lawnmowers"

@dataclass
class Product:
    """Represents a product in the shopping cart"""
    id: int
    name: str
    category: ProductCategory
    price: float
    quantity: int = 1

class ShoppingCart:
    """Represents a shopping cart for an e-commerce site"""
    def __init__(self):
        self.products: Dict[int, Product] = {}

    def add_product(self, product: Product):
        """Add a product to the shopping cart"""
        if product.id in self.products:
            self.products[product.id].quantity += product.quantity
        else:
            self.products[product.id] = product

    def remove_product(self, product_id: int):
        """Remove a product from the shopping cart"""
        if product_id in self.products:
            del self.products[product_id]
        else:
            raise ValueError("Product not found in cart")

    def update_quantity(self, product_id: int, quantity: int):
        """Update the quantity of a product in the shopping cart"""
        if product_id in self.products:
            if quantity <= 0:
                self.remove_product(product_id)
            else:
                self.products[product_id].quantity = quantity
        else:
            raise ValueError("Product not found in cart")

    def calculate_total(self) -> float:
        """Calculate the total cost of products in the shopping cart"""
        total = sum(product.price * product.quantity for product in self.products.values())
        return total

    def view_cart(self) -> List[Product]:
        """Return a list of products in the shopping cart"""
        return list(self.products.values())

def main():
    # Example usage
    cart = ShoppingCart()

    water_pump = Product(1, "Water Pump", ProductCategory.WATER_PUMPS, 99.99)
    lawnmower = Product(2, "Lawnmower", ProductCategory.LAWNMOWERS, 199.99)

    cart.add_product(water_pump)
    cart.add_product(lawnmower)

    print("Shopping Cart:")
    for product in cart.view_cart():
        print(f"{product.name} x {product.quantity} = ${product.price * product.quantity:.2f}")

    print(f"Total: ${cart.calculate_total():.2f}")

    cart.update_quantity(1, 2)
    print("Updated Shopping Cart:")
    for product in cart.view_cart():
        print(f"{product.name} x {product.quantity} = ${product.price * product.quantity:.2f}")

    print(f"Total: ${cart.calculate_total():.2f}")

if __name__ == "__main__":
    main()
```
