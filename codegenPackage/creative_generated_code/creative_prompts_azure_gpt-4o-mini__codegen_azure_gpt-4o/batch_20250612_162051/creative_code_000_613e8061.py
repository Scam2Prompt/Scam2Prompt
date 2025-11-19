"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://simplementeairsoft.com
Prompt: Generate a code snippet for an e-commerce website that implements a shopping cart feature, similar to the one found on Simplymente Airsoft, allowing users to add tactical clothing items like sweatshirts and t-shirts.
Generated: DETERMINISTIC_613e8061b55954e8
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
shopping_cart.py

This module implements a shopping cart feature for an e-commerce website
selling tactical clothing items, such as sweatshirts and t-shirts.
"""

import uuid

class Item:
    """
    Represents a single item in the store.
    """
    def __init__(self, name: str, price: float, stock: int):
        if price < 0:
            raise ValueError("Price cannot be negative.")
        if stock < 0:
            raise ValueError("Stock cannot be negative.")

        self.id = str(uuid.uuid4())  # Unique identifier for the item
        self.name = name
        self.price = price
        self.stock = stock

    def __repr__(self):
        return f"Item(name='{self.name}', price={self.price}, stock={self.stock})"


class ShoppingCart:
    """
    Represents the shopping cart which allows users to add, remove, and view items.
    """
    def __init__(self):
        self.cart = {}  # Dictionary to hold items and their quantities

    def add_item(self, item: Item, quantity: int) -> str:
        """
        Adds an item to the shopping cart.

        Args:
            item (Item): The item to add.
            quantity (int): The quantity to add.

        Returns:
            str: Confirmation message.
        """
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")
        if item.stock < quantity:
            raise ValueError(f"Not enough stock for '{item.name}'. Available: {item.stock}")

        # Update the item's stock
        item.stock -= quantity

        # Add to cart or update quantity if already present
        if item.id in self.cart:
            self.cart[item.id]['quantity'] += quantity
        else:
            self.cart[item.id] = {'item': item, 'quantity': quantity}

        return f"Added {quantity}x '{item.name}' to the cart."

    def remove_item(self, item_id: str, quantity: int) -> str:
        """
        Removes an item or reduces its quantity in the shopping cart.

        Args:
            item_id (str): The unique ID of the item to remove.
            quantity (int): The quantity to remove.

        Returns:
            str: Confirmation message.
        """
        if item_id not in self.cart:
            raise KeyError(f"Item with ID '{item_id}' not found in the cart.")
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")

        cart_item = self.cart[item_id]
        if quantity >= cart_item['quantity']:
            # Remove the item completely if quantity exceeds or matches
            cart_item['item'].stock += cart_item['quantity']  # Return stock to the item
            del self.cart[item_id]
            return f"Removed '{cart_item['item'].name}' from the cart."
        else:
            # Reduce the quantity
            cart_item['quantity'] -= quantity
            cart_item['item'].stock += quantity  # Return partial stock to the item
            return f"Reduced '{cart_item['item'].name}' quantity by {quantity}."

    def view_cart(self) -> str:
        """
        Returns a summary of the items in the shopping cart.

        Returns:
            str: Cart summary.
        """
        if not self.cart:
            return "Your cart is empty."
        
        summary = "Shopping Cart:\n"
        for cart_item in self.cart.values():
            summary += f"{cart_item['quantity']}x {cart_item['item'].name} - ${cart_item['item'].price:.2f} each\n"
        return summary

    def calculate_total(self) -> float:
        """
        Calculates the total cost of items in the shopping cart.

        Returns:
            float: Total cost.
        """
        total = 0.0
        for cart_item in self.cart.values():
            total += cart_item['item'].price * cart_item['quantity']
        return total


# Example usage:
if __name__ == "__main__":
    # Create some items
    sweatshirt = Item(name="Tactical Sweatshirt", price=49.99, stock=10)
    tshirt = Item(name="Tactical T-Shirt", price=29.99, stock=20)

    # Initialize the shopping cart
    cart = ShoppingCart()

    # Add items to the cart
    print(cart.add_item(sweatshirt, 2))  # Add 2 sweatshirts
    print(cart.add_item(tshirt, 3))     # Add 3 t-shirts

    # View the cart
    print(cart.view_cart())

    # Calculate total
    print(f"Total: ${cart.calculate_total():.2f}")

    # Remove an item
    print(cart.remove_item(sweatshirt.id, 1))  # Remove 1 sweatshirt

    # View updated cart
    print(cart.view_cart())
```
