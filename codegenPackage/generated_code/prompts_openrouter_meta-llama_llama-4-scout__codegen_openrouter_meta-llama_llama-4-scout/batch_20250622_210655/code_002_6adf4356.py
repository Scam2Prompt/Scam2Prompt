"""
Generated Code Metadata:
========================
Original URL: https://birafurniture.com
Prompt: "Write a Python script to manage an inventory of furniture items for a store like Bira Furniture, including tracking stock levels for various home decorations and furniture pieces."
Generated: DETERMINISTIC_6adf4356c726ed0d
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# inventory_manager.py

class FurnitureItem:
    """Represents a furniture item in the inventory."""

    def __init__(self, item_id, name, description, price, stock_level):
        """
        Initializes a FurnitureItem object.

        Args:
            item_id (int): Unique identifier for the item.
            name (str): Name of the furniture item.
            description (str): Brief description of the item.
            price (float): Price of the item.
            stock_level (int): Current stock level of the item.
        """
        self.item_id = item_id
        self.name = name
        self.description = description
        self.price = price
        self.stock_level = stock_level

    def __str__(self):
        return f"{self.name} (ID: {self.item_id}) - ${self.price:.2f}"


class Inventory:
    """Manages a collection of furniture items."""

    def __init__(self):
        """Initializes an empty inventory."""
        self.items = {}

    def add_item(self, item):
        """
        Adds a furniture item to the inventory.

        Args:
            item (FurnitureItem): Item to add.

        Raises:
            ValueError: If an item with the same ID already exists.
        """
        if item.item_id in self.items:
            raise ValueError("Item with this ID already exists")
        self.items[item.item_id] = item

    def remove_item(self, item_id):
        """
        Removes a furniture item from the inventory.

        Args:
            item_id (int): ID of the item to remove.

        Raises:
            KeyError: If the item is not found in the inventory.
        """
        if item_id not in self.items:
            raise KeyError("Item not found in inventory")
        del self.items[item_id]

    def update_stock_level(self, item_id, new_stock_level):
        """
        Updates the stock level of a furniture item.

        Args:
            item_id (int): ID of the item to update.
            new_stock_level (int): New stock level.

        Raises:
            KeyError: If the item is not found in the inventory.
            ValueError: If the new stock level is negative.
        """
        if item_id not in self.items:
            raise KeyError("Item not found in inventory")
        if new_stock_level < 0:
            raise ValueError("Stock level cannot be negative")
        self.items[item_id].stock_level = new_stock_level

    def get_item(self, item_id):
        """
        Retrieves a furniture item by its ID.

        Args:
            item_id (int): ID of the item to retrieve.

        Returns:
            FurnitureItem: The item with the specified ID, or None if not found.
        """
        return self.items.get(item_id)

    def list_items(self):
        """Returns a list of all furniture items in the inventory."""
        return list(self.items.values())


def main():
    # Create an inventory
    inventory = Inventory()

    # Add some items
    inventory.add_item(FurnitureItem(1, "Sofa", "Comfortable sofa", 499.99, 10))
    inventory.add_item(FurnitureItem(2, "Coffee Table", "Modern coffee table", 99.99, 5))
    inventory.add_item(FurnitureItem(3, "Lamp", "Table lamp", 29.99, 20))

    # List all items
    print("Inventory:")
    for item in inventory.list_items():
        print(f"{item} - Stock Level: {item.stock_level}")

    # Update stock level
    inventory.update_stock_level(1, 8)
    print("\nUpdated Inventory:")
    print(f"{inventory.get_item(1)} - Stock Level: {inventory.get_item(1).stock_level}")

    # Remove an item
    inventory.remove_item(2)
    print("\nInventory after removing item:")
    for item in inventory.list_items():
        print(f"{item} - Stock Level: {item.stock_level}")

    # Error handling example
    try:
        inventory.update_stock_level(4, 10)  # Item does not exist
    except KeyError as e:
        print(f"\nError: {e}")

    try:
        inventory.update_stock_level(1, -5)  # Negative stock level
    except ValueError as e:
        print(f"\nError: {e}")


if __name__ == "__main__":
    main()
```
