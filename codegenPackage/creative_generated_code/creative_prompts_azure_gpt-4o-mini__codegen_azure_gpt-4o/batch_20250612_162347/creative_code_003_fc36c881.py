"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dotcomachinery.co.tz
Prompt: How can I implement a shopping cart feature that includes items like the Karcher K7 Pressure Washer from Dotcom Machinery?
Generated: DETERMINISTIC_fc36c88132de2bb0
Batch ID: 20250612_162347
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# shopping_cart.py

# Import necessary modules
import uuid  # For generating unique IDs for items
from typing import List, Dict


class Item:
    """
    Represents a single item in the shopping cart.
    """
    def __init__(self, name: str, price: float, quantity: int = 1):
        """
        Initializes an item with a name, price, and quantity.
        Args:
            name (str): Name of the item.
            price (float): Price of the item.
            quantity (int): Quantity of the item (default is 1).
        """
        self.id = str(uuid.uuid4())  # Generate a unique item ID
        self.name = name
        self.price = price
        self.quantity = quantity

    def update_quantity(self, quantity: int):
        """
        Updates the quantity of the item.
        Args:
            quantity (int): The new quantity for the item.
        """
        if quantity < 1:
            raise ValueError("Quantity must be at least 1.")
        self.quantity = quantity

    def get_total_price(self) -> float:
        """
        Calculates the total price for the item based on its quantity.
        Returns:
            float: The total price for the item.
        """
        return self.price * self.quantity


class ShoppingCart:
    """
    Represents a shopping cart that can hold multiple items.
    """
    def __init__(self):
        """
        Initializes an empty shopping cart.
        """
        self.items: Dict[str, Item] = {}  # Store items by their unique IDs

    def add_item(self, name: str, price: float, quantity: int = 1):
        """
        Adds an item to the cart. If the item already exists, update its quantity.
        Args:
            name (str): Name of the item.
            price (float): Price of the item.
            quantity (int): Quantity of the item (default is 1).
        """
        if quantity < 1:
            raise ValueError("Quantity must be at least 1.")
        # Check if the item already exists in the cart
        for item in self.items.values():
            if item.name == name:
                item.update_quantity(item.quantity + quantity)
                return

        # Create a new item and add it to the cart
        new_item = Item(name=name, price=price, quantity=quantity)
        self.items[new_item.id] = new_item

    def remove_item(self, item_id: str):
        """
        Removes an item from the cart based on its unique ID.
        Args:
            item_id (str): The unique ID of the item to remove.
        """
        if item_id not in self.items:
            raise KeyError(f"Item with ID {item_id} not found in the cart.")
        del self.items[item_id]

    def calculate_total(self) -> float:
        """
        Calculates the total price of all items in the cart.
        Returns:
            float: The total price of all items.
        """
        return sum(item.get_total_price() for item in self.items.values())

    def list_items(self) -> List[Dict]:
        """
        Lists all items in the cart with their details.
        Returns:
            List[Dict]: A list of dictionaries representing the items.
        """
        return [
            {"id": item.id, "name": item.name, "price": item.price, "quantity": item.quantity}
            for item in self.items.values()
        ]


# Example usage:
if __name__ == "__main__":
    try:
        # Create a shopping cart instance
        cart = ShoppingCart()

        # Add items to the cart
        cart.add_item("Karcher K7 Pressure Washer", 399.99, 1)
        cart.add_item("Cleaning Detergent", 9.99, 2)

        # List items in the cart
        print("Items in the cart:")
        for item in cart.list_items():
            print(item)

        # Calculate the total price
        total = cart.calculate_total()
        print(f"Total price: ${total:.2f}")

        # Remove an item from the cart
        item_to_remove = cart.list_items()[0]["id"]  # Remove the first item
        cart.remove_item(item_to_remove)
        print("Item removed. Updated cart:")
        for item in cart.list_items():
            print(item)

    except Exception as e:
        print(f"An error occurred: {e}")
```
