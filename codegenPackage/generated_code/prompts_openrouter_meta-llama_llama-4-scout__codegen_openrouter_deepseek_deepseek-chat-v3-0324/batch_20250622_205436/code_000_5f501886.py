"""
Generated Code Metadata:
========================
Original URL: https://bgmarkazi.com
Prompt: "Write a Python script to manage an e-commerce inventory system for mobile phone accessories, including items like chargers, cables, and phone cases."
Generated: DETERMINISTIC_5f501886ee64b727
Batch ID: 20250622_205436
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
    """Class representing an inventory item."""
    
    def __init__(self, item_id: str, name: str, category: str, price: float, quantity: int):
        """Initialize an inventory item.
        
        Args:
            item_id: Unique identifier for the item
            name: Name of the item
            category: Category of the item (e.g., 'charger', 'cable', 'case')
            price: Price of the item
            quantity: Quantity in stock
        """
        self.item_id = item_id
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity
    
    def to_dict(self) -> Dict:
        """Convert item to dictionary for serialization."""
        return {
            'item_id': self.item_id,
            'name': self.name,
            'category': self.category,
            'price': self.price,
            'quantity': self.quantity
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'InventoryItem':
        """Create item from dictionary."""
        return cls(
            item_id=data['item_id'],
            name=data['name'],
            category=data['category'],
            price=data['price'],
            quantity=data['quantity']
        )

class InventoryManager:
    """Class to manage inventory operations."""
    
    def __init__(self, file_path: str = 'inventory.json'):
        """Initialize inventory manager.
        
        Args:
            file_path: Path to JSON file for storing inventory data
        """
        self.file_path = file_path
        self.inventory: Dict[str, InventoryItem] = {}
        self.load_inventory()
    
    def load_inventory(self) -> None:
        """Load inventory from JSON file."""
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
        """Save inventory to JSON file."""
        try:
            with open(self.file_path, 'w') as file:
                json.dump(
                    {item_id: item.to_dict() for item_id, item in self.inventory.items()},
                    file,
                    indent=4
                )
        except Exception as e:
            print(f"Error saving inventory: {e}")
    
    def add_item(self, item: InventoryItem) -> bool:
        """Add an item to inventory.
        
        Args:
            item: Item to add
            
        Returns:
            True if item was added successfully, False otherwise
        """
        if item.item_id in self.inventory:
            print(f"Item with ID {item.item_id} already exists.")
            return False
        
        self.inventory[item.item_id] = item
        self.save_inventory()
        return True
    
    def update_item(self, item_id: str, **kwargs) -> bool:
        """Update item attributes.
        
        Args:
            item_id: ID of item to update
            **kwargs: Attributes to update (name, category, price, quantity)
            
        Returns:
            True if item was updated successfully, False otherwise
        """
        if item_id not in self.inventory:
            print(f"Item with ID {item_id} not found.")
            return False
        
        item = self.inventory[item_id]
        for key, value in kwargs.items():
            if hasattr(item, key):
                setattr(item, key, value)
        
        self.save_inventory()
        return True
    
    def remove_item(self, item_id: str) -> bool:
        """Remove item from inventory.
        
        Args:
            item_id: ID of item to remove
            
        Returns:
            True if item was removed successfully, False otherwise
        """
        if item_id not in self.inventory:
            print(f"Item with ID {item_id} not found.")
            return False
        
        del self.inventory[item_id]
        self.save_inventory()
        return True
    
    def get_item(self, item_id: str) -> Optional[InventoryItem]:
        """Get item by ID.
        
        Args:
            item_id: ID of item to retrieve
            
        Returns:
            InventoryItem if found, None otherwise
        """
        return self.inventory.get(item_id)
    
    def list_items(self, category: Optional[str] = None) -> List[InventoryItem]:
        """List all items, optionally filtered by category.
        
        Args:
            category: Category to filter by (optional)
            
        Returns:
            List of InventoryItem objects
        """
        if category:
            return [item for item in self.inventory.values() if item.category == category]
        return list(self.inventory.values())
    
    def check_stock(self, item_id: str, quantity: int) -> bool:
        """Check if sufficient stock is available.
        
        Args:
            item_id: ID of item to check
            quantity: Quantity needed
            
        Returns:
            True if sufficient stock is available, False otherwise
        """
        item = self.get_item(item_id)
        if not item:
            print(f"Item with ID {item_id} not found.")
            return False
        return item.quantity >= quantity
    
    def process_sale(self, item_id: str, quantity: int) -> bool:
        """Process a sale by reducing item quantity.
        
        Args:
            item_id: ID of item sold
            quantity: Quantity sold
            
        Returns:
            True if sale was processed successfully, False otherwise
        """
        if not self.check_stock(item_id, quantity):
            return False
        
        item = self.inventory[item_id]
        item.quantity -= quantity
        self.save_inventory()
        return True

def main():
    """Example usage of the inventory system."""
    manager = InventoryManager()
    
    # Add some sample items
    manager.add_item(InventoryItem("001", "USB-C Cable", "cable", 12.99, 50))
    manager.add_item(InventoryItem("002", "Wireless Charger", "charger", 29.99, 30))
    manager.add_item(InventoryItem("003", "iPhone Case", "case", 19.99, 100))
    
    # List all items
    print("All Items:")
    for item in manager.list_items():
        print(f"{item.item_id}: {item.name} - ${item.price} - Qty: {item.quantity}")
    
    # List items in a category
    print("\nCables:")
    for item in manager.list_items("cable"):
        print(f"{item.item_id}: {item.name}")
    
    # Process a sale
    if manager.process_sale("001", 2):
        print("\nSold 2 USB-C Cables")
    
    # Update an item
    manager.update_item("002", price=24.99)
    updated_item = manager.get_item("002")
    print(f"\nUpdated price for {updated_item.name}: ${updated_item.price}")

if __name__ == "__main__":
    main()
```
