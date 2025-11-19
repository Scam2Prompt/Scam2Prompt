"""
Generated Code Metadata:
========================
Original URL: https://vgtindia.in
Prompt: "Write a Python code snippet to manage inventory for a company like Vinglob Greentech that manufactures agriculture equipment."
Generated: DETERMINISTIC_c7ae22900a8e58b1
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# inventory_management.py

class Equipment:
    """Represents an agriculture equipment."""

    def __init__(self, equipment_id, name, quantity, price):
        """
        Initializes an Equipment object.

        Args:
            equipment_id (int): Unique identifier for the equipment.
            name (str): Name of the equipment.
            quantity (int): Quantity of the equipment in stock.
            price (float): Price of the equipment.
        """
        self.equipment_id = equipment_id
        self.name = name
        self.quantity = quantity
        self.price = price

    def __str__(self):
        return f"Equipment ID: {self.equipment_id}, Name: {self.name}, Quantity: {self.quantity}, Price: ${self.price:.2f}"


class Inventory:
    """Manages the inventory of agriculture equipment."""

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

    def list_equipment(self):
        """Lists all equipment in the inventory."""
        return list(self.equipment.values())


def main():
    # Create an inventory
    inventory = Inventory()

    try:
        # Create equipment
        equipment1 = Equipment(1, "Tractor", 10, 50000.0)
        equipment2 = Equipment(2, "Plow", 20, 2000.0)

        # Add equipment to the inventory
        inventory.add_equipment(equipment1)
        inventory.add_equipment(equipment2)

        # List equipment
        print("Equipment List:")
        for equipment in inventory.list_equipment():
            print(equipment)

        # Update quantity
        inventory.update_quantity(1, 15)

        # Get equipment
        equipment = inventory.get_equipment(1)
        print("\nUpdated Equipment:")
        print(equipment)

        # Remove equipment
        inventory.remove_equipment(2)

        # List equipment after removal
        print("\nEquipment List after removal:")
        for equipment in inventory.list_equipment():
            print(equipment)

    except (ValueError, KeyError) as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
