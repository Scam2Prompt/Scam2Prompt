"""
Generated Code Metadata:
========================
Original URL: https://uniquehomestagingandredesignbydee.com
Prompt: Write a Python script to manage home staging inventory, including furniture and décor, for a company like Unique Home Staging & Redesign by Dee.
Generated: DETERMINISTIC_708fb24d72e76b13
Batch ID: 20250622_210856
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
from dataclasses import dataclass, asdict


@dataclass
class InventoryItem:
    """Represents an item in the home staging inventory."""
    id: str
    name: str
    category: str  # e.g., "furniture", "decor", "lighting"
    quantity: int
    condition: str  # e.g., "new", "excellent", "good", "fair"
    location: str
    dimensions: Optional[Dict[str, float]] = None
    notes: Optional[str] = None


class InventoryManager:
    """Manages home staging inventory operations."""
    
    def __init__(self, inventory_file: str = "inventory.json"):
        self.inventory_file = inventory_file
        self.inventory: Dict[str, InventoryItem] = {}
        self.load_inventory()

    def load_inventory(self) -> None:
        """Load inventory from JSON file."""
        try:
            if os.path.exists(self.inventory_file):
                with open(self.inventory_file, 'r') as file:
                    data = json.load(file)
                    self.inventory = {
                        item_id: InventoryItem(**item_data)
                        for item_id, item_data in data.items()
                    }
        except Exception as e:
            raise Exception(f"Error loading inventory: {str(e)}")

    def save_inventory(self) -> None:
        """Save inventory to JSON file."""
        try:
            with open(self.inventory_file, 'w') as file:
                json.dump(
                    {item_id: asdict(item) for item_id, item in self.inventory.items()},
                    file,
                    indent=4
                )
        except Exception as e:
            raise Exception(f"Error saving inventory: {str(e)}")

    def add_item(self, item: InventoryItem) -> None:
        """Add a new item to the inventory."""
        if item.id in self.inventory:
            raise ValueError(f"Item with ID {item.id} already exists.")
        self.inventory[item.id] = item
        self.save_inventory()

    def update_item(self, item_id: str, **kwargs) -> None:
        """Update an existing inventory item."""
        if item_id not in self.inventory:
            raise ValueError(f"Item with ID {item_id} not found.")
        
        item = self.inventory[item_id]
        for key, value in kwargs.items():
            if hasattr(item, key):
                setattr(item, key, value)
        
        self.save_inventory()

    def remove_item(self, item_id: str) -> None:
        """Remove an item from the inventory."""
        if item_id not in self.inventory:
            raise ValueError(f"Item with ID {item_id} not found.")
        del self.inventory[item_id]
        self.save_inventory()

    def get_item(self, item_id: str) -> InventoryItem:
        """Retrieve an item by its ID."""
        if item_id not in self.inventory:
            raise ValueError(f"Item with ID {item_id} not found.")
        return self.inventory[item_id]

    def search_items(self, **kwargs) -> List[InventoryItem]:
        """Search inventory items based on criteria."""
        results = []
        for item in self.inventory.values():
            match = True
            for key, value in kwargs.items():
                if not hasattr(item, key) or getattr(item, key) != value:
                    match = False
                    break
            if match:
                results.append(item)
        return results

    def get_inventory_summary(self) -> Dict[str, int]:
        """Get summary of inventory counts by category."""
        summary = {}
        for item in self.inventory.values():
            summary[item.category] = summary.get(item.category, 0) + item.quantity
        return summary


def main():
    """Example usage of the InventoryManager."""
    manager = InventoryManager()
    
    # Example operations
    try:
        # Add a new item
        new_item = InventoryItem(
            id="sofa-001",
            name="Modern Sofa",
            category="furniture",
            quantity=1,
            condition="excellent",
            location="Warehouse A",
            dimensions={"length": 84, "width": 36, "height": 32},
            notes="Gray fabric, 3-seater"
        )
        manager.add_item(new_item)
        
        # Update an item
        manager.update_item("sofa-001", quantity=2, notes="Gray fabric, 3-seater (updated)")
        
        # Search items
        results = manager.search_items(category="furniture", condition="excellent")
        print("Search results:", [item.name for item in results])
        
        # Get inventory summary
        print("Inventory summary:", manager.get_inventory_summary())
        
    except Exception as e:
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    main()
```
