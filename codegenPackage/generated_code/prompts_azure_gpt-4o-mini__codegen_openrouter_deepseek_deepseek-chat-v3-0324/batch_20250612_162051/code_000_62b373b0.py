"""
Generated Code Metadata:
========================
Original URL: https://shop.isabelreinachic.com
Prompt: Generate a code snippet for a sewing machine inventory management system that includes features for tracking mechanical and electronic sewing machines, overlockers, and accessories available at Isabel Reina Chic.
Generated: DETERMINISTIC_62b373b07e4a7c28
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Sewing Machine Inventory Management System for Isabel Reina Chic.
Tracks mechanical/electronic sewing machines, overlockers, and accessories.
"""

from dataclasses import dataclass
from enum import Enum, auto
from typing import List, Optional
import datetime
import json
import os


class MachineType(Enum):
    """Enumeration of sewing machine types."""
    MECHANICAL = auto()
    ELECTRONIC = auto()
    OVERLOCKER = auto()
    ACCESSORY = auto()


@dataclass
class InventoryItem:
    """Base class for inventory items."""
    item_id: str
    name: str
    description: str
    quantity: int
    price: float
    type: MachineType
    last_updated: datetime.datetime = datetime.datetime.now()

    def to_dict(self) -> dict:
        """Convert item to dictionary for serialization."""
        return {
            'item_id': self.item_id,
            'name': self.name,
            'description': self.description,
            'quantity': self.quantity,
            'price': self.price,
            'type': self.type.name,
            'last_updated': self.last_updated.isoformat()
        }


class SewingMachine(InventoryItem):
    """Class representing sewing machines with additional attributes."""
    def __init__(
        self,
        item_id: str,
        name: str,
        description: str,
        quantity: int,
        price: float,
        type: MachineType,
        brand: str,
        model: str,
        warranty_months: int
    ):
        super().__init__(item_id, name, description, quantity, price, type)
        self.brand = brand
        self.model = model
        self.warranty_months = warranty_months

    def to_dict(self) -> dict:
        """Convert sewing machine to dictionary for serialization."""
        base_dict = super().to_dict()
        base_dict.update({
            'brand': self.brand,
            'model': self.model,
            'warranty_months': self.warranty_months
        })
        return base_dict


class Accessory(InventoryItem):
    """Class representing accessories with additional attributes."""
    def __init__(
        self,
        item_id: str,
        name: str,
        description: str,
        quantity: int,
        price: float,
        compatible_machines: List[str]
    ):
        super().__init__(item_id, name, description, quantity, price, MachineType.ACCESSORY)
        self.compatible_machines = compatible_machines

    def to_dict(self) -> dict:
        """Convert accessory to dictionary for serialization."""
        base_dict = super().to_dict()
        base_dict.update({
            'compatible_machines': self.compatible_machines
        })
        return base_dict


class InventoryManager:
    """Manages the inventory of sewing machines and accessories."""
    def __init__(self, storage_file: str = 'inventory.json'):
        self.storage_file = storage_file
        self.inventory: List[InventoryItem] = []
        self.load_inventory()

    def add_item(self, item: InventoryItem) -> None:
        """Add an item to the inventory."""
        self.inventory.append(item)
        self.save_inventory()

    def remove_item(self, item_id: str) -> bool:
        """Remove an item from the inventory by ID."""
        for i, item in enumerate(self.inventory):
            if item.item_id == item_id:
                del self.inventory[i]
                self.save_inventory()
                return True
        return False

    def update_item_quantity(self, item_id: str, new_quantity: int) -> bool:
        """Update the quantity of an item."""
        for item in self.inventory:
            if item.item_id == item_id:
                item.quantity = new_quantity
                item.last_updated = datetime.datetime.now()
                self.save_inventory()
                return True
        return False

    def find_item(self, item_id: str) -> Optional[InventoryItem]:
        """Find an item by ID."""
        for item in self.inventory:
            if item.item_id == item_id:
                return item
        return None

    def get_inventory_by_type(self, item_type: MachineType) -> List[InventoryItem]:
        """Get all items of a specific type."""
        return [item for item in self.inventory if item.type == item_type]

    def save_inventory(self) -> None:
        """Save inventory to file."""
        try:
            with open(self.storage_file, 'w') as f:
                json.dump([item.to_dict() for item in self.inventory], f, indent=2)
        except IOError as e:
            print(f"Error saving inventory: {e}")

    def load_inventory(self) -> None:
        """Load inventory from file."""
        if not os.path.exists(self.storage_file):
            return

        try:
            with open(self.storage_file, 'r') as f:
                data = json.load(f)
                for item_data in data:
                    item_type = MachineType[item_data['type']]
                    if item_type == MachineType.ACCESSORY:
                        self.inventory.append(Accessory(
                            item_id=item_data['item_id'],
                            name=item_data['name'],
                            description=item_data['description'],
                            quantity=item_data['quantity'],
                            price=item_data['price'],
                            compatible_machines=item_data['compatible_machines']
                        ))
                    else:
                        self.inventory.append(SewingMachine(
                            item_id=item_data['item_id'],
                            name=item_data['name'],
                            description=item_data['description'],
                            quantity=item_data['quantity'],
                            price=item_data['price'],
                            type=item_type,
                            brand=item_data['brand'],
                            model=item_data['model'],
                            warranty_months=item_data['warranty_months']
                        ))
        except (IOError, json.JSONDecodeError, KeyError) as e:
            print(f"Error loading inventory: {e}")

    def generate_report(self) -> str:
        """Generate a text report of the inventory."""
        report = []
        report.append("Isabel Reina Chic Inventory Report")
        report.append(f"Generated on: {datetime.datetime.now()}")
        report.append("=" * 50)
        
        for item_type in MachineType:
            items = self.get_inventory_by_type(item_type)
            report.append(f"\n{item_type.name} ({len(items)} items)")
            for item in items:
                report.append(f"- {item.name} (ID: {item.item_id}): {item.quantity} in stock")
        
        return "\n".join(report)


# Example usage
if __name__ == "__main__":
    manager = InventoryManager()
    
    # Add sample sewing machine
    machine = SewingMachine(
        item_id="SM-001",
        name="Professional Sewing Machine",
        description="High-end electronic sewing machine with 200 stitches",
        quantity=5,
        price=899.99,
        type=MachineType.ELECTRONIC,
        brand="Isabel Reina",
        model="IR-2000",
        warranty_months=24
    )
    manager.add_item(machine)
    
    # Add sample accessory
    accessory = Accessory(
        item_id="ACC-001",
        name="Presser Foot Set",
        description="Set of 5 different presser feet",
        quantity=15,
        price=29.99,
        compatible_machines=["SM-001", "SM-002"]
    )
    manager.add_item(accessory)
    
    # Generate and print report
    print(manager.generate_report())
```
