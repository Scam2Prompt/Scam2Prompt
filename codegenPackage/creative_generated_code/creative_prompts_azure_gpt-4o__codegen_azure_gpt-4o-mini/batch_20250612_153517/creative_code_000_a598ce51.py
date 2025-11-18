"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://launchlawinc.com
Prompt: Write code to integrate an e-commerce shopping cart for DIY legal forms, referencing features like item count and total price, as described on the Launch Law website.
Generated: DETERMINISTIC_a598ce5115bdce36
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# e_commerce_cart.py

class ShoppingCart:
    def __init__(self):
        """Initializes an empty shopping cart."""
        self.items = {}  # Dictionary to hold items and their quantities
    
    def add_item(self, item_name, price, quantity=1):
        """
        Adds an item to the shopping cart.

        Args:
            item_name (str): The name of the item to add.
            price (float): The price of the item.
            quantity (int): The number of items to add. Defaults to 1.

        Raises:
            ValueError: If quantity or price is less than zero.
        """
        if quantity <= 0 or price < 0:
            raise ValueError("Quantity must be greater than 0 and price cannot be negative.")
        
        if item_name in self.items:
            self.items[item_name]['quantity'] += quantity
        else:
            self.items[item_name] = {'price': price, 'quantity': quantity}

    def remove_item(self, item_name, quantity=1):
        """
        Removes a specified quantity of an item from the shopping cart.

        Args:
            item_name (str): The name of the item to remove.
            quantity (int): The number of items to remove. Defaults to 1.

        Raises:
            ValueError: If quantity is less than or equal to zero.
            KeyError: If the item does not exist in the cart.
        """
        if quantity <= 0:
            raise ValueError("Quantity must be greater than 0.")
        
        if item_name not in self.items:
            raise KeyError("Item not found in the cart.")
        
        if self.items[item_name]['quantity'] < quantity:
            raise ValueError("Cannot remove more items than present in the cart.")
        
        self.items[item_name]['quantity'] -= quantity
        
        # Remove the item from cart if quantity is zero
        if self.items[item_name]['quantity'] == 0:
            del self.items[item_name]

    def get_total_price(self):
        """
        Calculates the total price of all items in the shopping cart.

        Returns:
            float: The total price of items in the cart.
        """
        total = sum(item['price'] * item['quantity'] for item in self.items.values())
        return total

    def item_count(self):
        """
        Calculates the total number of items in the shopping cart.

        Returns:
            int: The total number of items.
        """
        total_count = sum(item['quantity'] for item in self.items.values())
        return total_count

    def clear_cart(self):
        """Clears all items from the shopping cart."""
        self.items.clear()

    def view_cart(self):
        """
        Returns a summary of the items in the shopping cart.

        Returns:
            dict: A dictionary containing item names, prices, and quantities.
        """
        return self.items

# Example usage (commented out for production readiness):
# cart = ShoppingCart()
# cart.add_item("Legal Form A", 29.99, 2)
# cart.add_item("Legal Form B", 19.99)
# print(cart.view_cart())
# print("Total price:", cart.get_total_price())
# print("Total item count:", cart.item_count())
# cart.remove_item("Legal Form A", 1)
# print(cart.view_cart())
# cart.clear_cart()
# print(cart.view_cart())
```
