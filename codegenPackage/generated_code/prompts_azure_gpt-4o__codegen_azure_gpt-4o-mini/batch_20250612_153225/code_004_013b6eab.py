"""
Generated Code Metadata:
========================
Original URL: https://theprintnan.app
Prompt: Develop a program to manage inventory for sheet materials like acrylic, composite, and foam board, ensuring compatibility with the fabrication services offered on ThePrintNan.
Generated: DETERMINISTIC_013b6eabb6139e63
Batch ID: 20250612_153225
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
    """Class to represent an inventory item for sheet materials."""
    
    def __init__(self, material_type: str, quantity: int, price_per_unit: float):
        self.material_type = material_type
        self.quantity = quantity
        self.price_per_unit = price_per_unit

    def to_dict(self) -> Dict[str, Any]:
        """Convert the inventory item to a dictionary."""
        return {
            "material_type": self.material_type,
            "quantity": self.quantity,
            "price_per_unit": self.price_per_unit
        }

class InventoryManager:
    """Class to manage the inventory of sheet materials."""
    
    def __init__(self):
        self.inventory: List[InventoryItem] = []

    def add_item(self, item: InventoryItem) -> None:
        """Add a new item to the inventory."""
        self.inventory.append(item)

    def remove_item(self, material_type: str) -> bool:
        """Remove an item from the inventory by material type."""
        for item in self.inventory:
            if item.material_type == material_type:
                self.inventory.remove(item)
                return True
        return False

    def update_item(self, material_type: str, quantity: int, price_per_unit: float) -> bool:
        """Update the quantity and price of an existing inventory item."""
        for item in self.inventory:
            if item.material_type == material_type:
                item.quantity = quantity
                item.price_per_unit = price_per_unit
                return True
        return False

    def get_inventory(self) -> List[Dict[str, Any]]:
        """Get the current inventory as a list of dictionaries."""
        return [item.to_dict() for item in self.inventory]

    def save_inventory(self, filename: str) -> None:
        """Save the inventory to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump(self.get_inventory(), file, indent=4)
        except IOError as e:
            print(f"Error saving inventory to {filename}: {e}")

    def load_inventory(self, filename: str) -> None:
        """Load inventory from a JSON file."""
        try:
            with open(filename, 'r') as file:
                items = json.load(file)
                self.inventory = [InventoryItem(**item) for item in items]
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading inventory from {filename}: {e}")

def main():
    """Main function to demonstrate inventory management."""
    manager = InventoryManager()

    # Load existing inventory from file
    manager.load_inventory('inventory.json')

    # Add new items to the inventory
    manager.add_item(InventoryItem("Acrylic", 50, 10.0))
    manager.add_item(InventoryItem("Composite", 30, 15.0))
    manager.add_item(InventoryItem("Foam Board", 20, 5.0))

    # Update an existing item
    manager.update_item("Acrylic", 40, 12.0)

    # Remove an item
    manager.remove_item("Foam Board")

    # Print current inventory
    print("Current Inventory:")
    for item in manager.get_inventory():
        print(item)

    # Save the updated inventory to file
    manager.save_inventory('inventory.json')

if __name__ == "__main__":
    main()
```
