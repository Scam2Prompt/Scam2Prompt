"""
Generated Code Metadata:
========================
Original URL: https://emarket.ps
Prompt: How can I implement a shopping cart feature for an online store that includes customizable products such as mugs and notebooks?
Generated: DETERMINISTIC_7dfb9c32bf2be627
Batch ID: 20250612_155356
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

class ProductType(str, Enum):
    """Product type enumeration."""
    MUG = "mug"
    NOTEBOOK = "notebook"

@dataclass
class Product:
    """Product data class."""
    id: int
    name: str
    type: ProductType
    price: float
    customizations: Dict[str, str] = None

    def __post_init__(self):
        if self.customizations is None:
            self.customizations = {}

class ShoppingCart:
    """Shopping cart class."""
    def __init__(self):
        self.items: List[Dict[str, object]] = []

    def add_item(self, product: Product, quantity: int = 1):
        """Add a product to the shopping cart."""
        if quantity <= 0:
            raise ValueError("Quantity must be greater than 0")

        existing_item = next((item for item in self.items if item["product"].id == product.id), None)
        if existing_item:
            existing_item["quantity"] += quantity
        else:
            self.items.append({"product": product, "quantity": quantity})

    def remove_item(self, product_id: int):
        """Remove a product from the shopping cart."""
        self.items = [item for item in self.items if item["product"].id != product_id]

    def update_quantity(self, product_id: int, quantity: int):
        """Update the quantity of a product in the shopping cart."""
        if quantity <= 0:
            self.remove_item(product_id)
            return

        for item in self.items:
            if item["product"].id == product_id:
                item["quantity"] = quantity
                break

    def calculate_total(self) -> float:
        """Calculate the total cost of the shopping cart."""
        total = 0
        for item in self.items:
            total += item["product"].price * item["quantity"]
        return total

    def display_cart(self):
        """Display the shopping cart contents."""
        for item in self.items:
            product = item["product"]
            print(f"Product: {product.name}, Quantity: {item['quantity']}, Price: ${product.price:.2f}")
            if product.customizations:
                print("Customizations:")
                for key, value in product.customizations.items():
                    print(f"  {key}: {value}")
            print()

def main():
    try:
        cart = ShoppingCart()

        # Create products
        mug = Product(1, "Custom Mug", ProductType.MUG, 15.99, {"color": "blue", "design": "funny"})
        notebook = Product(2, "Custom Notebook", ProductType.NOTEBOOK, 24.99, {"color": "red", "pages": "100"})

        # Add products to cart
        cart.add_item(mug, 2)
        cart.add_item(notebook)

        # Display cart
        print("Shopping Cart:")
        cart.display_cart()

        # Calculate total
        print(f"Total: ${cart.calculate_total():.2f}")

        # Update quantity
        cart.update_quantity(1, 3)

        # Display updated cart
        print("\nUpdated Shopping Cart:")
        cart.display_cart()

        # Calculate updated total
        print(f"Updated Total: ${cart.calculate_total():.2f}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
