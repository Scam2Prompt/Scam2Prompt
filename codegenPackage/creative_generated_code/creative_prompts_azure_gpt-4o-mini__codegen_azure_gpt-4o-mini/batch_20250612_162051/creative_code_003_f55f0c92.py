"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nomnompr.com
Prompt: Develop a shopping cart feature for a food delivery website that mirrors the user experience of Nom Nom's online store.
Generated: DETERMINISTIC_f55f0c9275c8f7be
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

from decimal import Decimal
from typing import List, Dict, Optional

class Item:
    """
    Represents an item in the shopping cart.
    
    Attributes:
        name (str): Name of the food item.
        price (Decimal): Price of the food item.
        quantity (int): Quantity of the item in the cart.
    """
    def __init__(self, name: str, price: Decimal, quantity: int = 1):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_price(self) -> Decimal:
        """Calculates the total price for this item based on quantity."""
        return self.price * self.quantity

class ShoppingCart:
    """
    Represents a shopping cart for the food delivery website.
    
    Attributes:
        items (List[Item]): A list of items in the shopping cart.
    """
    def __init__(self):
        self.items: List[Item] = []

    def add_item(self, item: Item) -> None:
        """Adds an item to the shopping cart."""
        self.items.append(item)

    def remove_item(self, item_name: str) -> bool:
        """Removes an item from the shopping cart by name."""
        for i, item in enumerate(self.items):
            if item.name == item_name:
                del self.items[i]
                return True
        return False

    def update_item_quantity(self, item_name: str, quantity: int) -> Optional[str]:
        """Updates the quantity of an item in the shopping cart."""
        if quantity < 1:
            return "Quantity must be at least 1."
        
        for item in self.items:
            if item.name == item_name:
                item.quantity = quantity
                return None
        return "Item not found in the cart."

    def calculate_total(self) -> Decimal:
        """Calculates the total cost of the items in the shopping cart."""
        return sum(item.total_price() for item in self.items)

    def clear_cart(self) -> None:
        """Clears all items from the shopping cart."""
        self.items.clear()

    def get_items(self) -> List[Dict[str, str]]:
        """Returns a list of items in a dictionary format for easier display."""
        return [{'name': item.name, 'price': str(item.price), 'quantity': item.quantity} for item in self.items]

# Example usage
if __name__ == "__main__":
    try:
        cart = ShoppingCart()
        cart.add_item(Item("Margherita Pizza", Decimal('12.99'), 2))
        cart.add_item(Item("Cheeseburger", Decimal('8.49'), 1))
        
        print("Items in cart:", cart.get_items())
        print("Total cost:", cart.calculate_total())

        cart.update_item_quantity("Margherita Pizza", 3)
        print("Updated cart:", cart.get_items())
        print("Updated total cost:", cart.calculate_total())

        cart.remove_item("Cheeseburger")
        print("Items after removal:", cart.get_items())
        print("Final total cost:", cart.calculate_total())

        cart.clear_cart()
        print("Cart after clearing:", cart.get_items())

    except Exception as e:
        print(f"An error occurred: {e}")
```

This code implements a simple shopping cart functionality with item management, including adding, removing, updating quantities, and calculating total prices. It is designed to be clean, efficient, and ready for production use.
