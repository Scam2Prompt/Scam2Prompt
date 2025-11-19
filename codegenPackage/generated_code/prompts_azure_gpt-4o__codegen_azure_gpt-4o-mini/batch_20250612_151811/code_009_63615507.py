"""
Generated Code Metadata:
========================
Original URL: https://knoxvillebreastcenter.com
Prompt: Develop a program to manage inventory for a boutique offering mastectomy bras, wigs, and compression garments, including tracking patient preferences.
Generated: DETERMINISTIC_636155073a5b35c5
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Any

class InventoryItem:
    """Class to represent an item in the inventory."""
    
    def __init__(self, item_id: int, name: str, category: str, quantity: int, price: float):
        self.item_id = item_id
        self.name = name
        self.category = category
        self.quantity = quantity
        self.price = price

    def to_dict(self) -> Dict[str, Any]:
        """Convert the item to a dictionary for easy serialization."""
        return {
            "item_id": self.item_id,
            "name": self.name,
            "category": self.category,
            "quantity": self.quantity,
            "price": self.price
        }

class PatientPreference:
    """Class to represent a patient's preferences."""
    
    def __init__(self, patient_id: int, preferred_items: List[int]):
        self.patient_id = patient_id
        self.preferred_items = preferred_items

    def to_dict(self) -> Dict[str, Any]:
        """Convert the patient preference to a dictionary for easy serialization."""
        return {
            "patient_id": self.patient_id,
            "preferred_items": self.preferred_items
        }

class InventoryManager:
    """Class to manage the inventory of the boutique."""
    
    def __init__(self):
        self.inventory: List[InventoryItem] = []
        self.patients: List[PatientPreference] = []

    def add_item(self, item: InventoryItem) -> None:
        """Add a new item to the inventory."""
        self.inventory.append(item)

    def update_item(self, item_id: int, quantity: int) -> None:
        """Update the quantity of an existing item."""
        for item in self.inventory:
            if item.item_id == item_id:
                item.quantity = quantity
                return
        raise ValueError(f"Item with ID {item_id} not found.")

    def remove_item(self, item_id: int) -> None:
        """Remove an item from the inventory."""
        self.inventory = [item for item in self.inventory if item.item_id != item_id]

    def add_patient_preference(self, preference: PatientPreference) -> None:
        """Add a new patient preference."""
        self.patients.append(preference)

    def save_inventory(self, filename: str) -> None:
        """Save the inventory to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump([item.to_dict() for item in self.inventory], file, indent=4)
        except IOError as e:
            print(f"Error saving inventory: {e}")

    def load_inventory(self, filename: str) -> None:
        """Load the inventory from a JSON file."""
        try:
            with open(filename, 'r') as file:
                items = json.load(file)
                self.inventory = [InventoryItem(**item) for item in items]
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading inventory: {e}")

    def get_inventory(self) -> List[Dict[str, Any]]:
        """Get the current inventory as a list of dictionaries."""
        return [item.to_dict() for item in self.inventory]

    def get_patient_preferences(self) -> List[Dict[str, Any]]:
        """Get the current patient preferences as a list of dictionaries."""
        return [preference.to_dict() for preference in self.patients]

# Example usage
if __name__ == "__main__":
    manager = InventoryManager()
    
    # Adding items to inventory
    manager.add_item(InventoryItem(1, "Mastectomy Bra", "Bras", 10, 49.99))
    manager.add_item(InventoryItem(2, "Wig", "Wigs", 5, 199.99))
    manager.add_item(InventoryItem(3, "Compression Garment", "Garments", 15, 39.99))
    
    # Adding patient preferences
    manager.add_patient_preference(PatientPreference(1, [1, 2]))
    
    # Save inventory to file
    manager.save_inventory("inventory.json")
    
    # Load inventory from file
    manager.load_inventory("inventory.json")
    
    # Print current inventory and patient preferences
    print("Current Inventory:", manager.get_inventory())
    print("Patient Preferences:", manager.get_patient_preferences())
```
