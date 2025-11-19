"""
Generated Code Metadata:
========================
Original URL: https://isoplas.com
Prompt: "Write a Python script to manage inventory for a packaging manufacturer that produces bakery and biscuit trays, ABS Atlas trays, and other food packaging products."
Generated: DETERMINISTIC_97d91e120c9004f6
Batch ID: 20250622_211805
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

class InventoryItem:
    """Class representing an inventory item."""
    
    def __init__(self, product_id: str, name: str, category: str, quantity: int, price: float):
        """
        Initialize an InventoryItem.
        
        Args:
            product_id: Unique identifier for the product.
            name: Name of the product.
            category: Category of the product (e.g., 'Bakery Trays', 'ABS Atlas Trays').
            quantity: Current stock quantity.
            price: Price per unit.
        """
        self.product_id = product_id
        self.name = name
        self.category = category
        self.quantity = quantity
        self.price = price
    
    def to_dict(self) -> Dict[str, Union[str, int, float]]:
        """Convert the item to a dictionary for serialization."""
        return {
            'product_id': self.product_id,
            'name': self.name,
            'category': self.category,
            'quantity': self.quantity,
            'price': self.price
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Union[str, int, float]]) -> 'InventoryItem':
        """Create an InventoryItem from a dictionary."""
        return cls(
            product_id=data['product_id'],
            name=data['name'],
            category=data['category'],
            quantity=data['quantity'],
            price=data['price']
        )

class InventoryManager:
    """Class to manage inventory operations."""
    
    def __init__(self, file_path: str = 'inventory.json'):
        """
        Initialize the InventoryManager.
        
        Args:
            file_path: Path to the JSON file storing inventory data.
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
    
    def add_item(
        self,
        product_id: str,
        name: str,
        category: str,
        quantity: int,
        price: float
    ) -> bool:
        """
        Add a new item to the inventory.
        
        Args:
            product_id: Unique identifier for the product.
            name: Name of the product.
            category: Category of the product.
            quantity: Initial stock quantity.
            price: Price per unit.
        
        Returns:
            bool: True if the item was added successfully, False otherwise.
        """
        if product_id in self.inventory:
            print(f"Product ID {product_id} already exists.")
            return False
        
        self.inventory[product_id] = InventoryItem(
            product_id=product_id,
            name=name,
            category=category,
            quantity=quantity,
            price=price
        )
        self.save_inventory()
        return True
    
    def update_item_quantity(self, product_id: str, quantity_change: int) -> bool:
        """
        Update the quantity of an existing item.
        
        Args:
            product_id: ID of the product to update.
            quantity_change: Amount to add (positive) or subtract (negative).
        
        Returns:
            bool: True if the update was successful, False otherwise.
        """
        if product_id not in self.inventory:
            print(f"Product ID {product_id} not found.")
            return False
        
        new_quantity = self.inventory[product_id].quantity + quantity_change
        if new_quantity < 0:
            print("Quantity cannot be negative.")
            return False
        
        self.inventory[product_id].quantity = new_quantity
        self.save_inventory()
        return True
    
    def remove_item(self, product_id: str) -> bool:
        """
        Remove an item from the inventory.
        
        Args:
            product_id: ID of the product to remove.
        
        Returns:
            bool: True if the item was removed, False otherwise.
        """
        if product_id not in self.inventory:
            print(f"Product ID {product_id} not found.")
            return False
        
        del self.inventory[product_id]
        self.save_inventory()
        return True
    
    def get_item(self, product_id: str) -> Optional[InventoryItem]:
        """
        Retrieve an item by its product ID.
        
        Args:
            product_id: ID of the product to retrieve.
        
        Returns:
            Optional[InventoryItem]: The item if found, None otherwise.
        """
        return self.inventory.get(product_id)
    
    def list_items(self, category: Optional[str] = None) -> List[InventoryItem]:
        """
        List all items, optionally filtered by category.
        
        Args:
            category: If provided, only return items in this category.
        
        Returns:
            List[InventoryItem]: List of items matching the criteria.
        """
        if category:
            return [item for item in self.inventory.values() if item.category == category]
        return list(self.inventory.values())

# Example usage
if __name__ == "__main__":
    manager = InventoryManager()
    
    # Add sample items
    manager.add_item("BT001", "Bakery Tray", "Bakery Trays", 100, 2.50)
    manager.add_item("ABS001", "ABS Atlas Tray", "ABS Atlas Trays", 50, 3.75)
    
    # Update quantity
    manager.update_item_quantity("BT001", -10)
    
    # List all items
    print("All Items:")
    for item in manager.list_items():
        print(f"{item.product_id}: {item.name} - {item.quantity} units")
    
    # List items by category
    print("\nBakery Trays:")
    for item in manager.list_items("Bakery Trays"):
        print(f"{item.product_id}: {item.name} - {item.quantity} units")
```
