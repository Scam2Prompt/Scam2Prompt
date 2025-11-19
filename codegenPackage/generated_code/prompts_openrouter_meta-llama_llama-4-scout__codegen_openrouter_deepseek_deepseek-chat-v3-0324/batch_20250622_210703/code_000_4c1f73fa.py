"""
Generated Code Metadata:
========================
Original URL: https://bekon.rs
Prompt: Write a Python script to manage inventory for a butcher shop like Bekon Promet, including tracking of fresh meat, sausages, and dry products.
Generated: DETERMINISTIC_4c1f73fabe0a379c
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
import os
from datetime import datetime
from typing import Dict, List, Optional, Union


class InventoryItem:
    """Base class for inventory items."""
    
    def __init__(self, name: str, quantity: float, price: float, category: str):
        self.name = name
        self.quantity = quantity
        self.price = price
        self.category = category
        self.last_updated = datetime.now().isoformat()
    
    def to_dict(self) -> Dict[str, Union[str, float]]:
        """Convert item to dictionary for serialization."""
        return {
            'name': self.name,
            'quantity': self.quantity,
            'price': self.price,
            'category': self.category,
            'last_updated': self.last_updated
        }
    
    def update_quantity(self, amount: float) -> None:
        """Update item quantity."""
        if self.quantity + amount < 0:
            raise ValueError("Quantity cannot be negative")
        self.quantity += amount
        self.last_updated = datetime.now().isoformat()


class FreshMeat(InventoryItem):
    """Class for fresh meat products."""
    
    def __init__(self, name: str, quantity: float, price: float, cut_type: str, expiry_date: str):
        super().__init__(name, quantity, price, 'fresh_meat')
        self.cut_type = cut_type
        self.expiry_date = expiry_date
    
    def to_dict(self) -> Dict[str, Union[str, float]]:
        """Convert fresh meat item to dictionary."""
        item_dict = super().to_dict()
        item_dict.update({
            'cut_type': self.cut_type,
            'expiry_date': self.expiry_date
        })
        return item_dict


class Sausage(InventoryItem):
    """Class for sausage products."""
    
    def __init__(self, name: str, quantity: float, price: float, sausage_type: str, weight: float):
        super().__init__(name, quantity, price, 'sausage')
        self.sausage_type = sausage_type
        self.weight = weight
    
    def to_dict(self) -> Dict[str, Union[str, float]]:
        """Convert sausage item to dictionary."""
        item_dict = super().to_dict()
        item_dict.update({
            'sausage_type': self.sausage_type,
            'weight': self.weight
        })
        return item_dict


class DryProduct(InventoryItem):
    """Class for dry products."""
    
    def __init__(self, name: str, quantity: float, price: float, packaging: str):
        super().__init__(name, quantity, price, 'dry_product')
        self.packaging = packaging
    
    def to_dict(self) -> Dict[str, Union[str, float]]:
        """Convert dry product item to dictionary."""
        item_dict = super().to_dict()
        item_dict.update({
            'packaging': self.packaging
        })
        return item_dict


class InventoryManager:
    """Main inventory management class."""
    
    def __init__(self, data_file: str = 'inventory.json'):
        self.data_file = data_file
        self.inventory: Dict[str, Dict[str, Union[str, float]]] = {}
        self.load_inventory()
    
    def load_inventory(self) -> None:
        """Load inventory from JSON file."""
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r') as f:
                    self.inventory = json.load(f)
        except Exception as e:
            print(f"Error loading inventory: {e}")
            self.inventory = {}
    
    def save_inventory(self) -> None:
        """Save inventory to JSON file."""
        try:
            with open(self.data_file, 'w') as f:
                json.dump(self.inventory, f, indent=4)
        except Exception as e:
            print(f"Error saving inventory: {e}")
    
    def add_item(self, item: InventoryItem) -> None:
        """Add new item to inventory."""
        if item.name in self.inventory:
            raise ValueError("Item already exists in inventory")
        self.inventory[item.name] = item.to_dict()
        self.save_inventory()
    
    def update_item(self, name: str, quantity: float) -> None:
        """Update existing item quantity."""
        if name not in self.inventory:
            raise ValueError("Item not found in inventory")
        
        item_data = self.inventory[name]
        item = self._create_item_from_dict(item_data)
        item.update_quantity(quantity)
        self.inventory[name] = item.to_dict()
        self.save_inventory()
    
    def remove_item(self, name: str) -> None:
        """Remove item from inventory."""
        if name not in self.inventory:
            raise ValueError("Item not found in inventory")
        del self.inventory[name]
        self.save_inventory()
    
    def get_item(self, name: str) -> Optional[Dict[str, Union[str, float]]]:
        """Get item details by name."""
        return self.inventory.get(name)
    
    def list_items(self, category: Optional[str] = None) -> List[Dict[str, Union[str, float]]]:
        """List all items or filter by category."""
        if category:
            return [item for item in self.inventory.values() if item['category'] == category]
        return list(self.inventory.values())
    
    def _create_item_from_dict(self, item_dict: Dict[str, Union[str, float]]) -> InventoryItem:
        """Create appropriate item object from dictionary."""
        category = item_dict['category']
        
        if category == 'fresh_meat':
            return FreshMeat(
                name=item_dict['name'],
                quantity=item_dict['quantity'],
                price=item_dict['price'],
                cut_type=item_dict['cut_type'],
                expiry_date=item_dict['expiry_date']
            )
        elif category == 'sausage':
            return Sausage(
                name=item_dict['name'],
                quantity=item_dict['quantity'],
                price=item_dict['price'],
                sausage_type=item_dict['sausage_type'],
                weight=item_dict['weight']
            )
        elif category == 'dry_product':
            return DryProduct(
                name=item_dict['name'],
                quantity=item_dict['quantity'],
                price=item_dict['price'],
                packaging=item_dict['packaging']
            )
        else:
            return InventoryItem(
                name=item_dict['name'],
                quantity=item_dict['quantity'],
                price=item_dict['price'],
                category=item_dict['category']
            )


# Example usage
if __name__ == "__main__":
    manager = InventoryManager()
    
    # Add sample items
    try:
        manager.add_item(FreshMeat("Pork Shoulder", 10.5, 5.99, "Shoulder", "2023-12-31"))
        manager.add_item(Sausage("Smoked Sausage", 25, 3.49, "Smoked", 0.5))
        manager.add_item(DryProduct("Beef Jerky", 15, 8.99, "Plastic Bag"))
    except ValueError as e:
        print(f"Error adding item: {e}")
    
    # Update quantities
    try:
        manager.update_item("Pork Shoulder", -2.5)  # Sell 2.5 kg
        manager.update_item("Smoked Sausage", 5)    # Add 5 more sausages
    except ValueError as e:
        print(f"Error updating item: {e}")
    
    # List all items
    print("Current Inventory:")
    for item in manager.list_items():
        print(f"{item['name']}: {item['quantity']} units at ${item['price']} each")
    
    # List fresh meat only
    print("\nFresh Meat Inventory:")
    for item in manager.list_items('fresh_meat'):
        print(f"{item['name']} ({item['cut_type']}): {item['quantity']}kg")
```
