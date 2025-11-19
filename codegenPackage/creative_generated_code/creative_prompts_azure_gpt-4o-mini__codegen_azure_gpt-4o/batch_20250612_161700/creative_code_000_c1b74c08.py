"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://karlakarita.com.br
Prompt: Generate a code snippet that creates a shopping cart feature for an e-commerce site selling casual clothing, similar to the offerings on karlakarita.com.br.
Generated: DETERMINISTIC_c1b74c08ec907773
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

# Import necessary modules
import uuid

# Define the ShoppingCart class
class ShoppingCart:
    """
    A class to represent a shopping cart for an e-commerce site.
    Allows adding, removing, and listing items, as well as calculating totals.
    """
    def __init__(self):
        """
        Initialize the shopping cart with an empty items dictionary.
        Each item will be stored as {item_id: {name, price, quantity}}.
        """
        self.items = {}

    def add_item(self, name, price, quantity=1):
        """
        Add an item to the cart.

        Args:
            name (str): Name of the item.
            price (float): Price of the item.
            quantity (int): Quantity of the item (default: 1).

        Returns:
            str: A confirmation message.
        """
        if quantity < 1:
            raise ValueError("Quantity must be at least 1.")

        item_id = str(uuid.uuid4())  # Generate a unique ID for the item
        self.items[item_id] = {
            "name": name,
            "price": price,
            "quantity": quantity
        }

        return f"Item '{name}' added to the cart."

    def remove_item(self, item_id):
        """
        Remove an item from the cart.

        Args:
            item_id (str): The unique ID of the item to remove.

        Returns:
            str: A confirmation message, or an error message if the item is not found.
        """
        if item_id in self.items:
            removed_item = self.items.pop(item_id)
            return f"Item '{removed_item['name']}' removed from the cart."
        else:
            return "Item not found in the cart."

    def list_items(self):
        """
        List all items in the cart.

        Returns:
            list: A list of dictionaries representing items in the cart.
        """
        return [
            {"id": item_id, **item_details}
            for item_id, item_details in self.items.items()
        ]

    def calculate_total(self):
        """
        Calculate the total cost of all items in the cart.

        Returns:
            float: The total cost.
        """
        return sum(item["price"] * item["quantity"] for item in self.items.values())

    def clear_cart(self):
        """
        Clear all items from the cart.

        Returns:
            str: A confirmation message.
        """
        self.items.clear()
        return "Cart has been cleared."


# Example usage
if __name__ == "__main__":
    # Create a new shopping cart
    cart = ShoppingCart()

    # Add items to the cart
    print(cart.add_item("T-Shirt", 19.99, 2))
    print(cart.add_item("Jeans", 49.99, 1))

    # List items in the cart
    print("Items in the cart:", cart.list_items())

    # Calculate the total cost
    print("Total cost:", cart.calculate_total())

    # Remove an item (replace with correct item ID for testing)
    for item in cart.list_items():
        print(cart.remove_item(item["id"]))

    # Clear the cart
    print(cart.clear_cart())

    # Final cart state
    print("Final cart state:", cart.list_items())
```
