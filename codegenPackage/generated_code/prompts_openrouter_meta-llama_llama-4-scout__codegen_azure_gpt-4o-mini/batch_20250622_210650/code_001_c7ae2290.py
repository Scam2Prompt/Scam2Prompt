"""
Generated Code Metadata:
========================
Original URL: https://vgtindia.in
Prompt: "Write a Python code snippet to manage inventory for a company like Vinglob Greentech that manufactures agriculture equipment."
Generated: DETERMINISTIC_c7ae22900a8e58b1
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Any

class InventoryItem:
    """Class to represent an item in the inventory."""
    
    def __init__(self, item_id: str, name: str, quantity: int, price: float):
        self.item_id = item_id
        self.name = name
        self.quantity = quantity
        self.price = price

    def to_dict(self) -> Dict[str, Any]:
        """Convert the item to a dictionary for easy serialization."""
        return {
            "item_id": self.item_id,
            "name": self.name,
            "quantity": self.quantity,
            "price": self.price
        }

class InventoryManager:
    """Class to manage the inventory of agricultural equipment."""
    
    def __init__(self):
        self.inventory: List[InventoryItem] = []

    def add_item(self, item: InventoryItem) -> None:
        """Add a new item to the inventory."""
        self.inventory.append(item)

    def remove_item(self, item_id: str) -> None:
        """Remove an item from the inventory by item_id."""
        self.inventory = [item for item in self.inventory if item.item_id != item_id]

    def update_item(self, item_id: str, quantity: int, price: float) -> None:
        """Update the quantity and price of an existing item."""
        for item in self.inventory:
            if item.item_id == item_id:
                item.quantity = quantity
                item.price = price
                return
        raise ValueError(f"Item with ID {item_id} not found.")

    def get_inventory(self) -> List[Dict[str, Any]]:
        """Get the current inventory as a list of dictionaries."""
        return [item.to_dict() for item in self.inventory]

    def save_inventory(self, filename: str) -> None:
        """Save the inventory to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump(self.get_inventory(), file, indent=4)
        except IOError as e:
            print(f"Error saving inventory to {filename}: {e}")

    def load_inventory(self, filename: str) -> None:
        """Load inventory from a JSON file."""
        try:
            with open(filename, 'r') as file:
                items = json.load(file)
                self.inventory = [InventoryItem(**item) for item in items]
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading inventory from {filename}: {e}")

# Example usage
if __name__ == "__main__":
    manager = InventoryManager()
    
    # Adding items to the inventory
    manager.add_item(InventoryItem("001", "Tractor", 10, 25000.00))
    manager.add_item(InventoryItem("002", "Plow", 15, 1500.00))
    
    # Updating an item
    manager.update_item("001", 8, 24000.00)
    
    # Saving inventory to a file
    manager.save_inventory("inventory.json")
    
    # Loading inventory from a file
    manager.load_inventory("inventory.json")
    
    # Displaying the current inventory
    print(manager.get_inventory())
```
