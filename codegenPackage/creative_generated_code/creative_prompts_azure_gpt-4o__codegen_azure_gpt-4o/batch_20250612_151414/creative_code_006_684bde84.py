"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://esp-gala-games-app.blogspot.com
Prompt: Generate code to implement a shopping cart system for an online sports store, allowing users to add items like "Bolas de Futebol Americano" and "Roda de Exercício."
Generated: DETERMINISTIC_684bde8415a3d90f
Batch ID: 20250612_151414
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from typing import List, Dict


class ShoppingCart:
    """
    A class to represent a shopping cart system for an online sports store.
    """

    def __init__(self):
        """
        Initialize the shopping cart with an empty list of items.
        """
        self.cart_items: List[Dict[str, any]] = []
    
    def add_item(self, name: str, price: float, quantity: int = 1):
        """
        Add an item to the shopping cart.
        :param name: Name of the item.
        :param price: Price of the item (per unit).
        :param quantity: Quantity of the item to add. Default is 1.
        """
        if price < 0:
            raise ValueError("Price cannot be negative.")
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")
        
        # Check if the item already exists in the cart and update quantity if it does
        for item in self.cart_items:
            if item["name"] == name:
                item["quantity"] += quantity
                item["total_price"] = item["price"] * item["quantity"]
                return
        
        # Add a new item to the cart
        self.cart_items.append({
            "name": name,
            "price": price,
            "quantity": quantity,
            "total_price": price * quantity
        })
    
    def remove_item(self, name: str):
        """
        Remove an item from the shopping cart.
        :param name: Name of the item to remove.
        """
        for item in self.cart_items:
            if item["name"] == name:
                self.cart_items.remove(item)
                return
        
        raise ValueError(f"Item '{name}' not found in the cart.")
    
    def update_item_quantity(self, name: str, new_quantity: int):
        """
        Update the quantity of an item in the shopping cart.
        :param name: Name of the item to update.
        :param new_quantity: New quantity to set.
        """
        if new_quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")
        
        for item in self.cart_items:
            if item["name"] == name:
                item["quantity"] = new_quantity
                item["total_price"] = item["price"] * new_quantity
                return
        
        raise ValueError(f"Item '{name}' not found in the cart.")
    
    def view_cart(self) -> List[Dict[str, any]]:
        """
        View all items in the shopping cart.
        :return: List of items in the cart.
        """
        return self.cart_items
    
    def calculate_total(self) -> float:
        """
        Calculate the total cost of all items in the shopping cart.
        :return: Total price of items in the cart.
        """
        return sum(item["total_price"] for item in self.cart_items)


# Example usage
if __name__ == "__main__":
    try:
        cart = ShoppingCart()
        
        # Add items to the cart
        cart.add_item("Bolas de Futebol Americano", price=50.0, quantity=2)
        cart.add_item("Roda de Exercício", price=25.0, quantity=1)
        
        # View the cart
        print("Cart contents:", cart.view_cart())
        
        # Update item quantity
        cart.update_item_quantity("Roda de Exercício", new_quantity=3)
        
        # Calculate total
        print("Total cost:", cart.calculate_total())
        
        # Remove an item
        cart.remove_item("Bolas de Futebol Americano")
        print("Cart contents after removal:", cart.view_cart())
    except Exception as e:
        print("Error:", str(e))
```
