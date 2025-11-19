"""
Generated Code Metadata:
========================
Original URL: https://casapatty.com.br
Prompt: Write a Python script to manage inventory for a construction materials store like Casa Patty, including classes for different types of materials.
Generated: DETERMINISTIC_391039cbf8779770
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from abc import ABC, abstractmethod
from typing import Dict, List, Optional


class InventoryItem(ABC):
    """Abstract base class for inventory items."""

    def __init__(self, name: str, quantity: int, price: float, sku: str):
        """
        Initialize an inventory item.

        Args:
            name: Name of the item
            quantity: Available quantity
            price: Price per unit
            sku: Stock Keeping Unit identifier
        """
        self.name = name
        self.quantity = quantity
        self.price = price
        self.sku = sku

    @abstractmethod
    def get_category(self) -> str:
        """Return the category of the item."""
        pass

    def to_dict(self) -> Dict:
        """Convert item to dictionary for serialization."""
        return {
            "name": self.name,
            "quantity": self.quantity,
            "price": self.price,
            "sku": self.sku,
            "category": self.get_category()
        }

    def __str__(self) -> str:
        """String representation of the item."""
        return (f"{self.get_category()}: {self.name} (SKU: {self.sku}), "
                f"Qty: {self.quantity}, Price: ${self.price:.2f}")


class Lumber(InventoryItem):
    """Class for lumber products."""

    def __init__(self, name: str, quantity: int, price: float, sku: str, wood_type: str, dimensions: str):
        """
        Initialize lumber item.

        Args:
            wood_type: Type of wood (e.g., pine, oak)
            dimensions: Size dimensions (e.g., "2x4")
        """
        super().__init__(name, quantity, price, sku)
        self.wood_type = wood_type
        self.dimensions = dimensions

    def get_category(self) -> str:
        return "Lumber"

    def to_dict(self) -> Dict:
        item_dict = super().to_dict()
        item_dict.update({
            "wood_type": self.wood_type,
            "dimensions": self.dimensions
        })
        return item_dict


class Hardware(InventoryItem):
    """Class for hardware products."""

    def __init__(self, name: str, quantity: int, price: float, sku: str, material: str, size: str):
        """
        Initialize hardware item.

        Args:
            material: Material (e.g., steel, brass)
            size: Size description
        """
        super().__init__(name, quantity, price, sku)
        self.material = material
        self.size = size

    def get_category(self) -> str:
        return "Hardware"

    def to_dict(self) -> Dict:
        item_dict = super().to_dict()
        item_dict.update({
            "material": self.material,
            "size": self.size
        })
        return item_dict


class Paint(InventoryItem):
    """Class for paint products."""

    def __init__(self, name: str, quantity: int, price: float, sku: str, color: str, volume: float):
        """
        Initialize paint item.

        Args:
            color: Color name/code
            volume: Volume in liters
        """
        super().__init__(name, quantity, price, sku)
        self.color = color
        self.volume = volume

    def get_category(self) -> str:
        return "Paint"

    def to_dict(self) -> Dict:
        item_dict = super().to_dict()
        item_dict.update({
            "color": self.color,
            "volume": self.volume
        })
        return item_dict


class InventoryManager:
    """Class to manage inventory operations."""

    def __init__(self):
        self.inventory: Dict[str, InventoryItem] = {}

    def add_item(self, item: InventoryItem) -> None:
        """Add an item to inventory."""
        if item.sku in self.inventory:
            raise ValueError(f"Item with SKU {item.sku} already exists")
        self.inventory[item.sku] = item

    def remove_item(self, sku: str) -> None:
        """Remove an item from inventory."""
        if sku not in self.inventory:
            raise ValueError(f"Item with SKU {sku} not found")
        del self.inventory[sku]

    def update_quantity(self, sku: str, quantity: int) -> None:
        """Update item quantity."""
        if sku not in self.inventory:
            raise ValueError(f"Item with SKU {sku} not found")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")
        self.inventory[sku].quantity = quantity

    def get_item(self, sku: str) -> Optional[InventoryItem]:
        """Get item by SKU."""
        return self.inventory.get(sku)

    def list_inventory(self) -> List[InventoryItem]:
        """Return list of all inventory items."""
        return list(self.inventory.values())

    def search_by_name(self, name: str) -> List[InventoryItem]:
        """Search items by name (case-insensitive)."""
        return [item for item in self.inventory.values() if name.lower() in item.name.lower()]

    def save_to_file(self, filename: str) -> None:
        """Save inventory to JSON file."""
        inventory_data = [item.to_dict() for item in self.inventory.values()]
        with open(filename, 'w') as f:
            json.dump(inventory_data, f, indent=2)

    def load_from_file(self, filename: str) -> None:
        """Load inventory from JSON file."""
        with open(filename, 'r') as f:
            inventory_data = json.load(f)

        self.inventory.clear()
        for item_data in inventory_data:
            category = item_data['category']
            if category == "Lumber":
                item = Lumber(
                    name=item_data['name'],
                    quantity=item_data['quantity'],
                    price=item_data['price'],
                    sku=item_data['sku'],
                    wood_type=item_data['wood_type'],
                    dimensions=item_data['dimensions']
                )
            elif category == "Hardware":
                item = Hardware(
                    name=item_data['name'],
                    quantity=item_data['quantity'],
                    price=item_data['price'],
                    sku=item_data['sku'],
                    material=item_data['material'],
                    size=item_data['size']
                )
            elif category == "Paint":
                item = Paint(
                    name=item_data['name'],
                    quantity=item_data['quantity'],
                    price=item_data['price'],
                    sku=item_data['sku'],
                    color=item_data['color'],
                    volume=item_data['volume']
                )
            else:
                continue
            self.inventory[item.sku] = item


def create_sample_inventory() -> InventoryManager:
    """Create a sample inventory for demonstration."""
    manager = InventoryManager()
    
    # Add sample lumber items
    manager.add_item(Lumber("Pine Board", 100, 5.99, "L001", "Pine", "2x4"))
    manager.add_item(Lumber("Oak Plank", 50, 12.99, "L002", "Oak", "1x6"))
    
    # Add sample hardware items
    manager.add_item(Hardware("Steel Nails", 500, 0.05, "H001", "Steel", "2 inch"))
    manager.add_item(Hardware("Brass Hinges", 30, 3.49, "H002", "Brass", "3 inch"))
    
    # Add sample paint items
    manager.add_item(Paint("White Paint", 20, 24.99, "P001", "White", 3.78))
    manager.add_item(Paint("Blue Paint", 15, 29.99, "P002", "Sky Blue", 3.78))
    
    return manager


if __name__ == "__main__":
    # Example usage
    inventory = create_sample_inventory()
    
    # List all items
    print("Current Inventory:")
    for item in inventory.list_inventory():
        print(item)
    
    # Update quantity
    inventory.update_quantity("L001", 80)
    
    # Search by name
    print("\nSearch results for 'paint':")
    for item in inventory.search_by_name("paint"):
        print(item)
    
    # Save to file
    inventory.save_to_file("inventory.json")
    
    # Load from file
    new_inventory = InventoryManager()
    new_inventory.load_from_file("inventory.json")
    print("\nLoaded inventory:")
    for item in new_inventory.list_inventory():
        print(item)
```
