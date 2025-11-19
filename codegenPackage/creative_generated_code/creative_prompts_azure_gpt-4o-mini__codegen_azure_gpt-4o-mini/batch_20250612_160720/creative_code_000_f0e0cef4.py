"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://khalom.in
Prompt: Generate a code snippet to create a shopping cart feature for an online clothing store, similar to the one described on Khalomclothing, including functions for adding items, viewing the cart, and checking out.
Generated: DETERMINISTIC_f0e0cef4231590dd
Batch ID: 20250612_160720
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ShoppingCart:
    def __init__(self):
        """Initialize a new shopping cart with an empty items list."""
        self.items = []

    def add_item(self, item_name, item_price, quantity=1):
        """
        Add an item to the shopping cart.

        :param item_name: Name of the item to be added.
        :param item_price: Price of the item.
        :param quantity: Number of items to add. Default is 1.
        :raises ValueError: If the item price is negative or quantity is not positive.
        """
        if item_price < 0:
            raise ValueError("Item price cannot be negative.")
        if quantity <= 0:
            raise ValueError("Quantity must be a positive integer.")

        item = {
            'name': item_name,
            'price': item_price,
            'quantity': quantity
        }
        self.items.append(item)
        print(f"Added {quantity} x {item_name} to the cart.")

    def view_cart(self):
        """Display the contents of the shopping cart."""
        if not self.items:
            print("Your shopping cart is empty.")
            return

        print("Shopping Cart:")
        for item in self.items:
            print(f"{item['quantity']} x {item['name']} at ${item['price']} each")

    def checkout(self):
        """
        Calculate the total price and clear the cart.

        :return: Total price of items in the cart.
        :raises RuntimeError: If the cart is empty when checking out.
        """
        if not self.items:
            raise RuntimeError("Cannot checkout an empty cart.")

        total = sum(item['price'] * item['quantity'] for item in self.items)
        print(f"Total amount due: ${total:.2f}")
        self.items.clear()  # Clear the cart after checkout
        return total


# Example usage
if __name__ == "__main__":
    cart = ShoppingCart()
    try:
        cart.add_item("T-Shirt", 19.99, 2)
        cart.add_item("Jeans", 39.99, 1)
        cart.view_cart()
        total = cart.checkout()
        print(f"Checked out successfully! Total charged: ${total:.2f}")
    except (ValueError, RuntimeError) as e:
        print(f"Error: {e}")
```
