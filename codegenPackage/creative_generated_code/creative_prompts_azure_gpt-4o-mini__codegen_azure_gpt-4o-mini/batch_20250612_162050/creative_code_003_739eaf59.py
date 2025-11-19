"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://obsidiajeans.com.br
Prompt: Develop a shopping cart feature in Python that allows users to add items like the wide leg pants or high-stretch shorts from Obsidia Jeans to their cart.
Generated: DETERMINISTIC_739eaf59e84c943c
Batch ID: 20250612_162050
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
        """Initialize an empty shopping cart."""
        self.items = []
    
    def add_item(self, item, quantity=1):
        """
        Add an item to the shopping cart.
        
        :param item: A dictionary representing the item (must include 'name' and 'price').
        :param quantity: The quantity of the item to add (default is 1).
        """
        if not isinstance(item, dict) or 'name' not in item or 'price' not in item:
            raise ValueError("Item must be a dictionary with 'name' and 'price' keys.")
        
        if quantity <= 0:
            raise ValueError("Quantity must be a positive integer.")
        
        # Add the item to the cart
        self.items.append({'item': item, 'quantity': quantity})
    
    def remove_item(self, item_name):
        """
        Remove an item from the shopping cart by name.
        
        :param item_name: The name of the item to remove.
        """
        for i, cart_item in enumerate(self.items):
            if cart_item['item']['name'] == item_name:
                del self.items[i]
                return
        raise ValueError(f"Item '{item_name}' not found in cart.")
    
    def view_cart(self):
        """Return the current items in the shopping cart."""
        if not self.items:
            return "Your shopping cart is empty."
        
        cart_summary = "Items in your shopping cart:\n"
        for cart_item in self.items:
            item = cart_item['item']
            quantity = cart_item['quantity']
            cart_summary += f"{quantity} x {item['name']} - ${item['price']:.2f} each\n"
        
        return cart_summary
    
    def total_price(self):
        """Calculate the total price of items in the shopping cart."""
        total = 0.0
        for cart_item in self.items:
            total += cart_item['item']['price'] * cart_item['quantity']
        return total

# Example Usage
if __name__ == "__main__":
    cart = ShoppingCart()
    
    # Define example items
    wide_leg_pants = {'name': 'Wide Leg Pants', 'price': 49.99}
    high_stretch_shorts = {'name': 'High-Stretch Shorts', 'price': 29.99}
    
    # Add items to the cart
    try:
        cart.add_item(wide_leg_pants, quantity=2)
        cart.add_item(high_stretch_shorts, quantity=1)
        
        # View cart contents
        print(cart.view_cart())
        
        # Total price
        print(f"Total Price: ${cart.total_price():.2f}")
        
        # Remove an item
        cart.remove_item('Wide Leg Pants')
        print(cart.view_cart())
    except ValueError as e:
        print(f"Error: {e}")
```
