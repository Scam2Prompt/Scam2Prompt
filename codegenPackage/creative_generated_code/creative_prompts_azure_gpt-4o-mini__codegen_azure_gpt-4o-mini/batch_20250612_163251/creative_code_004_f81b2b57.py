"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rp-galagames-app.blogspot.com
Prompt: Illustrate how to implement a shopping cart feature that allows users to add items like polos and t-shirts, reflecting the shopping experience offered by Vila Romana.
Generated: DETERMINISTIC_f81b2b57853f9a98
Batch ID: 20250612_163251
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# shopping_cart.py

class Item:
    """Class to represent an item in the shopping cart."""
    
    def __init__(self, name, price):
        """Initialize the item with a name and a price."""
        self.name = name
        self.price = price

    def __repr__(self):
        """Return a string representation of the item."""
        return f"{self.name} (${self.price:.2f})"


class ShoppingCart:
    """Class to represent a shopping cart."""

    def __init__(self):
        """Initialize an empty shopping cart."""
        self.items = []

    def add_item(self, item):
        """Add an item to the shopping cart.

        Args:
            item (Item): The item to be added.
        """
        if not isinstance(item, Item):
            raise ValueError("Only Item instances can be added to the cart.")
        self.items.append(item)
        print(f"Added {item} to the cart.")

    def remove_item(self, item):
        """Remove an item from the shopping cart.

        Args:
            item (Item): The item to be removed.

        Raises:
            ValueError: If the item is not in the cart.
        """
        try:
            self.items.remove(item)
            print(f"Removed {item} from the cart.")
        except ValueError:
            raise ValueError("Item not found in the cart.")

    def total_price(self):
        """Calculate the total price of the items in the cart.

        Returns:
            float: The total price of the cart.
        """
        return sum(item.price for item in self.items)

    def view_cart(self):
        """Display the items in the shopping cart and the total price."""
        if not self.items:
            print("Your cart is empty.")
            return
        print("Items in your cart:")
        for item in self.items:
            print(f"- {item}")
        print(f"Total Price: ${self.total_price():.2f}")


# Sample usage
if __name__ == "__main__":
    # Create a shopping cart instance
    cart = ShoppingCart()

    # Create some items
    polo = Item("Polo Shirt", 29.99)
    tshirt = Item("T-Shirt", 19.99)

    # Add items to the cart
    cart.add_item(polo)
    cart.add_item(tshirt)

    # View the cart
    cart.view_cart()

    # Remove an item and view cart again
    cart.remove_item(tshirt)
    cart.view_cart()
```
