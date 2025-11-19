"""
Generated Code Metadata:
========================
Original URL: https://biamtechintl.com
Prompt: "Write a Python code snippet to manage inventory of laparoscopic instruments, including graspers, scissors, trocars, and dissectors."
Generated: DETERMINISTIC_de2d313c1a6cbad2
Batch ID: 20250622_205955
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# laparoscopic_instrument_inventory.py

class LaparoscopicInstrument:
    """Base class for laparoscopic instruments."""

    def __init__(self, name, quantity):
        """
        Initialize an instrument.

        Args:
            name (str): Name of the instrument.
            quantity (int): Initial quantity of the instrument.
        """
        self.name = name
        self.quantity = quantity

    def __str__(self):
        return f"{self.name}: {self.quantity}"


class Grasper(LaparoscopicInstrument):
    """Class for graspers."""

    def __init__(self, name, quantity, jaw_size):
        """
        Initialize a grasper.

        Args:
            name (str): Name of the grasper.
            quantity (int): Initial quantity of the grasper.
            jaw_size (float): Jaw size of the grasper in mm.
        """
        super().__init__(name, quantity)
        self.jaw_size = jaw_size

    def __str__(self):
        return f"Grasper {super().__str__()}, Jaw Size: {self.jaw_size}mm"


class Scissors(LaparoscopicInstrument):
    """Class for scissors."""

    def __init__(self, name, quantity, blade_type):
        """
        Initialize scissors.

        Args:
            name (str): Name of the scissors.
            quantity (int): Initial quantity of the scissors.
            blade_type (str): Type of blade (e.g., curved, straight).
        """
        super().__init__(name, quantity)
        self.blade_type = blade_type

    def __str__(self):
        return f"Scissors {super().__str__()}, Blade Type: {self.blade_type}"


class Trocars(LaparoscopicInstrument):
    """Class for trocars."""

    def __init__(self, name, quantity, diameter):
        """
        Initialize trocars.

        Args:
            name (str): Name of the trocars.
            quantity (int): Initial quantity of the trocars.
            diameter (float): Diameter of the trocars in mm.
        """
        super().__init__(name, quantity)
        self.diameter = diameter

    def __str__(self):
        return f"Trocars {super().__str__()}, Diameter: {self.diameter}mm"


class Dissector(LaparoscopicInstrument):
    """Class for dissectors."""

    def __init__(self, name, quantity, tip_type):
        """
        Initialize dissectors.

        Args:
            name (str): Name of the dissectors.
            quantity (int): Initial quantity of the dissectors.
            tip_type (str): Type of tip (e.g., blunt, sharp).
        """
        super().__init__(name, quantity)
        self.tip_type = tip_type

    def __str__(self):
        return f"Dissector {super().__str__()}, Tip Type: {self.tip_type}"


class Inventory:
    """Class to manage inventory of laparoscopic instruments."""

    def __init__(self):
        self.instruments = []

    def add_instrument(self, instrument):
        """
        Add an instrument to the inventory.

        Args:
            instrument (LaparoscopicInstrument): Instrument to add.

        Raises:
            ValueError: If instrument quantity is less than 0.
        """
        if instrument.quantity < 0:
            raise ValueError("Instrument quantity cannot be less than 0")
        self.instruments.append(instrument)

    def remove_instrument(self, instrument_name):
        """
        Remove an instrument from the inventory.

        Args:
            instrument_name (str): Name of the instrument to remove.

        Raises:
            ValueError: If instrument is not found in the inventory.
        """
        for instrument in self.instruments:
            if instrument.name == instrument_name:
                self.instruments.remove(instrument)
                return
        raise ValueError("Instrument not found in the inventory")

    def update_quantity(self, instrument_name, new_quantity):
        """
        Update the quantity of an instrument.

        Args:
            instrument_name (str): Name of the instrument to update.
            new_quantity (int): New quantity of the instrument.

        Raises:
            ValueError: If instrument is not found in the inventory or new quantity is less than 0.
        """
        for instrument in self.instruments:
            if instrument.name == instrument_name:
                if new_quantity < 0:
                    raise ValueError("Instrument quantity cannot be less than 0")
                instrument.quantity = new_quantity
                return
        raise ValueError("Instrument not found in the inventory")

    def __str__(self):
        inventory_str = "Laparoscopic Instrument Inventory:\n"
        for instrument in self.instruments:
            inventory_str += f"- {instrument}\n"
        return inventory_str


def main():
    # Create an inventory
    inventory = Inventory()

    # Create instruments
    grasper = Grasper("Grasper 1", 5, 10.0)
    scissors = Scissors("Scissors 1", 3, "curved")
    trocars = Trocars("Trocars 1", 10, 5.0)
    dissector = Dissector("Dissector 1", 2, "blunt")

    # Add instruments to the inventory
    inventory.add_instrument(grasper)
    inventory.add_instrument(scissors)
    inventory.add_instrument(trocars)
    inventory.add_instrument(dissector)

    # Print the inventory
    print(inventory)

    # Update quantity of an instrument
    inventory.update_quantity("Grasper 1", 7)

    # Print the updated inventory
    print("\nUpdated Inventory:")
    print(inventory)

    # Remove an instrument from the inventory
    inventory.remove_instrument("Scissors 1")

    # Print the updated inventory
    print("\nUpdated Inventory after removal:")
    print(inventory)


if __name__ == "__main__":
    main()
```
