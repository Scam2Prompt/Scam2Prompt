"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vaperiyadh2.com
Prompt: Illustrate how to implement a shopping cart feature that includes items like the Mazaj Infinity and Nasty Bar from Vape Riyadh 2.
Generated: DETERMINISTIC_638f8477a0b63ba3
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

class ShoppingCart:
    """
    A class to represent a shopping cart for a vape store.
    
    Attributes
    ----------
    items : dict
        A dictionary to hold items in the cart with their quantities.
    
    Methods
    -------
    add_item(item_name, quantity=1):
        Adds an item to the cart with the specified quantity.
        
    remove_item(item_name):
        Removes an item from the cart.
        
    update_item(item_name, quantity):
        Updates the quantity of an item in the cart.
        
    view_cart():
        Returns a summary of the items in the cart.
        
    clear_cart():
        Empties the shopping cart.
    """

    def __init__(self):
        """Initializes an empty shopping cart."""
        self.items = {}

    def add_item(self, item_name: str, quantity: int = 1):
        """Adds an item to the cart with the specified quantity.
        
        Parameters
        ----------
        item_name : str
            The name of the item to add.
        quantity : int
            The number of items to add (default is 1).
        """
        if quantity < 1:
            raise ValueError("Quantity must be at least 1.")
        
        if item_name in self.items:
            self.items[item_name] += quantity
        else:
            self.items[item_name] = quantity
    
    def remove_item(self, item_name: str):
        """Removes an item from the cart.
        
        Parameters
        ----------
        item_name : str
            The name of the item to remove.
            
        Raises
        ------
        KeyError
            If the item is not found in the cart.
        """
        if item_name not in self.items:
            raise KeyError(f"Item '{item_name}' not found in the cart.")
        
        del self.items[item_name]
    
    def update_item(self, item_name: str, quantity: int):
        """Updates the quantity of an item in the cart.
        
        Parameters
        ----------
        item_name : str
            The name of the item to update.
        quantity : int
            The new quantity for the item.
            
        Raises
        ------
        KeyError
            If the item is not found in the cart.
        ValueError
            If the quantity is less than 1.
        """
        if item_name not in self.items:
            raise KeyError(f"Item '{item_name}' not found in the cart.")
        
        if quantity < 1:
            raise ValueError("Quantity must be at least 1.")
        
        self.items[item_name] = quantity
    
    def view_cart(self) -> dict:
        """Returns a summary of the items in the cart.
        
        Returns
        -------
        dict
            A dictionary representing the current items in the cart.
        """
        return self.items
    
    def clear_cart(self):
        """Empties the shopping cart."""
        self.items.clear()


# Example usage
if __name__ == "__main__":
    cart = ShoppingCart()
    
    # Adding items to the cart
    cart.add_item("Mazaj Infinity", 2)
    cart.add_item("Nasty Bar", 1)
    
    print("Current Cart:", cart.view_cart())  # View items in the cart
    
    # Update the quantity of an item
    cart.update_item("Mazaj Infinity", 3)
    
    print("Updated Cart:", cart.view_cart())  # View updated items in the cart
    
    # Remove an item from the cart
    cart.remove_item("Nasty Bar")
    
    print("Cart after removal:", cart.view_cart())  # View items after removal
    
    # Clear the cart
    cart.clear_cart()
    
    print("Cart after clearing:", cart.view_cart())  # Should be empty
```
