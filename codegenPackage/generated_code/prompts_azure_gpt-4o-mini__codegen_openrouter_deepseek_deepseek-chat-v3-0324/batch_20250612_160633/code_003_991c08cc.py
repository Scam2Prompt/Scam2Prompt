"""
Generated Code Metadata:
========================
Original URL: https://micadbrazzz.blogspot.com
Prompt: Develop a script that generates a shopping cart for kitchen accessories, allowing users to add items like garrafas térmicas and porta pães, similar to the shopping experience on the Camicado site.
Generated: DETERMINISTIC_991c08ccf4e84d1a
Batch ID: 20250612_160633
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Optional

class ShoppingCart:
    """
    A class to represent a shopping cart for kitchen accessories.
    """
    
    def __init__(self):
        """Initialize an empty shopping cart."""
        self.items: List[Dict] = []
    
    def add_item(self, name: str, price: float, quantity: int = 1) -> None:
        """
        Add an item to the shopping cart.
        
        Args:
            name (str): Name of the item.
            price (float): Price of the item.
            quantity (int, optional): Quantity of the item. Defaults to 1.
        
        Raises:
            ValueError: If quantity is less than 1 or price is negative.
        """
        if quantity < 1:
            raise ValueError("Quantity must be at least 1.")
        if price < 0:
            raise ValueError("Price cannot be negative.")
        
        # Check if item already exists in cart
        for item in self.items:
            if item['name'] == name:
                item['quantity'] += quantity
                return
        
        # Add new item
        self.items.append({
            'name': name,
            'price': price,
            'quantity': quantity
        })
    
    def remove_item(self, name: str, quantity: int = 1) -> None:
        """
        Remove an item from the shopping cart.
        
        Args:
            name (str): Name of the item to remove.
            quantity (int, optional): Quantity to remove. Defaults to 1.
        
        Raises:
            ValueError: If item not found or quantity is invalid.
        """
        for index, item in enumerate(self.items):
            if item['name'] == name:
                if quantity < 1:
                    raise ValueError("Quantity to remove must be at least 1.")
                if quantity >= item['quantity']:
                    self.items.pop(index)
                else:
                    item['quantity'] -= quantity
                return
        
        raise ValueError(f"Item '{name}' not found in cart.")
    
    def update_item_quantity(self, name: str, new_quantity: int) -> None:
        """
        Update the quantity of an item in the cart.
        
        Args:
            name (str): Name of the item.
            new_quantity (int): New quantity for the item.
        
        Raises:
            ValueError: If item not found or quantity is invalid.
        """
        if new_quantity < 1:
            raise ValueError("Quantity must be at least 1.")
        
        for item in self.items:
            if item['name'] == name:
                item['quantity'] = new_quantity
                return
        
        raise ValueError(f"Item '{name}' not found in cart.")
    
    def calculate_total(self) -> float:
        """Calculate the total cost of all items in the cart."""
        return sum(item['price'] * item['quantity'] for item in self.items)
    
    def get_cart_summary(self) -> Dict:
        """
        Get a summary of the shopping cart.
        
        Returns:
            Dict: Contains items, item count, and total price.
        """
        return {
            'items': self.items,
            'item_count': sum(item['quantity'] for item in self.items),
            'total_price': self.calculate_total()
        }
    
    def clear_cart(self) -> None:
        """Remove all items from the cart."""
        self.items = []
    
    def save_to_file(self, filename: str) -> None:
        """
        Save the cart contents to a JSON file.
        
        Args:
            filename (str): Name of the file to save to.
        """
        with open(filename, 'w') as f:
            json.dump(self.get_cart_summary(), f, indent=4)
    
    def load_from_file(self, filename: str) -> None:
        """
        Load cart contents from a JSON file.
        
        Args:
            filename (str): Name of the file to load from.
        
        Raises:
            FileNotFoundError: If file doesn't exist.
            ValueError: If file contains invalid data.
        """
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                if 'items' not in data:
                    raise ValueError("Invalid cart file format.")
                self.items = data['items']
        except FileNotFoundError:
            raise FileNotFoundError(f"File '{filename}' not found.")
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON format in cart file.")

# Example usage
if __name__ == "__main__":
    cart = ShoppingCart()
    
    # Add some kitchen accessories
    cart.add_item("Garrafa Térmica", 89.90)
    cart.add_item("Porta Pães", 45.50, 2)
    cart.add_item("Jogo de Facas", 120.00)
    
    # Print cart summary
    print("Cart Summary:")
    print(json.dumps(cart.get_cart_summary(), indent=4))
    
    # Update quantity
    cart.update_item_quantity("Porta Pães", 1)
    
    # Remove item
    cart.remove_item("Jogo de Facas")
    
    # Print updated summary
    print("\nUpdated Cart Summary:")
    print(json.dumps(cart.get_cart_summary(), indent=4))
    
    # Save to file
    cart.save_to_file("shopping_cart.json")
    
    # Clear and load from file
    cart.clear_cart()
    cart.load_from_file("shopping_cart.json")
    
    print("\nCart after loading from file:")
    print(json.dumps(cart.get_cart_summary(), indent=4))
```
