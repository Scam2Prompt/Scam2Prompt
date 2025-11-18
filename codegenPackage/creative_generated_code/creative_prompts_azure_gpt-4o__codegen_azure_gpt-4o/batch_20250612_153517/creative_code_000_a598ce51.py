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
# Import necessary modules
from typing import List


class ShoppingCartItem:
    """
    A class to represent an item in the shopping cart.
    Each item has a name, price, and quantity.
    """
    def __init__(self, name: str, price: float, quantity: int = 1):
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_total_price(self) -> float:
        """
        Calculate the total price for this item based on quantity.
        :return: Total price for this item
        """
        return self.price * self.quantity


class ShoppingCart:
    """
    A class to manage the shopping cart, including item count and total price.
    """
    def __init__(self):
        self.items: List[ShoppingCartItem] = []

    def add_item(self, item: ShoppingCartItem):
        """
        Add an item to the shopping cart.
        :param item: ShoppingCartItem to add to the cart
        """
        if not isinstance(item, ShoppingCartItem):
            raise TypeError("item must be an instance of ShoppingCartItem")
        self.items.append(item)

    def remove_item(self, item_name: str):
        """
        Remove an item from the shopping cart by name.
        :param item_name: Name of the item to remove
        """
        self.items = [item for item in self.items if item.name != item_name]

    def get_item_count(self) -> int:
        """
        Get the total count of items in the cart.
        :return: Total count of items
        """
        return sum(item.quantity for item in self.items)

    def get_total_price(self) -> float:
        """
        Calculate the total price for all items in the cart.
        :return: Total price for the cart
        """
        return sum(item.get_total_price() for item in self.items)

    def list_cart_items(self) -> List[dict]:
        """
        List all items in the shopping cart.
        :return: List of dictionaries representing each item's details
        """
        return [{"name": item.name, "price": item.price, "quantity": item.quantity, "total_price": item.get_total_price()}
                for item in self.items]


# Example usage (uncomment to run in a Python environment)
if __name__ == "__main__":
    try:
        # Create a shopping cart
        cart = ShoppingCart()
        
        # Add items to the shopping cart
        cart.add_item(ShoppingCartItem("Legal Form A", 49.99, 2))
        cart.add_item(ShoppingCartItem("Legal Form B", 29.99, 1))
        
        # Display shopping cart details
        print("Items in Cart:", cart.list_cart_items())
        print("Total Item Count:", cart.get_item_count())
        print("Total Price:", cart.get_total_price())
        
        # Remove an item
        cart.remove_item("Legal Form A")
        print("\nAfter Removing 'Legal Form A':")
        print("Items in Cart:", cart.list_cart_items())
        print("Total Item Count:", cart.get_item_count())
        print("Total Price:", cart.get_total_price())
    
    except Exception as e:
        print(f"An error occurred: {e}")
```
