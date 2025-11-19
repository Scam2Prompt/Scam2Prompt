"""
Generated Code Metadata:
========================
Original URL: https://accutrolsystems.com
Prompt: Create a program to track and manage spare parts inventory for solar water heaters and gas boilers, referencing the after-sales service model mentioned on the Accutrol Systems website.
Generated: DETERMINISTIC_aade1262375c64a3
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# inventory_management.py

class SparePart:
    """Represents a spare part for solar water heaters or gas boilers."""

    def __init__(self, part_number, description, quantity, unit_cost):
        """
        Initializes a SparePart object.

        Args:
            part_number (str): Unique identifier for the spare part.
            description (str): Brief description of the spare part.
            quantity (int): Current quantity in stock.
            unit_cost (float): Cost of a single unit of the spare part.
        """
        self.part_number = part_number
        self.description = description
        self.quantity = quantity
        self.unit_cost = unit_cost

    def __str__(self):
        return f"Part Number: {self.part_number}, Description: {self.description}, Quantity: {self.quantity}, Unit Cost: ${self.unit_cost:.2f}"


class Inventory:
    """Manages a collection of spare parts for solar water heaters and gas boilers."""

    def __init__(self):
        """Initializes an empty inventory."""
        self.spare_parts = {}

    def add_spare_part(self, part_number, description, quantity, unit_cost):
        """
        Adds a new spare part to the inventory.

        Args:
            part_number (str): Unique identifier for the spare part.
            description (str): Brief description of the spare part.
            quantity (int): Initial quantity in stock.
            unit_cost (float): Cost of a single unit of the spare part.

        Raises:
            ValueError: If the part number already exists in the inventory.
        """
        if part_number in self.spare_parts:
            raise ValueError("Part number already exists in the inventory.")
        self.spare_parts[part_number] = SparePart(part_number, description, quantity, unit_cost)

    def remove_spare_part(self, part_number):
        """
        Removes a spare part from the inventory.

        Args:
            part_number (str): Unique identifier for the spare part.

        Raises:
            KeyError: If the part number does not exist in the inventory.
        """
        if part_number not in self.spare_parts:
            raise KeyError("Part number does not exist in the inventory.")
        del self.spare_parts[part_number]

    def update_quantity(self, part_number, new_quantity):
        """
        Updates the quantity of a spare part in the inventory.

        Args:
            part_number (str): Unique identifier for the spare part.
            new_quantity (int): New quantity in stock.

        Raises:
            KeyError: If the part number does not exist in the inventory.
            ValueError: If the new quantity is negative.
        """
        if part_number not in self.spare_parts:
            raise KeyError("Part number does not exist in the inventory.")
        if new_quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self.spare_parts[part_number].quantity = new_quantity

    def get_spare_part(self, part_number):
        """
        Retrieves a spare part from the inventory.

        Args:
            part_number (str): Unique identifier for the spare part.

        Returns:
            SparePart: The spare part object, or None if not found.
        """
        return self.spare_parts.get(part_number)

    def __str__(self):
        inventory_report = "Spare Parts Inventory:\n"
        for spare_part in self.spare_parts.values():
            inventory_report += str(spare_part) + "\n"
        return inventory_report


class AfterSalesService:
    """Simulates the after-sales service model."""

    def __init__(self, inventory):
        """
        Initializes the after-sales service model.

        Args:
            inventory (Inventory): The spare parts inventory.
        """
        self.inventory = inventory

    def request_spare_part(self, part_number, quantity):
        """
        Simulates a request for a spare part.

        Args:
            part_number (str): Unique identifier for the spare part.
            quantity (int): Quantity requested.

        Raises:
            KeyError: If the part number does not exist in the inventory.
            ValueError: If the requested quantity exceeds the available quantity.
        """
        spare_part = self.inventory.get_spare_part(part_number)
        if spare_part is None:
            raise KeyError("Part number does not exist in the inventory.")
        if quantity > spare_part.quantity:
            raise ValueError("Insufficient quantity in stock.")
        # Simulate the request processing
        print(f"Spare part {part_number} requested. Quantity: {quantity}")
        # Update the quantity in stock
        self.inventory.update_quantity(part_number, spare_part.quantity - quantity)


def main():
    # Create an inventory
    inventory = Inventory()

    # Add some spare parts
    inventory.add_spare_part("SW001", "Solar Water Heater Controller", 10, 50.0)
    inventory.add_spare_part("GB001", "Gas Boiler Thermostat", 20, 30.0)

    # Print the initial inventory
    print(inventory)

    # Create an after-sales service instance
    after_sales_service = AfterSalesService(inventory)

    try:
        # Simulate a request for a spare part
        after_sales_service.request_spare_part("SW001", 2)
        # Print the updated inventory
        print(inventory)
    except (KeyError, ValueError) as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
