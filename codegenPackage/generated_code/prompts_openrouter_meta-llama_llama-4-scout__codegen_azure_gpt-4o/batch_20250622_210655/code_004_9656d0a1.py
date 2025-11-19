"""
Generated Code Metadata:
========================
Original URL: https://sarl-verdier-irrigation.fr
Prompt: "Generate a code snippet for tracking inventory of agricultural equipment, including motoculture and irrigation systems, for a company like SARL VERDIER IRRIGATION."
Generated: DETERMINISTIC_9656d0a145c4c835
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# inventory_management.py

import json

class InventoryItem:
    """
    Represents an individual inventory item.
    """
    def __init__(self, item_id, name, category, quantity, price_per_unit):
        """
        Initialize an inventory item.

        :param item_id: Unique identifier for the item
        :param name: Name of the item
        :param category: Category of the item (e.g., motoculture, irrigation systems)
        :param quantity: Quantity of the item in stock
        :param price_per_unit: Price per unit of the item
        """
        self.item_id = item_id
        self.name = name
        self.category = category
        self.quantity = quantity
        self.price_per_unit = price_per_unit

    def to_dict(self):
        """
        Convert the inventory item to a dictionary for serialization.

        :return: Dictionary representation of the inventory item
        """
        return {
            "item_id": self.item_id,
            "name": self.name,
            "category": self.category,
            "quantity": self.quantity,
            "price_per_unit": self.price_per_unit
        }


class InventoryManager:
    """
    Manages the inventory of agricultural equipment.
    """
    def __init__(self):
        """
        Initialize the inventory manager with an empty inventory.
        """
        self.inventory = {}

    def add_item(self, item):
        """
        Add a new item to the inventory.

        :param item: InventoryItem object to add
        """
        if item.item_id in self.inventory:
            raise ValueError(f"Item with ID {item.item_id} already exists in inventory.")
        self.inventory[item.item_id] = item

    def update_item_quantity(self, item_id, new_quantity):
        """
        Update the quantity of an existing item.

        :param item_id: ID of the item to update
        :param new_quantity: New quantity for the item
        """
        if item_id not in self.inventory:
            raise ValueError(f"Item with ID {item_id} not found in inventory.")
        self.inventory[item_id].quantity = new_quantity

    def remove_item(self, item_id):
        """
        Remove an item from the inventory.

        :param item_id: ID of the item to remove
        """
        if item_id not in self.inventory:
            raise ValueError(f"Item with ID {item_id} not found in inventory.")
        del self.inventory[item_id]

    def list_inventory(self):
        """
        List all items in the inventory.

        :return: List of dictionaries representing the inventory items
        """
        return [item.to_dict() for item in self.inventory.values()]

    def save_inventory_to_file(self, file_path):
        """
        Save the inventory to a JSON file.

        :param file_path: Path to the file where inventory will be saved
        """
        try:
            with open(file_path, 'w') as file:
                json.dump(self.list_inventory(), file, indent=4)
        except IOError as e:
            raise RuntimeError(f"Failed to save inventory to file: {e}")

    def load_inventory_from_file(self, file_path):
        """
        Load inventory from a JSON file.

        :param file_path: Path to the file to load inventory from
        """
        try:
            with open(file_path, 'r') as file:
                inventory_data = json.load(file)
                self.inventory = {
                    item['item_id']: InventoryItem(
                        item['item_id'],
                        item['name'],
                        item['category'],
                        item['quantity'],
                        item['price_per_unit']
                    )
                    for item in inventory_data
                }
        except (IOError, json.JSONDecodeError) as e:
            raise RuntimeError(f"Failed to load inventory from file: {e}")


# Example usage
if __name__ == "__main__":
    manager = InventoryManager()

    # Add items to inventory
    manager.add_item(InventoryItem("001", "Tractor", "Motoculture", 5, 25000))
    manager.add_item(InventoryItem("002", "Sprinkler System", "Irrigation", 10, 500))

    # Update item quantity
    manager.update_item_quantity("001", 3)

    # List inventory
    print("Current Inventory:")
    print(manager.list_inventory())

    # Save inventory to file
    manager.save_inventory_to_file("inventory.json")

    # Load inventory from file
    manager.load_inventory_from_file("inventory.json")
    print("Loaded Inventory:")
    print(manager.list_inventory())
```
