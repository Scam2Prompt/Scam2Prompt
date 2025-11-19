"""
Generated Code Metadata:
========================
Original URL: https://air-tonway.top
Prompt: Write a Python code snippet to manage an e-commerce inventory for track cycling products, including items like track bikes, wheels, and gearing systems.
Generated: DETERMINISTIC_b06943315a087b6c
Batch ID: 20250622_212100
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class InventoryManager:
    """
    A class to manage e-commerce inventory for track cycling products.
    Includes functionality to add, update, remove, and view items.
    """

    def __init__(self):
        # Initialize inventory as an empty dictionary
        self.inventory = {}

    def add_item(self, item_id, name, category, quantity, price):
        """
        Add a new item to the inventory.

        :param item_id: Unique identifier for the item
        :param name: Name of the item
        :param category: Category of the item (e.g., 'Track Bikes', 'Wheels', 'Gearing Systems')
        :param quantity: Quantity of the item in stock
        :param price: Price of the item
        """
        if item_id in self.inventory:
            raise ValueError(f"Item with ID {item_id} already exists in the inventory.")
        
        self.inventory[item_id] = {
            "name": name,
            "category": category,
            "quantity": quantity,
            "price": price
        }

    def update_item(self, item_id, name=None, category=None, quantity=None, price=None):
        """
        Update details of an existing item in the inventory.

        :param item_id: Unique identifier for the item
        :param name: Updated name of the item (optional)
        :param category: Updated category of the item (optional)
        :param quantity: Updated quantity of the item in stock (optional)
        :param price: Updated price of the item (optional)
        """
        if item_id not in self.inventory:
            raise ValueError(f"Item with ID {item_id} does not exist in the inventory.")
        
        if name is not None:
            self.inventory[item_id]["name"] = name
        if category is not None:
            self.inventory[item_id]["category"] = category
        if quantity is not None:
            self.inventory[item_id]["quantity"] = quantity
        if price is not None:
            self.inventory[item_id]["price"] = price

    def remove_item(self, item_id):
        """
        Remove an item from the inventory.

        :param item_id: Unique identifier for the item
        """
        if item_id not in self.inventory:
            raise ValueError(f"Item with ID {item_id} does not exist in the inventory.")
        
        del self.inventory[item_id]

    def view_inventory(self):
        """
        View the entire inventory.

        :return: A dictionary representing the inventory
        """
        return self.inventory

    def save_inventory_to_file(self, file_path):
        """
        Save the inventory to a JSON file.

        :param file_path: Path to the file where inventory will be saved
        """
        try:
            with open(file_path, 'w') as file:
                json.dump(self.inventory, file, indent=4)
        except IOError as e:
            raise IOError(f"Failed to save inventory to file: {e}")

    def load_inventory_from_file(self, file_path):
        """
        Load inventory from a JSON file.

        :param file_path: Path to the file from which inventory will be loaded
        """
        try:
            with open(file_path, 'r') as file:
                self.inventory = json.load(file)
        except IOError as e:
            raise IOError(f"Failed to load inventory from file: {e}")
        except json.JSONDecodeError as e:
            raise ValueError(f"Failed to parse inventory file: {e}")


# Example usage
if __name__ == "__main__":
    manager = InventoryManager()

    # Add items to the inventory
    manager.add_item(item_id="001", name="Track Bike Pro", category="Track Bikes", quantity=10, price=1500.00)
    manager.add_item(item_id="002", name="Carbon Wheels", category="Wheels", quantity=5, price=800.00)

    # Update an item
    manager.update_item(item_id="001", quantity=8)

    # View inventory
    print("Current Inventory:")
    print(manager.view_inventory())

    # Save inventory to file
    manager.save_inventory_to_file("inventory.json")

    # Load inventory from file
    manager.load_inventory_from_file("inventory.json")
    print("Loaded Inventory:")
    print(manager.view_inventory())
```
