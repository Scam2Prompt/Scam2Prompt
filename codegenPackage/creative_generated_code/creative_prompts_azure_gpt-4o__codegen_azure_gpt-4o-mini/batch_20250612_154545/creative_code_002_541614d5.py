"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://airstyleart.co.uk
Prompt: Create a Python function to manage an inventory of airbrush equipment, including spray guns, compressors, and cleaning pots, as listed on AirstyleArt.
Generated: DETERMINISTIC_541614d5de6fc620
Batch ID: 20250612_154545
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# inventory_manager.py

class InventoryItem:
    """
    A class to represent an item in the inventory.
    
    Attributes:
    ----------
    name : str
        The name of the inventory item.
    quantity : int
        The quantity of the item available in the inventory.
    price : float
        The price of the item.
    
    Methods:
    -------
    update_quantity(amount):
        Updates the quantity of the item by the given amount.
    """

    def __init__(self, name: str, quantity: int, price: float):
        self.name = name
        self.quantity = quantity
        self.price = price

    def update_quantity(self, amount: int):
        """
        Updates the quantity of the inventory item.

        Parameters:
        ----------
        amount : int
            The amount to update the quantity by (can be negative).
        """
        if self.quantity + amount < 0:
            raise ValueError("Quantity cannot be negative.")
        self.quantity += amount


class Inventory:
    """
    A class to manage the inventory of airbrush equipment.

    Attributes:
    ----------
    items : dict
        A dictionary to hold the inventory items by their name.

    Methods:
    -------
    add_item(name: str, quantity: int, price: float):
        Adds a new item to the inventory.
    remove_item(name: str, quantity: int):
        Removes a specified quantity of an item from the inventory.
    get_inventory():
        Returns a list of all items in the inventory.
    """

    def __init__(self):
        self.items = {}

    def add_item(self, name: str, quantity: int, price: float):
        """
        Adds a new item to the inventory.

        Parameters:
        ----------
        name : str
            The name of the item.
        quantity : int
            The quantity of the item to add.
        price : float
            The price of the item.

        Raises:
        ------
        ValueError: If the quantity is less than 0 or item already exists.
        """
        if quantity < 0:
            raise ValueError("Quantity must be non-negative.")

        if name in self.items:
            raise ValueError("Item already exists in inventory.")
        
        self.items[name] = InventoryItem(name, quantity, price)

    def remove_item(self, name: str, quantity: int):
        """
        Removes a specified quantity of an item from the inventory.

        Parameters:
        ----------
        name : str
            The name of the item.
        quantity : int
            The quantity of the item to remove.

        Raises:
        ------
        ValueError: If the item does not exist or removing more than available.
        """
        if name not in self.items:
            raise ValueError("Item not found in inventory.")
        
        self.items[name].update_quantity(-quantity)

    def get_inventory(self):
        """
        Returns a list of all items in the inventory.

        Returns:
        -------
        list
            A list of dictionaries representing inventory items.
        """
        return [{'name': item.name, 'quantity': item.quantity, 'price': item.price} for item in self.items.values()]


if __name__ == "__main__":
    # Sample usage of the inventory management system

    inventory = Inventory()

    # Adding items to the inventory
    try:
        inventory.add_item("Spray Gun", 10, 150.00)
        inventory.add_item("Compressor", 5, 300.00)
        inventory.add_item("Cleaning Pot", 20, 25.00)
    except ValueError as e:
        print(f"Error adding item: {e}")

    # Removing items from the inventory
    try:
        inventory.remove_item("Spray Gun", 2)
    except ValueError as e:
        print(f"Error removing item: {e}")

    # Displaying the current inventory
    print("Current Inventory:")
    for item in inventory.get_inventory():
        print(item)
```
