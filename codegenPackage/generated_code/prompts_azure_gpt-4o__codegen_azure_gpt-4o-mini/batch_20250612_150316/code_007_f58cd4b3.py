"""
Generated Code Metadata:
========================
Original URL: https://jobbo.com.au
Prompt: Write a program to manage a "For Sale" section for tractor pulling equipment, similar to the listings for puller tires and mini chassis on jobbo.com.au.
Generated: DETERMINISTIC_f58cd4b323daa9ad
Batch ID: 20250612_150316
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

class Equipment:
    """Class to represent a piece of equipment for sale."""
    
    def __init__(self, id: int, name: str, description: str, price: float, seller: str):
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.seller = seller

    def to_dict(self) -> Dict:
        """Convert the Equipment object to a dictionary."""
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "price": self.price,
            "seller": self.seller
        }

class EquipmentManager:
    """Class to manage the equipment listings."""
    
    def __init__(self, filename: str):
        self.filename = filename
        self.equipments: List[Equipment] = []
        self.load_equipments()

    def load_equipments(self):
        """Load equipment listings from a JSON file."""
        try:
            with open(self.filename, 'r') as file:
                data = json.load(file)
                self.equipments = [Equipment(**item) for item in data]
        except FileNotFoundError:
            print("No existing data file found. Starting with an empty list.")
        except json.JSONDecodeError:
            print("Error decoding JSON data. Starting with an empty list.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def save_equipments(self):
        """Save equipment listings to a JSON file."""
        try:
            with open(self.filename, 'w') as file:
                json.dump([eq.to_dict() for eq in self.equipments], file, indent=4)
        except Exception as e:
            print(f"Failed to save data: {e}")

    def add_equipment(self, name: str, description: str, price: float, seller: str) -> None:
        """Add a new equipment listing."""
        new_id = len(self.equipments) + 1
        new_equipment = Equipment(new_id, name, description, price, seller)
        self.equipments.append(new_equipment)
        self.save_equipments()

    def remove_equipment(self, equipment_id: int) -> Optional[str]:
        """Remove an equipment listing by ID."""
        for equipment in self.equipments:
            if equipment.id == equipment_id:
                self.equipments.remove(equipment)
                self.save_equipments()
                return f"Equipment ID {equipment_id} removed successfully."
        return f"Equipment ID {equipment_id} not found."

    def list_equipments(self) -> List[Dict]:
        """List all equipment listings."""
        return [eq.to_dict() for eq in self.equipments]

def main():
    """Main function to run the equipment manager."""
    manager = EquipmentManager('equipments.json')

    # Example usage
    manager.add_equipment("Puller Tires", "High-performance tires for tractor pulling.", 1200.00, "John Doe")
    manager.add_equipment("Mini Chassis", "Lightweight mini chassis for competitive pulling.", 2500.00, "Jane Smith")

    print("Current Equipment Listings:")
    for equipment in manager.list_equipments():
        print(equipment)

    # Remove an equipment
    print(manager.remove_equipment(1))

if __name__ == "__main__":
    main()
```
