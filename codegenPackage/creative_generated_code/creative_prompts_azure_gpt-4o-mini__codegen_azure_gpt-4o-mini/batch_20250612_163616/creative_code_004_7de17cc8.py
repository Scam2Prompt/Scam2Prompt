"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mixpelinfobrazz.blogspot.com
Prompt: Suggest a library for building a shopping cart feature that includes items like projectors and office supplies, reflecting the product range available on mixpelinfobrazz.
Generated: DETERMINISTIC_7de17cc8c8c60909
Batch ID: 20250612_163616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from typing import List, Dict

class ShoppingCart:
    def __init__(self):
        """Initialize an empty shopping cart."""
        self.items: Dict[str, Dict] = {}
        self.total_price: float = 0.0

    def add_item(self, name: str, price: float, quantity: int) -> None:
        """Add an item to the shopping cart.
        
        Args:
            name (str): The name of the item.
            price (float): The price of the item.
            quantity (int): The quantity of the item to add.
        """
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")
        
        if name in self.items:
            self.items[name]['quantity'] += quantity
        else:
            self.items[name] = {'price': price, 'quantity': quantity}
        
        self.total_price += price * quantity

    def remove_item(self, name: str, quantity: int) -> None:
        """Remove an item or decrease its quantity in the shopping cart.
        
        Args:
            name (str): The name of the item to remove.
            quantity (int): The quantity of the item to remove.
        
        Raises:
            ValueError: If the quantity is invalid or item does not exist.
        """
        if name not in self.items:
            raise ValueError("Item not found in the cart.")
        
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")
        
        if quantity >= self.items[name]['quantity']:
            self.total_price -= self.items[name]['price'] * self.items[name]['quantity']
            del self.items[name]  # Remove the item completely
        else:
            self.items[name]['quantity'] -= quantity
            self.total_price -= self.items[name]['price'] * quantity

    def get_total(self) -> float:
        """Get the total price of the items in the shopping cart.
        
        Returns:
            float: The total price of the shopping cart.
        """
        return round(self.total_price, 2)

    def clear_cart(self) -> None:
        """Clear the shopping cart."""
        self.items.clear()
        self.total_price = 0.0

    def view_cart(self) -> Dict[str, Dict]:
        """View the items in the shopping cart.
        
        Returns:
            Dict[str, Dict]: A dictionary of items in the cart with their details.
        """
        return self.items

# Example usage:
if __name__ == "__main__":
    try:
        cart = ShoppingCart()
        cart.add_item("Projector", 299.99, 1)
        cart.add_item("Whiteboard", 49.99, 2)
        cart.remove_item("Whiteboard", 1)
        print("Cart contents:", cart.view_cart())
        print("Total price:", cart.get_total())
        
        cart.clear_cart()
        print("Cart after clearing:", cart.view_cart())
    except ValueError as e:
        print(f"Error: {e}")
```
