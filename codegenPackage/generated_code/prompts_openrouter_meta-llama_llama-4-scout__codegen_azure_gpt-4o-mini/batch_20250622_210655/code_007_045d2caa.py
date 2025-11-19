"""
Generated Code Metadata:
========================
Original URL: https://stockyardrefacing.com
Prompt: "Create an inventory management system for tracking materials used in cabinet refacing projects, such as veneers, finishes, and hardware, based on the services offered by Stockyard Refacing."
Generated: DETERMINISTIC_045d2caa86fe0e85
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Optional

class InventoryItem:
    """Class to represent an inventory item."""
    
    def __init__(self, name: str, quantity: int, unit: str):
        """
        Initialize an inventory item.

        :param name: Name of the inventory item
        :param quantity: Quantity of the item in stock
        :param unit: Unit of measurement for the item (e.g., 'pieces', 'liters')
        """
        self.name = name
        self.quantity = quantity
        self.unit = unit

    def __repr__(self):
        return f"{self.name} ({self.quantity} {self.unit})"


class Inventory:
    """Class to manage the inventory of materials."""
    
    def __init__(self):
        """Initialize the inventory with an empty list of items."""
        self.items: List[InventoryItem] = []

    def add_item(self, item: InventoryItem):
        """
        Add an item to the inventory.

        :param item: InventoryItem to be added
        """
        self.items.append(item)
        print(f"Added {item} to inventory.")

    def remove_item(self, name: str, quantity: int):
        """
        Remove a specified quantity of an item from the inventory.

        :param name: Name of the item to remove
        :param quantity: Quantity to remove
        :raises ValueError: If the item is not found or insufficient quantity
        """
        for item in self.items:
            if item.name == name:
                if item.quantity >= quantity:
                    item.quantity -= quantity
                    print(f"Removed {quantity} {item.unit} of {name} from inventory.")
                    if item.quantity == 0:
                        self.items.remove(item)
                        print(f"{name} is now out of stock and removed from inventory.")
                    return
                else:
                    raise ValueError(f"Insufficient quantity of {name} in inventory.")
        raise ValueError(f"Item {name} not found in inventory.")

    def get_inventory(self) -> List[Dict[str, str]]:
        """
        Get a list of all items in the inventory.

        :return: List of dictionaries representing inventory items
        """
        return [{"name": item.name, "quantity": item.quantity, "unit": item.unit} for item in self.items]

    def save_inventory(self, filename: str):
        """
        Save the current inventory to a JSON file.

        :param filename: Name of the file to save the inventory
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.get_inventory(), file, indent=4)
            print(f"Inventory saved to {filename}.")
        except IOError as e:
            print(f"Error saving inventory: {e}")

    def load_inventory(self, filename: str):
        """
        Load inventory from a JSON file.

        :param filename: Name of the file to load the inventory from
        :raises FileNotFoundError: If the file does not exist
        :raises ValueError: If the file content is invalid
        """
        try:
            with open(filename, 'r') as file:
                items = json.load(file)
                for item in items:
                    self.add_item(InventoryItem(item['name'], item['quantity'], item['unit']))
            print(f"Inventory loaded from {filename}.")
        except FileNotFoundError:
            print(f"Error: The file {filename} was not found.")
        except json.JSONDecodeError:
            print("Error: The file content is not valid JSON.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


# Example usage
if __name__ == "__main__":
    inventory = Inventory()
    
    # Adding items to the inventory
    inventory.add_item(InventoryItem("Veneer", 50, "sheets"))
    inventory.add_item(InventoryItem("Finish", 20, "liters"))
    inventory.add_item(InventoryItem("Hardware", 100, "pieces"))

    # Display current inventory
    print("Current Inventory:", inventory.get_inventory())

    # Remove some items
    try:
        inventory.remove_item("Veneer", 10)
    except ValueError as e:
        print(e)

    # Save inventory to a file
    inventory.save_inventory("inventory.json")

    # Load inventory from a file
    inventory.load_inventory("inventory.json")
```
