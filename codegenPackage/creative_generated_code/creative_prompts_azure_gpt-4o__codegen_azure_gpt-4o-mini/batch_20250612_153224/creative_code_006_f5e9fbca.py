"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vivekenterprises.co.in
Prompt: Create a Python script to manage inventory for an interior contracting company, including tracking materials for civil works, furniture, and electronic surveillance installations.
Generated: DETERMINISTIC_f5e9fbca7668f9d6
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
import os
from typing import Dict, Any, List

class InventoryManager:
    """
    A class to manage inventory for an interior contracting company.
    It supports tracking materials for civil works, furniture, and electronic surveillance installations.
    """

    def __init__(self, inventory_file: str):
        """
        Initializes the inventory manager with a specific inventory file.
        
        Args:
            inventory_file (str): The path to the inventory JSON file.
        """
        self.inventory_file = inventory_file
        self.inventory: Dict[str, Any] = {}
        self.load_inventory()

    def load_inventory(self) -> None:
        """
        Loads the inventory from the JSON file.
        If the file does not exist, initializes an empty inventory.
        """
        if os.path.exists(self.inventory_file):
            with open(self.inventory_file, 'r') as file:
                try:
                    self.inventory = json.load(file)
                except json.JSONDecodeError:
                    print("Error: Could not decode the JSON file. Initializing empty inventory.")
                    self.inventory = {}
        else:
            print("Inventory file not found. Initializing empty inventory.")
            self.inventory = {}

    def save_inventory(self) -> None:
        """
        Saves the current inventory to the JSON file.
        """
        with open(self.inventory_file, 'w') as file:
            json.dump(self.inventory, file, indent=4)

    def add_material(self, category: str, material_name: str, quantity: int) -> None:
        """
        Adds a material to the inventory in a specific category.
        
        Args:
            category (str): The category of the material (e.g., 'civil', 'furniture', 'surveillance').
            material_name (str): The name of the material.
            quantity (int): The quantity of the material to add.
        """
        if category not in self.inventory:
            self.inventory[category] = {}

        if material_name in self.inventory[category]:
            self.inventory[category][material_name] += quantity
        else:
            self.inventory[category][material_name] = quantity
        
        self.save_inventory()

    def remove_material(self, category: str, material_name: str, quantity: int) -> None:
        """
        Removes a specified quantity of material from the inventory.

        Args:
            category (str): The category of the material.
            material_name (str): The name of the material.
            quantity (int): The quantity of the material to remove.

        Raises:
            ValueError: If the quantity to remove exceeds the available stock.
        """
        if category in self.inventory and material_name in self.inventory[category]:
            if self.inventory[category][material_name] >= quantity:
                self.inventory[category][material_name] -= quantity
                if self.inventory[category][material_name] == 0:
                    del self.inventory[category][material_name]
                self.save_inventory()
            else:
                raise ValueError("Error: Not enough stock to remove the specified quantity.")
        else:
            raise ValueError("Error: Material not found in inventory.")

    def get_inventory_summary(self) -> Dict[str, Any]:
        """
        Returns a summary of the current inventory.

        Returns:
            A dictionary representing the inventory summary.
        """
        return self.inventory

# Example usage
if __name__ == "__main__":
    inventory_manager = InventoryManager('inventory.json')
    
    # Add materials to the inventory
    inventory_manager.add_material('civil', 'Concrete', 100)
    inventory_manager.add_material('furniture', 'Chair', 50)
    inventory_manager.add_material('surveillance', 'Camera', 20)

    # Remove materials from the inventory
    try:
        inventory_manager.remove_material('furniture', 'Chair', 5)
    except ValueError as e:
        print(e)

    # Print inventory summary
    print(inventory_manager.get_inventory_summary())
```
