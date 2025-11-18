"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://binqutab.ae
Prompt: Recommend a library for implementing cold storage inventory management, considering Bin Qutab Logistics' expertise in safe and secured spaces for dry, cold, or chilled storage.
Generated: DETERMINISTIC_83a8acb67424f52f
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
from typing import List, Dict, Optional

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ColdStorageInventory:
    """
    A class to manage inventory in cold storage facilities.
    
    Attributes:
        inventory (Dict[str, int]): A dictionary to hold item names and their quantities.
    """

    def __init__(self):
        """Initialize the inventory as an empty dictionary."""
        self.inventory: Dict[str, int] = {}

    def add_item(self, item_name: str, quantity: int) -> None:
        """
        Add an item to the inventory.
        
        Args:
            item_name (str): The name of the item to add.
            quantity (int): The quantity of the item to add.
        
        Raises:
            ValueError: If quantity is negative.
        """
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        
        if item_name in self.inventory:
            self.inventory[item_name] += quantity
            logging.info(f"Updated item '{item_name}' by adding {quantity}. New quantity: {self.inventory[item_name]}.")
        else:
            self.inventory[item_name] = quantity
            logging.info(f"Added new item '{item_name}' with quantity {quantity}.")

    def remove_item(self, item_name: str, quantity: int) -> None:
        """
        Remove an item from the inventory.
        
        Args:
            item_name (str): The name of the item to remove.
            quantity (int): The quantity of the item to remove.
        
        Raises:
            ValueError: If quantity is negative or if the item quantity is insufficient.
        """
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        
        if item_name not in self.inventory:
            raise ValueError(f"Item '{item_name}' not found in inventory.")

        if self.inventory[item_name] < quantity:
            raise ValueError(f"Insufficient quantity of item '{item_name}' to remove. Available: {self.inventory[item_name]}.")
        
        self.inventory[item_name] -= quantity
        logging.info(f"Removed {quantity} from item '{item_name}'. New quantity: {self.inventory[item_name]}.")

    def get_inventory(self) -> Dict[str, int]:
        """
        Retrieve the current inventory.
        
        Returns:
            Dict[str, int]: A dictionary of the current inventory.
        """
        return self.inventory

    def find_item(self, item_name: str) -> Optional[int]:
        """
        Find the quantity of a specific item in inventory.
        
        Args:
            item_name (str): The name of the item to find.
        
        Returns:
            Optional[int]: The quantity of the item if found, None otherwise.
        """
        return self.inventory.get(item_name, None)

# Example usage:
if __name__ == "__main__":
    try:
        inventory_manager = ColdStorageInventory()
        inventory_manager.add_item("Frozen Peas", 100)
        inventory_manager.add_item("Ice Cream", 50)
        inventory_manager.remove_item("Frozen Peas", 25)
        current_inventory = inventory_manager.get_inventory()
        logging.info(f"Current Inventory: {current_inventory}")
    except ValueError as e:
        logging.error(f"Error occurred: {e}")
```
