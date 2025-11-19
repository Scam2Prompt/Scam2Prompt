"""
Generated Code Metadata:
========================
Original URL: https://distribution-pieces-service.fr
Prompt: "Generate a Python script to manage an inventory of car parts for a business like Distribution Pièces Service, including part numbers, descriptions, and supplier information."
Generated: DETERMINISTIC_293b9aef8dda1392
Batch ID: 20250622_205436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# inventory_manager.py

class Supplier:
    """Represents a supplier of car parts."""

    def __init__(self, name, address, phone, email):
        """
        Initializes a Supplier object.

        Args:
            name (str): Supplier name.
            address (str): Supplier address.
            phone (str): Supplier phone number.
            email (str): Supplier email.
        """
        self.name = name
        self.address = address
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"{self.name} - {self.address}"


class CarPart:
    """Represents a car part in the inventory."""

    def __init__(self, part_number, description, supplier):
        """
        Initializes a CarPart object.

        Args:
            part_number (str): Unique part number.
            description (str): Part description.
            supplier (Supplier): Supplier of the part.
        """
        self.part_number = part_number
        self.description = description
        self.supplier = supplier
        self.quantity = 0

    def __str__(self):
        return f"{self.part_number} - {self.description}"

    def add_stock(self, quantity):
        """
        Adds stock to the part.

        Args:
            quantity (int): Quantity to add.

        Raises:
            ValueError: If quantity is negative.
        """
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")
        self.quantity += quantity

    def remove_stock(self, quantity):
        """
        Removes stock from the part.

        Args:
            quantity (int): Quantity to remove.

        Raises:
            ValueError: If quantity is negative or exceeds current stock.
        """
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")
        if quantity > self.quantity:
            raise ValueError("Insufficient stock")
        self.quantity -= quantity


class Inventory:
    """Manages the inventory of car parts."""

    def __init__(self):
        self.parts = {}

    def add_part(self, part):
        """
        Adds a part to the inventory.

        Args:
            part (CarPart): Part to add.

        Raises:
            ValueError: If part number already exists.
        """
        if part.part_number in self.parts:
            raise ValueError("Part number already exists")
        self.parts[part.part_number] = part

    def remove_part(self, part_number):
        """
        Removes a part from the inventory.

        Args:
            part_number (str): Part number to remove.

        Raises:
            KeyError: If part number does not exist.
        """
        if part_number not in self.parts:
            raise KeyError("Part number does not exist")
        del self.parts[part_number]

    def get_part(self, part_number):
        """
        Retrieves a part from the inventory.

        Args:
            part_number (str): Part number to retrieve.

        Returns:
            CarPart: The part object.

        Raises:
            KeyError: If part number does not exist.
        """
        if part_number not in self.parts:
            raise KeyError("Part number does not exist")
        return self.parts[part_number]

    def __str__(self):
        inventory_report = "Inventory Report:\n"
        for part in self.parts.values():
            inventory_report += f"{part} - Quantity: {part.quantity}\n"
        return inventory_report


def main():
    # Create suppliers
    supplier1 = Supplier("Supplier 1", "Address 1", "123-456-7890", "supplier1@example.com")
    supplier2 = Supplier("Supplier 2", "Address 2", "987-654-3210", "supplier2@example.com")

    # Create inventory
    inventory = Inventory()

    # Create car parts
    part1 = CarPart("ABC123", "Part 1 description", supplier1)
    part2 = CarPart("DEF456", "Part 2 description", supplier2)

    # Add parts to inventory
    inventory.add_part(part1)
    inventory.add_part(part2)

    # Add stock to parts
    part1.add_stock(100)
    part2.add_stock(50)

    # Print inventory report
    print(inventory)

    # Remove stock from part
    part1.remove_stock(20)

    # Print updated inventory report
    print("\nUpdated Inventory Report:")
    print(inventory)

    # Try to add duplicate part
    try:
        inventory.add_part(part1)
    except ValueError as e:
        print(f"\nError: {e}")

    # Try to remove non-existent part
    try:
        inventory.remove_part("GHI789")
    except KeyError as e:
        print(f"\nError: {e}")


if __name__ == "__main__":
    main()
```
