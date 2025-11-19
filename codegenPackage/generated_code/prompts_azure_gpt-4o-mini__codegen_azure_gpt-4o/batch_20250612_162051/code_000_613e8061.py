"""
Generated Code Metadata:
========================
Original URL: https://simplementeairsoft.com
Prompt: Generate a code snippet for an e-commerce website that implements a shopping cart feature, similar to the one found on Simplymente Airsoft, allowing users to add tactical clothing items like sweatshirts and t-shirts.
Generated: DETERMINISTIC_613e8061b55954e8
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# shopping_cart.py

from typing import List, Dict

class Item:
    """
    Represents an item in the store.
    """
    def __init__(self, name: str, price: float, quantity: int = 1):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name} - ${self.price:.2f} x {self.quantity}"

    def total_price(self) -> float:
        """
        Calculate the total price for this item based on quantity.
        """
        return self.price * self.quantity


class ShoppingCart:
    """
    Represents a shopping cart for an e-commerce website.
    """
    def __init__(self):
        self.items: Dict[str, Item] = {}

    def add_item(self, name: str, price: float, quantity: int = 1):
        """
        Add an item to the shopping cart. If the item already exists, update its quantity.
        """
        if name in self.items:
            self.items[name].quantity += quantity
        else:
            self.items[name] = Item(name, price, quantity)

    def remove_item(self, name: str):
        """
        Remove an item from the shopping cart.
        """
        if name in self.items:
            del self.items[name]
        else:
            print(f"Item '{name}' not found in the cart.")

    def update_quantity(self, name: str, quantity: int):
        """
        Update the quantity of an item in the shopping cart.
        """
        if name in self.items:
            if quantity <= 0:
                self.remove_item(name)
            else:
                self.items[name].quantity = quantity
        else:
            print(f"Item '{name}' not found in the cart.")

    def view_cart(self) -> List[str]:
        """
        View all items in the shopping cart.
        """
        if not self.items:
            return ["Your cart is empty."]
        return [str(item) for item in self.items.values()]

    def calculate_total(self) -> float:
        """
        Calculate the total cost of all items in the shopping cart.
        """
        return sum(item.total_price() for item in self.items.values())


# Example usage
if __name__ == "__main__":
    try:
        cart = ShoppingCart()
        cart.add_item("Tactical Sweatshirt", 49.99, 2)
        cart.add_item("Tactical T-Shirt", 29.99, 1)
        cart.add_item("Tactical Sweatshirt", 49.99, 1)  # Adding more of the same item

        print("Cart Contents:")
        for item in cart.view_cart():
            print(item)

        print(f"Total Price: ${cart.calculate_total():.2f}")

        cart.update_quantity("Tactical T-Shirt", 3)
        print("\nUpdated Cart Contents:")
        for item in cart.view_cart():
            print(item)

        print(f"Total Price: ${cart.calculate_total():.2f}")

        cart.remove_item("Tactical Sweatshirt")
        print("\nCart Contents After Removal:")
        for item in cart.view_cart():
            print(item)

        print(f"Total Price: ${cart.calculate_total():.2f}")
    except Exception as e:
        print(f"An error occurred: {e}")
```
