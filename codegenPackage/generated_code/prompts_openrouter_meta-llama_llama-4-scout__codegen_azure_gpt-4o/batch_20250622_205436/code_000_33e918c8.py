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

class InventoryManagementSystem:
    """
    A digital inventory management system for a sports business.
    Allows managing a configurable catalog of available and potential inventory.
    """

    def __init__(self):
        """
        Initializes the inventory management system with empty inventory and catalog.
        """
        self.inventory = {}  # Dictionary to store available inventory
        self.catalog = {}    # Dictionary to store potential inventory

    def add_to_inventory(self, item_id, name, quantity, price, rank):
        """
        Adds an item to the inventory.

        :param item_id: Unique identifier for the item
        :param name: Name of the item
        :param quantity: Quantity of the item in stock
        :param price: Price of the item
        :param rank: Rank of the item (e.g., popularity, demand)
        """
        if item_id in self.inventory:
            raise ValueError(f"Item with ID {item_id} already exists in inventory.")
        self.inventory[item_id] = {
            "name": name,
            "quantity": quantity,
            "price": price,
            "rank": rank
        }

    def add_to_catalog(self, item_id, name, price, rank):
        """
        Adds an item to the catalog.

        :param item_id: Unique identifier for the item
        :param name: Name of the item
        :param price: Price of the item
        :param rank: Rank of the item (e.g., popularity, demand)
        """
        if item_id in self.catalog:
            raise ValueError(f"Item with ID {item_id} already exists in catalog.")
        self.catalog[item_id] = {
            "name": name,
            "price": price,
            "rank": rank
        }

    def update_inventory(self, item_id, quantity=None, price=None, rank=None):
        """
        Updates the details of an item in the inventory.

        :param item_id: Unique identifier for the item
        :param quantity: New quantity of the item (optional)
        :param price: New price of the item (optional)
        :param rank: New rank of the item (optional)
        """
        if item_id not in self.inventory:
            raise ValueError(f"Item with ID {item_id} does not exist in inventory.")
        if quantity is not None:
            self.inventory[item_id]["quantity"] = quantity
        if price is not None:
            self.inventory[item_id]["price"] = price
        if rank is not None:
            self.inventory[item_id]["rank"] = rank

    def remove_from_inventory(self, item_id):
        """
        Removes an item from the inventory.

        :param item_id: Unique identifier for the item
        """
        if item_id not in self.inventory:
            raise ValueError(f"Item with ID {item_id} does not exist in inventory.")
        del self.inventory[item_id]

    def remove_from_catalog(self, item_id):
        """
        Removes an item from the catalog.

        :param item_id: Unique identifier for the item
        """
        if item_id not in self.catalog:
            raise ValueError(f"Item with ID {item_id} does not exist in catalog.")
        del self.catalog[item_id]

    def list_inventory(self):
        """
        Lists all items in the inventory.

        :return: A dictionary of inventory items
        """
        return self.inventory

    def list_catalog(self):
        """
        Lists all items in the catalog.

        :return: A dictionary of catalog items
        """
        return self.catalog

    def save_to_file(self, filename):
        """
        Saves the inventory and catalog to a JSON file.

        :param filename: Name of the file to save data
        """
        data = {
            "inventory": self.inventory,
            "catalog": self.catalog
        }
        try:
            with open(filename, 'w') as file:
                json.dump(data, file, indent=4)
        except IOError as e:
            raise IOError(f"Error saving data to file: {e}")

    def load_from_file(self, filename):
        """
        Loads the inventory and catalog from a JSON file.

        :param filename: Name of the file to load data
        """
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                self.inventory = data.get("inventory", {})
                self.catalog = data.get("catalog", {})
        except IOError as e:
            raise IOError(f"Error loading data from file: {e}")
        except json.JSONDecodeError as e:
            raise ValueError(f"Error decoding JSON data: {e}")


# Example usage
if __name__ == "__main__":
    ims = InventoryManagementSystem()

    # Adding items to inventory
    ims.add_to_inventory(item_id="001", name="Soccer Ball", quantity=50, price=25.99, rank=1)
    ims.add_to_inventory(item_id="002", name="Tennis Racket", quantity=30, price=89.99, rank=2)

    # Adding items to catalog
    ims.add_to_catalog(item_id="101", name="Basketball", price=29.99, rank=3)
    ims.add_to_catalog(item_id="102", name="Golf Club", price=199.99, rank=4)

    # Updating inventory
    ims.update_inventory(item_id="001", quantity=45)

    # Listing inventory and catalog
    print("Inventory:", ims.list_inventory())
    print("Catalog:", ims.list_catalog())

    # Saving to file
    ims.save_to_file("sports_inventory.json")

    # Loading from file
    ims.load_from_file("sports_inventory.json")
    print("Loaded Inventory:", ims.list_inventory())
    print("Loaded Catalog:", ims.list_catalog())
```
