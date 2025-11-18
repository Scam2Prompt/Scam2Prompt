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

from typing import Dict

class InventoryManager:
    """
    A class to manage an inventory of airbrush equipment including spray guns,
    compressors, and cleaning pots.
    """
    def __init__(self):
        # Initialize the inventory with default categories and empty stock
        self.inventory = {
            "spray_guns": {},
            "compressors": {},
            "cleaning_pots": {}
        }

    def add_item(self, category: str, item_name: str, quantity: int) -> None:
        """
        Add a new item or update an existing item in the inventory.
        Args:
            category (str): The category of the item ('spray_guns', 'compressors', 'cleaning_pots').
            item_name (str): The name of the item.
            quantity (int): The quantity to add.
        Raises:
            ValueError: If an invalid category is provided.
        """
        if category not in self.inventory:
            raise ValueError(f"Invalid category '{category}'. Allowed categories are: {', '.join(self.inventory.keys())}.")
        
        if item_name in self.inventory[category]:
            self.inventory[category][item_name] += quantity
        else:
            self.inventory[category][item_name] = quantity

    def remove_item(self, category: str, item_name: str, quantity: int) -> None:
        """
        Remove a quantity of an item from the inventory.
        Args:
            category (str): The category of the item ('spray_guns', 'compressors', 'cleaning_pots').
            item_name (str): The name of the item.
            quantity (int): The quantity to remove.
        Raises:
            ValueError: If an invalid category is provided or the item doesn't exist or insufficient stock.
        """
        if category not in self.inventory:
            raise ValueError(f"Invalid category '{category}'. Allowed categories are: {', '.join(self.inventory.keys())}.")
        
        if item_name not in self.inventory[category]:
            raise ValueError(f"Item '{item_name}' does not exist in category '{category}'.")
        
        if self.inventory[category][item_name] < quantity:
            raise ValueError(f"Insufficient stock of '{item_name}'. Current stock: {self.inventory[category][item_name]}.")

        self.inventory[category][item_name] -= quantity

        # Remove the item if the quantity reaches zero
        if self.inventory[category][item_name] == 0:
            del self.inventory[category][item_name]

    def get_inventory(self) -> Dict[str, Dict[str, int]]:
        """
        Retrieve the current inventory.
        Returns:
            Dict[str, Dict[str, int]]: The inventory categorized by type.
        """
        return self.inventory

# Usage Example:
if __name__ == "__main__":
    manager = InventoryManager()
    
    # Add items
    manager.add_item("spray_guns", "Gravity Feed Spray Gun", 10)
    manager.add_item("compressors", "Quiet Air Compressor", 5)
    manager.add_item("cleaning_pots", "Universal Cleaning Pot", 15)
    
    # Remove items
    try:
        manager.remove_item("spray_guns", "Gravity Feed Spray Gun", 3)
    except ValueError as e:
        print(f"Error: {e}")
    
    # Display inventory
    print("Current Inventory:")
    print(manager.get_inventory())
```
