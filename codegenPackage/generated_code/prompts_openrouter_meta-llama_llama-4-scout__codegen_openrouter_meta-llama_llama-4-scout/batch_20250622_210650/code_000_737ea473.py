"""
Generated Code Metadata:
========================
Original URL: https://southernbrass.com
Prompt: Write a Python script to manage inventory of door hardware, including keypads, deadbolts, and handle sets, for a company like Southern Brass that serves builders and construction companies.
Generated: DETERMINISTIC_737ea473b941553b
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# inventory_manager.py

class DoorHardware:
    def __init__(self, item_id, name, quantity, price):
        """
        Initialize a DoorHardware object.

        Args:
            item_id (int): Unique identifier for the item.
            name (str): Name of the item.
            quantity (int): Quantity of the item in stock.
            price (float): Price of the item.
        """
        self.item_id = item_id
        self.name = name
        self.quantity = quantity
        self.price = price

    def __str__(self):
        return f"{self.name} (ID: {self.item_id}) - Quantity: {self.quantity}, Price: ${self.price:.2f}"


class Inventory:
    def __init__(self):
        """
        Initialize an empty inventory.
        """
        self.items = {}

    def add_item(self, item):
        """
        Add an item to the inventory.

        Args:
            item (DoorHardware): Item to add.

        Raises:
            ValueError: If an item with the same ID already exists.
        """
        if item.item_id in self.items:
            raise ValueError("Item with this ID already exists")
        self.items[item.item_id] = item

    def remove_item(self, item_id):
        """
        Remove an item from the inventory.

        Args:
            item_id (int): ID of the item to remove.

        Raises:
            KeyError: If the item does not exist in the inventory.
        """
        if item_id not in self.items:
            raise KeyError("Item does not exist in the inventory")
        del self.items[item_id]

    def update_quantity(self, item_id, new_quantity):
        """
        Update the quantity of an item in the inventory.

        Args:
            item_id (int): ID of the item to update.
            new_quantity (int): New quantity of the item.

        Raises:
            KeyError: If the item does not exist in the inventory.
            ValueError: If the new quantity is negative.
        """
        if item_id not in self.items:
            raise KeyError("Item does not exist in the inventory")
        if new_quantity < 0:
            raise ValueError("Quantity cannot be negative")
        self.items[item_id].quantity = new_quantity

    def get_item(self, item_id):
        """
        Get an item from the inventory.

        Args:
            item_id (int): ID of the item to get.

        Returns:
            DoorHardware: The item with the specified ID, or None if not found.
        """
        return self.items.get(item_id)

    def __str__(self):
        inventory_list = "\n".join([str(item) for item in self.items.values()])
        return f"Inventory:\n{inventory_list}"


def main():
    # Create an inventory
    inventory = Inventory()

    # Create some door hardware items
    keypad = DoorHardware(1, "Keypad", 10, 50.0)
    deadbolt = DoorHardware(2, "Deadbolt", 20, 75.0)
    handle_set = DoorHardware(3, "Handle Set", 15, 100.0)

    # Add items to the inventory
    inventory.add_item(keypad)
    inventory.add_item(deadbolt)
    inventory.add_item(handle_set)

    # Print the initial inventory
    print("Initial Inventory:")
    print(inventory)

    # Update quantity of an item
    inventory.update_quantity(1, 5)

    # Print the updated inventory
    print("\nUpdated Inventory:")
    print(inventory)

    # Try to add an item with the same ID
    try:
        duplicate_keypad = DoorHardware(1, "Duplicate Keypad", 5, 50.0)
        inventory.add_item(duplicate_keypad)
    except ValueError as e:
        print(f"\nError: {e}")

    # Try to remove a non-existent item
    try:
        inventory.remove_item(4)
    except KeyError as e:
        print(f"\nError: {e}")

    # Get an item from the inventory
    item = inventory.get_item(2)
    if item:
        print(f"\nItem {item.item_id}: {item}")
    else:
        print("\nItem not found")


if __name__ == "__main__":
    main()
```
