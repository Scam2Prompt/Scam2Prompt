"""
Generated Code Metadata:
========================
Original URL: https://linea.eu
Prompt: Write a Python script to manage inventory for a company like PDC Brush that produces private label household cleaning tools, considering factors like FSC-certified wood and sustainability.
Generated: DETERMINISTIC_5aa03fc155e09616
Batch ID: 20250622_212556
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

class InventoryManager:
    """
    A class to manage inventory for a company producing household cleaning tools.
    Includes support for tracking FSC-certified wood and sustainability factors.
    """

    def __init__(self, inventory_file="inventory.json"):
        """
        Initialize the inventory manager.

        :param inventory_file: Path to the inventory file (default: 'inventory.json').
        """
        self.inventory_file = inventory_file
        self.inventory = {}
        self.load_inventory()

    def load_inventory(self):
        """
        Load inventory from a JSON file. If the file does not exist, initialize an empty inventory.
        """
        if os.path.exists(self.inventory_file):
            try:
                with open(self.inventory_file, 'r') as file:
                    self.inventory = json.load(file)
            except json.JSONDecodeError:
                print("Error: Inventory file is corrupted. Initializing empty inventory.")
                self.inventory = {}
        else:
            self.inventory = {}

    def save_inventory(self):
        """
        Save the current inventory to a JSON file.
        """
        try:
            with open(self.inventory_file, 'w') as file:
                json.dump(self.inventory, file, indent=4)
        except IOError as e:
            print(f"Error: Unable to save inventory to file. {e}")

    def add_item(self, item_name, quantity, fsc_certified, sustainable_materials):
        """
        Add a new item to the inventory.

        :param item_name: Name of the item.
        :param quantity: Quantity of the item.
        :param fsc_certified: Boolean indicating if the item uses FSC-certified wood.
        :param sustainable_materials: Boolean indicating if the item uses sustainable materials.
        """
        if item_name in self.inventory:
            print(f"Error: Item '{item_name}' already exists in the inventory.")
            return

        self.inventory[item_name] = {
            "quantity": quantity,
            "fsc_certified": fsc_certified,
            "sustainable_materials": sustainable_materials
        }
        self.save_inventory()
        print(f"Item '{item_name}' added successfully.")

    def update_item(self, item_name, quantity=None, fsc_certified=None, sustainable_materials=None):
        """
        Update an existing item in the inventory.

        :param item_name: Name of the item.
        :param quantity: New quantity of the item (optional).
        :param fsc_certified: New FSC-certified status (optional).
        :param sustainable_materials: New sustainable materials status (optional).
        """
        if item_name not in self.inventory:
            print(f"Error: Item '{item_name}' does not exist in the inventory.")
            return

        if quantity is not None:
            self.inventory[item_name]["quantity"] = quantity
        if fsc_certified is not None:
            self.inventory[item_name]["fsc_certified"] = fsc_certified
        if sustainable_materials is not None:
            self.inventory[item_name]["sustainable_materials"] = sustainable_materials

        self.save_inventory()
        print(f"Item '{item_name}' updated successfully.")

    def remove_item(self, item_name):
        """
        Remove an item from the inventory.

        :param item_name: Name of the item to remove.
        """
        if item_name not in self.inventory:
            print(f"Error: Item '{item_name}' does not exist in the inventory.")
            return

        del self.inventory[item_name]
        self.save_inventory()
        print(f"Item '{item_name}' removed successfully.")

    def view_inventory(self):
        """
        Display the current inventory in a readable format.
        """
        if not self.inventory:
            print("Inventory is empty.")
            return

        print("Current Inventory:")
        for item_name, details in self.inventory.items():
            print(f"- {item_name}: Quantity={details['quantity']}, FSC-Certified={details['fsc_certified']}, "
                  f"Sustainable Materials={details['sustainable_materials']}")

# Example usage
if __name__ == "__main__":
    manager = InventoryManager()

    # Add items
    manager.add_item("Wooden Brush", 100, True, True)
    manager.add_item("Plastic Scrubber", 200, False, False)

    # View inventory
    manager.view_inventory()

    # Update an item
    manager.update_item("Wooden Brush", quantity=120)

    # Remove an item
    manager.remove_item("Plastic Scrubber")

    # View inventory again
    manager.view_inventory()
```
