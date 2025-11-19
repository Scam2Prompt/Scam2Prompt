"""
Generated Code Metadata:
========================
Original URL: https://binqutab.ae
Prompt: Write a Python code snippet to manage a logistics company's warehouse, including storage and inventory tracking, inspired by Bin Qutab Logistics L.L.C's warehousing services.
Generated: DETERMINISTIC_4623e60ab56a74cc
Batch ID: 20250622_205836
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# warehouse_management.py

class Warehouse:
    def __init__(self, name):
        """
        Initialize a Warehouse object.

        Args:
            name (str): Name of the warehouse.
        """
        self.name = name
        self.inventory = {}  # {item_id: quantity}

    def add_item(self, item_id, quantity):
        """
        Add items to the warehouse inventory.

        Args:
            item_id (str): Unique identifier for the item.
            quantity (int): Quantity of items to add.

        Raises:
            ValueError: If quantity is not a positive integer.
        """
        if not isinstance(quantity, int) or quantity <= 0:
            raise ValueError("Quantity must be a positive integer.")

        if item_id in self.inventory:
            self.inventory[item_id] += quantity
        else:
            self.inventory[item_id] = quantity

    def remove_item(self, item_id, quantity):
        """
        Remove items from the warehouse inventory.

        Args:
            item_id (str): Unique identifier for the item.
            quantity (int): Quantity of items to remove.

        Raises:
            ValueError: If quantity is not a positive integer.
            KeyError: If item_id is not in the inventory.
            RuntimeError: If quantity exceeds available stock.
        """
        if not isinstance(quantity, int) or quantity <= 0:
            raise ValueError("Quantity must be a positive integer.")

        if item_id not in self.inventory:
            raise KeyError(f"Item {item_id} not found in inventory.")

        if quantity > self.inventory[item_id]:
            raise RuntimeError(f"Insufficient stock for item {item_id}.")

        self.inventory[item_id] -= quantity
        if self.inventory[item_id] == 0:
            del self.inventory[item_id]

    def get_inventory(self):
        """
        Get the current warehouse inventory.

        Returns:
            dict: {item_id: quantity}
        """
        return self.inventory.copy()

    def get_item_quantity(self, item_id):
        """
        Get the quantity of a specific item in the warehouse.

        Args:
            item_id (str): Unique identifier for the item.

        Returns:
            int: Quantity of the item.

        Raises:
            KeyError: If item_id is not in the inventory.
        """
        if item_id not in self.inventory:
            raise KeyError(f"Item {item_id} not found in inventory.")
        return self.inventory[item_id]


class Storage:
    def __init__(self, warehouse):
        """
        Initialize a Storage object.

        Args:
            warehouse (Warehouse): Warehouse object.
        """
        self.warehouse = warehouse
        self.storage_locations = {}  # {item_id: location}

    def store_item(self, item_id, location):
        """
        Store an item in a specific location.

        Args:
            item_id (str): Unique identifier for the item.
            location (str): Storage location.

        Raises:
            KeyError: If item_id is not in the warehouse inventory.
        """
        if item_id not in self.warehouse.get_inventory():
            raise KeyError(f"Item {item_id} not found in warehouse inventory.")

        self.storage_locations[item_id] = location

    def retrieve_item_location(self, item_id):
        """
        Retrieve the storage location of an item.

        Args:
            item_id (str): Unique identifier for the item.

        Returns:
            str: Storage location of the item.

        Raises:
            KeyError: If item_id is not in the storage locations.
        """
        if item_id not in self.storage_locations:
            raise KeyError(f"Item {item_id} not found in storage locations.")
        return self.storage_locations[item_id]


def main():
    # Create a warehouse
    warehouse = Warehouse("Bin Qutab Logistics")

    # Add items to the warehouse
    warehouse.add_item("item1", 100)
    warehouse.add_item("item2", 50)

    # Create a storage
    storage = Storage(warehouse)

    # Store items in specific locations
    storage.store_item("item1", "Aisle 1, Shelf 1")
    storage.store_item("item2", "Aisle 2, Shelf 2")

    # Retrieve item locations
    print(storage.retrieve_item_location("item1"))  # Aisle 1, Shelf 1
    print(storage.retrieve_item_location("item2"))  # Aisle 2, Shelf 2

    # Get warehouse inventory
    print(warehouse.get_inventory())  # {'item1': 100, 'item2': 50}

    # Remove items from the warehouse
    warehouse.remove_item("item1", 20)

    # Get updated warehouse inventory
    print(warehouse.get_inventory())  # {'item1': 80, 'item2': 50}


if __name__ == "__main__":
    main()
```
