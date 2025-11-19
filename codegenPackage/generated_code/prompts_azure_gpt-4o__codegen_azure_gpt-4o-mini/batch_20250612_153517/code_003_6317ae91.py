"""
Generated Code Metadata:
========================
Original URL: https://fabricarecosmeticos.ind.br
Prompt: Create a script to automate the process of managing raw material inventory for high-performance cosmetic production, based on Fabricare Cosméticos' emphasis on advanced technology and rich active ingredients.
Generated: DETERMINISTIC_6317ae913246c583
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import os
from typing import List, Dict

class RawMaterial:
    """Class to represent a raw material in the inventory."""
    
    def __init__(self, name: str, quantity: int, unit: str):
        self.name = name
        self.quantity = quantity
        self.unit = unit

    def __repr__(self):
        return f"{self.name}: {self.quantity} {self.unit}"

class InventoryManager:
    """Class to manage the raw material inventory."""
    
    def __init__(self, inventory_file: str):
        self.inventory_file = inventory_file
        self.inventory: List[RawMaterial] = []
        self.load_inventory()

    def load_inventory(self):
        """Load inventory from a JSON file."""
        if os.path.exists(self.inventory_file):
            with open(self.inventory_file, 'r') as file:
                data = json.load(file)
                self.inventory = [RawMaterial(**item) for item in data]
        else:
            print("Inventory file not found. Starting with an empty inventory.")

    def save_inventory(self):
        """Save the current inventory to a JSON file."""
        with open(self.inventory_file, 'w') as file:
            json.dump([item.__dict__ for item in self.inventory], file, indent=4)

    def add_material(self, name: str, quantity: int, unit: str):
        """Add a new raw material to the inventory."""
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self.inventory.append(RawMaterial(name, quantity, unit))
        self.save_inventory()

    def update_material(self, name: str, quantity: int):
        """Update the quantity of an existing raw material."""
        for material in self.inventory:
            if material.name == name:
                if quantity < 0:
                    raise ValueError("Quantity cannot be negative.")
                material.quantity = quantity
                self.save_inventory()
                return
        raise ValueError(f"Material '{name}' not found in inventory.")

    def remove_material(self, name: str):
        """Remove a raw material from the inventory."""
        self.inventory = [material for material in self.inventory if material.name != name]
        self.save_inventory()

    def list_inventory(self) -> List[Dict[str, str]]:
        """List all raw materials in the inventory."""
        return [material.__dict__ for material in self.inventory]

def main():
    """Main function to run the inventory manager."""
    inventory_file = 'inventory.json'
    manager = InventoryManager(inventory_file)

    # Example usage
    try:
        manager.add_material("Hyaluronic Acid", 100, "grams")
        manager.add_material("Vitamin C", 50, "grams")
        manager.update_material("Hyaluronic Acid", 120)
        manager.remove_material("Vitamin C")
        
        # Print current inventory
        print("Current Inventory:")
        for item in manager.list_inventory():
            print(item)
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
