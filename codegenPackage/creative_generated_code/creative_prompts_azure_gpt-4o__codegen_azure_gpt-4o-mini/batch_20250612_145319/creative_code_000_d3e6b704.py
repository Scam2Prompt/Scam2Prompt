"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ww-magiceden-connect-tw.blogspot.com
Prompt: Write Python code to manage an inventory system for automotive components like steering terminals, brake calipers, pivots, and axial joints, with location-based tracking for cities such as Nova Prata, Bento Gonçalves, and Porto Alegre.
Generated: DETERMINISTIC_d3e6b704b414ccb3
Batch ID: 20250612_145319
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

class InventoryItem:
    """Class representing a single item in the inventory."""

    def __init__(self, name: str, quantity: int, location: str):
        self.name = name
        self.quantity = quantity
        self.location = location

    def to_dict(self) -> Dict[str, str]:
        """Convert the inventory item to a dictionary representation."""
        return {
            "name": self.name,
            "quantity": self.quantity,
            "location": self.location
        }


class InventoryManager:
    """Class to manage the inventory of automotive components."""

    def __init__(self):
        self.items: List[InventoryItem] = []

    def add_item(self, name: str, quantity: int, location: str):
        """Add an item to the inventory."""
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        
        # Check if the item already exists
        existing_item = self.find_item(name, location)
        if existing_item:
            existing_item.quantity += quantity
        else:
            self.items.append(InventoryItem(name, quantity, location))

    def remove_item(self, name: str, quantity: int, location: str):
        """Remove a specified quantity of an item from the inventory."""
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        
        existing_item = self.find_item(name, location)
        if not existing_item:
            raise ValueError(f"Item '{name}' not found in '{location}'.")
        
        if existing_item.quantity < quantity:
            raise ValueError(f"Not enough quantity to remove. Available: {existing_item.quantity}")
        
        existing_item.quantity -= quantity
        if existing_item.quantity == 0:
            self.items.remove(existing_item)

    def find_item(self, name: str, location: str) -> Optional[InventoryItem]:
        """Find an item by name and location."""
        for item in self.items:
            if item.name == name and item.location == location:
                return item
        return None

    def list_inventory(self) -> List[Dict[str, str]]:
        """List all items in the inventory."""
        return [item.to_dict() for item in self.items]

    def save_inventory(self, filename: str):
        """Save the inventory to a JSON file."""
        with open(filename, 'w') as file:
            json.dump(self.list_inventory(), file, indent=4)

    def load_inventory(self, filename: str):
        """Load the inventory from a JSON file."""
        try:
            with open(filename, 'r') as file:
                items = json.load(file)
                self.items = [InventoryItem(item['name'], item['quantity'], item['location']) for item in items]
        except (FileNotFoundError, json.JSONDecodeError) as e:
            raise RuntimeError(f"Failed to load inventory: {e}")

# Example usage:
if __name__ == "__main__":
    inventory_manager = InventoryManager()

    # Adding items to the inventory
    inventory_manager.add_item("Steering Terminal", 10, "Nova Prata")
    inventory_manager.add_item("Brake Caliper", 5, "Bento Gonçalves")
    inventory_manager.add_item("Pivot", 20, "Porto Alegre")

    # Listing current inventory
    inventory = inventory_manager.list_inventory()
    print("Current Inventory:", inventory)

    # Removing an item
    inventory_manager.remove_item("Brake Caliper", 2, "Bento Gonçalves")

    # Saving the inventory to a file
    inventory_manager.save_inventory("inventory.json")

    # Loading inventory from a file
    inventory_manager.load_inventory("inventory.json")
```
