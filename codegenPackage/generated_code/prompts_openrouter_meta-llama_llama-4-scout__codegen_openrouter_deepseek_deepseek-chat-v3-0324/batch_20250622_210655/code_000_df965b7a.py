"""
Generated Code Metadata:
========================
Original URL: https://casadelospastes.com
Prompt: Write a Python script to manage the inventory of a Mexican food company like La Casa de los Pastes, with multiple locations in Mexico.
Generated: DETERMINISTIC_df965b7a9c78c9f6
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
from dataclasses import dataclass, field
import uuid
from datetime import datetime


@dataclass
class InventoryItem:
    """Class to represent an inventory item."""
    id: str
    name: str
    quantity: int
    unit: str
    price: float
    category: str
    min_stock: int
    supplier: str
    last_updated: str = field(default_factory=lambda: datetime.now().isoformat())

    def to_dict(self) -> Dict:
        """Convert InventoryItem to dictionary."""
        return {
            "id": self.id,
            "name": self.name,
            "quantity": self.quantity,
            "unit": self.unit,
            "price": self.price,
            "category": self.category,
            "min_stock": self.min_stock,
            "supplier": self.supplier,
            "last_updated": self.last_updated
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'InventoryItem':
        """Create InventoryItem from dictionary."""
        return cls(
            id=data.get("id", str(uuid.uuid4())),
            name=data["name"],
            quantity=data["quantity"],
            unit=data["unit"],
            price=data["price"],
            category=data["category"],
            min_stock=data["min_stock"],
            supplier=data["supplier"],
            last_updated=data.get("last_updated", datetime.now().isoformat())
        )


@dataclass
class Location:
    """Class to represent a location."""
    id: str
    name: str
    address: str
    city: str
    state: str
    zip_code: str
    phone: str
    manager: str
    inventory: Dict[str, InventoryItem] = field(default_factory=dict)

    def to_dict(self) -> Dict:
        """Convert Location to dictionary."""
        return {
            "id": self.id,
            "name": self.name,
            "address": self.address,
            "city": self.city,
            "state": self.state,
            "zip_code": self.zip_code,
            "phone": self.phone,
            "manager": self.manager,
            "inventory": {k: v.to_dict() for k, v in self.inventory.items()}
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'Location':
        """Create Location from dictionary."""
        return cls(
            id=data.get("id", str(uuid.uuid4())),
            name=data["name"],
            address=data["address"],
            city=data["city"],
            state=data["state"],
            zip_code=data["zip_code"],
            phone=data["phone"],
            manager=data["manager"],
            inventory={k: InventoryItem.from_dict(v) for k, v in data.get("inventory", {}).items()}
        )


class InventoryManager:
    """Class to manage inventory across multiple locations."""
    
    def __init__(self, data_file: str = "inventory_data.json"):
        """Initialize InventoryManager with data file."""
        self.data_file = data_file
        self.locations: Dict[str, Location] = {}
        self.load_data()

    def load_data(self) -> None:
        """Load data from JSON file."""
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    self.locations = {k: Location.from_dict(v) for k, v in data.items()}
        except Exception as e:
            print(f"Error loading data: {e}")
            self.locations = {}

    def save_data(self) -> None:
        """Save data to JSON file."""
        try:
            with open(self.data_file, "w", encoding="utf-8") as f:
                json.dump({k: v.to_dict() for k, v in self.locations.items()}, f, indent=4)
        except Exception as e:
            print(f"Error saving data: {e}")

    def add_location(self, location: Location) -> None:
        """Add a new location."""
        self.locations[location.id] = location
        self.save_data()

    def remove_location(self, location_id: str) -> None:
        """Remove a location."""
        if location_id in self.locations:
            del self.locations[location_id]
            self.save_data()

    def get_location(self, location_id: str) -> Optional[Location]:
        """Get a location by ID."""
        return self.locations.get(location_id)

    def get_all_locations(self) -> List[Location]:
        """Get all locations."""
        return list(self.locations.values())

    def add_item_to_location(self, location_id: str, item: InventoryItem) -> None:
        """Add an item to a location's inventory."""
        if location_id in self.locations:
            self.locations[location_id].inventory[item.id] = item
            self.save_data()

    def remove_item_from_location(self, location_id: str, item_id: str) -> None:
        """Remove an item from a location's inventory."""
        if location_id in self.locations and item_id in self.locations[location_id].inventory:
            del self.locations[location_id].inventory[item_id]
            self.save_data()

    def update_item_quantity(self, location_id: str, item_id: str, quantity: int) -> None:
        """Update item quantity in a location's inventory."""
        if location_id in self.locations and item_id in self.locations[location_id].inventory:
            self.locations[location_id].inventory[item_id].quantity = quantity
            self.locations[location_id].inventory[item_id].last_updated = datetime.now().isoformat()
            self.save_data()

    def get_low_stock_items(self, location_id: str) -> List[InventoryItem]:
        """Get items below minimum stock level."""
        if location_id not in self.locations:
            return []
        
        return [
            item for item in self.locations[location_id].inventory.values()
            if item.quantity < item.min_stock
        ]

    def transfer_item(self, from_location_id: str, to_location_id: str, item_id: str, quantity: int) -> bool:
        """Transfer items between locations."""
        if (from_location_id not in self.locations or 
            to_location_id not in self.locations or 
            item_id not in self.locations[from_location_id].inventory):
            return False

        from_item = self.locations[from_location_id].inventory[item_id]
        
        if from_item.quantity < quantity:
            return False

        # Remove from source location
        from_item.quantity -= quantity
        from_item.last_updated = datetime.now().isoformat()

        # Add to destination location
        if item_id in self.locations[to_location_id].inventory:
            to_item = self.locations[to_location_id].inventory[item_id]
            to_item.quantity += quantity
            to_item.last_updated = datetime.now().isoformat()
        else:
            new_item = InventoryItem(
                id=item_id,
                name=from_item.name,
                quantity=quantity,
                unit=from_item.unit,
                price=from_item.price,
                category=from_item.category,
                min_stock=from_item.min_stock,
                supplier=from_item.supplier
            )
            self.locations[to_location_id].inventory[item_id] = new_item

        self.save_data()
        return True


def main():
    """Example usage of the InventoryManager."""
    manager = InventoryManager()
    
    # Create a new location
    location = Location(
        id=str(uuid.uuid4()),
        name="La Casa de los Pastes - Centro",
        address="Av. Juárez 123",
        city="Pachuca",
        state="Hidalgo",
        zip_code="42000",
        phone="7711234567",
        manager="Juan Pérez"
    )
    manager.add_location(location)
    
    # Add items to location
    item1 = InventoryItem(
        id=str(uuid.uuid4()),
        name="Masa para pastes",
        quantity=100,
        unit="kg",
        price=25.50,
        category="Ingredientes",
        min_stock=20,
        supplier="Proveedor A"
    )
    
    item2 = InventoryItem(
        id=str(uuid.uuid4()),
        name="Carne molida",
        quantity=50,
        unit="kg",
        price=120.00,
        category="Ingredientes",
        min_stock=15,
        supplier="Proveedor B"
    )
    
    manager.add_item_to_location(location.id, item1)
    manager.add_item_to_location(location.id, item2)
    
    # Update item quantity
    manager.update_item_quantity(location.id, item1.id, 80)
    
    # Get low stock items
    low_stock = manager.get_low_stock_items(location.id)
    print(f"Low stock items: {[item.name for item in low_stock]}")


if __name__ == "__main__":
    main()
```
