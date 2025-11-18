"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cmcbukittinggi.co.id
Prompt: Generate a Python function that calculates the total cost of items added to the cart on the Central Multi Computer website (https://cmcbukittinggi.co.id), including discounts applied to promotional products.
Generated: DETERMINISTIC_45d2b9bb7ce4b0e4
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import requests

class Cart:
    def __init__(self):
        """
        Initializes an empty cart.
        """
        self.items = []

    def add_item(self, item_name, price, quantity=1, discount=0):
        """
        Adds an item to the cart.

        :param item_name: Name of the item to add
        :param price: Price of a single item
        :param quantity: Number of items to add (default is 1)
        :param discount: Discount percentage to apply (default is 0)
        """
        if price < 0 or quantity < 1 or discount < 0:
            raise ValueError("Price must be non-negative, quantity must be at least 1, and discount must be non-negative.")
        
        item_total = price * quantity
        if discount > 0:
            item_total -= item_total * (discount / 100)
        
        self.items.append({
            'name': item_name,
            'price': price,
            'quantity': quantity,
            'discount': discount,
            'total': item_total
        })

    def calculate_total(self):
        """
        Calculates the total cost of items in the cart.

        :return: Total cost of items in the cart
        """
        total_cost = sum(item['total'] for item in self.items)
        return total_cost

    def clear_cart(self):
        """
        Clears the cart.
        """
        self.items = []

def main():
    # Create a cart instance
    cart = Cart()

    # Example items to add
    try:
        cart.add_item("Laptop", 1200.00, quantity=1, discount=10)  # $120 off
        cart.add_item("Mouse", 25.00, quantity=2)  # No discount
        cart.add_item("Keyboard", 45.00, quantity=1, discount=5)  # $2.25 off

        # Calculate total cost
        total_cost = cart.calculate_total()
        print(f"Total cost of items in the cart: ${total_cost:.2f}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
