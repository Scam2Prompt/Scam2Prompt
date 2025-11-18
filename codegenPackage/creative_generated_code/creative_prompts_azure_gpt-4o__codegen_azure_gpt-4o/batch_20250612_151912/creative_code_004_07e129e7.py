"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://adhive.net
Prompt: Write a script to implement a "View Cart" functionality for an online store, similar to the one described on Adhive Marketplace.
Generated: DETERMINISTIC_07e129e7c7eedbb4
Batch ID: 20250612_151912
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# view_cart.py

# Import necessary libraries
from typing import List, Dict


class Cart:
    """
    Class representing a shopping cart in an online store.

    Attributes:
        items (List[Dict]): A list of items in the cart. Each item is represented as a dictionary.
    """

    def __init__(self):
        """
        Initialize the shopping cart with an empty list of items.
        """
        self.items: List[Dict] = []

    def add_item(self, item_name: str, price: float, quantity: int = 1) -> None:
        """
        Add an item to the cart.

        Args:
            item_name (str): Name of the item.
            price (float): Price of the item (per unit).
            quantity (int): Quantity of the item. Defaults to 1.

        Raises:
            ValueError: If price or quantity are invalid.
        """
        if price <= 0:
            raise ValueError("Price must be greater than zero.")
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")

        # Check if item already exists in the cart
        for item in self.items:
            if item["item_name"] == item_name:
                item["quantity"] += quantity
                return

        # If item doesn't exist, add it as a new entry
        self.items.append({"item_name": item_name, "price": price, "quantity": quantity})

    def remove_item(self, item_name: str) -> None:
        """
        Remove an item from the cart.

        Args:
            item_name (str): Name of the item to be removed.

        Raises:
            ValueError: If the item is not found in the cart.
        """
        for item in self.items:
            if item["item_name"] == item_name:
                self.items.remove(item)
                return

        raise ValueError(f"Item '{item_name}' not found in the cart.")

    def view_cart(self) -> None:
        """
        Display the items in the cart along with their details.
        """
        if not self.items:
            print("Your cart is empty.")
            return

        print("Your Cart:")
        print("=" * 40)
        total_cost = 0.0

        for item in self.items:
            item_total = item["price"] * item["quantity"]
            total_cost += item_total
            print(f"Item: {item['item_name']}")
            print(f"  Price: ${item['price']:.2f}")
            print(f"  Quantity: {item['quantity']}")
            print(f"  Total: ${item_total:.2f}")
            print("-" * 40)

        print(f"Total Cost: ${total_cost:.2f}")
        print("=" * 40)


# Example Usage
if __name__ == "__main__":
    try:
        cart = Cart()

        # Add items to the cart
        cart.add_item("Laptop", 1200.00, 1)
        cart.add_item("Headphones", 200.00, 2)
        cart.add_item("Mouse", 50.00, 1)

        # View cart
        cart.view_cart()

        # Remove an item
        cart.remove_item("Mouse")
        print("\nAfter removing 'Mouse':")
        cart.view_cart()

    except Exception as e:
        print(f"Error: {e}")
```
