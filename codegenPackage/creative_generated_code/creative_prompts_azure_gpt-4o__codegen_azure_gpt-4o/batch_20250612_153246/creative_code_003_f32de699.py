"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gvika.in
Prompt: Write a script to implement a shopping cart system in an online store, ensuring it supports subtotal calculations and checkout options, as seen on Gvika's website.
Generated: DETERMINISTIC_f32de699b6cd2eca
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid
from typing import List

class Product:
    """
    Represents a product in the store.
    """
    def __init__(self, name: str, price: float):
        if price < 0:
            raise ValueError("Price cannot be negative.")
        self.id = str(uuid.uuid4())  # Unique identifier for the product
        self.name = name
        self.price = price

    def __repr__(self):
        return f"Product(id={self.id}, name={self.name}, price={self.price})"


class ShoppingCart:
    """
    Represents a shopping cart system.
    """
    def __init__(self):
        self.items: List[Product] = []

    def add_item(self, product: Product) -> None:
        """
        Adds a product to the shopping cart.
        """
        self.items.append(product)
        print(f"{product.name} has been added to the cart.")

    def remove_item(self, product_id: str) -> None:
        """
        Removes a product from the shopping cart by its ID.
        """
        for item in self.items:
            if item.id == product_id:
                self.items.remove(item)
                print(f"{item.name} has been removed from the cart.")
                return
        print("Item not found in the cart.")

    def calculate_subtotal(self) -> float:
        """
        Calculates the subtotal of all items in the cart.
        """
        return sum(item.price for item in self.items)

    def checkout(self) -> None:
        """
        Displays the checkout details and clears the cart.
        """
        if not self.items:
            print("Your cart is empty. Add items before checkout.")
            return

        print("Checkout Summary:")
        for item in self.items:
            print(f"- {item.name}: ${item.price:.2f}")
        print(f"Subtotal: ${self.calculate_subtotal():.2f}")
        self.items.clear()
        print("Thank you for your purchase!")

# Example usage
if __name__ == "__main__":
    try:
        # Create some products
        apple = Product(name="Apple", price=0.99)
        banana = Product(name="Banana", price=0.59)
        chocolate = Product(name="Chocolate Bar", price=1.49)

        # Initialize shopping cart
        cart = ShoppingCart()

        # Add items to the cart
        cart.add_item(apple)
        cart.add_item(banana)
        cart.add_item(chocolate)

        # Display subtotal
        print(f"Cart Subtotal: ${cart.calculate_subtotal():.2f}")

        # Remove an item
        cart.remove_item(apple.id)

        # Checkout
        cart.checkout()

    except Exception as e:
        print(f"An error occurred: {e}")
```
