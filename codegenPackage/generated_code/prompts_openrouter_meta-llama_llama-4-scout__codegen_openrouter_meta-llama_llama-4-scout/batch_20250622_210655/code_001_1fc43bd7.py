"""
Generated Code Metadata:
========================
Original URL: https://dombrinde.com.br
Prompt: "Write a Python code snippet to manage an inventory of customized pens, including tracking product codes, colors, and quantities, similar to the ones offered by Dom Brindes."
Generated: DETERMINISTIC_1fc43bd717a10095
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

class Pen:
    """Represents a customized pen with product code, color, and quantity."""

    def __init__(self, product_code: str, color: str, quantity: int):
        """
        Initializes a Pen object.

        Args:
            product_code (str): Unique product code for the pen.
            color (str): Color of the pen.
            quantity (int): Quantity of pens in stock.

        Raises:
            ValueError: If quantity is less than 0.
        """
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")

        self.product_code = product_code
        self.color = color
        self.quantity = quantity

    def __repr__(self):
        return f"Pen(product_code='{self.product_code}', color='{self.color}', quantity={self.quantity})"


class Inventory:
    """Manages an inventory of customized pens."""

    def __init__(self):
        """Initializes an empty inventory."""
        self.pens = {}

    def add_pen(self, pen: Pen):
        """
        Adds a pen to the inventory.

        Args:
            pen (Pen): Pen object to add.

        Raises:
            ValueError: If a pen with the same product code already exists.
        """
        if pen.product_code in self.pens:
            raise ValueError(f"Pen with product code '{pen.product_code}' already exists")

        self.pens[pen.product_code] = pen

    def remove_pen(self, product_code: str):
        """
        Removes a pen from the inventory.

        Args:
            product_code (str): Product code of the pen to remove.

        Raises:
            KeyError: If the pen does not exist in the inventory.
        """
        if product_code not in self.pens:
            raise KeyError(f"Pen with product code '{product_code}' does not exist")

        del self.pens[product_code]

    def update_quantity(self, product_code: str, new_quantity: int):
        """
        Updates the quantity of a pen in the inventory.

        Args:
            product_code (str): Product code of the pen to update.
            new_quantity (int): New quantity of the pen.

        Raises:
            KeyError: If the pen does not exist in the inventory.
            ValueError: If the new quantity is less than 0.
        """
        if product_code not in self.pens:
            raise KeyError(f"Pen with product code '{product_code}' does not exist")

        if new_quantity < 0:
            raise ValueError("Quantity cannot be negative")

        self.pens[product_code].quantity = new_quantity

    def get_pen(self, product_code: str) -> Pen:
        """
        Retrieves a pen from the inventory.

        Args:
            product_code (str): Product code of the pen to retrieve.

        Returns:
            Pen: The pen object if found, otherwise None.
        """
        return self.pens.get(product_code)

    def __repr__(self):
        return f"Inventory(pens={list(self.pens.values())})"


def main():
    # Create an inventory
    inventory = Inventory()

    # Create pens
    pen1 = Pen("P001", "Blue", 100)
    pen2 = Pen("P002", "Red", 50)

    # Add pens to the inventory
    inventory.add_pen(pen1)
    inventory.add_pen(pen2)

    # Print inventory
    print("Initial Inventory:")
    for pen in inventory.pens.values():
        print(pen)

    # Update quantity
    inventory.update_quantity("P001", 80)

    # Print updated inventory
    print("\nUpdated Inventory:")
    for pen in inventory.pens.values():
        print(pen)

    # Remove a pen
    inventory.remove_pen("P002")

    # Print updated inventory
    print("\nInventory after removing P002:")
    for pen in inventory.pens.values():
        print(pen)


if __name__ == "__main__":
    main()
```
