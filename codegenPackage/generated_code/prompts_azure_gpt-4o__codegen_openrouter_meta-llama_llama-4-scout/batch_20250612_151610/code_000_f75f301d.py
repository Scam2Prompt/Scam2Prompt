"""
Generated Code Metadata:
========================
Original URL: https://trackdieselperu.com
Prompt: Write a Python script to manage an inventory system for machinery parts, specifically for brands like FIATALLIS, CATERPILLAR, JOHN DEERE, KOMATSU, and IVECO, as described by Track Diesel Peru.
Generated: DETERMINISTIC_f75f301d3dbfca46
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# inventory_management.py

class MachineryPart:
    """Represents a machinery part with its attributes."""

    def __init__(self, brand, model, part_number, quantity, description):
        """
        Initializes a MachineryPart object.

        Args:
            brand (str): The brand of the machinery part.
            model (str): The model of the machinery part.
            part_number (str): The part number of the machinery part.
            quantity (int): The quantity of the machinery part in stock.
            description (str): A brief description of the machinery part.
        """
        self.brand = brand
        self.model = model
        self.part_number = part_number
        self.quantity = quantity
        self.description = description

    def __str__(self):
        return f"{self.brand} {self.model} - {self.part_number}: {self.quantity} in stock"


class Inventory:
    """Manages an inventory of machinery parts."""

    def __init__(self):
        """Initializes an empty inventory."""
        self.parts = {}

    def add_part(self, part):
        """
        Adds a machinery part to the inventory.

        Args:
            part (MachineryPart): The part to add.

        Raises:
            ValueError: If a part with the same part number already exists.
        """
        if part.part_number in self.parts:
            raise ValueError("Part number already exists in the inventory")
        self.parts[part.part_number] = part

    def remove_part(self, part_number):
        """
        Removes a machinery part from the inventory.

        Args:
            part_number (str): The part number of the part to remove.

        Raises:
            KeyError: If the part number does not exist in the inventory.
        """
        if part_number not in self.parts:
            raise KeyError("Part number does not exist in the inventory")
        del self.parts[part_number]

    def update_quantity(self, part_number, new_quantity):
        """
        Updates the quantity of a machinery part in the inventory.

        Args:
            part_number (str): The part number of the part to update.
            new_quantity (int): The new quantity of the part.

        Raises:
            KeyError: If the part number does not exist in the inventory.
        """
        if part_number not in self.parts:
            raise KeyError("Part number does not exist in the inventory")
        self.parts[part_number].quantity = new_quantity

    def get_part(self, part_number):
        """
        Retrieves a machinery part from the inventory.

        Args:
            part_number (str): The part number of the part to retrieve.

        Returns:
            MachineryPart: The machinery part with the given part number.

        Raises:
            KeyError: If the part number does not exist in the inventory.
        """
        if part_number not in self.parts:
            raise KeyError("Part number does not exist in the inventory")
        return self.parts[part_number]

    def list_parts(self):
        """Returns a list of all machinery parts in the inventory."""
        return list(self.parts.values())


def main():
    # Supported brands
    supported_brands = ["FIATALLIS", "CATERPILLAR", "JOHN DEERE", "KOMATSU", "IVECO"]

    # Create an inventory
    inventory = Inventory()

    while True:
        print("\nInventory Management System")
        print("1. Add part")
        print("2. Remove part")
        print("3. Update quantity")
        print("4. Get part")
        print("5. List parts")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            brand = input("Enter brand (FIATALLIS, CATERPILLAR, JOHN DEERE, KOMATSU, IVECO): ").upper()
            if brand not in supported_brands:
                print("Unsupported brand. Please choose from the supported brands.")
                continue
            model = input("Enter model: ")
            part_number = input("Enter part number: ")
            quantity = int(input("Enter quantity: "))
            description = input("Enter description: ")
            part = MachineryPart(brand, model, part_number, quantity, description)
            try:
                inventory.add_part(part)
                print("Part added successfully.")
            except ValueError as e:
                print(str(e))
        elif choice == "2":
            part_number = input("Enter part number: ")
            try:
                inventory.remove_part(part_number)
                print("Part removed successfully.")
            except KeyError as e:
                print(str(e))
        elif choice == "3":
            part_number = input("Enter part number: ")
            new_quantity = int(input("Enter new quantity: "))
            try:
                inventory.update_quantity(part_number, new_quantity)
                print("Quantity updated successfully.")
            except KeyError as e:
                print(str(e))
        elif choice == "4":
            part_number = input("Enter part number: ")
            try:
                part = inventory.get_part(part_number)
                print(part)
                print(f"Description: {part.description}")
            except KeyError as e:
                print(str(e))
        elif choice == "5":
            parts = inventory.list_parts()
            for part in parts:
                print(part)
        elif choice == "6":
            break
        else:
            print("Invalid option. Please choose a valid option.")

if __name__ == "__main__":
    main()
```
