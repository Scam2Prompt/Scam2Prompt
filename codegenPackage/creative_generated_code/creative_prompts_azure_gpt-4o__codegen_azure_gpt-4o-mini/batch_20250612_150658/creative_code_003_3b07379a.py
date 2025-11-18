"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://krosmetal.com
Prompt: Provide a Python script for inventory management of stainless steel materials, including profiles, fittings, and flanges, as detailed on the Kros Metal website.
Generated: DETERMINISTIC_3b07379aa6d846fb
Batch ID: 20250612_150658
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import Dict, List, Union

class InventoryItem:
    """Class to represent an inventory item."""
    
    def __init__(self, item_id: str, name: str, quantity: int, item_type: str):
        """
        Initializes an InventoryItem.

        :param item_id: Unique identifier for the item
        :param name: Name of the item
        :param quantity: Number of items in stock
        :param item_type: Type of the item (profile, fitting, flange)
        """
        self.item_id = item_id
        self.name = name
        self.quantity = quantity
        self.item_type = item_type

    def to_dict(self) -> Dict[str, Union[str, int]]:
        """Converts the InventoryItem to a dictionary."""
        return {
            'item_id': self.item_id,
            'name': self.name,
            'quantity': self.quantity,
            'item_type': self.item_type
        }

class Inventory:
    """Class to manage inventory of stainless steel materials."""
    
    def __init__(self):
        """Initializes an empty inventory."""
        self.items: List[InventoryItem] = []

    def add_item(self, item: InventoryItem) -> None:
        """Adds an item to inventory.

        :param item: InventoryItem to add
        """
        self.items.append(item)

    def remove_item(self, item_id: str) -> None:
        """Removes an item from inventory by item_id.

        :param item_id: Unique identifier of the item to remove
        :raises ValueError: If the item is not found
        """
        item_to_remove = next((item for item in self.items if item.item_id == item_id), None)
        if item_to_remove:
            self.items.remove(item_to_remove)
        else:
            raise ValueError(f"Item with ID {item_id} not found in inventory.")

    def update_item_quantity(self, item_id: str, quantity: int) -> None:
        """Updates the quantity of a specific item in inventory.

        :param item_id: Unique identifier of the item to update
        :param quantity: New quantity of the item
        :raises ValueError: If the item is not found
        """
        item_to_update = next((item for item in self.items if item.item_id == item_id), None)
        if item_to_update:
            item_to_update.quantity = quantity
        else:
            raise ValueError(f"Item with ID {item_id} not found in inventory.")

    def get_inventory(self) -> List[Dict[str, Union[str, int]]]:
        """Returns a list of all inventory items as dictionaries."""
        return [item.to_dict() for item in self.items]

    def save_to_file(self, file_path: str) -> None:
        """Saves the inventory to a JSON file.

        :param file_path: Path to the file where the inventory will be saved
        :raises IOError: If the file cannot be written
        """
        try:
            with open(file_path, 'w') as f:
                json.dump(self.get_inventory(), f, indent=4)
        except IOError as e:
            raise IOError(f"Failed to save inventory to file {file_path}: {e}")

    def load_from_file(self, file_path: str) -> None:
        """Loads inventory from a JSON file.

        :param file_path: Path to the file from which to load the inventory
        :raises IOError: If the file cannot be read
        :raises ValueError: If the file contains invalid data
        """
        try:
            with open(file_path, 'r') as f:
                items_data = json.load(f)
                self.items = [InventoryItem(**item) for item in items_data]
        except IOError as e:
            raise IOError(f"Failed to load inventory from file {file_path}: {e}")
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid data in inventory file {file_path}: {e}")

def main():
    """Main function to demonstrate inventory management."""
    inventory = Inventory()

    # Example of adding items
    inventory.add_item(InventoryItem("101", "Stainless Steel Profile A", 50, "profile"))
    inventory.add_item(InventoryItem("102", "Stainless Steel Fitting B", 30, "fitting"))

    # Example of updating an item's quantity
    try:
        inventory.update_item_quantity("101", 70)
    except ValueError as e:
        print(e)

    # Example of removing an item
    try:
        inventory.remove_item("102")
    except ValueError as e:
        print(e)

    # Save inventory to file
    try:
        inventory.save_to_file("inventory.json")
    except IOError as e:
        print(e)

    # Load inventory from file
    try:
        inventory.load_from_file("inventory.json")
        print("Inventory loaded successfully.")
    except (IOError, ValueError) as e:
        print(e)

    # Print current inventory
    print(inventory.get_inventory())

if __name__ == "__main__":
    main()
```
