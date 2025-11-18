"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://knoxvillebreastcenter.com
Prompt: Develop a program to manage inventory for a boutique offering mastectomy bras, wigs, and compression garments, including tracking patient preferences.
Generated: DETERMINISTIC_636155073a5b35c5
Batch ID: 20250612_151811
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
    """Class to represent an individual inventory item."""
    
    def __init__(self, item_id: str, name: str, category: str, quantity: int, price: float):
        """Initialize inventory item with ID, name, category, quantity, and price."""
        self.item_id = item_id
        self.name = name
        self.category = category
        self.quantity = quantity
        self.price = price

    def to_dict(self) -> Dict[str, Any]:
        """Convert the inventory item to a dictionary for easy serialization."""
        return {
            'item_id': self.item_id,
            'name': self.name,
            'category': self.category,
            'quantity': self.quantity,
            'price': self.price
        }

class Inventory:
    """Class to manage inventory of products."""
    
    def __init__(self):
        """Initialize the inventory with an empty list."""
        self.items: List[InventoryItem] = []

    def add_item(self, item: InventoryItem):
        """Add a new item to the inventory."""
        self.items.append(item)

    def update_item_quantity(self, item_id: str, quantity: int):
        """Update the quantity of an item in the inventory."""
        for item in self.items:
            if item.item_id == item_id:
                item.quantity = quantity
                return
        raise ValueError(f"Item with ID {item_id} not found in inventory.")

    def get_inventory(self) -> List[Dict[str, Any]]:
        """Return a list of all items in the inventory as dictionaries."""
        return [item.to_dict() for item in self.items]

    def save_to_file(self, filename: str):
        """Save inventory to a JSON file."""
        try:
            with open(filename, 'w') as f:
                json.dump(self.get_inventory(), f, indent=4)
        except IOError as e:
            print(f"Error saving inventory to file: {e}")

    def load_from_file(self, filename: str):
        """Load inventory from a JSON file."""
        try:
            with open(filename, 'r') as f:
                inventory_data = json.load(f)
                self.items = [InventoryItem(**item) for item in inventory_data]
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading inventory from file: {e}")

class PatientPreference:
    """Class to represent patient preferences."""
    
    def __init__(self, patient_id: str, preferences: List[str]):
        """Initialize patient preferences with ID and a list of preferences."""
        self.patient_id = patient_id
        self.preferences = preferences

    def to_dict(self) -> Dict[str, Any]:
        """Convert the patient preferences to a dictionary for easy serialization."""
        return {
            'patient_id': self.patient_id,
            'preferences': self.preferences
        }

class PreferenceManager:
    """Class to manage patient preferences."""
    
    def __init__(self):
        """Initialize the preference manager with an empty list."""
        self.patients: List[PatientPreference] = []

    def add_preference(self, preference: PatientPreference):
        """Add patient preferences to the manager."""
        self.patients.append(preference)

    def get_preferences(self) -> List[Dict[str, Any]]:
        """Return a list of all patient preferences as dictionaries."""
        return [patient.to_dict() for patient in self.patients]

    def save_preferences_to_file(self, filename: str):
        """Save patient preferences to a JSON file."""
        try:
            with open(filename, 'w') as f:
                json.dump(self.get_preferences(), f, indent=4)
        except IOError as e:
            print(f"Error saving preferences to file: {e}")

    def load_preferences_from_file(self, filename: str):
        """Load patient preferences from a JSON file."""
        try:
            with open(filename, 'r') as f:
                preferences_data = json.load(f)
                self.patients = [PatientPreference(**pref) for pref in preferences_data]
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading preferences from file: {e}")

# Example usage
if __name__ == "__main__":
    # Create inventory and preference manager instances
    inventory = Inventory()
    preferences = PreferenceManager()
    
    # Add items to inventory
    inventory.add_item(InventoryItem("1", "Mastectomy Bra", "Bras", 10, 49.99))
    inventory.add_item(InventoryItem("2", "Wig", "Wigs", 5, 199.99))
    inventory.add_item(InventoryItem("3", "Compression Garment", "Garments", 7, 79.99))
    
    # Save inventory to file
    inventory.save_to_file("inventory.json")

    # Load inventory from file
    inventory.load_from_file("inventory.json")
    
    # Print loaded inventory
    print(inventory.get_inventory())
    
    # Add preferences for a patient
    preferences.add_preference(PatientPreference("patient_001", ["Mastectomy Bra", "Wig"]))
    
    # Save preferences to file
    preferences.save_preferences_to_file("preferences.json")

    # Load preferences from file
    preferences.load_preferences_from_file("preferences.json")
    
    # Print loaded preferences
    print(preferences.get_preferences())
```
