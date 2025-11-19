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
import os
from typing import Dict, List, Optional, Union

class InventoryItem:
    """Represents an inventory item (flavor or topping)."""
    def __init__(self, name: str, quantity: float, unit: str, cost_per_unit: float, location: str):
        self.name = name
        self.quantity = quantity
        self.unit = unit
        self.cost_per_unit = cost_per_unit
        self.location = location

    def to_dict(self) -> Dict:
        """Convert the item to a dictionary for serialization."""
        return {
            'name': self.name,
            'quantity': self.quantity,
            'unit': self.unit,
            'cost_per_unit': self.cost_per_unit,
            'location': self.location
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'InventoryItem':
        """Create an InventoryItem from a dictionary."""
        return cls(
            name=data['name'],
            quantity=data['quantity'],
            unit=data['unit'],
            cost_per_unit=data['cost_per_unit'],
            location=data['location']
        )

class FrozenYogurtInventory:
    """Manages inventory for a frozen yogurt shop with multiple locations."""
    def __init__(self, data_file: str = 'inventory.json'):
        self.data_file = data_file
        self.inventory: Dict[str, List[InventoryItem]] = {}
        self.locations: List[str] = []
        self.load_inventory()

    def load_inventory(self) -> None:
        """Load inventory data from the JSON file."""
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r') as f:
                    data = json.load(f)
                    self.inventory = {
                        loc: [InventoryItem.from_dict(item) for item in items]
                        for loc, items in data.items()
                    }
                    self.locations = list(data.keys())
            else:
                self.inventory = {}
                self.locations = []
        except Exception as e:
            raise Exception(f"Error loading inventory: {str(e)}")

    def save_inventory(self) -> None:
        """Save inventory data to the JSON file."""
        try:
            data = {
                loc: [item.to_dict() for item in items]
                for loc, items in self.inventory.items()
            }
            with open(self.data_file, 'w') as f:
                json.dump(data, f, indent=2)
        except Exception as e:
            raise Exception(f"Error saving inventory: {str(e)}")

    def add_location(self, location: str) -> None:
        """Add a new location to the inventory system."""
        if location in self.locations:
            raise ValueError(f"Location '{location}' already exists")
        self.inventory[location] = []
        self.locations.append(location)
        self.save_inventory()

    def add_item(self, location: str, item: InventoryItem) -> None:
        """Add an item to a specific location's inventory."""
        if location not in self.locations:
            raise ValueError(f"Location '{location}' does not exist")
        
        existing_item = next((i for i in self.inventory[location] if i.name == item.name), None)
        if existing_item:
            existing_item.quantity += item.quantity
        else:
            self.inventory[location].append(item)
        self.save_inventory()

    def remove_item(self, location: str, item_name: str, quantity: float) -> None:
        """Remove a quantity of an item from a location's inventory."""
        if location not in self.locations:
            raise ValueError(f"Location '{location}' does not exist")
        
        item = next((i for i in self.inventory[location] if i.name == item_name), None)
        if not item:
            raise ValueError(f"Item '{item_name}' not found in location '{location}'")
        
        if item.quantity < quantity:
            raise ValueError(f"Not enough quantity available (available: {item.quantity}, requested: {quantity})")
        
        item.quantity -= quantity
        if item.quantity <= 0:
            self.inventory[location].remove(item)
        self.save_inventory()

    def transfer_item(self, from_location: str, to_location: str, item_name: str, quantity: float) -> None:
        """Transfer an item between locations."""
        if from_location not in self.locations:
            raise ValueError(f"Source location '{from_location}' does not exist")
        if to_location not in self.locations:
            raise ValueError(f"Destination location '{to_location}' does not exist")
        
        from_item = next((i for i in self.inventory[from_location] if i.name == item_name), None)
        if not from_item:
            raise ValueError(f"Item '{item_name}' not found in source location '{from_location}'")
        
        if from_item.quantity < quantity:
            raise ValueError(f"Not enough quantity available (available: {from_item.quantity}, requested: {quantity})")
        
        to_item = next((i for i in self.inventory[to_location] if i.name == item_name), None)
        
        from_item.quantity -= quantity
        if to_item:
            to_item.quantity += quantity
        else:
            self.inventory[to_location].append(
                InventoryItem(
                    name=item_name,
                    quantity=quantity,
                    unit=from_item.unit,
                    cost_per_unit=from_item.cost_per_unit,
                    location=to_location
                )
            )
        
        if from_item.quantity <= 0:
            self.inventory[from_location].remove(from_item)
        
        self.save_inventory()

    def get_inventory(self, location: str = None) -> Dict[str, List[InventoryItem]]:
        """Get inventory for a specific location or all locations."""
        if location:
            if location not in self.locations:
                raise ValueError(f"Location '{location}' does not exist")
            return {location: self.inventory[location]}
        return self.inventory

    def get_item(self, location: str, item_name: str) -> Optional[InventoryItem]:
        """Get a specific item from a location's inventory."""
        if location not in self.locations:
            raise ValueError(f"Location '{location}' does not exist")
        return next((i for i in self.inventory[location] if i.name == item_name), None)

    def generate_report(self) -> str:
        """Generate a formatted inventory report."""
        report = []
        for location, items in self.inventory.items():
            report.append(f"Location: {location}")
            report.append("-" * 40)
            for item in items:
                report.append(f"{item.name}: {item.quantity} {item.unit} (Cost: ${item.cost_per_unit:.2f} per {item.unit})")
            report.append("\n")
        return "\n".join(report)

# Example usage
if __name__ == "__main__":
    inventory = FrozenYogurtInventory()
    
    # Add locations
    inventory.add_location("Downtown")
    inventory.add_location("Uptown")
    
    # Add items
    inventory.add_item("Downtown", InventoryItem("Vanilla", 10.0, "gallons", 5.99, "Downtown"))
    inventory.add_item("Downtown", InventoryItem("Chocolate", 8.0, "gallons", 6.99, "Downtown"))
    inventory.add_item("Downtown", InventoryItem("Sprinkles", 5.0, "pounds", 2.99, "Downtown"))
    
    inventory.add_item("Uptown", InventoryItem("Strawberry", 7.0, "gallons", 5.99, "Uptown"))
    inventory.add_item("Uptown", InventoryItem("Gummy Bears", 3.0, "pounds", 3.99, "Uptown"))
    
    # Transfer items
    inventory.transfer_item("Downtown", "Uptown", "Sprinkles", 2.0)
    
    # Remove items
    inventory.remove_item("Downtown", "Chocolate", 1.0)
    
    # Generate report
    print(inventory.generate_report())
```
