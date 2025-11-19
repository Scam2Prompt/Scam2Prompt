"""
Generated Code Metadata:
========================
Original URL: https://w-magiceden-ww.blogspot.com
Prompt: Generate a code snippet for an e-commerce website that displays a shopping cart with items, similar to the "Carrinho de Compras" feature on aquarelaesmalte.
Generated: DETERMINISTIC_117939f9d393ed84
Batch ID: 20250612_164310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# shopping_cart.py

from typing import List, Dict

class ShoppingCart:
    """
    A class to represent a shopping cart for an e-commerce website.
    """

    def __init__(self):
        """
        Initializes an empty shopping cart.
        """
        self.items = []  # List to store items in the cart

    def add_item(self, item_name: str, quantity: int, price: float):
        """
        Adds an item to the shopping cart.

        :param item_name: Name of the item
        :param quantity: Quantity of the item
        :param price: Price per unit of the item
        """
        if quantity <= 0 or price <= 0:
            raise ValueError("Quantity and price must be greater than zero.")
        
        # Check if the item already exists in the cart
        for item in self.items:
            if item['name'] == item_name:
                item['quantity'] += quantity
                item['total_price'] = item['quantity'] * item['price']
                return
        
        # Add new item to the cart
        self.items.append({
            'name': item_name,
            'quantity': quantity,
            'price': price,
            'total_price': quantity * price
        })

    def remove_item(self, item_name: str):
        """
        Removes an item from the shopping cart.

        :param item_name: Name of the item to remove
        """
        self.items = [item for item in self.items if item['name'] != item_name]

    def view_cart(self) -> List[Dict]:
        """
        Returns the current items in the shopping cart.

        :return: List of items in the cart
        """
        return self.items

    def calculate_total(self) -> float:
        """
        Calculates the total cost of items in the shopping cart.

        :return: Total cost of items
        """
        return sum(item['total_price'] for item in self.items)

    def clear_cart(self):
        """
        Clears all items from the shopping cart.
        """
        self.items = []


# Example usage
if __name__ == "__main__":
    try:
        cart = ShoppingCart()
        cart.add_item("Nail Polish", 2, 12.99)
        cart.add_item("Top Coat", 1, 15.99)
        cart.add_item("Nail Polish Remover", 1, 8.99)

        print("Shopping Cart:")
        for item in cart.view_cart():
            print(f"Item: {item['name']}, Quantity: {item['quantity']}, Price: ${item['price']:.2f}, Total: ${item['total_price']:.2f}")

        print(f"\nTotal Cost: ${cart.calculate_total():.2f}")

        cart.remove_item("Top Coat")
        print("\nAfter removing 'Top Coat':")
        for item in cart.view_cart():
            print(f"Item: {item['name']}, Quantity: {item['quantity']}, Price: ${item['price']:.2f}, Total: ${item['total_price']:.2f}")

        print(f"\nTotal Cost: ${cart.calculate_total():.2f}")

        cart.clear_cart()
        print("\nCart after clearing:", cart.view_cart())

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
