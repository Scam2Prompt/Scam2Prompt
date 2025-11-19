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
"""
Shopping Cart Module

This module provides functionality to manage a shopping cart. Users can view items, add items,
remove items, update item quantities, and calculate the total price of the cart.
"""

class ShoppingCart:
    def __init__(self):
        """Initialize an empty shopping cart."""
        self.items = {}  # Dictionary to store items in the format {item_id: {"name": str, "price": float, "quantity": int}}

    def add_item(self, item_id, name, price, quantity=1):
        """
        Add an item to the shopping cart. If the item already exists, its quantity is updated.
        
        Args:
            item_id (str): Unique identifier for the item.
            name (str): Name of the item.
            price (float): Price of the item.
            quantity (int): Quantity to add. Defaults to 1.
        """
        if item_id in self.items:
            self.items[item_id]["quantity"] += quantity
        else:
            self.items[item_id] = {"name": name, "price": price, "quantity": quantity}

    def remove_item(self, item_id):
        """
        Remove an item from the shopping cart.
        
        Args:
            item_id (str): Unique identifier for the item to be removed.
        
        Raises:
            KeyError: If the item does not exist in the cart.
        """
        if item_id in self.items:
            del self.items[item_id]
        else:
            raise KeyError(f"Item with ID '{item_id}' not found in the cart.")

    def update_quantity(self, item_id, quantity):
        """
        Update the quantity of a specific item in the cart.
        
        Args:
            item_id (str): Unique identifier for the item.
            quantity (int): New quantity for the item.
        
        Raises:
            KeyError: If the item does not exist in the cart.
            ValueError: If the quantity is less than 1.
        """
        if item_id not in self.items:
            raise KeyError(f"Item with ID '{item_id}' not found in the cart.")
        if quantity < 1:
            raise ValueError("Quantity must be at least 1.")
        self.items[item_id]["quantity"] = quantity

    def view_cart(self):
        """
        View items in the shopping cart.
        
        Returns:
            list: A list of items in the cart, where each item is a dictionary with keys "item_id", "name", "price", and "quantity".
        """
        return [{"item_id": item_id, **details} for item_id, details in self.items.items()]

    def calculate_total(self):
        """
        Calculate the total price of all items in the cart.
        
        Returns:
            float: The total price of all items.
        """
        return sum(details["price"] * details["quantity"] for details in self.items.values())


# Example usage
if __name__ == "__main__":
    cart = ShoppingCart()
    try:
        # Add items to the cart
        cart.add_item("001", "Apple", 0.5, 3)
        cart.add_item("002", "Banana", 0.2, 5)
        cart.add_item("003", "Cherry", 1.0)

        # View the cart
        print("Cart Contents:")
        for item in cart.view_cart():
            print(item)

        # Update quantity
        cart.update_quantity("002", 10)

        # Remove an item
        cart.remove_item("003")

        # Calculate total
        print("\nTotal Price:", cart.calculate_total())
    except (KeyError, ValueError) as e:
        print(f"Error: {e}")
```
