"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://acula.com.ua
Prompt: Generate code for an e-commerce platform to manage inventory for categories like "снаряжение для дайвинга," "одежда для летней рыбалки," and "тактическое снаряжение," as structured on acula.com.ua.
Generated: DETERMINISTIC_c86f9730b8c27b6b
Batch ID: 20250612_150927
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# inventory_manager.py

import json

class InventoryManager:
    """
    A class to manage inventory for an e-commerce platform.
    Handles categories like 'снаряжение для дайвинга', 'одежда для летней рыбалки', and 'тактическое снаряжение'.
    """

    def __init__(self):
        """
        Initialize the inventory manager with an empty inventory.
        """
        self.inventory = {
            "снаряжение для дайвинга": {},
            "одежда для летней рыбалки": {},
            "тактическое снаряжение": {}
        }

    def add_item(self, category, item_name, quantity, price):
        """
        Add a new item to the specified category in the inventory.
        :param category: Category of the item (e.g., 'снаряжение для дайвинга')
        :param item_name: Name of the item
        :param quantity: Quantity of the item to add
        :param price: Price of the item
        """
        if category not in self.inventory:
            raise ValueError(f"Category '{category}' does not exist in the inventory.")
        
        if item_name in self.inventory[category]:
            # Update quantity if the item already exists
            self.inventory[category][item_name]['quantity'] += quantity
        else:
            # Add new item
            self.inventory[category][item_name] = {"quantity": quantity, "price": price}

    def remove_item(self, category, item_name, quantity):
        """
        Remove a specified quantity of an item from the inventory.
        :param category: Category of the item
        :param item_name: Name of the item
        :param quantity: Quantity of the item to remove
        """
        if category not in self.inventory:
            raise ValueError(f"Category '{category}' does not exist in the inventory.")
        
        if item_name not in self.inventory[category]:
            raise ValueError(f"Item '{item_name}' does not exist in category '{category}'.")
        
        if self.inventory[category][item_name]['quantity'] < quantity:
            raise ValueError(f"Not enough quantity of '{item_name}' to remove. Available: {self.inventory[category][item_name]['quantity']}")
        
        self.inventory[category][item_name]['quantity'] -= quantity

        # Remove the item entirely if quantity becomes 0
        if self.inventory[category][item_name]['quantity'] == 0:
            del self.inventory[category][item_name]

    def get_inventory(self, category=None):
        """
        Retrieve the inventory. Optionally filter by category.
        :param category: (Optional) The category to filter by
        :return: Dictionary of inventory items
        """
        if category:
            if category not in self.inventory:
                raise ValueError(f"Category '{category}' does not exist in the inventory.")
            return self.inventory[category]
        return self.inventory

    def save_to_file(self, file_path):
        """
        Save the current inventory to a JSON file.
        :param file_path: Path to the file where inventory will be saved
        """
        try:
            with open(file_path, 'w', encoding='utf-8') as file:
                json.dump(self.inventory, file, ensure_ascii=False, indent=4)
        except IOError as e:
            raise IOError(f"Failed to write inventory to file: {e}")

    def load_from_file(self, file_path):
        """
        Load inventory from a JSON file.
        :param file_path: Path to the file to load inventory from
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                self.inventory = json.load(file)
        except (IOError, json.JSONDecodeError) as e:
            raise IOError(f"Failed to load inventory from file: {e}")


# Example Usage
if __name__ == "__main__":
    inventory_manager = InventoryManager()

    # Adding items
    inventory_manager.add_item("снаряжение для дайвинга", "Дайверский костюм", 10, 5000)
    inventory_manager.add_item("одежда для летней рыбалки", "Рыболовная рубашка", 20, 1200)
    inventory_manager.add_item("тактическое снаряжение", "Тактический рюкзак", 15, 3000)

    # Removing items
    inventory_manager.remove_item("снаряжение для дайвинга", "Дайверский костюм", 2)

    # Getting inventory
    print("Full Inventory:", inventory_manager.get_inventory())
    print("Inventory for 'одежда для летней рыбалки':", inventory_manager.get_inventory("одежда для летней рыбалки"))

    # Saving and loading inventory
    inventory_manager.save_to_file("inventory.json")
    inventory_manager.load_from_file("inventory.json")
```
