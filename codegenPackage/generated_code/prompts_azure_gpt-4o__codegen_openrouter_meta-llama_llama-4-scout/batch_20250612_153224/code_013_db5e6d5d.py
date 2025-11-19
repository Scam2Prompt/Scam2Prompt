"""
Generated Code Metadata:
========================
Original URL: https://himsaral.com
Prompt: Write a function to manage inventory for schools, including stock tracking and purchase records, inspired by Him Saral's Inventory module.
Generated: DETERMINISTIC_db5e6d5d66b30156
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# inventory_manager.py

from datetime import datetime
from typing import Dict, List

class InventoryItem:
    """Represents an item in the inventory."""

    def __init__(self, item_id: int, name: str, quantity: int, price: float):
        """
        Initializes an InventoryItem.

        Args:
        - item_id (int): Unique identifier for the item.
        - name (str): Name of the item.
        - quantity (int): Initial quantity of the item.
        - price (float): Price of the item.
        """
        self.item_id = item_id
        self.name = name
        self.quantity = quantity
        self.price = price

class PurchaseRecord:
    """Represents a purchase record."""

    def __init__(self, purchase_id: int, item_id: int, quantity: int, date: str, total_cost: float):
        """
        Initializes a PurchaseRecord.

        Args:
        - purchase_id (int): Unique identifier for the purchase record.
        - item_id (int): Foreign key referencing the InventoryItem.
        - quantity (int): Quantity of items purchased.
        - date (str): Date of purchase in YYYY-MM-DD format.
        - total_cost (float): Total cost of the purchase.
        """
        self.purchase_id = purchase_id
        self.item_id = item_id
        self.quantity = quantity
        self.date = date
        self.total_cost = total_cost

class InventoryManager:
    """Manages school inventory, including stock tracking and purchase records."""

    def __init__(self):
        """Initializes an empty inventory and purchase record database."""
        self.inventory: Dict[int, InventoryItem] = {}
        self.purchase_records: Dict[int, PurchaseRecord] = {}
        self.item_id_counter = 1
        self.purchase_id_counter = 1

    def add_item(self, name: str, quantity: int, price: float) -> int:
        """
        Adds a new item to the inventory.

        Args:
        - name (str): Name of the item.
        - quantity (int): Initial quantity of the item.
        - price (float): Price of the item.

        Returns:
        - int: The item_id of the newly added item.
        """
        item_id = self.item_id_counter
        self.inventory[item_id] = InventoryItem(item_id, name, quantity, price)
        self.item_id_counter += 1
        return item_id

    def remove_item(self, item_id: int) -> bool:
        """
        Removes an item from the inventory.

        Args:
        - item_id (int): The item_id of the item to remove.

        Returns:
        - bool: True if the item was removed, False if it does not exist.
        """
        if item_id in self.inventory:
            del self.inventory[item_id]
            return True
        return False

    def update_quantity(self, item_id: int, new_quantity: int) -> bool:
        """
        Updates the quantity of an item in the inventory.

        Args:
        - item_id (int): The item_id of the item to update.
        - new_quantity (int): The new quantity of the item.

        Returns:
        - bool: True if the quantity was updated, False if the item does not exist.
        """
        if item_id in self.inventory:
            self.inventory[item_id].quantity = new_quantity
            return True
        return False

    def record_purchase(self, item_id: int, quantity: int) -> int:
        """
        Records a purchase of an item.

        Args:
        - item_id (int): The item_id of the item purchased.
        - quantity (int): Quantity of items purchased.

        Returns:
        - int: The purchase_id of the newly recorded purchase.
        """
        if item_id in self.inventory:
            purchase_id = self.purchase_id_counter
            item = self.inventory[item_id]
            total_cost = quantity * item.price
            date = datetime.now().strftime("%Y-%m-%d")
            self.purchase_records[purchase_id] = PurchaseRecord(purchase_id, item_id, quantity, date, total_cost)
            self.purchase_id_counter += 1
            item.quantity += quantity
            return purchase_id
        raise ValueError("Item does not exist in inventory.")

    def get_item(self, item_id: int) -> InventoryItem:
        """
        Retrieves an item from the inventory.

        Args:
        - item_id (int): The item_id of the item to retrieve.

        Returns:
        - InventoryItem: The item with the specified item_id, or None if it does not exist.
        """
        return self.inventory.get(item_id)

    def get_purchase_record(self, purchase_id: int) -> PurchaseRecord:
        """
        Retrieves a purchase record.

        Args:
        - purchase_id (int): The purchase_id of the record to retrieve.

        Returns:
        - PurchaseRecord: The purchase record with the specified purchase_id, or None if it does not exist.
        """
        return self.purchase_records.get(purchase_id)

def main():
    # Example usage:
    manager = InventoryManager()
    item_id = manager.add_item("Pencils", 100, 0.50)
    print(f"Added item with ID {item_id}")
    purchase_id = manager.record_purchase(item_id, 20)
    print(f"Recorded purchase with ID {purchase_id}")
    item = manager.get_item(item_id)
    print(f"Item {item.name} has quantity {item.quantity}")
    purchase_record = manager.get_purchase_record(purchase_id)
    print(f"Purchase record {purchase_record.purchase_id} has date {purchase_record.date} and total cost {purchase_record.total_cost}")

if __name__ == "__main__":
    main()
```
