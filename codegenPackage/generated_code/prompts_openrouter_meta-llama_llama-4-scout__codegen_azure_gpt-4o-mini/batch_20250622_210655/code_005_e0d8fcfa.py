"""
Generated Code Metadata:
========================
Original URL: https://workshopgranada.com
Prompt: "Develop a system for tracking and managing inventory of fabrics, threads, and other sewing materials for a workshop, including features for supplier management and material requisition."
Generated: DETERMINISTIC_e0d8fcfad08e442f
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Optional

class Material:
    """Class representing a sewing material."""
    
    def __init__(self, name: str, quantity: int, unit: str):
        self.name = name
        self.quantity = quantity
        self.unit = unit

    def __repr__(self):
        return f"{self.name} ({self.quantity} {self.unit})"

class Supplier:
    """Class representing a supplier."""
    
    def __init__(self, name: str, contact_info: str):
        self.name = name
        self.contact_info = contact_info

    def __repr__(self):
        return f"{self.name} - {self.contact_info}"

class Inventory:
    """Class to manage inventory of sewing materials."""
    
    def __init__(self):
        self.materials: Dict[str, Material] = {}
        self.suppliers: Dict[str, Supplier] = {}

    def add_material(self, name: str, quantity: int, unit: str):
        """Add a new material to the inventory."""
        if name in self.materials:
            self.materials[name].quantity += quantity
        else:
            self.materials[name] = Material(name, quantity, unit)

    def remove_material(self, name: str, quantity: int):
        """Remove a specified quantity of material from the inventory."""
        if name in self.materials:
            if self.materials[name].quantity >= quantity:
                self.materials[name].quantity -= quantity
                if self.materials[name].quantity == 0:
                    del self.materials[name]
            else:
                raise ValueError("Not enough material in inventory.")
        else:
            raise KeyError("Material not found in inventory.")

    def add_supplier(self, name: str, contact_info: str):
        """Add a new supplier to the inventory."""
        self.suppliers[name] = Supplier(name, contact_info)

    def get_materials(self) -> List[Material]:
        """Return a list of all materials in the inventory."""
        return list(self.materials.values())

    def get_suppliers(self) -> List[Supplier]:
        """Return a list of all suppliers."""
        return list(self.suppliers.values())

    def requisition_material(self, name: str, quantity: int):
        """Requisition a specified quantity of material."""
        try:
            self.remove_material(name, quantity)
            print(f"Requisitioned {quantity} of {name}.")
        except (KeyError, ValueError) as e:
            print(f"Error during requisition: {e}")

    def save_inventory(self, filename: str):
        """Save the current inventory to a JSON file."""
        with open(filename, 'w') as f:
            json.dump({
                'materials': {name: vars(material) for name, material in self.materials.items()},
                'suppliers': {name: vars(supplier) for name, supplier in self.suppliers.items()}
            }, f, indent=4)

    def load_inventory(self, filename: str):
        """Load inventory from a JSON file."""
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                self.materials = {name: Material(**material) for name, material in data['materials'].items()}
                self.suppliers = {name: Supplier(**supplier) for name, supplier in data['suppliers'].items()}
        except FileNotFoundError:
            print("File not found. Starting with an empty inventory.")
        except json.JSONDecodeError:
            print("Error decoding JSON. Please check the file format.")

# Example usage
if __name__ == "__main__":
    inventory = Inventory()
    
    # Adding materials
    inventory.add_material("Cotton", 50, "meters")
    inventory.add_material("Polyester", 30, "meters")
    
    # Adding suppliers
    inventory.add_supplier("Fabric World", "contact@fabricworld.com")
    
    # Requisitioning materials
    inventory.requisition_material("Cotton", 10)
    
    # Saving inventory to a file
    inventory.save_inventory("inventory.json")
    
    # Loading inventory from a file
    inventory.load_inventory("inventory.json")
    
    # Displaying current inventory and suppliers
    print("Current Inventory:", inventory.get_materials())
    print("Current Suppliers:", inventory.get_suppliers())
```
