"""
Generated Code Metadata:
========================
Original URL: https://www.cymrepuestos.com.ar
Prompt: "Write a Python script to manage an inventory of automotive spare parts, including batteries, alternators, starters, lighting, suspension, lubricants, and filters."
Generated: DETERMINISTIC_b367b231ab3937c7
Batch ID: 20250622_212100
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# inventory_manager.py

class SparePart:
    """Base class for all spare parts."""

    def __init__(self, part_number, description, quantity, price):
        """
        Initialize a spare part.

        Args:
            part_number (str): Unique part number.
            description (str): Brief description of the part.
            quantity (int): Current quantity in stock.
            price (float): Price of the part.
        """
        self.part_number = part_number
        self.description = description
        self.quantity = quantity
        self.price = price

    def __str__(self):
        return f"{self.part_number} - {self.description}, Quantity: {self.quantity}, Price: ${self.price:.2f}"


class Battery(SparePart):
    """Represents a battery spare part."""

    def __init__(self, part_number, description, quantity, price, voltage, ampere):
        """
        Initialize a battery.

        Args:
            part_number (str): Unique part number.
            description (str): Brief description of the battery.
            quantity (int): Current quantity in stock.
            price (float): Price of the battery.
            voltage (int): Voltage rating.
            ampere (int): Ampere rating.
        """
        super().__init__(part_number, description, quantity, price)
        self.voltage = voltage
        self.ampere = ampere

    def __str__(self):
        return super().__str__() + f", Voltage: {self.voltage}V, Ampere: {self.ampere}A"


class Alternator(SparePart):
    """Represents an alternator spare part."""

    def __init__(self, part_number, description, quantity, price, wattage):
        """
        Initialize an alternator.

        Args:
            part_number (str): Unique part number.
            description (str): Brief description of the alternator.
            quantity (int): Current quantity in stock.
            price (float): Price of the alternator.
            wattage (int): Wattage rating.
        """
        super().__init__(part_number, description, quantity, price)
        self.wattage = wattage

    def __str__(self):
        return super().__str__() + f", Wattage: {self.wattage}W"


class Starter(SparePart):
    """Represents a starter spare part."""

    def __init__(self, part_number, description, quantity, price, horsepower):
        """
        Initialize a starter.

        Args:
            part_number (str): Unique part number.
            description (str): Brief description of the starter.
            quantity (int): Current quantity in stock.
            price (float): Price of the starter.
            horsepower (int): Horsepower rating.
        """
        super().__init__(part_number, description, quantity, price)
        self.horsepower = horsepower

    def __str__(self):
        return super().__str__() + f", Horsepower: {self.horsepower}HP"


class Lighting(SparePart):
    """Represents a lighting spare part."""

    def __init__(self, part_number, description, quantity, price, lumens):
        """
        Initialize a lighting part.

        Args:
            part_number (str): Unique part number.
            description (str): Brief description of the lighting.
            quantity (int): Current quantity in stock.
            price (float): Price of the lighting.
            lumens (int): Lumen rating.
        """
        super().__init__(part_number, description, quantity, price)
        self.lumens = lumens

    def __str__(self):
        return super().__str__() + f", Lumens: {self.lumens}lm"


class Suspension(SparePart):
    """Represents a suspension spare part."""

    def __init__(self, part_number, description, quantity, price, type):
        """
        Initialize a suspension part.

        Args:
            part_number (str): Unique part number.
            description (str): Brief description of the suspension.
            quantity (int): Current quantity in stock.
            price (float): Price of the suspension.
            type (str): Type of suspension.
        """
        super().__init__(part_number, description, quantity, price)
        self.type = type

    def __str__(self):
        return super().__str__() + f", Type: {self.type}"


class Lubricant(SparePart):
    """Represents a lubricant spare part."""

    def __init__(self, part_number, description, quantity, price, viscosity):
        """
        Initialize a lubricant.

        Args:
            part_number (str): Unique part number.
            description (str): Brief description of the lubricant.
            quantity (int): Current quantity in stock.
            price (float): Price of the lubricant.
            viscosity (str): Viscosity rating.
        """
        super().__init__(part_number, description, quantity, price)
        self.viscosity = viscosity

    def __str__(self):
        return super().__str__() + f", Viscosity: {self.viscosity}"


class Filter(SparePart):
    """Represents a filter spare part."""

    def __init__(self, part_number, description, quantity, price, type):
        """
        Initialize a filter.

        Args:
            part_number (str): Unique part number.
            description (str): Brief description of the filter.
            quantity (int): Current quantity in stock.
            price (float): Price of the filter.
            type (str): Type of filter.
        """
        super().__init__(part_number, description, quantity, price)
        self.type = type

    def __str__(self):
        return super().__str__() + f", Type: {self.type}"


class Inventory:
    """Manages an inventory of spare parts."""

    def __init__(self):
        self.parts = []

    def add_part(self, part):
        """
        Add a spare part to the inventory.

        Args:
            part (SparePart): The part to add.
        """
        self.parts.append(part)

    def remove_part(self, part_number):
        """
        Remove a spare part from the inventory.

        Args:
            part_number (str): The part number of the part to remove.

        Raises:
            ValueError: If the part is not found.
        """
        for part in self.parts:
            if part.part_number == part_number:
                self.parts.remove(part)
                return
        raise ValueError("Part not found")

    def update_quantity(self, part_number, new_quantity):
        """
        Update the quantity of a spare part.

        Args:
            part_number (str): The part number of the part to update.
            new_quantity (int): The new quantity.

        Raises:
            ValueError: If the part is not found.
        """
        for part in self.parts:
            if part.part_number == part_number:
                part.quantity = new_quantity
                return
        raise ValueError("Part not found")

    def __str__(self):
        inventory_list = "Spare Parts Inventory:\n"
        for part in self.parts:
            inventory_list += str(part) + "\n"
        return inventory_list


def main():
    # Create an inventory
    inventory = Inventory()

    # Create some spare parts
    battery = Battery("B001", "Car Battery", 10, 50.99, 12, 60)
    alternator = Alternator("A001", "Car Alternator", 5, 100.99, 100)
    starter = Starter("S001", "Car Starter", 8, 75.99, 1)
    lighting = Lighting("L001", "Headlight Bulb", 20, 5.99, 1000)
    suspension = Suspension("SU001", "Shock Absorber", 12, 30.99, "Coil Spring")
    lubricant = Lubricant("LU001", "Engine Oil", 15, 20.99, "5W-30")
    filter = Filter("F001", "Air Filter", 10, 10.99, "Paper")

    # Add parts to the inventory
    inventory.add_part(battery)
    inventory.add_part(alternator)
    inventory.add_part(starter)
    inventory.add_part(lighting)
    inventory.add_part(suspension)
    inventory.add_part(lubricant)
    inventory.add_part(filter)

    # Print the inventory
    print(inventory)

    # Update quantity and print again
    inventory.update_quantity("B001", 8)
    print("\nUpdated Inventory:")
    print(inventory)

    # Remove a part and print again
    inventory.remove_part("A001")
    print("\nUpdated Inventory after removal:")
    print(inventory)


if __name__ == "__main__":
    main()
```
