"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://alwan.om
Prompt: Can you provide code examples for integrating a shopping cart functionality that allows users to view and manage their items, as seen on Alwan's site?
Generated: DETERMINISTIC_98157c9d821ef9dc
Batch ID: 20250612_162051
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
    """Class to represent a shopping cart."""

    def __init__(self):
        """Initialize an empty shopping cart."""
        self.items = {}
    
    def add_item(self, item_id, item_name, price, quantity):
        """Add an item to the shopping cart.
        
        Args:
            item_id (str): Unique identifier for the item
            item_name (str): Name of the item
            price (float): Price of the item
            quantity (int): Quantity of the item to add
        """
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")
        
        if item_id in self.items:
            self.items[item_id]['quantity'] += quantity
        else:
            self.items[item_id] = {'name': item_name, 'price': price, 'quantity': quantity}
    
    def remove_item(self, item_id, quantity=1):
        """Remove an item or quantity of an item from the shopping cart.
        
        Args:
            item_id (str): Unique identifier for the item
            quantity (int): Quantity of the item to remove
        """
        if item_id not in self.items:
            raise KeyError("Item not found in cart.")
        
        if quantity >= self.items[item_id]['quantity']:
            del self.items[item_id]
        else:
            self.items[item_id]['quantity'] -= quantity
    
    def view_cart(self):
        """Return the current items in the shopping cart."""
        return self.items
    
    def clear_cart(self):
        """Empty the shopping cart."""
        self.items.clear()
    
    def total_cost(self):
        """Calculate the total cost of items in the shopping cart.
        
        Returns:
            float: Total cost of the shopping cart
        """
        total = sum(item['price'] * item['quantity'] for item in self.items.values())
        return total

# Example usage
if __name__ == "__main__":
    cart = ShoppingCart()
    
    try:
        cart.add_item("001", "Apple", 0.50, 3)
        cart.add_item("002", "Banana", 0.30, 2)
        
        print("Cart Items:", cart.view_cart())
        print("Total Cost: $", cart.total_cost())
        
        cart.remove_item("001", 1)
        print("Cart Items after removal:", cart.view_cart())
        
        cart.clear_cart()
        print("Cart Items after clearing:", cart.view_cart())
        
    except Exception as e:
        print("An error occurred:", str(e))
```
