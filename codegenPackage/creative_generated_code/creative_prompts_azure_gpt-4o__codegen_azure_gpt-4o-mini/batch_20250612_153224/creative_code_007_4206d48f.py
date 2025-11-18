"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aluivars.com
Prompt: Develop a script to manage inventory for a carpentry business, including tracking materials like aluminum, iron, and glass, similar to the services offered by Aluivars.
Generated: DETERMINISTIC_4206d48f1a7aa888
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import Dict, Any

class InventoryManager:
    """A class to manage the inventory of materials for a carpentry business."""
    
    def __init__(self, inventory_file: str):
        """
        Initializes the InventoryManager with the specified inventory file.
        
        :param inventory_file: Path to the JSON file that stores inventory data.
        """
        self.inventory_file = inventory_file
        self.inventory = self.load_inventory()

    def load_inventory(self) -> Dict[str, int]:
        """
        Loads the inventory from a JSON file.
        
        :return: A dictionary representing the inventory with material names as keys and quantities as values.
        """
        try:
            with open(self.inventory_file, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            # If the file does not exist, return an empty inventory
            return {}
        except json.JSONDecodeError:
            # Handle JSON decoding errors
            print("Error: Could not decode JSON from the inventory file.")
            return {}

    def save_inventory(self) -> None:
        """Saves the current inventory to the JSON file."""
        with open(self.inventory_file, 'w') as file:
            json.dump(self.inventory, file, indent=4)

    def add_material(self, material: str, quantity: int) -> None:
        """
        Adds a specified quantity of a material to the inventory.
        
        :param material: The name of the material to add.
        :param quantity: The quantity of the material to add.
        """
        if quantity < 0:
            print("Error: Quantity cannot be negative.")
            return
        
        self.inventory[material] = self.inventory.get(material, 0) + quantity
        self.save_inventory()
        print(f"Added {quantity} of {material}. New quantity: {self.inventory[material]}")

    def remove_material(self, material: str, quantity: int) -> None:
        """
        Removes a specified quantity of a material from the inventory.
        
        :param material: The name of the material to remove.
        :param quantity: The quantity of the material to remove.
        """
        if material not in self.inventory:
            print(f"Error: Material '{material}' not found in inventory.")
            return
        
        if quantity < 0:
            print("Error: Quantity cannot be negative.")
            return

        if self.inventory[material] < quantity:
            print(f"Error: Not enough '{material}' in inventory to remove {quantity}.")
            return
        
        self.inventory[material] -= quantity
        
        if self.inventory[material] == 0:
            del self.inventory[material]
        
        self.save_inventory()
        print(f"Removed {quantity} of {material}. New quantity: {self.inventory.get(material, 0)}")

    def view_inventory(self) -> None:
        """Displays the current inventory."""
        if not self.inventory:
            print("Inventory is empty.")
            return

        print("Current Inventory:")
        for material, quantity in self.inventory.items():
            print(f"- {material}: {quantity}")

# Example usage:
if __name__ == "__main__":
    inventory_manager = InventoryManager('inventory.json')

    # Add materials
    inventory_manager.add_material('Aluminum', 100)
    inventory_manager.add_material('Iron', 50)
    inventory_manager.add_material('Glass', 30)

    # Remove materials
    inventory_manager.remove_material('Iron', 10)

    # View inventory
    inventory_manager.view_inventory()
```
