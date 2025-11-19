"""
Generated Code Metadata:
========================
Original URL: https://generate-digital.com
Prompt: Write a Python code to create a digital inventory management system for a sports business, including a configurable catalogue of available and potential inventory ranked by various factors.
Generated: DETERMINISTIC_33e918c86b5827b1
Batch ID: 20250622_205436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# inventory_management_system.py

from enum import Enum
from typing import List, Dict

class InventoryStatus(Enum):
    """Enum for inventory status"""
    AVAILABLE = 1
    RESERVED = 2
    OUT_OF_STOCK = 3

class InventoryItem:
    """Class representing an inventory item"""
    def __init__(self, 
                 item_id: int, 
                 name: str, 
                 description: str, 
                 quantity: int, 
                 status: InventoryStatus, 
                 category: str, 
                 supplier: str, 
                 price: float):
        self.item_id = item_id
        self.name = name
        self.description = description
        self.quantity = quantity
        self.status = status
        self.category = category
        self.supplier = supplier
        self.price = price

    def __repr__(self):
        return f"InventoryItem(item_id={self.item_id}, name='{self.name}', quantity={self.quantity}, status={self.status})"

class Inventory:
    """Class representing the inventory"""
    def __init__(self):
        self.items: Dict[int, InventoryItem] = {}

    def add_item(self, item: InventoryItem):
        """Add an item to the inventory"""
        self.items[item.item_id] = item

    def remove_item(self, item_id: int):
        """Remove an item from the inventory"""
        if item_id in self.items:
            del self.items[item_id]
        else:
            raise ValueError(f"Item with ID {item_id} not found")

    def update_item(self, item_id: int, **kwargs):
        """Update an item in the inventory"""
        if item_id in self.items:
            for key, value in kwargs.items():
                setattr(self.items[item_id], key, value)
        else:
            raise ValueError(f"Item with ID {item_id} not found")

    def get_item(self, item_id: int) -> InventoryItem:
        """Get an item from the inventory"""
        return self.items.get(item_id)

    def list_items(self, category: str = None, status: InventoryStatus = None) -> List[InventoryItem]:
        """List items in the inventory"""
        items = list(self.items.values())
        if category:
            items = [item for item in items if item.category == category]
        if status:
            items = [item for item in items if item.status == status]
        return items

class Catalogue:
    """Class representing the catalogue"""
    def __init__(self):
        self.inventory = Inventory()

    def add_item_to_catalogue(self, item: InventoryItem):
        """Add an item to the catalogue"""
        self.inventory.add_item(item)

    def remove_item_from_catalogue(self, item_id: int):
        """Remove an item from the catalogue"""
        self.inventory.remove_item(item_id)

    def list_available_items(self) -> List[InventoryItem]:
        """List available items in the catalogue"""
        return self.inventory.list_items(status=InventoryStatus.AVAILABLE)

    def list_items_by_category(self, category: str) -> List[InventoryItem]:
        """List items in the catalogue by category"""
        return self.inventory.list_items(category=category)

def main():
    catalogue = Catalogue()

    # Create some items
    item1 = InventoryItem(1, "Football", "Leather football", 10, InventoryStatus.AVAILABLE, "Ball", "Supplier A", 20.0)
    item2 = InventoryItem(2, "Basketball", "Rubber basketball", 5, InventoryStatus.RESERVED, "Ball", "Supplier B", 15.0)
    item3 = InventoryItem(3, "Tennis Racket", "Aluminum tennis racket", 8, InventoryStatus.AVAILABLE, "Racket", "Supplier C", 50.0)

    # Add items to catalogue
    catalogue.add_item_to_catalogue(item1)
    catalogue.add_item_to_catalogue(item2)
    catalogue.add_item_to_catalogue(item3)

    # List available items
    print("Available Items:")
    for item in catalogue.list_available_items():
        print(item)

    # List items by category
    print("\nItems by Category 'Ball':")
    for item in catalogue.list_items_by_category("Ball"):
        print(item)

if __name__ == "__main__":
    main()
```
