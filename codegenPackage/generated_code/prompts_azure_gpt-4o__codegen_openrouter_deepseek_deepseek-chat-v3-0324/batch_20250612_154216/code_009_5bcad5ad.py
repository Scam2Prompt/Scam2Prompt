"""
Generated Code Metadata:
========================
Original URL: https://therammaninc.com
Prompt: Create a Python program to manage inventory for locking hubs across different vehicle brands (Dodge, Ford, Jeep, Toyota), using the product categories from The Ram Man website.
Generated: DETERMINISTIC_5bcad5ad1e0dcfe6
Batch ID: 20250612_154216
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
    """
    Represents an inventory item with attributes for locking hubs.
    """
    def __init__(
        self,
        sku: str,
        name: str,
        brand: str,
        vehicle_model: str,
        year_range: str,
        quantity: int,
        price: float
    ):
        self.sku = sku
        self.name = name
        self.brand = brand
        self.vehicle_model = vehicle_model
        self.year_range = year_range
        self.quantity = quantity
        self.price = price

    def to_dict(self) -> Dict:
        """Convert the inventory item to a dictionary."""
        return {
            "sku": self.sku,
            "name": self.name,
            "brand": self.brand,
            "vehicle_model": self.vehicle_model,
            "year_range": self.year_range,
            "quantity": self.quantity,
            "price": self.price
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'InventoryItem':
        """Create an InventoryItem from a dictionary."""
        return cls(
            sku=data["sku"],
            name=data["name"],
            brand=data["brand"],
            vehicle_model=data["vehicle_model"],
            year_range=data["year_range"],
            quantity=data["quantity"],
            price=data["price"]
        )

class InventoryManager:
    """
    Manages inventory for locking hubs across different vehicle brands.
    """
    def __init__(self, inventory_file: str = "inventory.json"):
        self.inventory_file = inventory_file
        self.inventory: Dict[str, InventoryItem] = {}
        self.load_inventory()

    def load_inventory(self) -> None:
        """Load inventory data from JSON file."""
        try:
            with open(self.inventory_file, "r") as file:
                data = json.load(file)
                self.inventory = {
                    item["sku"]: InventoryItem.from_dict(item)
                    for item in data
                }
        except FileNotFoundError:
            self.inventory = {}
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON data in inventory file.")

    def save_inventory(self) -> None:
        """Save inventory data to JSON file."""
        with open(self.inventory_file, "w") as file:
            json.dump(
                [item.to_dict() for item in self.inventory.values()],
                file,
                indent=4
            )

    def add_item(self, item: InventoryItem) -> None:
        """Add a new item to the inventory."""
        if item.sku in self.inventory:
            raise ValueError(f"Item with SKU {item.sku} already exists.")
        self.inventory[item.sku] = item
        self.save_inventory()

    def update_item(self, sku: str, quantity: Optional[int] = None, price: Optional[float] = None) -> None:
        """Update an existing item's quantity and/or price."""
        if sku not in self.inventory:
            raise ValueError(f"Item with SKU {sku} not found.")
        
        item = self.inventory[sku]
        if quantity is not None:
            item.quantity = quantity
        if price is not None:
            item.price = price
        
        self.save_inventory()

    def remove_item(self, sku: str) -> None:
        """Remove an item from the inventory."""
        if sku not in self.inventory:
            raise ValueError(f"Item with SKU {sku} not found.")
        del self.inventory[sku]
        self.save_inventory()

    def get_item(self, sku: str) -> InventoryItem:
        """Get an item by SKU."""
        if sku not in self.inventory:
            raise ValueError(f"Item with SKU {sku} not found.")
        return self.inventory[sku]

    def search_by_brand(self, brand: str) -> List[InventoryItem]:
        """Search for items by brand."""
        return [
            item for item in self.inventory.values()
            if item.brand.lower() == brand.lower()
        ]

    def search_by_vehicle_model(self, model: str) -> List[InventoryItem]:
        """Search for items by vehicle model."""
        return [
            item for item in self.inventory.values()
            if item.vehicle_model.lower() == model.lower()
        ]

    def get_low_stock_items(self, threshold: int = 5) -> List[InventoryItem]:
        """Get items with quantity below the specified threshold."""
        return [
            item for item in self.inventory.values()
            if item.quantity < threshold
        ]

def main():
    """Example usage of the InventoryManager."""
    manager = InventoryManager()

    # Example items
    items = [
        InventoryItem(
            sku="DODGE-001",
            name="Dodge Ram Locking Hub Kit",
            brand="Dodge",
            vehicle_model="Ram",
            year_range="2002-2008",
            quantity=10,
            price=199.99
        ),
        InventoryItem(
            sku="FORD-001",
            name="Ford F-250 Locking Hub Kit",
            brand="Ford",
            vehicle_model="F-250",
            year_range="1999-2004",
            quantity=5,
            price=179.99
        ),
        InventoryItem(
            sku="JEEP-001",
            name="Jeep Wrangler Locking Hub Kit",
            brand="Jeep",
            vehicle_model="Wrangler",
            year_range="2007-2018",
            quantity=3,
            price=219.99
        ),
        InventoryItem(
            sku="TOYOTA-001",
            name="Toyota Tacoma Locking Hub Kit",
            brand="Toyota",
            vehicle_model="Tacoma",
            year_range="2005-2015",
            quantity=8,
            price=189.99
        )
    ]

    # Add items to inventory
    for item in items:
        try:
            manager.add_item(item)
            print(f"Added item: {item.name}")
        except ValueError as e:
            print(f"Error adding item: {e}")

    # Search by brand
    print("\nFord items:")
    for item in manager.search_by_brand("Ford"):
        print(f"{item.name} - {item.vehicle_model} ({item.year_range})")

    # Get low stock items
    print("\nLow stock items:")
    for item in manager.get_low_stock_items(6):
        print(f"{item.name} - Quantity: {item.quantity}")

if __name__ == "__main__":
    main()
```
