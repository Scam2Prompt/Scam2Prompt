"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tecnicos-whirlpool.com
Prompt: Develop a system to manage inventory for Whirlpool appliance replacement parts, ensuring high-quality and reliable replacements as emphasized on the website.
Generated: DETERMINISTIC_eea283fd59c91c26
Batch ID: 20250612_152511
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import os
from typing import List, Dict, Any

class InventoryManager:
    """A class to manage the inventory of Whirlpool appliance replacement parts."""

    def __init__(self, inventory_file: str):
        """
        Initialize the InventoryManager with the given inventory file.

        Args:
            inventory_file (str): The path to the JSON file where inventory data is stored.
        """
        self.inventory_file = inventory_file
        self.inventory = self.load_inventory()

    def load_inventory(self) -> List[Dict[str, Any]]:
        """Load inventory data from a JSON file.

        Returns:
            List[Dict[str, Any]]: A list of inventory items.
        """
        if not os.path.exists(self.inventory_file):
            return []  # Return an empty list if the file doesn't exist
        try:
            with open(self.inventory_file, 'r') as file:
                return json.load(file)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error loading inventory: {e}")
            return []

    def save_inventory(self) -> None:
        """Save the current inventory data back to the JSON file."""
        try:
            with open(self.inventory_file, 'w') as file:
                json.dump(self.inventory, file, indent=4)
        except IOError as e:
            print(f"Error saving inventory: {e}")

    def add_part(self, part: Dict[str, Any]) -> None:
        """Add a new part to the inventory.

        Args:
            part (Dict[str, Any]): A dictionary representing the part to add.
        """
        self.inventory.append(part)
        self.save_inventory()

    def remove_part(self, part_id: str) -> None:
        """Remove a part from the inventory by its ID.

        Args:
            part_id (str): The ID of the part to remove.
        """
        self.inventory = [part for part in self.inventory if part['id'] != part_id]
        self.save_inventory()

    def update_part(self, part_id: str, updated_part: Dict[str, Any]) -> None:
        """Update an existing part in the inventory.

        Args:
            part_id (str): The ID of the part to update.
            updated_part (Dict[str, Any]): A dictionary representing the updated part.
        """
        for idx, part in enumerate(self.inventory):
            if part['id'] == part_id:
                self.inventory[idx] = updated_part
                self.save_inventory()
                return
        print(f"Part with ID {part_id} not found.")

    def list_parts(self) -> List[Dict[str, Any]]:
        """List all parts in the inventory.

        Returns:
            List[Dict[str, Any]]: A list of all parts.
        """
        return self.inventory

# Example usage
if __name__ == "__main__":
    inventory_manager = InventoryManager('inventory.json')

    # Adding a part
    new_part = {'id': 'W10123456', 'name': 'Water Filter', 'quantity': 100, 'price': 29.99}
    inventory_manager.add_part(new_part)

    # Listing all parts
    print("Current Inventory:")
    for part in inventory_manager.list_parts():
        print(part)

    # Updating a part
    updated_part = {'id': 'W10123456', 'name': 'Water Filter', 'quantity': 90, 'price': 27.99}
    inventory_manager.update_part('W10123456', updated_part)

    # Removing a part
    inventory_manager.remove_part('W10123456')
```
