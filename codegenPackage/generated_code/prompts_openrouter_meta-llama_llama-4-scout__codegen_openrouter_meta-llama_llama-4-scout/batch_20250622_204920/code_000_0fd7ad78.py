"""
Generated Code Metadata:
========================
Original URL: https://poweredproductions.com.au
Prompt: Write a Python script to manage inventory of replica firearms and police uniforms for a film production company, considering NSW legislation and regulations.
Generated: DETERMINISTIC_0fd7ad78668636bf
Batch ID: 20250622_204920
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# inventory_manager.py

import datetime

class InventoryItem:
    """Represents an item in the inventory."""

    def __init__(self, item_id, name, category, quantity):
        """
        Initializes an InventoryItem.

        Args:
            item_id (int): Unique identifier for the item.
            name (str): Name of the item.
            category (str): Category of the item (e.g., firearm, uniform).
            quantity (int): Quantity of the item in stock.
        """
        self.item_id = item_id
        self.name = name
        self.category = category
        self.quantity = quantity

    def __str__(self):
        return f"{self.name} ({self.category}) - Quantity: {self.quantity}"


class Firearm(InventoryItem):
    """Represents a replica firearm in the inventory."""

    def __init__(self, item_id, name, category, quantity, prop_number):
        """
        Initializes a Firearm.

        Args:
            item_id (int): Unique identifier for the item.
            name (str): Name of the firearm.
            category (str): Category of the item (e.g., firearm).
            quantity (int): Quantity of the firearm in stock.
            prop_number (str): Prop number for the firearm.
        """
        super().__init__(item_id, name, category, quantity)
        self.prop_number = prop_number

    def __str__(self):
        return super().__str__() + f" - Prop Number: {self.prop_number}"


class Uniform(InventoryItem):
    """Represents a police uniform in the inventory."""

    def __init__(self, item_id, name, category, quantity, size):
        """
        Initializes a Uniform.

        Args:
            item_id (int): Unique identifier for the item.
            name (str): Name of the uniform.
            category (str): Category of the item (e.g., uniform).
            quantity (int): Quantity of the uniform in stock.
            size (str): Size of the uniform.
        """
        super().__init__(item_id, name, category, quantity)
        self.size = size

    def __str__(self):
        return super().__str__() + f" - Size: {self.size}"


class Inventory:
    """Manages the inventory of replica firearms and police uniforms."""

    def __init__(self):
        self.items = []

    def add_item(self, item):
        """
        Adds an item to the inventory.

        Args:
            item (InventoryItem): Item to add.
        """
        self.items.append(item)

    def remove_item(self, item_id):
        """
        Removes an item from the inventory.

        Args:
            item_id (int): ID of the item to remove.

        Raises:
            ValueError: If the item is not found in the inventory.
        """
        for item in self.items:
            if item.item_id == item_id:
                self.items.remove(item)
                return
        raise ValueError("Item not found in inventory")

    def update_quantity(self, item_id, quantity):
        """
        Updates the quantity of an item in the inventory.

        Args:
            item_id (int): ID of the item to update.
            quantity (int): New quantity.

        Raises:
            ValueError: If the item is not found in the inventory.
        """
        for item in self.items:
            if item.item_id == item_id:
                item.quantity = quantity
                return
        raise ValueError("Item not found in inventory")

    def __str__(self):
        inventory_str = "Inventory:\n"
        for item in self.items:
            inventory_str += f"- {item}\n"
        return inventory_str


def validate_firearm_prop_number(prop_number):
    """
    Validates a firearm prop number according to NSW legislation and regulations.

    Args:
        prop_number (str): Prop number to validate.

    Raises:
        ValueError: If the prop number is invalid.
    """
    # NSW legislation and regulations require a prop number to be in the format "LGxxxx"
    if not isinstance(prop_number, str) or len(prop_number) != 6 or not prop_number.startswith("LG"):
        raise ValueError("Invalid prop number")


def main():
    try:
        inventory = Inventory()

        # Add some items to the inventory
        firearm = Firearm(1, "Replica Firearm", "Firearm", 5, "LG1234")
        validate_firearm_prop_number(firearm.prop_number)
        inventory.add_item(firearm)

        uniform = Uniform(2, "Police Uniform", "Uniform", 10, "M")
        inventory.add_item(uniform)

        # Print the inventory
        print(inventory)

        # Update the quantity of an item
        inventory.update_quantity(1, 3)
        print(inventory)

        # Remove an item from the inventory
        inventory.remove_item(2)
        print(inventory)

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
