"""
Generated Code Metadata:
========================
Original URL: https://odasloucabrazzz.blogspot.com
Prompt: Write a Python script to manage inventory for a kitchen utensil store like Varejão das Louças in Pedreira-SP.
Generated: DETERMINISTIC_9bbee8b51ca2588f
Batch ID: 20250622_212122
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
    """Represents an item in the inventory."""
    
    def __init__(self, name: str, quantity: int, price: float, category: str):
        """
        Initialize an inventory item.
        
        Args:
            name: Name of the item.
            quantity: Quantity in stock.
            price: Price per unit.
            category: Category of the item (e.g., 'cutlery', 'cookware').
        """
        self.name = name
        self.quantity = quantity
        self.price = price
        self.category = category
    
    def to_dict(self) -> Dict:
        """Convert the item to a dictionary for serialization."""
        return {
            'name': self.name,
            'quantity': self.quantity,
            'price': self.price,
            'category': self.category
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'InventoryItem':
        """Create an InventoryItem from a dictionary."""
        return cls(
            name=data['name'],
            quantity=data['quantity'],
            price=data['price'],
            category=data['category']
        )

class InventoryManager:
    """Manages the inventory of kitchen utensils."""
    
    def __init__(self, file_path: str = 'inventory.json'):
        """
        Initialize the inventory manager.
        
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
                        item['name']: InventoryItem.from_dict(item)
                        for item in data
                    }
        except Exception as e:
            print(f"Error loading inventory: {e}")
            self.inventory = {}
    
    def save_inventory(self) -> None:
        """Save inventory data to the JSON file."""
        try:
            with open(self.file_path, 'w') as file:
                json.dump(
                    [item.to_dict() for item in self.inventory.values()],
                    file,
                    indent=2
                )
        except Exception as e:
            print(f"Error saving inventory: {e}")
    
    def add_item(self, name: str, quantity: int, price: float, category: str) -> None:
        """
        Add a new item to the inventory.
        
        Args:
            name: Name of the item.
            quantity: Quantity to add.
            price: Price per unit.
            category: Category of the item.
        """
        if name in self.inventory:
            print(f"Item '{name}' already exists. Use update_item to modify.")
            return
        self.inventory[name] = InventoryItem(name, quantity, price, category)
        self.save_inventory()
    
    def update_item(self, name: str, quantity: Optional[int] = None, 
                    price: Optional[float] = None, category: Optional[str] = None) -> None:
        """
        Update an existing item in the inventory.
        
        Args:
            name: Name of the item to update.
            quantity: New quantity (optional).
            price: New price (optional).
            category: New category (optional).
        """
        if name not in self.inventory:
            print(f"Item '{name}' not found.")
            return
        
        item = self.inventory[name]
        if quantity is not None:
            item.quantity = quantity
        if price is not None:
            item.price = price
        if category is not None:
            item.category = category
        
        self.save_inventory()
    
    def remove_item(self, name: str) -> None:
        """
        Remove an item from the inventory.
        
        Args:
            name: Name of the item to remove.
        """
        if name not in self.inventory:
            print(f"Item '{name}' not found.")
            return
        
        del self.inventory[name]
        self.save_inventory()
    
    def list_items(self) -> List[Dict]:
        """List all items in the inventory."""
        return [item.to_dict() for item in self.inventory.values()]
    
    def search_items(self, name: Optional[str] = None, 
                     category: Optional[str] = None) -> List[Dict]:
        """
        Search for items by name or category.
        
        Args:
            name: Name to search for (optional).
            category: Category to search for (optional).
        
        Returns:
            List of matching items.
        """
        results = []
        for item in self.inventory.values():
            if (name and name.lower() in item.name.lower()) or \
               (category and category.lower() == item.category.lower()):
                results.append(item.to_dict())
        return results

def main():
    """Example usage of the InventoryManager."""
    manager = InventoryManager()
    
    # Add some items
    manager.add_item("Wooden Spoon", 50, 12.99, "utensils")
    manager.add_item("Non-stick Pan", 30, 45.50, "cookware")
    manager.add_item("Chef's Knife", 20, 29.99, "cutlery")
    
    # Update an item
    manager.update_item("Wooden Spoon", quantity=45)
    
    # List all items
    print("Inventory Items:")
    for item in manager.list_items():
        print(item)
    
    # Search items by category
    print("\nCookware Items:")
    for item in manager.search_items(category="cookware"):
        print(item)

if __name__ == "__main__":
    main()
```
