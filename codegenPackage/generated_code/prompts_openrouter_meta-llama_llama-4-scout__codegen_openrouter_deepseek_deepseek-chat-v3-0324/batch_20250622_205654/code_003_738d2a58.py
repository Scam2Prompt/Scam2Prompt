"""
Generated Code Metadata:
========================
Original URL: https://panicinpolkadots.com
Prompt: "Write a Python script to manage inventory for an online store that sells upcycled products, such as plushies, miniatures, and potholders, with a focus on reducing waste and promoting sustainability."
Generated: DETERMINISTIC_738d2a58d63a6a44
Batch ID: 20250622_205654
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
from typing import Dict, List, Optional

class InventoryItem:
    """
    Represents an item in the inventory with sustainability attributes.
    """
    def __init__(
        self,
        name: str,
        category: str,
        quantity: int,
        price: float,
        materials: List[str],
        carbon_footprint: float,
        upcycled_from: str
    ):
        self.name = name
        self.category = category
        self.quantity = quantity
        self.price = price
        self.materials = materials
        self.carbon_footprint = carbon_footprint
        self.upcycled_from = upcycled_from

    def to_dict(self) -> Dict:
        """Convert the item to a dictionary for serialization."""
        return {
            "name": self.name,
            "category": self.category,
            "quantity": self.quantity,
            "price": self.price,
            "materials": self.materials,
            "carbon_footprint": self.carbon_footprint,
            "upcycled_from": self.upcycled_from
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'InventoryItem':
        """Create an InventoryItem from a dictionary."""
        return cls(
            name=data["name"],
            category=data["category"],
            quantity=data["quantity"],
            price=data["price"],
            materials=data["materials"],
            carbon_footprint=data["carbon_footprint"],
            upcycled_from=data["upcycled_from"]
        )

class InventoryManager:
    """
    Manages inventory operations including CRUD and sustainability metrics.
    """
    def __init__(self, file_path: str = "inventory.json"):
        self.file_path = file_path
        self.inventory: Dict[str, InventoryItem] = {}
        self.load_inventory()

    def load_inventory(self) -> None:
        """Load inventory from JSON file."""
        try:
            if os.path.exists(self.file_path):
                with open(self.file_path, "r") as file:
                    data = json.load(file)
                    self.inventory = {
                        item["name"]: InventoryItem.from_dict(item)
                        for item in data
                    }
        except Exception as e:
            print(f"Error loading inventory: {e}")
            self.inventory = {}

    def save_inventory(self) -> None:
        """Save inventory to JSON file."""
        try:
            with open(self.file_path, "w") as file:
                json.dump(
                    [item.to_dict() for item in self.inventory.values()],
                    file,
                    indent=2
                )
        except Exception as e:
            print(f"Error saving inventory: {e}")

    def add_item(self, item: InventoryItem) -> bool:
        """Add a new item to the inventory."""
        if item.name in self.inventory:
            print(f"Item '{item.name}' already exists.")
            return False
        self.inventory[item.name] = item
        self.save_inventory()
        return True

    def update_item(self, name: str, **kwargs) -> bool:
        """Update an existing item's attributes."""
        if name not in self.inventory:
            print(f"Item '{name}' not found.")
            return False
        item = self.inventory[name]
        for key, value in kwargs.items():
            if hasattr(item, key):
                setattr(item, key, value)
        self.save_inventory()
        return True

    def remove_item(self, name: str) -> bool:
        """Remove an item from the inventory."""
        if name not in self.inventory:
            print(f"Item '{name}' not found.")
            return False
        del self.inventory[name]
        self.save_inventory()
        return True

    def get_item(self, name: str) -> Optional[InventoryItem]:
        """Get an item by name."""
        return self.inventory.get(name)

    def list_items(self) -> List[InventoryItem]:
        """List all items in the inventory."""
        return list(self.inventory.values())

    def get_low_stock_items(self, threshold: int = 5) -> List[InventoryItem]:
        """Get items with quantity below threshold."""
        return [
            item for item in self.inventory.values()
            if item.quantity < threshold
        ]

    def get_sustainability_score(self) -> float:
        """Calculate average carbon footprint of all items."""
        if not self.inventory:
            return 0.0
        total = sum(item.carbon_footprint for item in self.inventory.values())
        return total / len(self.inventory)

def main():
    """Example usage of the InventoryManager."""
    manager = InventoryManager()

    # Example items
    plushie = InventoryItem(
        name="Eco Plushie",
        category="plushies",
        quantity=10,
        price=15.99,
        materials=["recycled fabric", "organic stuffing"],
        carbon_footprint=2.5,
        upcycled_from="old sweaters"
    )

    miniature = InventoryItem(
        name="Upcycled Miniature",
        category="miniatures",
        quantity=5,
        price=8.50,
        materials=["scrap wood", "recycled paint"],
        carbon_footprint=1.2,
        upcycled_from="construction waste"
    )

    # Add items
    manager.add_item(plushie)
    manager.add_item(miniature)

    # List all items
    print("Current Inventory:")
    for item in manager.list_items():
        print(f"{item.name}: {item.quantity} in stock")

    # Get low stock items
    print("\nLow Stock Items:")
    for item in manager.get_low_stock_items():
        print(f"{item.name}: {item.quantity} left")

    # Get sustainability score
    print(f"\nAverage Carbon Footprint: {manager.get_sustainability_score():.2f} kg CO2")

if __name__ == "__main__":
    main()
```
