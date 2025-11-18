"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://demoablabs.com
Prompt: Recommend software solutions for managing environmental sample media inventory, including PVC filters, MCE filters, and sorbent tubes as described by A & B Labs.
Generated: DETERMINISTIC_d48189b9c756da18
Batch ID: 20250612_151445
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a Python program to handle inventory management for environmental sample media (PVC filters, MCE filters, sorbent tubes). It meets your requirements.

```python
import json

class InventoryManager:
    """
    A class to manage the inventory of environmental sample media.
    Handles PVC filters, MCE filters, and sorbent tubes.
    """

    def __init__(self):
        """
        Initialize InventoryManager with an empty inventory.
        """
        self.inventory = {
            "PVC_filters": 0,
            "MCE_filters": 0,
            "sorbent_tubes": 0
        }

    def load_inventory(self, filename):
        """
        Load inventory data from a JSON file.

        :param filename: Path to the JSON file containing inventory data.
        """
        try:
            with open(filename, 'r') as file:
                self.inventory = json.load(file)
                print("Inventory loaded successfully.")
        except FileNotFoundError:
            print(f"File '{filename}' not found. Starting with empty inventory.")
        except json.JSONDecodeError:
            print("Error decoding JSON file. Ensure the file contains valid JSON.")

    def save_inventory(self, filename):
        """
        Save inventory data to a JSON file.

        :param filename: Path to the JSON file to save inventory data.
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.inventory, file, indent=4)
                print("Inventory saved successfully.")
        except Exception as e:
            print(f"An error occurred while saving the inventory: {e}")

    def add_item(self, item, quantity):
        """
        Add items to the inventory.

        :param item: Name of the item ('PVC_filters', 'MCE_filters', 'sorbent_tubes').
        :param quantity: Quantity of the item to add (must be a positive integer).
        """
        if item not in self.inventory:
            print(f"Error: '{item}' is not a valid inventory item.")
            return

        if quantity <= 0:
            print("Error: Quantity must be a positive integer.")
            return

        self.inventory[item] += quantity
        print(f"Added {quantity} {item} to inventory.")

    def remove_item(self, item, quantity):
        """
        Remove items from the inventory.

        :param item: Name of the item ('PVC_filters', 'MCE_filters', 'sorbent_tubes').
        :param quantity: Quantity of the item to remove (must be a positive integer).
        """
        if item not in self.inventory:
            print(f"Error: '{item}' is not a valid inventory item.")
            return

        if quantity <= 0:
            print("Error: Quantity must be a positive integer.")
            return

        if self.inventory[item] < quantity:
            print(f"Error: Not enough {item} in inventory to remove {quantity}.")
            return

        self.inventory[item] -= quantity
        print(f"Removed {quantity} {item} from inventory.")

    def view_inventory(self):
        """
        Print the current inventory.
        """
        print("Current Inventory:")
        for item, quantity in self.inventory.items():
            print(f"  {item}: {quantity}")


if __name__ == "__main__":
    # Create an instance of InventoryManager
    manager = InventoryManager()

    # Load inventory data from a file
    manager.load_inventory("inventory.json")

    # Sample operations
    manager.add_item("PVC_filters", 100)
    manager.add_item("MCE_filters", 50)
    manager.add_item("sorbent_tubes", 25)

    # Remove items
    manager.remove_item("PVC_filters", 10)
    manager.remove_item("MCE_filters", 5)

    # View current inventory
    manager.view_inventory()

    # Save inventory to a file
    manager.save_inventory("inventory.json")
```

This program provides a simple inventory management solution for environmental sample media while adhering to your specifications. Adjust paths to `inventory.json` as needed.
