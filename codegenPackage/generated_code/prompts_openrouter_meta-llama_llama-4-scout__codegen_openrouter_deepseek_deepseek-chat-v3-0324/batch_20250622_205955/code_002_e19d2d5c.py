"""
Generated Code Metadata:
========================
Original URL: https://karmadolap.com
Prompt: "Write a Python script to manage inventory for a workshop that uses Karma Dolap's products, including workbenches, tool carts, and storage units."
Generated: DETERMINISTIC_e19d2d5c5d94deb5
Batch ID: 20250622_205955
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
    """Represents an inventory item with its properties."""
    
    def __init__(self, item_id: str, name: str, category: str, quantity: int, price: float):
        """Initialize an inventory item.
        
        Args:
            item_id: Unique identifier for the item
            name: Name of the item
            category: Category of the item (e.g., 'workbench', 'tool cart')
            quantity: Current stock quantity
            price: Unit price of the item
        """
        self.item_id = item_id
        self.name = name
        self.category = category
        self.quantity = quantity
        self.price = price
    
    def to_dict(self) -> Dict:
        """Convert the item to a dictionary for serialization."""
        return {
            'item_id': self.item_id,
            'name': self.name,
            'category': self.category,
            'quantity': self.quantity,
            'price': self.price
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'InventoryItem':
        """Create an InventoryItem from a dictionary."""
        return cls(
            item_id=data['item_id'],
            name=data['name'],
            category=data['category'],
            quantity=data['quantity'],
            price=data['price']
        )

class InventoryManager:
    """Manages inventory operations for Karma Dolap products."""
    
    def __init__(self, file_path: str = 'inventory.json'):
        """Initialize the inventory manager.
        
        Args:
            file_path: Path to the JSON file storing inventory data
        """
        self.file_path = file_path
        self.inventory: Dict[str, InventoryItem] = {}
        self.load_inventory()
    
    def load_inventory(self) -> None:
        """Load inventory data from the JSON file."""
        try:
            if os.path.exists(self.file_path):
                with open(self.file_path, 'r') as file:
                    data = json.load(file)
                    self.inventory = {
                        item_id: InventoryItem.from_dict(item_data)
                        for item_id, item_data in data.items()
                    }
        except Exception as e:
            print(f"Error loading inventory: {e}")
            self.inventory = {}
    
    def save_inventory(self) -> None:
        """Save inventory data to the JSON file."""
        try:
            with open(self.file_path, 'w') as file:
                json.dump(
                    {item_id: item.to_dict() for item_id, item in self.inventory.items()},
                    file,
                    indent=4
                )
        except Exception as e:
            print(f"Error saving inventory: {e}")
    
    def add_item(self, item_id: str, name: str, category: str, quantity: int, price: float) -> bool:
        """Add a new item to the inventory.
        
        Args:
            item_id: Unique identifier for the item
            name: Name of the item
            category: Category of the item
            quantity: Initial stock quantity
            price: Unit price of the item
            
        Returns:
            True if item was added successfully, False otherwise
        """
        if item_id in self.inventory:
            print(f"Item with ID {item_id} already exists.")
            return False
        
        self.inventory[item_id] = InventoryItem(item_id, name, category, quantity, price)
        self.save_inventory()
        return True
    
    def update_item_quantity(self, item_id: str, quantity_change: int) -> bool:
        """Update the quantity of an existing item.
        
        Args:
            item_id: ID of the item to update
            quantity_change: Amount to add/subtract from current quantity
            
        Returns:
            True if update was successful, False otherwise
        """
        if item_id not in self.inventory:
            print(f"Item with ID {item_id} not found.")
            return False
        
        new_quantity = self.inventory[item_id].quantity + quantity_change
        if new_quantity < 0:
            print("Cannot have negative quantity.")
            return False
        
        self.inventory[item_id].quantity = new_quantity
        self.save_inventory()
        return True
    
    def remove_item(self, item_id: str) -> bool:
        """Remove an item from the inventory.
        
        Args:
            item_id: ID of the item to remove
            
        Returns:
            True if removal was successful, False otherwise
        """
        if item_id not in self.inventory:
            print(f"Item with ID {item_id} not found.")
            return False
        
        del self.inventory[item_id]
        self.save_inventory()
        return True
    
    def get_item(self, item_id: str) -> Optional[InventoryItem]:
        """Get an item by its ID.
        
        Args:
            item_id: ID of the item to retrieve
            
        Returns:
            The InventoryItem if found, None otherwise
        """
        return self.inventory.get(item_id)
    
    def list_items(self, category: Optional[str] = None) -> List[InventoryItem]:
        """List all items, optionally filtered by category.
        
        Args:
            category: If specified, only return items of this category
            
        Returns:
            List of InventoryItem objects
        """
        if category:
            return [item for item in self.inventory.values() if item.category == category]
        return list(self.inventory.values())
    
    def get_inventory_value(self) -> float:
        """Calculate the total value of all items in inventory.
        
        Returns:
            Total inventory value
        """
        return sum(item.quantity * item.price for item in self.inventory.values())

def main():
    """Demonstrate the inventory management system."""
    manager = InventoryManager()
    
    # Example operations
    manager.add_item("WB-001", "Professional Workbench", "workbench", 5, 499.99)
    manager.add_item("TC-001", "Mobile Tool Cart", "tool cart", 10, 199.99)
    manager.add_item("SU-001", "Steel Storage Unit", "storage unit", 7, 349.99)
    
    manager.update_item_quantity("WB-001", -2)  # Sell 2 workbenches
    manager.update_item_quantity("TC-001", 3)   # Add 3 tool carts
    
    print("Current Inventory:")
    for item in manager.list_items():
        print(f"{item.item_id}: {item.name} ({item.category}) - Qty: {item.quantity}, Price: ${item.price:.2f}")
    
    print(f"\nTotal Inventory Value: ${manager.get_inventory_value():.2f}")

if __name__ == "__main__":
    main()
```
