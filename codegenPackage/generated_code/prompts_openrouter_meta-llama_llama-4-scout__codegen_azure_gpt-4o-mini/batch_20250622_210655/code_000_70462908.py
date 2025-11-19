"""
Generated Code Metadata:
========================
Original URL: https://andiasfrozenyogurt.com
Prompt: Write a Python script to manage inventory for a frozen yogurt shop with multiple locations like Andias Frozen Yogurt, including their 100+ toppings and 14 unique flavors.
Generated: DETERMINISTIC_70462908aa494c4f
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
from typing import Dict, List, Optional

class InventoryItem:
    """Class to represent an inventory item (flavor or topping)."""
    
    def __init__(self, name: str, quantity: int):
        self.name = name
        self.quantity = quantity

    def __repr__(self):
        return f"{self.name}: {self.quantity}"

class Location:
    """Class to represent a frozen yogurt shop location."""
    
    def __init__(self, name: str):
        self.name = name
        self.inventory: Dict[str, InventoryItem] = {}

    def add_item(self, item_name: str, quantity: int):
        """Add or update an inventory item."""
        if item_name in self.inventory:
            self.inventory[item_name].quantity += quantity
        else:
            self.inventory[item_name] = InventoryItem(item_name, quantity)

    def remove_item(self, item_name: str, quantity: int):
        """Remove a specified quantity of an inventory item."""
        if item_name in self.inventory:
            if self.inventory[item_name].quantity >= quantity:
                self.inventory[item_name].quantity -= quantity
                if self.inventory[item_name].quantity == 0:
                    del self.inventory[item_name]
            else:
                raise ValueError(f"Not enough {item_name} in inventory to remove.")
        else:
            raise KeyError(f"{item_name} not found in inventory.")

    def get_inventory(self) -> List[InventoryItem]:
        """Return a list of all inventory items."""
        return list(self.inventory.values())

class InventoryManager:
    """Class to manage multiple locations of the frozen yogurt shop."""
    
    def __init__(self):
        self.locations: Dict[str, Location] = {}

    def add_location(self, location_name: str):
        """Add a new location to the inventory manager."""
        if location_name not in self.locations:
            self.locations[location_name] = Location(location_name)
        else:
            raise ValueError(f"Location {location_name} already exists.")

    def get_location(self, location_name: str) -> Optional[Location]:
        """Retrieve a location by name."""
        return self.locations.get(location_name)

    def save_inventory(self, filename: str):
        """Save the inventory data to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump({loc: loc_obj.get_inventory() for loc, loc_obj in self.locations.items()},
                          file, default=lambda x: x.__dict__, indent=4)
        except IOError as e:
            print(f"Error saving inventory: {e}")

    def load_inventory(self, filename: str):
        """Load inventory data from a JSON file."""
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                for loc_name, items in data.items():
                    self.add_location(loc_name)
                    for item in items:
                        self.locations[loc_name].add_item(item['name'], item['quantity'])
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading inventory: {e}")

# Example usage
if __name__ == "__main__":
    manager = InventoryManager()
    
    # Adding locations
    manager.add_location("Andias Frozen Yogurt - Downtown")
    manager.add_location("Andias Frozen Yogurt - Uptown")

    # Adding items to inventory
    downtown = manager.get_location("Andias Frozen Yogurt - Downtown")
    downtown.add_item("Vanilla", 50)
    downtown.add_item("Chocolate", 30)
    downtown.add_item("Sprinkles", 100)

    uptown = manager.get_location("Andias Frozen Yogurt - Uptown")
    uptown.add_item("Strawberry", 40)
    uptown.add_item("Oreo", 20)
    uptown.add_item("Chocolate Chips", 60)

    # Saving inventory to a file
    manager.save_inventory("inventory.json")

    # Loading inventory from a file
    new_manager = InventoryManager()
    new_manager.load_inventory("inventory.json")
```
