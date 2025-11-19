"""
Generated Code Metadata:
========================
Original URL: https://brandsoutlet.qa
Prompt: Illustrate how to implement a shopping cart feature for an e-commerce site that mimics the functionality seen on Brands Outlet, including adding items to a wishlist.
Generated: DETERMINISTIC_f5372de6f6405eff
Batch ID: 20250612_155250
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# shopping_cart.py

import uuid

class Item:
    """
    Represents an item in the store.
    """
    def __init__(self, name, price, stock):
        self.id = str(uuid.uuid4())  # Unique identifier for the item
        self.name = name
        self.price = price
        self.stock = stock

    def __str__(self):
        return f"{self.name} - ${self.price:.2f} (Stock: {self.stock})"


class ShoppingCart:
    """
    Represents a shopping cart for a user.
    """
    def __init__(self):
        self.cart_items = {}  # Dictionary to store items and their quantities
        self.wishlist = []   # List to store items added to the wishlist

    def add_to_cart(self, item, quantity):
        """
        Adds an item to the shopping cart.
        """
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")
        if item.stock < quantity:
            raise ValueError("Insufficient stock available.")
        
        # Add item to cart or update quantity if already present
        if item.id in self.cart_items:
            self.cart_items[item.id]['quantity'] += quantity
        else:
            self.cart_items[item.id] = {'item': item, 'quantity': quantity}
        
        # Reduce stock from the item
        item.stock -= quantity

    def remove_from_cart(self, item_id):
        """
        Removes an item from the shopping cart.
        """
        if item_id not in self.cart_items:
            raise ValueError("Item not found in the cart.")
        
        # Restore stock to the item
        item = self.cart_items[item_id]['item']
        quantity = self.cart_items[item_id]['quantity']
        item.stock += quantity
        
        # Remove item from the cart
        del self.cart_items[item_id]

    def view_cart(self):
        """
        Displays the contents of the shopping cart.
        """
        if not self.cart_items:
            print("Your cart is empty.")
            return
        
        print("Shopping Cart:")
        for item_data in self.cart_items.values():
            item = item_data['item']
            quantity = item_data['quantity']
            print(f"{item.name} - ${item.price:.2f} x {quantity} = ${item.price * quantity:.2f}")

    def add_to_wishlist(self, item):
        """
        Adds an item to the wishlist.
        """
        if item in self.wishlist:
            print(f"{item.name} is already in your wishlist.")
            return
        
        self.wishlist.append(item)
        print(f"{item.name} has been added to your wishlist.")

    def view_wishlist(self):
        """
        Displays the contents of the wishlist.
        """
        if not self.wishlist:
            print("Your wishlist is empty.")
            return
        
        print("Wishlist:")
        for item in self.wishlist:
            print(item)


# Example usage
if __name__ == "__main__":
    # Create some items
    item1 = Item("T-Shirt", 19.99, 10)
    item2 = Item("Jeans", 49.99, 5)
    item3 = Item("Sneakers", 89.99, 2)

    # Create a shopping cart
    cart = ShoppingCart()

    # Add items to the cart
    try:
        cart.add_to_cart(item1, 2)
        cart.add_to_cart(item2, 1)
    except ValueError as e:
        print(f"Error: {e}")

    # View the cart
    cart.view_cart()

    # Add items to the wishlist
    cart.add_to_wishlist(item3)
    cart.add_to_wishlist(item1)

    # View the wishlist
    cart.view_wishlist()

    # Remove an item from the cart
    try:
        cart.remove_from_cart(item1.id)
    except ValueError as e:
        print(f"Error: {e}")

    # View the cart again
    cart.view_cart()
```
