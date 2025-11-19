"""
Generated Code Metadata:
========================
Original URL: https://esp-gala-games-app.blogspot.com
Prompt: Write a Python code snippet to catalog sports equipment inventory for a store like Loja dos Esportes, including items like beach volleyball gear and basketball equipment.
Generated: DETERMINISTIC_b28c21fdf5137268
Batch ID: 20250622_204855
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

class SportsEquipment:
    """Class to represent a sports equipment item."""
    
    def __init__(self, name: str, category: str, quantity: int, price: float):
        """
        Initialize a new sports equipment item.

        :param name: Name of the equipment
        :param category: Category of the equipment (e.g., 'Beach Volleyball', 'Basketball')
        :param quantity: Quantity available in inventory
        :param price: Price of the equipment
        """
        self.name = name
        self.category = category
        self.quantity = quantity
        self.price = price

    def to_dict(self) -> Dict[str, Any]:
        """Convert the equipment item to a dictionary."""
        return {
            'name': self.name,
            'category': self.category,
            'quantity': self.quantity,
            'price': self.price
        }

class Inventory:
    """Class to manage the sports equipment inventory."""
    
    def __init__(self):
        """Initialize an empty inventory."""
        self.items: List[SportsEquipment] = []

    def add_item(self, item: SportsEquipment) -> None:
        """Add a new item to the inventory.

        :param item: SportsEquipment object to add
        """
        self.items.append(item)

    def remove_item(self, name: str) -> bool:
        """Remove an item from the inventory by name.

        :param name: Name of the equipment to remove
        :return: True if the item was removed, False if not found
        """
        for item in self.items:
            if item.name == name:
                self.items.remove(item)
                return True
        return False

    def get_inventory(self) -> List[Dict[str, Any]]:
        """Get the current inventory as a list of dictionaries.

        :return: List of equipment items in dictionary format
        """
        return [item.to_dict() for item in self.items]

    def save_to_file(self, filename: str) -> None:
        """Save the inventory to a JSON file.

        :param filename: Name of the file to save the inventory
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.get_inventory(), file, indent=4)
        except IOError as e:
            print(f"Error saving inventory to file: {e}")

    def load_from_file(self, filename: str) -> None:
        """Load inventory from a JSON file.

        :param filename: Name of the file to load the inventory from
        """
        try:
            with open(filename, 'r') as file:
                items = json.load(file)
                for item in items:
                    self.add_item(SportsEquipment(**item))
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading inventory from file: {e}")

# Example usage
if __name__ == "__main__":
    inventory = Inventory()
    
    # Adding items to the inventory
    inventory.add_item(SportsEquipment("Beach Volleyball", "Beach Volleyball", 10, 29.99))
    inventory.add_item(SportsEquipment("Basketball", "Basketball", 15, 19.99))
    
    # Saving inventory to a file
    inventory.save_to_file("inventory.json")
    
    # Loading inventory from a file
    inventory.load_from_file("inventory.json")
    
    # Displaying the current inventory
    print(inventory.get_inventory())
```
