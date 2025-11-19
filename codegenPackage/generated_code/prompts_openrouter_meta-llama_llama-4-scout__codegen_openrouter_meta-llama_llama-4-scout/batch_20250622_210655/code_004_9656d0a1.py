"""
Generated Code Metadata:
========================
Original URL: https://sarl-verdier-irrigation.fr
Prompt: "Generate a code snippet for tracking inventory of agricultural equipment, including motoculture and irrigation systems, for a company like SARL VERDIER IRRIGATION."
Generated: DETERMINISTIC_9656d0a145c4c835
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# inventory_tracker.py

class Equipment:
    """Represents an agricultural equipment."""

    def __init__(self, equipment_id, name, type, quantity):
        """
        Initializes an Equipment object.

        Args:
            equipment_id (int): Unique identifier for the equipment.
            name (str): Name of the equipment.
            type (str): Type of the equipment (e.g., motoculture, irrigation).
            quantity (int): Quantity of the equipment in stock.
        """
        self.equipment_id = equipment_id
        self.name = name
        self.type = type
        self.quantity = quantity

    def __str__(self):
        return f"Equipment ID: {self.equipment_id}, Name: {self.name}, Type: {self.type}, Quantity: {self.quantity}"


class Inventory:
    """Manages the inventory of agricultural equipment."""

    def __init__(self):
        """Initializes an empty inventory."""
        self.equipment = {}

    def add_equipment(self, equipment):
        """
        Adds equipment to the inventory.

        Args:
            equipment (Equipment): Equipment object to add.

        Raises:
            ValueError: If equipment with the same ID already exists.
        """
        if equipment.equipment_id in self.equipment:
            raise ValueError("Equipment with the same ID already exists.")
        self.equipment[equipment.equipment_id] = equipment

    def remove_equipment(self, equipment_id):
        """
        Removes equipment from the inventory.

        Args:
            equipment_id (int): ID of the equipment to remove.

        Raises:
            KeyError: If equipment with the given ID does not exist.
        """
        if equipment_id not in self.equipment:
            raise KeyError("Equipment with the given ID does not exist.")
        del self.equipment[equipment_id]

    def update_quantity(self, equipment_id, new_quantity):
        """
        Updates the quantity of equipment in the inventory.

        Args:
            equipment_id (int): ID of the equipment to update.
            new_quantity (int): New quantity of the equipment.

        Raises:
            KeyError: If equipment with the given ID does not exist.
            ValueError: If new quantity is negative.
        """
        if equipment_id not in self.equipment:
            raise KeyError("Equipment with the given ID does not exist.")
        if new_quantity < 0:
            raise ValueError("New quantity cannot be negative.")
        self.equipment[equipment_id].quantity = new_quantity

    def get_equipment(self, equipment_id):
        """
        Retrieves equipment from the inventory.

        Args:
            equipment_id (int): ID of the equipment to retrieve.

        Returns:
            Equipment: Equipment object if found, None otherwise.
        """
        return self.equipment.get(equipment_id)

    def __str__(self):
        inventory_str = "Inventory:\n"
        for equipment in self.equipment.values():
            inventory_str += str(equipment) + "\n"
        return inventory_str


def main():
    # Create an inventory
    inventory = Inventory()

    try:
        # Add equipment
        motoculture = Equipment(1, "Tractor", "Motoculture", 5)
        irrigation_system = Equipment(2, "Drip Irrigation System", "Irrigation", 10)
        inventory.add_equipment(motoculture)
        inventory.add_equipment(irrigation_system)

        # Print inventory
        print(inventory)

        # Update quantity
        inventory.update_quantity(1, 3)
        print("Updated Inventory:")
        print(inventory)

        # Remove equipment
        inventory.remove_equipment(2)
        print("Updated Inventory after removal:")
        print(inventory)

    except (ValueError, KeyError) as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
