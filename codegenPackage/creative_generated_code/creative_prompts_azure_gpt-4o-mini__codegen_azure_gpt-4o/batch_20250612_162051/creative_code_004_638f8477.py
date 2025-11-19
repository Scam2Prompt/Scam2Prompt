"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vaperiyadh2.com
Prompt: Illustrate how to implement a shopping cart feature that includes items like the Mazaj Infinity and Nasty Bar from Vape Riyadh 2.
Generated: DETERMINISTIC_638f8477a0b63ba3
Batch ID: 20250612_162051
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
    """
    Represents an item in the shop.
    Attributes:
        name (str): Name of the item
        price (float): Price of the item
        quantity (int): Quantity of the item
    """
    def __init__(self, name, price, quantity=1):
        self.name = name
        self.price = price
        self.quantity = quantity

    def update_quantity(self, quantity):
        """Updates the quantity of the item."""
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self.quantity = quantity

    def calculate_total_price(self):
        """Calculates the total price for the item based on quantity."""
        return self.price * self.quantity


class ShoppingCart:
    """
    Represents a shopping cart.
    Attributes:
        items (dict): Dictionary storing items in the cart. Key is item name, value is Item object.
    """
    def __init__(self):
        self.items = {}

    def add_item(self, item):
        """
        Adds an item to the shopping cart. If the item already exists, it updates the quantity.
        Args:
            item (Item): The item to be added.
        """
        if item.name in self.items:
            self.items[item.name].update_quantity(self.items[item.name].quantity + item.quantity)
        else:
            self.items[item.name] = item

    def remove_item(self, item_name):
        """
        Removes an item from the cart.
        Args:
            item_name (str): Name of the item to be removed.
        """
        if item_name in self.items:
            del self.items[item_name]
        else:
            raise KeyError(f"Item '{item_name}' not found in the cart.")

    def calculate_total(self):
        """Calculates the total cost of items in the cart."""
        return sum(item.calculate_total_price() for item in self.items.values())

    def list_items(self):
        """
        Lists all items in the shopping cart.
        Returns:
            list: List of item details.
        """
        return [{"name": item.name, "price": item.price, "quantity": item.quantity} for item in self.items.values()]

    def clear_cart(self):
        """Clears all items from the shopping cart."""
        self.items.clear()


# Example Usage
if __name__ == "__main__":
    try:
        # Create instances of items
        mazaj_infinity = Item(name="Mazaj Infinity", price=25.99, quantity=2)
        nasty_bar = Item(name="Nasty Bar", price=15.49, quantity=1)

        # Create a shopping cart
        cart = ShoppingCart()

        # Add items to the cart
        cart.add_item(mazaj_infinity)
        cart.add_item(nasty_bar)

        # Display cart items
        print("Items in the cart:", cart.list_items())

        # Calculate total
        print("Total cost:", cart.calculate_total())

        # Remove an item
        cart.remove_item("Nasty Bar")
        print("Items after removal:", cart.list_items())

        # Clear the cart
        cart.clear_cart()
        print("Items after clearing the cart:", cart.list_items())

    except (ValueError, KeyError) as e:
        print(f"Error: {e}")
```
