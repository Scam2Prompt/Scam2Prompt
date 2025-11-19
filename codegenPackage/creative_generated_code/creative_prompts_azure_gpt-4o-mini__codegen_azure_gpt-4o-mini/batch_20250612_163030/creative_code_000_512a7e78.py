"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://millymally.pl
Prompt: Generate a code snippet for a shopping cart feature that includes items like "rowerki," "hulajnogi," and "jeździki" from Milly Mally's product range.
Generated: DETERMINISTIC_512a7e784ab1bd36
Batch ID: 20250612_163030
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ShoppingCart:
    """A class to represent a shopping cart."""

    def __init__(self):
        """Initialize an empty shopping cart."""
        self.items = {}

    def add_item(self, item_name, price, quantity=1):
        """Add an item to the shopping cart.

        Args:
            item_name (str): The name of the item.
            price (float): The price of the item.
            quantity (int): The quantity of the item to add (default is 1).
        """
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")
        if item_name in self.items:
            self.items[item_name]['quantity'] += quantity
        else:
            self.items[item_name] = {'price': price, 'quantity': quantity}

    def remove_item(self, item_name, quantity=1):
        """Remove an item from the shopping cart.

        Args:
            item_name (str): The name of the item.
            quantity (int): The quantity of the item to remove (default is 1).
        """
        if item_name not in self.items:
            raise KeyError(f"{item_name} not found in the cart.")
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")
        
        if self.items[item_name]['quantity'] < quantity:
            raise ValueError("Cannot remove more items than are in the cart.")
        
        self.items[item_name]['quantity'] -= quantity
        if self.items[item_name]['quantity'] == 0:
            del self.items[item_name]

    def total_cost(self):
        """Calculate the total cost of the shopping cart.

        Returns:
            float: The total cost of all items in the cart.
        """
        return sum(item['price'] * item['quantity'] for item in self.items.values())

    def clear_cart(self):
        """Clear all items from the shopping cart."""
        self.items.clear()

    def __str__(self):
        """Return a string representation of the shopping cart contents."""
        return '\n'.join([f"{item}: {details['quantity']} x {details['price']} PLN" 
                          for item, details in self.items.items()]) or "Cart is empty."


# Example usage
if __name__ == "__main__":
    cart = ShoppingCart()
    try:
        cart.add_item("rowerki", 299.99, 2)
        cart.add_item("hulajnogi", 199.99, 1)
        cart.add_item("jeździki", 159.99, 3)
        print(cart)
        print(f"Total Cost: {cart.total_cost()} PLN")

        cart.remove_item("hulajnogi")
        print(cart)
        print(f"Total Cost after removal: {cart.total_cost()} PLN")
        
        cart.clear_cart()
        print(cart)
        
    except (ValueError, KeyError) as e:
        print(f"Error: {e}")
```
