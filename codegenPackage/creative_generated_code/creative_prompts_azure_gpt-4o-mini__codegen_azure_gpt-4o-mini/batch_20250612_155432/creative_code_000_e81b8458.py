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

class ShoppingCart:
    def __init__(self):
        """Initialize an empty shopping cart."""
        self.items = []

    def add_item(self, item_name, item_price, quantity=1):
        """
        Add an item to the shopping cart.

        :param item_name: Name of the item to add.
        :param item_price: Price of the individual item.
        :param quantity: Number of items to add (default is 1).
        """
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")
        if item_price < 0:
            raise ValueError("Item price must be non-negative.")

        item = {
            'name': item_name,
            'price': item_price,
            'quantity': quantity,
            'total_price': item_price * quantity
        }
        self.items.append(item)
        print(f"Added {quantity} x {item_name} to the cart.")

    def view_cart(self):
        """Display the contents of the shopping cart."""
        if not self.items:
            print("Your cart is empty.")
            return

        print("Shopping Cart:")
        total_cost = 0
        for item in self.items:
            print(f"{item['quantity']} x {item['name']} at ${item['price']} each: ${item['total_price']:.2f}")
            total_cost += item['total_price']
        print(f"Total cost: ${total_cost:.2f}")

    def clear_cart(self):
        """Clear all items from the shopping cart."""
        self.items.clear()
        print("Your cart has been cleared.")

if __name__ == "__main__":
    # Example usage of the ShoppingCart class
    cart = ShoppingCart()
    try:
        cart.add_item("Medical Mask", 1.99, 3)
        cart.add_item("Hand Sanitizer", 5.49, 2)
        cart.view_cart()
        cart.clear_cart()
        cart.view_cart()
    except ValueError as e:
        print(f"Error: {e}")
```
