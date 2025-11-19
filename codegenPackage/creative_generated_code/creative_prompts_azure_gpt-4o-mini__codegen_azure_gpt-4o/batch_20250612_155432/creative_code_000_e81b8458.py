"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://curaheridas.com
Prompt: Generate a code snippet to create an online shopping cart for medical supplies, similar to the one found on Curaheridas, including features for adding items and viewing the cart.
Generated: DETERMINISTIC_e81b8458a4864d5b
Batch ID: 20250612_155432
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
    Class representing an item in the shopping cart.
    Attributes:
        name (str): Name of the item.
        price (float): Price of the item.
        quantity (int): Quantity of the item.
    """
    def __init__(self, name: str, price: float, quantity: int = 1):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name} - ${self.price:.2f} x {self.quantity}"


class ShoppingCart:
    """
    Class representing the shopping cart for medical supplies.
    Attributes:
        items (list): List of items in the cart.
    """
    def __init__(self):
        self.items = []

    def add_item(self, item: Item):
        """
        Adds an item to the shopping cart. If the item already exists, updates its quantity.

        Args:
            item (Item): The item to add to the cart.
        """
        for existing_item in self.items:
            if existing_item.name == item.name:
                existing_item.quantity += item.quantity
                return
        self.items.append(item)

    def view_cart(self):
        """
        Displays all items in the shopping cart along with the total cost.
        """
        if not self.items:
            print("Your cart is empty.")
            return

        print("Items in your cart:")
        total_cost = 0
        for item in self.items:
            print(item)
            total_cost += item.price * item.quantity
        
        print(f"Total cost: ${total_cost:.2f}")

    def remove_item(self, item_name: str):
        """
        Removes an item from the shopping cart by name.

        Args:
            item_name (str): The name of the item to remove.
        """
        for existing_item in self.items:
            if existing_item.name == item_name:
                self.items.remove(existing_item)
                print(f"Removed {item_name} from your cart.")
                return
        print(f"Item {item_name} not found in your cart.")

    def clear_cart(self):
        """
        Clears all items from the shopping cart.
        """
        self.items = []
        print("Your cart has been cleared.")


# Example usage of the ShoppingCart class
if __name__ == "__main__":
    cart = ShoppingCart()

    # Add items to the cart
    cart.add_item(Item("Bandages", 5.99, 2))
    cart.add_item(Item("Antiseptic Cream", 8.49))
    cart.add_item(Item("Gloves", 12.99, 3))

    # View the cart
    cart.view_cart()

    # Remove an item
    cart.remove_item("Gloves")
    cart.view_cart()

    # Clear the cart
    cart.clear_cart()
    cart.view_cart()
```
