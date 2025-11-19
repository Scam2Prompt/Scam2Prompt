"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tuningdesign.gr
Prompt: Illustrate how to implement a shopping cart feature for automotive parts, taking cues from Tuning Design's user interface.
Generated: DETERMINISTIC_584ae135c0cb48b1
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# shopping_cart.py
# This module implements a simple shopping cart feature for automotive parts.
# It includes classes for Cart and Item, and methods for adding, removing, and viewing items.

class Item:
    """Represents a single item in the shopping cart."""
    
    def __init__(self, item_id, name, price, quantity=1):
        """
        Initializes an Item instance.

        :param item_id: Unique identifier for the item.
        :param name: Name of the item.
        :param price: Price of the item.
        :param quantity: Quantity of the item (defaults to 1).
        """
        self.item_id = item_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        """String representation of the item."""
        return f"{self.name} (ID: {self.item_id}, Price: ${self.price:.2f}, Quantity: {self.quantity})"


class ShoppingCart:
    """Represents a shopping cart for automotive parts."""
    
    def __init__(self):
        """Initializes an empty shopping cart."""
        self.items = {}

    def add_item(self, item):
        """
        Adds an item to the shopping cart. If the item already exists,
        updates the quantity.

        :param item: An instance of Item to add to the cart.
        """
        if not isinstance(item, Item):
            raise TypeError("Expected an instance of Item.")
        
        if item.item_id in self.items:
            self.items[item.item_id].quantity += item.quantity
        else:
            self.items[item.item_id] = item

    def remove_item(self, item_id):
        """
        Removes an item from the shopping cart by item ID.

        :param item_id: The unique identifier of the item to remove.
        """
        if item_id in self.items:
            del self.items[item_id]
        else:
            raise KeyError(f"Item ID {item_id} not found in the cart.")

    def view_cart(self):
        """Returns a summary of items in the shopping cart."""
        if not self.items:
            return "The shopping cart is empty."

        cart_summary = ["Shopping Cart Summary:"]
        total_price = 0.0
        
        for item in self.items.values():
            cart_summary.append(str(item))
            total_price += item.price * item.quantity
        
        cart_summary.append(f"Total Price: ${total_price:.2f}")
        return "\n".join(cart_summary)

    def clear_cart(self):
        """Clears all items from the shopping cart."""
        self.items.clear()


# Example Usage
if __name__ == "__main__":
    try:
        cart = ShoppingCart()
        
        # Adding items to the cart
        item1 = Item(item_id=1, name="Brake Pads", price=49.99, quantity=2)
        item2 = Item(item_id=2, name="Air Filter", price=19.99, quantity=1)

        cart.add_item(item1)
        cart.add_item(item2)

        # Viewing the cart
        print(cart.view_cart())

        # Removing an item from the cart
        cart.remove_item(1)
        print("\nAfter removing Brake Pads:")
        print(cart.view_cart())

        # Clearing the cart
        cart.clear_cart()
        print("\nAfter clearing the cart:")
        print(cart.view_cart())

    except Exception as e:
        print(f"An error occurred: {e}")
```
