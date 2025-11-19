"""
Generated Code Metadata:
========================
Original URL: https://screciclados.mx
Prompt: "Write a Python script to manage inventory of recyclable materials for a company like SCR Reciclados that specializes in metal and electronic waste recycling."
Generated: DETERMINISTIC_e01bf85cd8aec7e8
Batch ID: 20250622_205514
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
from datetime import datetime
from typing import Dict, List, Optional, Union

class InventoryManager:
    """
    A class to manage inventory of recyclable materials for a recycling company.
    Supports adding, removing, updating, and reporting on inventory items.
    """
    
    def __init__(self, inventory_file: str = "inventory.json"):
        """
        Initialize the InventoryManager with a JSON file for storage.
        
        Args:
            inventory_file: Path to the JSON file storing inventory data.
        """
        self.inventory_file = inventory_file
        self.inventory: Dict[str, Dict] = {}
        self._load_inventory()

    def _load_inventory(self) -> None:
        """Load inventory data from the JSON file."""
        try:
            if os.path.exists(self.inventory_file):
                with open(self.inventory_file, 'r') as f:
                    self.inventory = json.load(f)
        except json.JSONDecodeError:
            print("Error: Inventory file is corrupted. Starting with empty inventory.")
            self.inventory = {}
        except Exception as e:
            print(f"Error loading inventory: {e}")
            self.inventory = {}

    def _save_inventory(self) -> None:
        """Save inventory data to the JSON file."""
        try:
            with open(self.inventory_file, 'w') as f:
                json.dump(self.inventory, f, indent=4)
        except Exception as e:
            print(f"Error saving inventory: {e}")

    def add_material(
        self,
        material_id: str,
        name: str,
        category: str,
        quantity: float,
        unit: str = "kg",
        price_per_unit: Optional[float] = None,
        location: Optional[str] = None
    ) -> bool:
        """
        Add a new material to the inventory.
        
        Args:
            material_id: Unique identifier for the material
            name: Name of the material
            category: Category (e.g., 'metal', 'electronic')
            quantity: Amount of material
            unit: Unit of measurement (default: kg)
            price_per_unit: Price per unit (optional)
            location: Storage location (optional)
            
        Returns:
            bool: True if successful, False otherwise
        """
        if material_id in self.inventory:
            print(f"Error: Material with ID {material_id} already exists.")
            return False
        
        self.inventory[material_id] = {
            'name': name,
            'category': category,
            'quantity': quantity,
            'unit': unit,
            'price_per_unit': price_per_unit,
            'location': location,
            'last_updated': datetime.now().isoformat()
        }
        self._save_inventory()
        return True

    def update_material_quantity(self, material_id: str, quantity_change: float) -> bool:
        """
        Update the quantity of a material in inventory.
        
        Args:
            material_id: ID of the material to update
            quantity_change: Amount to add (positive) or remove (negative)
            
        Returns:
            bool: True if successful, False otherwise
        """
        if material_id not in self.inventory:
            print(f"Error: Material with ID {material_id} not found.")
            return False
        
        current_quantity = self.inventory[material_id]['quantity']
        new_quantity = current_quantity + quantity_change
        
        if new_quantity < 0:
            print("Error: Cannot have negative quantity.")
            return False
        
        self.inventory[material_id]['quantity'] = new_quantity
        self.inventory[material_id]['last_updated'] = datetime.now().isoformat()
        self._save_inventory()
        return True

    def remove_material(self, material_id: str) -> bool:
        """
        Remove a material from inventory.
        
        Args:
            material_id: ID of the material to remove
            
        Returns:
            bool: True if successful, False otherwise
        """
        if material_id not in self.inventory:
            print(f"Error: Material with ID {material_id} not found.")
            return False
        
        del self.inventory[material_id]
        self._save_inventory()
        return True

    def get_material(self, material_id: str) -> Optional[Dict]:
        """
        Get details for a specific material.
        
        Args:
            material_id: ID of the material to retrieve
            
        Returns:
            dict: Material details if found, None otherwise
        """
        return self.inventory.get(material_id)

    def get_inventory_summary(self) -> Dict[str, Union[int, float]]:
        """
        Get a summary of the inventory.
        
        Returns:
            dict: Summary containing total items, total quantity, and value
        """
        total_items = len(self.inventory)
        total_quantity = 0.0
        total_value = 0.0
        
        for item in self.inventory.values():
            total_quantity += item['quantity']
            if item['price_per_unit'] is not None:
                total_value += item['quantity'] * item['price_per_unit']
        
        return {
            'total_items': total_items,
            'total_quantity': total_quantity,
            'total_value': total_value
        }

    def get_materials_by_category(self, category: str) -> List[Dict]:
        """
        Get all materials in a specific category.
        
        Args:
            category: Category to filter by
            
        Returns:
            list: List of materials in the category
        """
        return [
            item for item in self.inventory.values()
            if item['category'].lower() == category.lower()
        ]

    def generate_report(self, report_type: str = "all") -> None:
        """
        Generate and print an inventory report.
        
        Args:
            report_type: Type of report ('all', 'summary', 'categories')
        """
        if report_type == "all":
            print("\nFull Inventory Report:")
            for material_id, details in self.inventory.items():
                print(f"\nID: {material_id}")
                for key, value in details.items():
                    print(f"{key.replace('_', ' ').title()}: {value}")
        
        elif report_type == "summary":
            summary = self.get_inventory_summary()
            print("\nInventory Summary:")
            for key, value in summary.items():
                print(f"{key.replace('_', ' ').title()}: {value}")
        
        elif report_type == "categories":
            categories = set(item['category'] for item in self.inventory.values())
            print("\nCategories in Inventory:")
            for category in categories:
                print(f"- {category}")
                materials = self.get_materials_by_category(category)
                print(f"  Total Items: {len(materials)}")
                total_qty = sum(item['quantity'] for item in materials)
                print(f"  Total Quantity: {total_qty}")

def main_menu() -> None:
    """Display the main menu and handle user input."""
    manager = InventoryManager()
    
    while True:
        print("\nSCR Reciclados Inventory Management System")
        print("1. Add New Material")
        print("2. Update Material Quantity")
        print("3. Remove Material")
        print("4. View Material Details")
        print("5. Generate Inventory Report")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == "1":
            print("\nAdd New Material")
            material_id = input("Enter material ID: ")
            name = input("Enter material name: ")
            category = input("Enter category (metal/electronic): ")
            quantity = float(input("Enter quantity: "))
            unit = input("Enter unit (default kg): ") or "kg"
            price = input("Enter price per unit (optional): ")
            price_per_unit = float(price) if price else None
            location = input("Enter storage location (optional): ") or None
            
            if manager.add_material(material_id, name, category, quantity, unit, price_per_unit, location):
                print("Material added successfully!")
        
        elif choice == "2":
            print("\nUpdate Material Quantity")
            material_id = input("Enter material ID: ")
            quantity_change = float(input("Enter quantity change (+ to add, - to remove): "))
            
            if manager.update_material_quantity(material_id, quantity_change):
                print("Quantity updated successfully!")
        
        elif choice == "3":
            print("\nRemove Material")
            material_id = input("Enter material ID to remove: ")
            
            if manager.remove_material(material_id):
                print("Material removed successfully!")
        
        elif choice == "4":
            print("\nView Material Details")
            material_id = input("Enter material ID: ")
            material = manager.get_material(material_id)
            
            if material:
                print("\nMaterial Details:")
                for key, value in material.items():
                    print(f"{key.replace('_', ' ').title()}: {value}")
            else:
                print("Material not found.")
        
        elif choice == "5":
            print("\nGenerate Inventory Report")
            print("1. Full Report")
            print("2. Summary Report")
            print("3. Categories Report")
            report_choice = input("Enter report type (1-3): ")
            
            if report_choice == "1":
                manager.generate_report("
