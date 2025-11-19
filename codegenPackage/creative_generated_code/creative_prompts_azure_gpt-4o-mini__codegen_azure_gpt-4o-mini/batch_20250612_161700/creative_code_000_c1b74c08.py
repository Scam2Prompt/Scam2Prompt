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

from typing import List, Dict

class Item:
    """Class representing an item in the shopping cart."""

    def __init__(self, item_id: str, name: str, price: float, quantity: int = 1):
        """
        Initialize an item with an ID, name, price, and quantity.

        Parameters:
            item_id (str): Unique identifier for the item.
            name (str): Name of the item.
            price (float): Price of the item.
            quantity (int): Quantity of the item to be added to the cart.
        """
        self.item_id = item_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_price(self) -> float:
        """Calculate the total price for this item based on quantity."""
        return self.price * self.quantity


class ShoppingCart:
    """Class representing the shopping cart."""

    def __init__(self):
        """Initialize an empty shopping cart."""
        self.items: List[Item] = []

    def add_item(self, item: Item) -> None:
        """Add an item to the shopping cart.

        Parameters:
            item (Item): The item to add to the cart.
        """
        # Check if item already exists in cart
        for existing_item in self.items:
            if existing_item.item_id == item.item_id:
                existing_item.quantity += item.quantity
                return
        self.items.append(item)

    def remove_item(self, item_id: str) -> None:
        """Remove an item from the shopping cart by item ID.

        Parameters:
            item_id (str): The ID of the item to remove.
        """
        self.items = [item for item in self.items if item.item_id != item_id]

    def get_total(self) -> float:
        """Calculate the total price of all items in the cart."""
        return sum(item.total_price() for item in self.items)

    def clear_cart(self) -> None:
        """Clear all items from the shopping cart."""
        self.items = []

    def list_items(self) -> List[Dict[str, str]]:
        """List all items in the shopping cart.

        Returns:
            List[Dict[str, str]]: A list of items with their details.
        """
        return [{"item_id": item.item_id, "name": item.name, "price": item.price, "quantity": item.quantity} for item in self.items]


# Example usage (this would usually be in a separate application file)
if __name__ == "__main__":
    cart = ShoppingCart()

    # Adding items to the cart
    cart.add_item(Item(item_id="1", name="Casual T-Shirt", price=29.99))
    cart.add_item(Item(item_id="2", name="Comfortable Jeans", price=49.99, quantity=2))

    # Listing items in cart
    print("Items in cart:", cart.list_items())

    # Getting total price
    print("Total price:", cart.get_total())

    # Removing an item from the cart
    cart.remove_item("1")
    print("Items in cart after removal:", cart.list_items())

    # Clear cart
    cart.clear_cart()
    print("Items in cart after clearing:", cart.list_items())
```
