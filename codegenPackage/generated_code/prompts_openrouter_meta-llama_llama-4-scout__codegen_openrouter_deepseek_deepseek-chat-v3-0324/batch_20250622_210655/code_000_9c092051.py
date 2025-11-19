"""
Generated Code Metadata:
========================
Original URL: https://harinderfarms.com
Prompt: Write a Python code to manage inventory of corn silage bales and potato seeds for a farm like Harinder Farms.
Generated: DETERMINISTIC_9c09205114170214
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
from typing import Dict, List, Optional
from datetime import datetime

class InventoryItem:
    """Base class for inventory items."""
    
    def __init__(self, name: str, quantity: int, unit: str, date_added: Optional[str] = None):
        """
        Initialize an inventory item.
        
        Args:
            name: Name of the item
            quantity: Quantity available
            unit: Unit of measurement (e.g., bales, kg)
            date_added: Date when item was added (YYYY-MM-DD)
        """
        self.name = name
        self.quantity = quantity
        self.unit = unit
        self.date_added = date_added if date_added else datetime.now().strftime("%Y-%m-%d")
    
    def to_dict(self) -> Dict:
        """Convert item to dictionary for serialization."""
        return {
            "name": self.name,
            "quantity": self.quantity,
            "unit": self.unit,
            "date_added": self.date_added
        }

class CornSilageBale(InventoryItem):
    """Class representing corn silage bales."""
    
    def __init__(self, quantity: int, bale_weight: float, date_added: Optional[str] = None):
        """
        Initialize corn silage bale item.
        
        Args:
            quantity: Number of bales
            bale_weight: Weight per bale in kg
            date_added: Date when added (YYYY-MM-DD)
        """
        super().__init__("Corn Silage Bale", quantity, "bales", date_added)
        self.bale_weight = bale_weight
    
    def to_dict(self) -> Dict:
        """Convert to dictionary including bale weight."""
        item_dict = super().to_dict()
        item_dict["bale_weight"] = self.bale_weight
        return item_dict

class PotatoSeed(InventoryItem):
    """Class representing potato seeds."""
    
    def __init__(self, quantity: int, variety: str, date_added: Optional[str] = None):
        """
        Initialize potato seed item.
        
        Args:
            quantity: Quantity in kg
            variety: Seed variety name
            date_added: Date when added (YYYY-MM-DD)
        """
        super().__init__("Potato Seed", quantity, "kg", date_added)
        self.variety = variety
    
    def to_dict(self) -> Dict:
        """Convert to dictionary including variety."""
        item_dict = super().to_dict()
        item_dict["variety"] = self.variety
        return item_dict

class FarmInventory:
    """Class to manage farm inventory."""
    
    def __init__(self, filename: str = "inventory.json"):
        """
        Initialize farm inventory.
        
        Args:
            filename: JSON file to store inventory data
        """
        self.filename = filename
        self.inventory: List[Dict] = []
        self._load_inventory()
    
    def _load_inventory(self) -> None:
        """Load inventory from JSON file."""
        try:
            with open(self.filename, "r") as f:
                self.inventory = json.load(f)
        except FileNotFoundError:
            self.inventory = []
        except json.JSONDecodeError:
            raise ValueError("Inventory file is corrupted")
    
    def _save_inventory(self) -> None:
        """Save inventory to JSON file."""
        with open(self.filename, "w") as f:
            json.dump(self.inventory, f, indent=2)
    
    def add_item(self, item: InventoryItem) -> None:
        """Add an item to the inventory."""
        self.inventory.append(item.to_dict())
        self._save_inventory()
    
    def remove_item(self, item_name: str, quantity: int) -> bool:
        """
        Remove quantity of an item from inventory.
        
        Args:
            item_name: Name of item to remove
            quantity: Quantity to remove
            
        Returns:
            bool: True if successful, False if item not found or insufficient quantity
        """
        for item in self.inventory:
            if item["name"] == item_name:
                if item["quantity"] >= quantity:
                    item["quantity"] -= quantity
                    self._save_inventory()
                    return True
                return False
        return False
    
    def get_inventory(self) -> List[Dict]:
        """Get current inventory."""
        return self.inventory
    
    def get_item(self, item_name: str) -> Optional[Dict]:
        """Get specific item by name."""
        for item in self.inventory:
            if item["name"] == item_name:
                return item
        return None
    
    def update_item(self, item_name: str, new_quantity: int) -> bool:
        """
        Update quantity of an existing item.
        
        Args:
            item_name: Name of item to update
            new_quantity: New quantity
            
        Returns:
            bool: True if successful, False if item not found
        """
        for item in self.inventory:
            if item["name"] == item_name:
                item["quantity"] = new_quantity
                self._save_inventory()
                return True
        return False

# Example usage
if __name__ == "__main__":
    inventory = FarmInventory()
    
    # Add corn silage bales
    corn_bales = CornSilageBale(quantity=50, bale_weight=500)
    inventory.add_item(corn_bales)
    
    # Add potato seeds
    potato_seeds = PotatoSeed(quantity=200, variety="Russet")
    inventory.add_item(potato_seeds)
    
    # Display inventory
    print("Current Inventory:")
    for item in inventory.get_inventory():
        print(f"{item['name']}: {item['quantity']} {item['unit']}")
```
