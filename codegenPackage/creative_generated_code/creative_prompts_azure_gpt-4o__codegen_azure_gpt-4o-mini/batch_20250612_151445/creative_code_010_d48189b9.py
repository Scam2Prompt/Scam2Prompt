"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://demoablabs.com
Prompt: Recommend software solutions for managing environmental sample media inventory, including PVC filters, MCE filters, and sorbent tubes as described by A & B Labs.
Generated: DETERMINISTIC_d48189b9c756da18
Batch ID: 20250612_151445
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict, Any

class InventoryItem:
    """
    Class to represent an inventory item for environmental sample media.
    """

    def __init__(self, item_id: str, item_type: str, quantity: int):
        """
        Initializes a new InventoryItem.

        :param item_id: Unique identifier for the item
        :param item_type: Type of the item (e.g., PVC filter, MCE filter, sorbent tube)
        :param quantity: Quantity of the item in inventory
        """
        self.item_id = item_id
        self.item_type = item_type
        self.quantity = quantity

    def to_dict(self) -> Dict[str, Any]:
        """
        Converts the InventoryItem to a dictionary.

        :return: Dictionary representation of the item
        """
        return {
            "item_id": self.item_id,
            "item_type": self.item_type,
            "quantity": self.quantity,
        }


class InventoryManager:
    """
    Class to manage the inventory of environmental sample media.
    """

    def __init__(self):
        """
        Initializes an empty inventory.
        """
        self.inventory: List[InventoryItem] = []

    def add_item(self, item: InventoryItem) -> None:
        """
        Adds a new item to the inventory.

        :param item: InventoryItem to add
        """
        self.inventory.append(item)

    def remove_item(self, item_id: str) -> bool:
        """
        Removes an item from the inventory based on the item ID.

        :param item_id: Unique identifier for the item to remove
        :return: True if the item was removed, False otherwise
        """
        for item in self.inventory:
            if item.item_id == item_id:
                self.inventory.remove(item)
                return True
        return False

    def update_quantity(self, item_id: str, quantity: int) -> bool:
        """
        Updates the quantity of an existing item in the inventory.

        :param item_id: Unique identifier for the item to update
        :param quantity: New quantity of the item
        :return: True if the quantity was updated, False otherwise
        """
        for item in self.inventory:
            if item.item_id == item_id:
                item.quantity = quantity
                return True
        return False

    def export_inventory(self, file_path: str) -> None:
        """
        Exports the current inventory to a JSON file.

        :param file_path: Path to the file where inventory should be saved
        """
        try:
            with open(file_path, 'w') as f:
                json.dump([item.to_dict() for item in self.inventory], f, indent=4)
        except IOError as e:
            print(f"Error writing to file {file_path}: {e}")

    def import_inventory(self, file_path: str) -> None:
        """
        Imports inventory items from a JSON file.

        :param file_path: Path to the file from which inventory should be loaded
        """
        try:
            with open(file_path, 'r') as f:
                items = json.load(f)
                for item_data in items:
                    item = InventoryItem(item_data['item_id'], item_data['item_type'], item_data['quantity'])
                    self.add_item(item)
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error reading from file {file_path}: {e}")


# Example usage
if __name__ == "__main__":
    inventory_manager = InventoryManager()

    # Add some inventory items
    inventory_manager.add_item(InventoryItem("001", "PVC Filter", 100))
    inventory_manager.add_item(InventoryItem("002", "MCE Filter", 50))
    inventory_manager.add_item(InventoryItem("003", "Sorbent Tube", 200))

    # Update an item
    inventory_manager.update_quantity("002", 75)

    # Export the inventory to a file
    inventory_manager.export_inventory("inventory.json")

    # Import inventory from a file
    inventory_manager.import_inventory("inventory.json")
```
