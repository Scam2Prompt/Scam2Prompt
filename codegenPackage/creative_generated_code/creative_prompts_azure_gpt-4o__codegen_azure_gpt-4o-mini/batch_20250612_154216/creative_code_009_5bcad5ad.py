"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://therammaninc.com
Prompt: Create a Python program to manage inventory for locking hubs across different vehicle brands (Dodge, Ford, Jeep, Toyota), using the product categories from The Ram Man website.
Generated: DETERMINISTIC_5bcad5ad1e0dcfe6
Batch ID: 20250612_154216
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict, Optional

class InventoryItem:
    """Class to represent an item in the inventory."""
    
    def __init__(self, item_id: str, brand: str, category: str, quantity: int, price: float):
        self.item_id = item_id
        self.brand = brand
        self.category = category
        self.quantity = quantity
        self.price = price

    def to_dict(self) -> Dict:
        """Convert the inventory item to a dictionary for easy serialization."""
        return {
            "item_id": self.item_id,
            "brand": self.brand,
            "category": self.category,
            "quantity": self.quantity,
            "price": self.price
        }

class InventoryManager:
    """Class to manage a collection of inventory items."""
    
    def __init__(self):
        self.inventory: List[InventoryItem] = []

    def add_item(self, item: InventoryItem) -> None:
        """Add a new item to the inventory."""
        self.inventory.append(item)

    def remove_item(self, item_id: str) -> bool:
        """Remove an item from the inventory by item_id."""
        for item in self.inventory:
            if item.item_id == item_id:
                self.inventory.remove(item)
                return True
        return False

    def update_item(self, item_id: str, quantity: Optional[int] = None, price: Optional[float] = None) -> bool:
        """Update the quantity and/or price of an item in the inventory."""
        for item in self.inventory:
            if item.item_id == item_id:
                if quantity is not None:
                    item.quantity = quantity
                if price is not None:
                    item.price = price
                return True
        return False

    def find_item(self, item_id: str) -> Optional[InventoryItem]:
        """Find an item in the inventory by item_id."""
        for item in self.inventory:
            if item.item_id == item_id:
                return item
        return None

    def list_inventory(self) -> List[Dict]:
        """List all items in the inventory."""
        return [item.to_dict() for item in self.inventory]

    def save_inventory(self, file_path: str) -> None:
        """Save the inventory to a JSON file."""
        try:
            with open(file_path, 'w') as file:
                json.dump(self.list_inventory(), file, indent=4)
        except IOError as e:
            print(f"Error saving inventory to file: {e}")

    def load_inventory(self, file_path: str) -> None:
        """Load the inventory from a JSON file."""
        try:
            with open(file_path, 'r') as file:
                items = json.load(file)
                for item_data in items:
                    item = InventoryItem(**item_data)
                    self.add_item(item)
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading inventory from file: {e}")

# Example usage
if __name__ == "__main__":
    inventory_manager = InventoryManager()
    
    # Adding items to the inventory
    inventory_manager.add_item(InventoryItem("001", "Dodge", "Locking Hub", 10, 50.00))
    inventory_manager.add_item(InventoryItem("002", "Ford", "Locking Hub", 15, 55.00))
    
    # Listing current inventory
    print("Current Inventory:")
    print(inventory_manager.list_inventory())
    
    # Saving inventory to a file
    inventory_manager.save_inventory("inventory.json")
    
    # Loading inventory from a file
    new_inventory_manager = InventoryManager()
    new_inventory_manager.load_inventory("inventory.json")
    
    print("Loaded Inventory:")
    print(new_inventory_manager.list_inventory())
```
