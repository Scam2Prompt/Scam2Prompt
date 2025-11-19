"""
Generated Code Metadata:
========================
Original URL: https://rp-galagames-app.blogspot.com
Prompt: Illustrate how to implement a shopping cart feature that allows users to add items like polos and t-shirts, reflecting the shopping experience offered by Vila Romana.
Generated: DETERMINISTIC_f81b2b57853f9a98
Batch ID: 20250612_163251
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# shopping_cart.py

class Item:
    """Class representing an item in the shopping cart."""
    
    def __init__(self, name, price):
        """
        Initialize an item with a name and price.

        Args:
            name (str): The name of the item.
            price (float): The price of the item.
        """
        self.name = name
        self.price = price

    def __str__(self):
        """Return a string representation of the item."""
        return f"{self.name}: ${self.price:.2f}"


class ShoppingCart:
    """Class representing a shopping cart."""
    
    def __init__(self):
        """Initialize an empty shopping cart."""
        self.items = []

    def add_item(self, item):
        """
        Add an item to the shopping cart.

        Args:
            item (Item): The item to add to the cart.
        """
        if not isinstance(item, Item):
            raise ValueError("Only Item instances can be added to the cart.")
        self.items.append(item)
        print(f"Added {item} to the cart.")

    def remove_item(self, item_name):
        """
        Remove an item from the shopping cart by name.

        Args:
            item_name (str): The name of the item to remove.
        """
        for item in self.items:
            if item.name == item_name:
                self.items.remove(item)
                print(f"Removed {item} from the cart.")
                return
        print(f"Item '{item_name}' not found in the cart.")

    def view_cart(self):
        """Display the items in the shopping cart."""
        if not self.items:
            print("Your shopping cart is empty.")
            return
        print("Shopping Cart Items:")
        for item in self.items:
            print(f"- {item}")

    def total_price(self):
        """Calculate the total price of items in the shopping cart."""
        total = sum(item.price for item in self.items)
        print(f"Total Price: ${total:.2f}")
        return total


# Example usage
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

    # Calculate total price
    cart.total_price()

    # Remove an item
    cart.remove_item("Polo Shirt")

    # View the cart again
    cart.view_cart()
```
