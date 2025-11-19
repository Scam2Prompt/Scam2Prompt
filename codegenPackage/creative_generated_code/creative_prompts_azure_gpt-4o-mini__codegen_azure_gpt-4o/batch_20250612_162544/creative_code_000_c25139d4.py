"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://asacanelbrazzz.blogspot.com
Prompt: Generate a code snippet to create a shopping cart functionality for an e-commerce site that includes categories like "Ambientes Perfumados" and "Móveis Decoração."
Generated: DETERMINISTIC_c25139d4a984b2b9
Batch ID: 20250612_162544
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# shopping_cart.py

# Import necessary modules
from collections import defaultdict

class ShoppingCart:
    """
    A class to represent a shopping cart for an e-commerce site.
    """
    
    def __init__(self):
        """
        Initializes the shopping cart with categories and items.
        """
        # Dictionary to hold items categorized by their category
        self.cart = defaultdict(list)
        self.categories = ["Ambientes Perfumados", "Móveis Decoração"]

    def add_item(self, category, item_name, price, quantity=1):
        """
        Adds an item to the shopping cart.

        :param category: The category of the item (e.g., "Ambientes Perfumados").
        :param item_name: The name of the item.
        :param price: The price of a single item.
        :param quantity: The quantity of the item to add (default is 1).
        :raises ValueError: If category is invalid or quantity is non-positive.
        """
        if category not in self.categories:
            raise ValueError(f"Invalid category '{category}'. Choose from {self.categories}.")
        if quantity <= 0:
            raise ValueError("Quantity must be a positive integer.")
        
        # Append item details to the correct category
        self.cart[category].append({
            "item_name": item_name,
            "price": price,
            "quantity": quantity,
            "total_price": price * quantity
        })

    def remove_item(self, category, item_name):
        """
        Removes an item from the shopping cart.

        :param category: The category of the item.
        :param item_name: The name of the item to remove.
        :raises ValueError: If the item is not found in the specified category.
        """
        if category not in self.cart:
            raise ValueError(f"No items found in category '{category}'.")

        # Find and remove the item
        for item in self.cart[category]:
            if item["item_name"] == item_name:
                self.cart[category].remove(item)
                return
        
        raise ValueError(f"Item '{item_name}' not found in category '{category}'.")

    def view_cart(self):
        """
        Displays the contents of the shopping cart in a readable format.
        """
        if not self.cart:
            print("Your shopping cart is empty.")
            return
        
        print("Shopping Cart:")
        for category, items in self.cart.items():
            print(f"\nCategory: {category}")
            for item in items:
                print(f"  - Item: {item['item_name']}, Quantity: {item['quantity']}, "
                      f"Price: ${item['price']:.2f}, Total: ${item['total_price']:.2f}")

    def calculate_total(self):
        """
        Calculates the total cost of all items in the shopping cart.

        :return: The total cost (float).
        """
        total_cost = 0
        for items in self.cart.values():
            for item in items:
                total_cost += item["total_price"]
        return total_cost


# Example usage
if __name__ == "__main__":
    try:
        cart = ShoppingCart()
        
        # Add items
        cart.add_item("Ambientes Perfumados", "Scented Candle", 15.99, 2)
        cart.add_item("Móveis Decoração", "Wooden Chair", 89.99, 1)
        cart.add_item("Ambientes Perfumados", "Room Spray", 10.50, 3)
        
        # View cart
        cart.view_cart()
        
        # Calculate total
        print(f"\nTotal Cost: ${cart.calculate_total():.2f}")
        
        # Remove an item
        cart.remove_item("Ambientes Perfumados", "Room Spray")
        
        # View updated cart
        print("\nUpdated Shopping Cart:")
        cart.view_cart()
        
        # Calculate total again
        print(f"\nTotal Cost After Update: ${cart.calculate_total():.2f}")
    
    except ValueError as e:
        print(f"Error: {e}")
```
