"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://adhive.net
Prompt: Write a script to implement a "View Cart" functionality for an online store, similar to the one described on Adhive Marketplace.
Generated: DETERMINISTIC_07e129e7c7eedbb4
Batch ID: 20250612_151912
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# cart.py

class CartItem:
    """Class to represent an item in the shopping cart."""
    def __init__(self, product_id, quantity, price):
        self.product_id = product_id
        self.quantity = quantity
        self.price = price

    def total_price(self):
        """Calculate total price for this cart item."""
        return self.quantity * self.price


class ShoppingCart:
    """Class to manage the shopping cart."""
    def __init__(self):
        self.items = []

    def add_item(self, product_id, quantity, price):
        """Add an item to the shopping cart."""
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")
        
        # Check if item already exists in the cart
        for item in self.items:
            if item.product_id == product_id:
                item.quantity += quantity
                return
        
        # If item does not exist, add a new item
        new_item = CartItem(product_id, quantity, price)
        self.items.append(new_item)

    def remove_item(self, product_id):
        """Remove an item from the shopping cart by product ID."""
        for idx, item in enumerate(self.items):
            if item.product_id == product_id:
                del self.items[idx]
                return
        raise ValueError("Item not found in cart.")

    def view_cart(self):
        """Display the contents of the shopping cart."""
        if not self.items:
            return "Your cart is empty."
        
        cart_contents = []
        total_cost = 0
        
        for item in self.items:
            item_total = item.total_price()
            total_cost += item_total
            cart_contents.append(f"Product ID: {item.product_id}, Quantity: {item.quantity}, Total Price: ${item_total:.2f}")
        
        cart_contents.append(f"Total Cost: ${total_cost:.2f}")
        return "\n".join(cart_contents)

    def clear_cart(self):
        """Clear all items from the shopping cart."""
        self.items.clear()


# Example usage:
if __name__ == "__main__":
    try:
        cart = ShoppingCart()
        cart.add_item("123", 2, 19.99)
        cart.add_item("456", 1, 29.99)
        print(cart.view_cart())
        
        cart.remove_item("123")
        print(cart.view_cart())
        
        cart.clear_cart()
        print(cart.view_cart())
    
    except ValueError as e:
        print(f"Error: {e}")
```
