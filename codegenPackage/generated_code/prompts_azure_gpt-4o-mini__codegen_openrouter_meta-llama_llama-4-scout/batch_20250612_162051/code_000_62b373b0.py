"""
Generated Code Metadata:
========================
Original URL: https://shop.isabelreinachic.com
Prompt: Generate a code snippet for a sewing machine inventory management system that includes features for tracking mechanical and electronic sewing machines, overlockers, and accessories available at Isabel Reina Chic.
Generated: DETERMINISTIC_62b373b07e4a7c28
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# sewing_machine_inventory.py

class SewingMachine:
    def __init__(self, machine_id, machine_type, brand, model, price):
        """
        Initialize a SewingMachine object.

        Args:
            machine_id (int): Unique identifier for the machine.
            machine_type (str): Type of sewing machine (mechanical or electronic).
            brand (str): Brand of the machine.
            model (str): Model of the machine.
            price (float): Price of the machine.
        """
        self.machine_id = machine_id
        self.machine_type = machine_type
        self.brand = brand
        self.model = model
        self.price = price

    def __str__(self):
        return f"Machine ID: {self.machine_id}, Type: {self.machine_type}, Brand: {self.brand}, Model: {self.model}, Price: ${self.price:.2f}"


class Overlocker:
    def __init__(self, overlocker_id, brand, model, price):
        """
        Initialize an Overlocker object.

        Args:
            overlocker_id (int): Unique identifier for the overlocker.
            brand (str): Brand of the overlocker.
            model (str): Model of the overlocker.
            price (float): Price of the overlocker.
        """
        self.overlocker_id = overlocker_id
        self.brand = brand
        self.model = model
        self.price = price

    def __str__(self):
        return f"Overlocker ID: {self.overlocker_id}, Brand: {self.brand}, Model: {self.model}, Price: ${self.price:.2f}"


class Accessory:
    def __init__(self, accessory_id, name, price):
        """
        Initialize an Accessory object.

        Args:
            accessory_id (int): Unique identifier for the accessory.
            name (str): Name of the accessory.
            price (float): Price of the accessory.
        """
        self.accessory_id = accessory_id
        self.name = name
        self.price = price

    def __str__(self):
        return f"Accessory ID: {self.accessory_id}, Name: {self.name}, Price: ${self.price:.2f}"


class Inventory:
    def __init__(self):
        """
        Initialize an Inventory object.
        """
        self.sewing_machines = []
        self.overlockers = []
        self.accessories = []

    def add_sewing_machine(self, machine):
        """
        Add a sewing machine to the inventory.

        Args:
            machine (SewingMachine): SewingMachine object to add.
        """
        self.sewing_machines.append(machine)

    def add_overlocker(self, overlocker):
        """
        Add an overlocker to the inventory.

        Args:
            overlocker (Overlocker): Overlocker object to add.
        """
        self.overlockers.append(overlocker)

    def add_accessory(self, accessory):
        """
        Add an accessory to the inventory.

        Args:
            accessory (Accessory): Accessory object to add.
        """
        self.accessories.append(accessory)

    def remove_sewing_machine(self, machine_id):
        """
        Remove a sewing machine from the inventory.

        Args:
            machine_id (int): ID of the machine to remove.

        Raises:
            ValueError: If the machine is not found in the inventory.
        """
        for machine in self.sewing_machines:
            if machine.machine_id == machine_id:
                self.sewing_machines.remove(machine)
                return
        raise ValueError("Machine not found in inventory")

    def remove_overlocker(self, overlocker_id):
        """
        Remove an overlocker from the inventory.

        Args:
            overlocker_id (int): ID of the overlocker to remove.

        Raises:
            ValueError: If the overlocker is not found in the inventory.
        """
        for overlocker in self.overlockers:
            if overlocker.overlocker_id == overlocker_id:
                self.overlockers.remove(overlocker)
                return
        raise ValueError("Overlocker not found in inventory")

    def remove_accessory(self, accessory_id):
        """
        Remove an accessory from the inventory.

        Args:
            accessory_id (int): ID of the accessory to remove.

        Raises:
            ValueError: If the accessory is not found in the inventory.
        """
        for accessory in self.accessories:
            if accessory.accessory_id == accessory_id:
                self.accessories.remove(accessory)
                return
        raise ValueError("Accessory not found in inventory")

    def __str__(self):
        inventory_str = "Sewing Machines:\n"
        for machine in self.sewing_machines:
            inventory_str += str(machine) + "\n"
        inventory_str += "\nOverlockers:\n"
        for overlocker in self.overlockers:
            inventory_str += str(overlocker) + "\n"
        inventory_str += "\nAccessories:\n"
        for accessory in self.accessories:
            inventory_str += str(accessory) + "\n"
        return inventory_str


def main():
    # Create an inventory
    inventory = Inventory()

    # Add some sewing machines
    machine1 = SewingMachine(1, "mechanical", "Brother", "FS100", 100.0)
    machine2 = SewingMachine(2, "electronic", "Janome", "Magnolia 7318", 500.0)
    inventory.add_sewing_machine(machine1)
    inventory.add_sewing_machine(machine2)

    # Add some overlockers
    overlocker1 = Overlocker(1, "Baby Lock", "BL9", 200.0)
    overlocker2 = Overlocker(2, "Jersey", "Coverstitch", 300.0)
    inventory.add_overlocker(overlocker1)
    inventory.add_overlocker(overlocker2)

    # Add some accessories
    accessory1 = Accessory(1, "Sewing needles", 10.0)
    accessory2 = Accessory(2, "Thread set", 20.0)
    inventory.add_accessory(accessory1)
    inventory.add_accessory(accessory2)

    # Print the inventory
    print(inventory)

    # Remove a sewing machine
    try:
        inventory.remove_sewing_machine(1)
        print("Machine removed successfully")
    except ValueError as e:
        print(e)

    # Print the updated inventory
    print("\nUpdated Inventory:")
    print(inventory)


if __name__ == "__main__":
    main()
```
