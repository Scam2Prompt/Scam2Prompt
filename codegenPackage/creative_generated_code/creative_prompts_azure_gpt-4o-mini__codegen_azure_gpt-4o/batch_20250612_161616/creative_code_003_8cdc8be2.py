"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thepointblank.in
Prompt: Develop a script that automates the process of applying a discount code "Bulk10" for orders above ₹5000 in a shopping cart application.
Generated: DETERMINISTIC_8cdc8be2ac06edb8
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class ShoppingCart:
    def __init__(self):
        # Initialize an empty cart and a total amount.
        self.cart_items = []
        self.total_amount = 0

    def add_item(self, name, price, quantity=1):
        """
        Add an item to the shopping cart.

        :param name: Name of the item
        :param price: Price of the item
        :param quantity: Quantity of the item
        """
        if price < 0 or quantity < 1:
            raise ValueError("Price must be non-negative and quantity must be greater than 0.")
        
        self.cart_items.append({'name': name, 'price': price, 'quantity': quantity})
        self.total_amount += price * quantity

    def apply_discount(self):
        """
        Apply the discount code 'Bulk10' for total orders above ₹5000.
        """
        DISCOUNT_THRESHOLD = 5000
        DISCOUNT_PERCENTAGE = 10  # 10% discount
        
        if self.total_amount > DISCOUNT_THRESHOLD:
            discount_amount = (self.total_amount * DISCOUNT_PERCENTAGE) / 100
            self.total_amount -= discount_amount
            return discount_amount  # Return the discount amount applied
        return 0  # No discount applied

    def display_cart(self):
        """
        Display the cart items and total amount.
        """
        print("Shopping Cart Items:")
        print(json.dumps(self.cart_items, indent=4))
        print(f"Total Amount: ₹{self.total_amount:.2f}")

# Example usage:

try:
    # Initialize the shopping cart
    cart = ShoppingCart()
    
    # Add items to the shopping cart
    cart.add_item(name="Laptop", price=45000, quantity=1)
    cart.add_item(name="Mouse", price=1500, quantity=2)
    cart.add_item(name="Keyboard", price=2500, quantity=1)
    cart.display_cart()

    # Apply the discount
    discount_applied = cart.apply_discount()
    if discount_applied:
        print(f"Discount applied: ₹{discount_applied:.2f}")
    else:
        print("No discount applied.")
    
    # Display the updated cart total
    cart.display_cart()

except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
```
