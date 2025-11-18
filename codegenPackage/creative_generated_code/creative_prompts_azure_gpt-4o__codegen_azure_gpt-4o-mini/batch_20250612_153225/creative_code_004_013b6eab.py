"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://theprintnan.app
Prompt: Develop a program to manage inventory for sheet materials like acrylic, composite, and foam board, ensuring compatibility with the fabrication services offered on ThePrintNan.
Generated: DETERMINISTIC_013b6eabb6139e63
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict, Optional

class InventoryManager:
    """
    A class to manage inventory for sheet materials like acrylic, composite, and foam board.
    """
    
    def __init__(self, inventory_file: str):
        """
        Initializes the InventoryManager with the provided inventory file.
        
        Args:
            inventory_file (str): Path to the JSON file that stores inventory data.
        """
        self.inventory_file = inventory_file
        self.inventory = self.load_inventory()

    def load_inventory(self) -> Dict[str, Dict[str, int]]:
        """
        Loads the inventory from a JSON file.

        Returns:
            Dict[str, Dict[str, int]]: A dictionary containing inventory data.
        """
        try:
            with open(self.inventory_file, 'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error loading inventory: {e}")
            return {}

    def save_inventory(self) -> None:
        """
        Saves the current inventory to the JSON file.
        """
        try:
            with open(self.inventory_file, 'w') as file:
                json.dump(self.inventory, file, indent=4)
        except IOError as e:
            print(f"Error saving inventory: {e}")

    def add_material(self, material_type: str, quantity: int) -> None:
        """
        Adds a specified quantity of a material type to the inventory.
        
        Args:
            material_type (str): The type of material to add (e.g., acrylic, composite).
            quantity (int): The quantity of material to add.

        Raises:
            ValueError: If quantity is not a positive integer.
        """
        if quantity <= 0:
            raise ValueError("Quantity must be a positive integer.")

        if material_type not in self.inventory:
            self.inventory[material_type] = {'quantity': 0}
        
        self.inventory[material_type]['quantity'] += quantity
        self.save_inventory()

    def remove_material(self, material_type: str, quantity: int) -> None:
        """
        Removes a specified quantity of a material type from the inventory.
        
        Args:
            material_type (str): The type of material to remove.
            quantity (int): The quantity of material to remove.

        Raises:
            ValueError: If quantity is not a positive integer or exceeds available inventory.
        """
        if quantity <= 0:
            raise ValueError("Quantity must be a positive integer.")
        
        if material_type not in self.inventory or self.inventory[material_type]['quantity'] < quantity:
            raise ValueError("Insufficient quantity in inventory.")
        
        self.inventory[material_type]['quantity'] -= quantity
        self.save_inventory()

    def check_inventory(self, material_type: str) -> Optional[int]:
        """
        Checks the inventory for a specified material type.
        
        Args:
            material_type (str): The type of material to check.

        Returns:
            Optional[int]: The available quantity of the material, or None if it doesn't exist.
        """
        return self.inventory.get(material_type, {}).get('quantity', None)

    def get_all_materials(self) -> Dict[str, int]:
        """
        Returns all materials and their quantities in the inventory.
        
        Returns:
            Dict[str, int]: A dictionary with material types as keys and available quantities as values.
        """
        return {material: data['quantity'] for material, data in self.inventory.items()}

# Example usage
if __name__ == "__main__":
    inventory_manager = InventoryManager("inventory.json")

    # Adding materials
    try:
        inventory_manager.add_material("acrylic", 50)
        inventory_manager.add_material("composite", 30)
    except ValueError as e:
        print(f"Error: {e}")

    # Checking inventory
    print("Current Inventory:", inventory_manager.get_all_materials())

    # Removing materials
    try:
        inventory_manager.remove_material("acrylic", 20)
    except ValueError as e:
        print(f"Error: {e}")

    # Checking inventory after removal
    print("Updated Inventory:", inventory_manager.get_all_materials())
```
