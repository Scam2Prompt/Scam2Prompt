"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://demirsoft.com
Prompt: Develop a software solution for managing franchise store operations using DemirSoft's "Zincir Franchise Şubeli Mağaza Yönetimi" tools.
Generated: DETERMINISTIC_8e64890b13b12ce8
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# franchise_management.py

class FranchiseStore:
    """
    A class to represent a franchise store.

    Attributes:
        store_id (int): The unique identifier for the store.
        name (str): The name of the franchise store.
        location (str): The location of the franchise store.
        inventory (dict): A dictionary to hold inventory items and their quantities.
    """

    def __init__(self, store_id, name, location):
        """
        Initializes the FranchiseStore with ID, name, location, and an empty inventory.

        Args:
            store_id (int): The unique identifier for the store.
            name (str): The name of the franchise store.
            location (str): The location of the franchise store.
        """
        self.store_id = store_id
        self.name = name
        self.location = location
        self.inventory = {}

    def add_inventory_item(self, item_name, quantity):
        """
        Adds an item to the inventory.

        Args:
            item_name (str): The name of the item to add.
            quantity (int): The quantity of the item to add.

        Raises:
            ValueError: If the quantity is not a positive integer.
        """
        if quantity <= 0:
            raise ValueError("Quantity must be a positive integer.")
        
        if item_name in self.inventory:
            self.inventory[item_name] += quantity
        else:
            self.inventory[item_name] = quantity

        print(f"Added {quantity} of {item_name} to inventory.")

    def remove_inventory_item(self, item_name, quantity):
        """
        Removes an item from the inventory.

        Args:
            item_name (str): The name of the item to remove.
            quantity (int): The quantity of the item to remove.

        Raises:
            ValueError: If the quantity is not a positive integer or exceeds the available quantity.
        """
        if quantity <= 0:
            raise ValueError("Quantity must be a positive integer.")
        
        if item_name not in self.inventory or self.inventory[item_name] < quantity:
            raise ValueError(f"Insufficient quantity of {item_name} in inventory.")
        
        self.inventory[item_name] -= quantity
        if self.inventory[item_name] == 0:
            del self.inventory[item_name]
        
        print(f"Removed {quantity} of {item_name} from inventory.")

    def view_inventory(self):
        """
        Displays the current inventory of the franchise store.
        """
        print(f"Inventory for {self.name} (Store ID: {self.store_id}):")
        for item, quantity in self.inventory.items():
            print(f"- {item}: {quantity}")

# Example Usage
if __name__ == "__main__":
    try:
        # Create a new franchise store
        store = FranchiseStore(store_id=1, name="DemirSoft Franchise", location="Istanbul")
        
        # Manage inventory
        store.add_inventory_item("Chocolate", 50)
        store.add_inventory_item("Ice Cream", 30)
        store.view_inventory()
        
        store.remove_inventory_item("Chocolate", 20)
        store.view_inventory()
        
        # Attempt to remove more items than available
        store.remove_inventory_item("Ice Cream", 35)
    except ValueError as e:
        print(f"Error: {e}")
```
