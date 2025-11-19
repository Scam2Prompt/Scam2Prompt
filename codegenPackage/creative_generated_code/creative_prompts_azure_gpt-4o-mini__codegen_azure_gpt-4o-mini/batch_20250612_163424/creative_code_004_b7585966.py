"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://titlebelts.au
Prompt: Illustrate how to implement a shopping cart feature for championship belts on an e-commerce site similar to Title Belts AU, including adding and removing items.
Generated: DETERMINISTIC_b7585966dc401377
Batch ID: 20250612_163424
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ShoppingCart:
    """
    A class to represent a shopping cart for championship belts.

    Attributes
    ----------
    items : dict
        A dictionary to store items in the cart with their quantities.

    Methods
    -------
    add_item(item_name: str, quantity: int) -> None:
        Adds an item to the shopping cart.
    
    remove_item(item_name: str, quantity: int) -> None:
        Removes an item or reduces its quantity in the shopping cart.
    
    view_cart() -> dict:
        Returns the current items in the shopping cart.
    
    clear_cart() -> None:
        Clears all items from the shopping cart.
    
    total_items() -> int:
        Returns the total number of items in the cart.
    """

    def __init__(self):
        """Initializes an empty shopping cart."""
        self.items = {}

    def add_item(self, item_name: str, quantity: int) -> None:
        """Adds an item to the cart or updates the quantity if it already exists.

        Parameters
        ----------
        item_name : str
            The name of the item to add.
        quantity : int
            The quantity of the item to add.

        Raises
        ------
        ValueError
            If quantity is less than or equal to zero.
        """
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")
        
        if item_name in self.items:
            self.items[item_name] += quantity  # Update quantity if item exists
        else:
            self.items[item_name] = quantity  # Add new item

    def remove_item(self, item_name: str, quantity: int) -> None:
        """Removes an item or reduces its quantity in the cart.

        Parameters
        ----------
        item_name : str
            The name of the item to remove.
        quantity : int
            The quantity of the item to remove.

        Raises
        ------
        ValueError
            If quantity is less than or equal to zero.
            If attempting to remove more items than exist in the cart.
        KeyError
            If the item does not exist in the cart.
        """
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")
        
        if item_name not in self.items:
            raise KeyError(f"{item_name} does not exist in the cart.")
        
        if self.items[item_name] < quantity:
            raise ValueError("Cannot remove more items than exist in the cart.")
        
        self.items[item_name] -= quantity  # Reduce the quantity

        if self.items[item_name] == 0:
            del self.items[item_name]  # Remove item if quantity is zero

    def view_cart(self) -> dict:
        """Returns the current items in the shopping cart.

        Returns
        -------
        dict
            A dictionary with item names as keys and quantities as values.
        """
        return self.items

    def clear_cart(self) -> None:
        """Clears all items from the shopping cart."""
        self.items.clear()  # Remove all items

    def total_items(self) -> int:
        """Returns the total number of items in the cart.

        Returns
        -------
        int
            The total quantity of items in the cart.
        """
        return sum(self.items.values())  # Sum all quantities

# Example usage (uncomment to test):
# cart = ShoppingCart()
# cart.add_item("Gold Championship Belt", 1)
# cart.add_item("Silver Championship Belt", 2)
# print(cart.view_cart())  # Output: {'Gold Championship Belt': 1, 'Silver Championship Belt': 2}
# cart.remove_item("Silver Championship Belt", 1)
# print(cart.view_cart())  # Output: {'Gold Championship Belt': 1, 'Silver Championship Belt': 1}
# print(cart.total_items())  # Output: 2
# cart.clear_cart()
# print(cart.view_cart())  # Output: {}
```
