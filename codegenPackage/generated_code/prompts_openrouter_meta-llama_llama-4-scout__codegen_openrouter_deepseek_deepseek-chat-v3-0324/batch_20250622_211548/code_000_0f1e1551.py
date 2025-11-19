"""
Generated Code Metadata:
========================
Original URL: https://centralseedandchem.co.nz
Prompt: Write a Python script to manage inventory for a seed and chemical supply company in Otago and Southland.
Generated: DETERMINISTIC_0f1e1551e816b494
Batch ID: 20250622_211548
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
import csv
from datetime import datetime


@dataclass
class InventoryItem:
    """Class representing an inventory item."""
    id: str
    name: str
    category: str  # e.g., 'seed', 'chemical', 'fertilizer'
    quantity: int
    unit: str  # e.g., 'kg', 'L', 'packet'
    price_per_unit: float
    supplier: str
    region: str  # 'Otago' or 'Southland'
    last_updated: str

    def to_dict(self) -> Dict:
        """Convert the item to a dictionary."""
        return asdict(self)


class InventoryManager:
    """Class to manage inventory operations."""

    def __init__(self, data_file: str = 'inventory.json'):
        """
        Initialize the inventory manager.
        
        Args:
            data_file: Path to the JSON file storing inventory data.
        """
        self.data_file = data_file
        self.inventory: Dict[str, InventoryItem] = {}
        self._load_inventory()

    def _load_inventory(self) -> None:
        """Load inventory data from the JSON file."""
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r') as file:
                    data = json.load(file)
                    self.inventory = {
                        item_id: InventoryItem(**item_data)
                        for item_id, item_data in data.items()
                    }
        except (json.JSONDecodeError, IOError) as e:
            raise RuntimeError(f"Error loading inventory data: {e}")

    def _save_inventory(self) -> None:
        """Save inventory data to the JSON file."""
        try:
            with open(self.data_file, 'w') as file:
                json.dump(
                    {item_id: item.to_dict() for item_id, item in self.inventory.items()},
                    file,
                    indent=4
                )
        except IOError as e:
            raise RuntimeError(f"Error saving inventory data: {e}")

    def add_item(self, item: InventoryItem) -> None:
        """
        Add a new item to the inventory.
        
        Args:
            item: InventoryItem to add.
        """
        if item.id in self.inventory:
            raise ValueError(f"Item with ID {item.id} already exists.")
        self.inventory[item.id] = item
        self._save_inventory()

    def update_item(self, item_id: str, **kwargs) -> None:
        """
        Update an existing inventory item.
        
        Args:
            item_id: ID of the item to update.
            **kwargs: Fields to update with their new values.
        """
        if item_id not in self.inventory:
            raise ValueError(f"Item with ID {item_id} not found.")
        
        item = self.inventory[item_id]
        for field, value in kwargs.items():
            if hasattr(item, field):
                setattr(item, field, value)
            else:
                raise ValueError(f"Invalid field: {field}")
        
        item.last_updated = datetime.now().isoformat()
        self._save_inventory()

    def remove_item(self, item_id: str) -> None:
        """
        Remove an item from the inventory.
        
        Args:
            item_id: ID of the item to remove.
        """
        if item_id not in self.inventory:
            raise ValueError(f"Item with ID {item_id} not found.")
        del self.inventory[item_id]
        self._save_inventory()

    def get_item(self, item_id: str) -> Optional[InventoryItem]:
        """
        Get an item by ID.
        
        Args:
            item_id: ID of the item to retrieve.
            
        Returns:
            The InventoryItem if found, None otherwise.
        """
        return self.inventory.get(item_id)

    def list_items(self, region: Optional[str] = None) -> List[InventoryItem]:
        """
        List all items, optionally filtered by region.
        
        Args:
            region: 'Otago' or 'Southland' to filter by region.
            
        Returns:
            List of InventoryItems matching the filter.
        """
        if region:
            return [item for item in self.inventory.values() if item.region == region]
        return list(self.inventory.values())

    def export_to_csv(self, filename: str, region: Optional[str] = None) -> None:
        """
        Export inventory data to a CSV file.
        
        Args:
            filename: Path to the CSV file.
            region: 'Otago' or 'Southland' to filter by region.
        """
        items = self.list_items(region)
        if not items:
            raise ValueError("No items to export.")
        
        fieldnames = list(InventoryItem.__annotations__.keys())
        try:
            with open(filename, 'w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                for item in items:
                    writer.writerow(item.to_dict())
        except IOError as e:
            raise RuntimeError(f"Error exporting to CSV: {e}")


def main():
    """Example usage of the InventoryManager."""
    manager = InventoryManager()
    
    # Example: Add a new item
    try:
        new_item = InventoryItem(
            id="seed-001",
            name="Ryegrass Seed",
            category="seed",
            quantity=100,
            unit="kg",
            price_per_unit=5.99,
            supplier="AgriSupplies",
            region="Otago",
            last_updated=datetime.now().isoformat()
        )
        manager.add_item(new_item)
        print("Item added successfully.")
    except Exception as e:
        print(f"Error adding item: {e}")

    # Example: List items in Otago
    try:
        otago_items = manager.list_items(region="Otago")
        print("\nItems in Otago:")
        for item in otago_items:
            print(f"{item.name} ({item.quantity} {item.unit})")
    except Exception as e:
        print(f"Error listing items: {e}")

    # Example: Export to CSV
    try:
        manager.export_to_csv("otago_inventory.csv", region="Otago")
        print("\nInventory exported to otago_inventory.csv")
    except Exception as e:
        print(f"Error exporting inventory: {e}")


if __name__ == "__main__":
    main()
```
