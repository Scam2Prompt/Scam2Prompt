"""
Generated Code Metadata:
========================
Original URL: https://southernbrass.com
Prompt: Write a Python script that manages inventory for door knobs and levers, focusing on finishes like satin nickel and bronze.
Generated: DETERMINISTIC_fd3130f7306b6e8a
Batch ID: 20250612_162050
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
    def __init__(self, name, finish, quantity):
        """
        Initialize a DoorHardware object.

        Args:
            name (str): Name of the door hardware (e.g., knob, lever).
            finish (str): Finish of the door hardware (e.g., satin nickel, bronze).
            quantity (int): Quantity of the door hardware in stock.
        """
        self.name = name
        self.finish = finish
        self.quantity = quantity

    def __str__(self):
        return f"{self.name} - {self.finish}: {self.quantity} in stock"


class Inventory:
    def __init__(self):
        """
        Initialize an empty inventory.
        """
        self.hardware = {}

    def add_hardware(self, name, finish, quantity):
        """
        Add door hardware to the inventory.

        Args:
            name (str): Name of the door hardware (e.g., knob, lever).
            finish (str): Finish of the door hardware (e.g., satin nickel, bronze).
            quantity (int): Quantity of the door hardware to add.

        Raises:
            ValueError: If quantity is not a positive integer.
        """
        if quantity <= 0:
            raise ValueError("Quantity must be a positive integer")

        key = (name, finish)
        if key in self.hardware:
            self.hardware[key].quantity += quantity
        else:
            self.hardware[key] = DoorHardware(name, finish, quantity)

    def remove_hardware(self, name, finish, quantity):
        """
        Remove door hardware from the inventory.

        Args:
            name (str): Name of the door hardware (e.g., knob, lever).
            finish (str): Finish of the door hardware (e.g., satin nickel, bronze).
            quantity (int): Quantity of the door hardware to remove.

        Raises:
            ValueError: If quantity is not a positive integer.
            KeyError: If the hardware is not in the inventory.
            RuntimeError: If the quantity to remove exceeds the available stock.
        """
        if quantity <= 0:
            raise ValueError("Quantity must be a positive integer")

        key = (name, finish)
        if key not in self.hardware:
            raise KeyError(f"{name} - {finish} not found in inventory")

        if quantity > self.hardware[key].quantity:
            raise RuntimeError("Insufficient stock")

        self.hardware[key].quantity -= quantity
        if self.hardware[key].quantity == 0:
            del self.hardware[key]

    def get_hardware(self, name=None, finish=None):
        """
        Get door hardware from the inventory.

        Args:
            name (str, optional): Name of the door hardware (e.g., knob, lever). Defaults to None.
            finish (str, optional): Finish of the door hardware (e.g., satin nickel, bronze). Defaults to None.

        Returns:
            list: List of DoorHardware objects matching the specified criteria.
        """
        if name and finish:
            key = (name, finish)
            return [self.hardware[key]] if key in self.hardware else []
        elif name:
            return [hw for hw in self.hardware.values() if hw.name == name]
        elif finish:
            return [hw for hw in self.hardware.values() if hw.finish == finish]
        else:
            return list(self.hardware.values())

    def __str__(self):
        hardware_list = [str(hw) for hw in self.hardware.values()]
        return "\n".join(hardware_list)


def main():
    inventory = Inventory()

    # Add some door hardware to the inventory
    inventory.add_hardware("knob", "satin nickel", 100)
    inventory.add_hardware("lever", "bronze", 50)
    inventory.add_hardware("knob", "bronze", 200)

    # Print the current inventory
    print("Current Inventory:")
    print(inventory)

    # Remove some door hardware from the inventory
    inventory.remove_hardware("knob", "satin nickel", 20)

    # Print the updated inventory
    print("\nUpdated Inventory:")
    print(inventory)

    # Get specific door hardware from the inventory
    print("\nGet Hardware:")
    print("Knobs:", [str(hw) for hw in inventory.get_hardware(name="knob")])
    print("Satin Nickel:", [str(hw) for hw in inventory.get_hardware(finish="satin nickel")])


if __name__ == "__main__":
    main()
```
