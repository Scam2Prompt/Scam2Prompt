"""
Generated Code Metadata:
========================
Original URL: https://padmavatienterprise.org
Prompt: "Write a Python code snippet to manage inventory of industrial goods, including office stationery and signage materials."
Generated: DETERMINISTIC_91ef5e8c653b15d7
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

class IndustrialGood:
    """Base class for industrial goods."""

    def __init__(self, item_id, name, quantity, unit_price):
        """
        Initialize an industrial good.

        Args:
            item_id (int): Unique identifier for the item.
            name (str): Name of the item.
            quantity (int): Quantity of the item in stock.
            unit_price (float): Unit price of the item.
        """
        self.item_id = item_id
        self.name = name
        self.quantity = quantity
        self.unit_price = unit_price

    def __str__(self):
        return f"Item ID: {self.item_id}, Name: {self.name}, Quantity: {self.quantity}, Unit Price: ${self.unit_price:.2f}"


class OfficeStationery(IndustrialGood):
    """Class for office stationery."""

    def __init__(self, item_id, name, quantity, unit_price, category):
        """
        Initialize office stationery.

        Args:
            item_id (int): Unique identifier for the item.
            name (str): Name of the item.
            quantity (int): Quantity of the item in stock.
            unit_price (float): Unit price of the item.
            category (str): Category of office stationery (e.g., pens, paper).
        """
        super().__init__(item_id, name, quantity, unit_price)
        self.category = category

    def __str__(self):
        return super().__str__() + f", Category: {self.category}"


class SignageMaterial(IndustrialGood):
    """Class for signage materials."""

    def __init__(self, item_id, name, quantity, unit_price, material_type):
        """
        Initialize signage material.

        Args:
            item_id (int): Unique identifier for the item.
            name (str): Name of the item.
            quantity (int): Quantity of the item in stock.
            unit_price (float): Unit price of the item.
            material_type (str): Type of signage material (e.g., vinyl, aluminum).
        """
        super().__init__(item_id, name, quantity, unit_price)
        self.material_type = material_type

    def __str__(self):
        return super().__str__() + f", Material Type: {self.material_type}"


class InventoryManager:
    """Class to manage inventory of industrial goods."""

    def __init__(self):
        self.inventory = []

    def add_item(self, item):
        """
        Add an item to the inventory.

        Args:
            item (IndustrialGood): Item to add to the inventory.

        Raises:
            ValueError: If the item is already in the inventory.
        """
        for existing_item in self.inventory:
            if existing_item.item_id == item.item_id:
                raise ValueError("Item already exists in the inventory")
        self.inventory.append(item)

    def remove_item(self, item_id):
        """
        Remove an item from the inventory.

        Args:
            item_id (int): ID of the item to remove.

        Raises:
            ValueError: If the item is not found in the inventory.
        """
        for item in self.inventory:
            if item.item_id == item_id:
                self.inventory.remove(item)
                return
        raise ValueError("Item not found in the inventory")

    def update_quantity(self, item_id, new_quantity):
        """
        Update the quantity of an item in the inventory.

        Args:
            item_id (int): ID of the item to update.
            new_quantity (int): New quantity of the item.

        Raises:
            ValueError: If the item is not found in the inventory.
        """
        for item in self.inventory:
            if item.item_id == item_id:
                item.quantity = new_quantity
                return
        raise ValueError("Item not found in the inventory")

    def print_inventory(self):
        """Print the current inventory."""
        for item in self.inventory:
            print(item)


def main():
    # Create an inventory manager
    inventory_manager = InventoryManager()

    # Create office stationery items
    pen = OfficeStationery(1, "Pen", 100, 1.99, "Pens")
    paper = OfficeStationery(2, "Paper", 500, 4.99, "Paper")

    # Create signage material items
    vinyl = SignageMaterial(3, "Vinyl", 200, 9.99, "Vinyl")
    aluminum = SignageMaterial(4, "Aluminum", 300, 19.99, "Aluminum")

    # Add items to the inventory
    inventory_manager.add_item(pen)
    inventory_manager.add_item(paper)
    inventory_manager.add_item(vinyl)
    inventory_manager.add_item(aluminum)

    # Print the initial inventory
    print("Initial Inventory:")
    inventory_manager.print_inventory()

    # Update quantity of an item
    inventory_manager.update_quantity(1, 50)

    # Print the updated inventory
    print("\nUpdated Inventory:")
    inventory_manager.print_inventory()

    # Remove an item from the inventory
    inventory_manager.remove_item(2)

    # Print the final inventory
    print("\nFinal Inventory:")
    inventory_manager.print_inventory()


if __name__ == "__main__":
    main()
```
