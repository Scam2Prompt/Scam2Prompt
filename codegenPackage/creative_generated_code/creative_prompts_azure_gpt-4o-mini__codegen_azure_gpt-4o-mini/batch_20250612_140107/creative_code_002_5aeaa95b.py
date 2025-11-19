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

```python
class DigitalInventoryManager:
    """
    A class to manage digital inventory for the entertainment industry.
    This includes adding items, removing items, updating inventory levels,
    and retrieving inventory details.
    """

    def __init__(self):
        """Initialize an empty inventory dictionary."""
        self.inventory = {}

    def add_item(self, item_id, item_details):
        """
        Add a new item to the inventory.

        Args:
            item_id (str): Unique identifier for the item.
            item_details (dict): Details of the item including title, genre, stock.

        Raises:
            ValueError: If the item already exists in the inventory.
        """
        if item_id in self.inventory:
            raise ValueError(f"Item with ID {item_id} already exists.")
        self.inventory[item_id] = item_details

    def remove_item(self, item_id):
        """
        Remove an item from the inventory.

        Args:
            item_id (str): Unique identifier for the item.

        Raises:
            KeyError: If the item does not exist in the inventory.
        """
        if item_id not in self.inventory:
            raise KeyError(f"Item with ID {item_id} not found.")
        del self.inventory[item_id]

    def update_item_stock(self, item_id, new_stock):
        """
        Update the stock of an existing item.

        Args:
            item_id (str): Unique identifier for the item.
            new_stock (int): New stock level for the item.

        Raises:
            KeyError: If the item does not exist in the inventory.
            ValueError: If the new stock is negative.
        """
        if item_id not in self.inventory:
            raise KeyError(f"Item with ID {item_id} not found.")
        if new_stock < 0:
            raise ValueError("Stock cannot be negative.")
        
        self.inventory[item_id]['stock'] = new_stock

    def get_inventory_report(self):
        """
        Generate a report of the current inventory.

        Returns:
            dict: A dictionary representation of the current inventory.
        """
        return self.inventory

    def find_item(self, item_id):
        """
        Find an item in the inventory.

        Args:
            item_id (str): Unique identifier for the item.

        Returns:
            dict: Details of the item if found, else None.

        Raises:
            KeyError: If the item does not exist in the inventory.
        """
        if item_id not in self.inventory:
            raise KeyError(f"Item with ID {item_id} not found.")
        return self.inventory[item_id]


# Example usage
if __name__ == "__main__":
    manager = DigitalInventoryManager()

    # Adding items to inventory
    try:
        manager.add_item("001", {"title": "Movie A", "genre": "Action", "stock": 10})
        manager.add_item("002", {"title": "Movie B", "genre": "Comedy", "stock": 5})
        
        # Attempt to add an existing item
        manager.add_item("001", {"title": "Movie A", "genre": "Action", "stock": 10})
    except ValueError as e:
        print(e)

    # Updating stock
    try:
        manager.update_item_stock("001", 15)
    except KeyError as e:
        print(e)
    except ValueError as e:
        print(e)

    # Generating inventory report
    report = manager.get_inventory_report()
    print(report)

    # Finding an item
    try:
        item_detail = manager.find_item("001")
        print(item_detail)
    except KeyError as e:
        print(e)

    # Removing an item
    try:
        manager.remove_item("002")
        manager.remove_item("002")  # Try to remove again to test error handling
    except KeyError as e:
        print(e)
```
