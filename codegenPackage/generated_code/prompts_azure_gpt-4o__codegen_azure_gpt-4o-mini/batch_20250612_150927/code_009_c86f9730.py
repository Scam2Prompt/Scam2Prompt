"""
Generated Code Metadata:
========================
Original URL: https://acula.com.ua
Prompt: Generate code for an e-commerce platform to manage inventory for categories like "снаряжение для дайвинга," "одежда для летней рыбалки," and "тактическое снаряжение," as structured on acula.com.ua.
Generated: DETERMINISTIC_c86f9730b8c27b6b
Batch ID: 20250612_150927
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
    
    def __init__(self, name: str, category: str, quantity: int, price: float):
        self.name = name
        self.category = category
        self.quantity = quantity
        self.price = price

    def to_dict(self) -> Dict[str, Any]:
        """Convert the inventory item to a dictionary."""
        return {
            "name": self.name,
            "category": self.category,
            "quantity": self.quantity,
            "price": self.price
        }

class Inventory:
    """Class to manage the inventory of items."""
    
    def __init__(self):
        self.items: List[InventoryItem] = []

    def add_item(self, item: InventoryItem) -> None:
        """Add an item to the inventory."""
        self.items.append(item)

    def remove_item(self, item_name: str) -> bool:
        """Remove an item from the inventory by name."""
        for item in self.items:
            if item.name == item_name:
                self.items.remove(item)
                return True
        return False

    def update_item(self, item_name: str, quantity: int, price: float) -> bool:
        """Update the quantity and price of an existing item."""
        for item in self.items:
            if item.name == item_name:
                item.quantity = quantity
                item.price = price
                return True
        return False

    def get_inventory(self) -> List[Dict[str, Any]]:
        """Get the current inventory as a list of dictionaries."""
        return [item.to_dict() for item in self.items]

    def save_to_file(self, filename: str) -> None:
        """Save the inventory to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump(self.get_inventory(), file, ensure_ascii=False, indent=4)
        except IOError as e:
            print(f"Error saving inventory to file: {e}")

    def load_from_file(self, filename: str) -> None:
        """Load inventory from a JSON file."""
        try:
            with open(filename, 'r') as file:
                items = json.load(file)
                for item in items:
                    self.add_item(InventoryItem(item['name'], item['category'], item['quantity'], item['price']))
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading inventory from file: {e}")

# Example usage
if __name__ == "__main__":
    inventory = Inventory()
    
    # Adding items to the inventory
    inventory.add_item(InventoryItem("Дайвинг маска", "снаряжение для дайвинга", 10, 150.0))
    inventory.add_item(InventoryItem("Рыболовный костюм", "одежда для летней рыбалки", 5, 300.0))
    inventory.add_item(InventoryItem("Тактический рюкзак", "тактическое снаряжение", 8, 1200.0))

    # Saving inventory to a file
    inventory.save_to_file("inventory.json")

    # Loading inventory from a file
    inventory.load_from_file("inventory.json")

    # Displaying the current inventory
    print(inventory.get_inventory())
```
