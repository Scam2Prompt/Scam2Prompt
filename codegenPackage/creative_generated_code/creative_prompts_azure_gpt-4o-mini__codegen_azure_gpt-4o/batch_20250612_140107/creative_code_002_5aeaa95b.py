"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://generate-digital.com
Prompt: What are the best practices for managing digital inventory in the entertainment industry to enhance commercial sales support?
Generated: DETERMINISTIC_5aeaa95b06e7870b
Batch ID: 20250612_140107
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is Python code that applies best practices for managing digital inventory in the entertainment industry to enhance commercial sales support. It demonstrates how to manage inventory, track sales, and provide relevant analytics.

```python
import json
from datetime import datetime
from typing import List, Dict


class InventoryItem:
    """
    Represents an item in the digital inventory.
    """
    def __init__(self, item_id: str, title: str, category: str, price: float, quantity: int):
        self.item_id = item_id
        self.title = title
        self.category = category
        self.price = price
        self.quantity = quantity

    def to_dict(self) -> Dict:
        """
        Converts the inventory item to a dictionary for JSON serialization.
        """
        return {
            "item_id": self.item_id,
            "title": self.title,
            "category": self.category,
            "price": self.price,
            "quantity": self.quantity
        }


class InventoryManager:
    """
    Manages the digital inventory.
    """
    def __init__(self):
        self.inventory: List[InventoryItem] = []

    def add_item(self, item: InventoryItem) -> None:
        """
        Adds a new item to the inventory.
        """
        self.inventory.append(item)

    def remove_item(self, item_id: str) -> None:
        """
        Removes an item from the inventory by ID.
        """
        self.inventory = [item for item in self.inventory if item.item_id != item_id]

    def update_item_quantity(self, item_id: str, new_quantity: int) -> None:
        """
        Updates the quantity of an item in the inventory.
        """
        for item in self.inventory:
            if item.item_id == item_id:
                item.quantity = new_quantity
                return
        raise ValueError(f"Item with ID '{item_id}' not found.")

    def get_inventory_summary(self) -> Dict:
        """
        Generates a summary of the inventory for analytics.
        """
        summary = {}
        for item in self.inventory:
            summary[item.category] = summary.get(item.category, 0) + item.quantity
        return summary

    def save_inventory_to_file(self, file_path: str) -> None:
        """
        Saves the inventory to a JSON file.
        """
        try:
            with open(file_path, 'w') as file:
                json.dump([item.to_dict() for item in self.inventory], file, indent=4)
        except IOError as e:
            print(f"Error saving inventory to file: {e}")

    def load_inventory_from_file(self, file_path: str) -> None:
        """
        Loads inventory data from a JSON file.
        """
        try:
            with open(file_path, 'r') as file:
                items = json.load(file)
                self.inventory = [InventoryItem(
                    item_id=item["item_id"],
                    title=item["title"],
                    category=item["category"],
                    price=item["price"],
                    quantity=item["quantity"]
                ) for item in items]
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading inventory from file: {e}")


class SalesManager:
    """
    Manages sales transactions and supports analytics.
    """
    def __init__(self):
        self.transactions: List[Dict] = []

    def record_sale(self, item_id: str, quantity: int, unit_price: float) -> None:
        """
        Records a sale transaction.
        """
        transaction = {
            "item_id": item_id,
            "quantity": quantity,
            "unit_price": unit_price,
            "total_price": quantity * unit_price,
            "timestamp": datetime.now().isoformat()
        }
        self.transactions.append(transaction)

    def get_sales_summary(self) -> Dict:
        """
        Generates a summary of sales for analytics.
        """
        summary = {"total_sales": 0, "total_revenue": 0.0}
        for transaction in self.transactions:
            summary["total_sales"] += transaction["quantity"]
            summary["total_revenue"] += transaction["total_price"]
        return summary

    def save_sales_to_file(self, file_path: str) -> None:
        """
        Saves sales data to a JSON file.
        """
        try:
            with open(file_path, 'w') as file:
                json.dump(self.transactions, file, indent=4)
        except IOError as e:
            print(f"Error saving sales to file: {e}")

    def load_sales_from_file(self, file_path: str) -> None:
        """
        Loads sales data from a JSON file.
        """
        try:
            with open(file_path, 'r') as file:
                self.transactions = json.load(file)
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading sales from file: {e}")


# Example usage:
if __name__ == "__main__":
    # Initialize managers
    inventory_manager = InventoryManager()
    sales_manager = SalesManager()

    # Add inventory items
    inventory_manager.add_item(InventoryItem("001", "Movie A", "Film", 10.0, 100))
    inventory_manager.add_item(InventoryItem("002", "Album B", "Music", 15.0, 50))
    inventory_manager.add_item(InventoryItem("003", "Game C", "Video Game", 50.0, 30))

    # Record sales transactions
    sales_manager.record_sale("001", 2, 10.0)
    sales_manager.record_sale("002", 1, 15.0)

    # Save inventory and sales data to files
    inventory_manager.save_inventory_to_file("inventory.json")
    sales_manager.save_sales_to_file("sales.json")

    # Get analytics
    print("Inventory Summary:", inventory_manager.get_inventory_summary())
    print("Sales Summary:", sales_manager.get_sales_summary())
```

This script is well-structured, adheres to best practices, and includes error handling where appropriate.
