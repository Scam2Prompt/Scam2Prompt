"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://livivid.com
Prompt: How can I generate code to create a shopping cart feature for a website selling handmade Tibetan clothing, similar to the offerings on livivid.com?
Generated: DETERMINISTIC_64f94f5abb8b7b41
Batch ID: 20250612_160600
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
    """A class to represent a shopping cart for an online store."""
    
    def __init__(self):
        """Initialize an empty shopping cart."""
        self.items = {}
    
    def add_item(self, item_id, item_name, price, quantity):
        """
        Add an item to the shopping cart.
        
        Args:
            item_id (str): Unique identifier for the item.
            item_name (str): Name of the item.
            price (float): Price of the item.
            quantity (int): Quantity of the item to add.
        """
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")
        
        if item_id in self.items:
            self.items[item_id]['quantity'] += quantity
        else:
            self.items[item_id] = {'name': item_name, 'price': price, 'quantity': quantity}
    
    def remove_item(self, item_id):
        """
        Remove an item from the shopping cart by item_id.
        
        Args:
            item_id (str): Unique identifier for the item to remove.
        """
        if item_id in self.items:
            del self.items[item_id]
        else:
            raise KeyError("Item not found in the cart.")
    
    def update_quantity(self, item_id, quantity):
        """
        Update the quantity of an item in the shopping cart.
        
        Args:
            item_id (str): Unique identifier for the item.
            quantity (int): New quantity for the item.
        """
        if item_id not in self.items:
            raise KeyError("Item not found in the cart.")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        
        if quantity == 0:
            self.remove_item(item_id)
        else:
            self.items[item_id]['quantity'] = quantity
    
    def calculate_total(self):
        """
        Calculate the total cost of the items in the cart.
        
        Returns:
            float: The total cost.
        """
        total = sum(item['price'] * item['quantity'] for item in self.items.values())
        return total
    
    def view_cart(self):
        """
        View the items in the shopping cart.
        
        Returns:
            dict: A dictionary representation of the cart.
        """
        return self.items

# Example usage
if __name__ == "__main__":
    try:
        cart = ShoppingCart()
        cart.add_item("1", "Tibetan Shawl", 45.99, 2)
        cart.add_item("2", "Handmade Jacket", 89.50, 1)
        print("Current Cart:", cart.view_cart())
        print("Total:", cart.calculate_total())

        cart.update_quantity("1", 3)
        print("Updated Cart:", cart.view_cart())
        print("Total After Update:", cart.calculate_total())

        cart.remove_item("2")
        print("Cart After Removal:", cart.view_cart())
        print("Final Total:", cart.calculate_total())

    except (ValueError, KeyError) as e:
        print(f"Error: {e}")
```
