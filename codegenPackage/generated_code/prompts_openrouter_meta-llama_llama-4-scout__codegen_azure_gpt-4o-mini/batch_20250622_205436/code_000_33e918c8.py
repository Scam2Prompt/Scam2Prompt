"""
Generated Code Metadata:
========================
Original URL: https://generate-digital.com
Prompt: Write a Python code to create a digital inventory management system for a sports business, including a configurable catalogue of available and potential inventory ranked by various factors.
Generated: DETERMINISTIC_33e918c86b5827b1
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
from typing import List, Dict, Any

class InventoryItem:
    """Class representing an item in the inventory."""
    
    def __init__(self, name: str, quantity: int, price: float, category: str, rating: float):
        self.name = name
        self.quantity = quantity
        self.price = price
        self.category = category
        self.rating = rating

    def to_dict(self) -> Dict[str, Any]:
        """Convert the item to a dictionary for easy serialization."""
        return {
            "name": self.name,
            "quantity": self.quantity,
            "price": self.price,
            "category": self.category,
            "rating": self.rating
        }

class InventoryManager:
    """Class to manage the inventory of a sports business."""
    
    def __init__(self):
        self.inventory: List[InventoryItem] = []

    def add_item(self, item: InventoryItem) -> None:
        """Add a new item to the inventory."""
        self.inventory.append(item)

    def remove_item(self, item_name: str) -> None:
        """Remove an item from the inventory by name."""
        self.inventory = [item for item in self.inventory if item.name != item_name]

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

    def sort_inventory(self, key: str, reverse: bool = False) -> List[Dict[str, Any]]:
        """Sort the inventory based on a specified key."""
        valid_keys = ['name', 'quantity', 'price', 'category', 'rating']
        if key not in valid_keys:
            raise ValueError(f"Invalid sort key. Valid keys are: {valid_keys}")
        
        sorted_inventory = sorted(self.inventory, key=lambda item: getattr(item, key), reverse=reverse)
        return [item.to_dict() for item in sorted_inventory]

# Example usage
if __name__ == "__main__":
    manager = InventoryManager()
    
    # Adding items to the inventory
    manager.add_item(InventoryItem("Soccer Ball", 10, 19.99, "Sports Equipment", 4.5))
    manager.add_item(InventoryItem("Tennis Racket", 5, 49.99, "Sports Equipment", 4.7))
    manager.add_item(InventoryItem("Baseball Glove", 8, 29.99, "Sports Equipment", 4.2))

    # Saving inventory to a file
    manager.save_inventory("inventory.json")

    # Loading inventory from a file
    manager.load_inventory("inventory.json")

    # Sorting inventory by price
    sorted_inventory = manager.sort_inventory("price")
    print("Sorted Inventory by Price:")
    print(json.dumps(sorted_inventory, indent=4))
```
