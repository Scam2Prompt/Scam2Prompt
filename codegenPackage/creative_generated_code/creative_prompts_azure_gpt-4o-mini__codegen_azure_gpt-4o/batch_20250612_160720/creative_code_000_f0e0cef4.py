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
# Shopping Cart Feature for an Online Clothing Store

class Item:
    """
    Represents a clothing item in the store.
    """
    def __init__(self, name, price, quantity=1):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def __str__(self):
        return f"{self.name} - ${self.price:.2f} x {self.quantity}"


class ShoppingCart:
    """
    Represents the shopping cart for the online clothing store.
    """
    def __init__(self):
        self.cart = {}
        self.total_cost = 0.0
    
    def add_item(self, item_name, price, quantity=1):
        """
        Adds an item to the cart. If the item already exists, increments the quantity.
        :param item_name: Name of the clothing item.
        :param price: Price of the clothing item.
        :param quantity: Quantity to add (default is 1).
        """
        if item_name in self.cart:
            self.cart[item_name].quantity += quantity
        else:
            self.cart[item_name] = Item(item_name, price, quantity)
        self._update_total()
    
    def remove_item(self, item_name):
        """
        Removes an item from the cart.
        :param item_name: Name of the clothing item to remove.
        """
        if item_name in self.cart:
            del self.cart[item_name]
            self._update_total()
        else:
            print(f"Item '{item_name}' not found in the cart.")
    
    def view_cart(self):
        """
        Displays the items currently in the cart.
        """
        if not self.cart:
            print("Your cart is empty.")
        else:
            print("Items in your cart:")
            for item in self.cart.values():
                print(item)
            print(f"Total Cost: ${self.total_cost:.2f}")
    
    def checkout(self):
        """
        Finalizes the purchase and clears the cart.
        """
        if not self.cart:
            print("Your cart is empty. Add items before checking out.")
        else:
            print("Checking out the following items:")
            for item in self.cart.values():
                print(item)
            print(f"Total Cost: ${self.total_cost:.2f}")
            print("Thank you for shopping with us!")
            self.cart.clear()
            self.total_cost = 0.0
    
    def _update_total(self):
        """
        Updates the total cost of the items in the cart.
        """
        self.total_cost = sum(item.price * item.quantity for item in self.cart.values())


# Example usage
if __name__ == "__main__":
    # Create a shopping cart instance
    cart = ShoppingCart()
    
    # Add items
    cart.add_item("T-shirt", 19.99, 2)
    cart.add_item("Jeans", 49.99)
    cart.add_item("Hat", 14.99)
    
    # View cart
    cart.view_cart()
    
    # Remove an item
    cart.remove_item("Hat")
    
    # View cart again
    cart.view_cart()
    
    # Checkout
    cart.checkout()

    # View the cart after checkout
    cart.view_cart()
```
