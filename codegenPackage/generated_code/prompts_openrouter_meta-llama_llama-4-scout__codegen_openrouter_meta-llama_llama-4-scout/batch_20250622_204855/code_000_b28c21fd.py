"""
Generated Code Metadata:
========================
Original URL: https://esp-gala-games-app.blogspot.com
Prompt: Write a Python code snippet to catalog sports equipment inventory for a store like Loja dos Esportes, including items like beach volleyball gear and basketball equipment.
Generated: DETERMINISTIC_b28c21fdf5137268
Batch ID: 20250622_204855
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# sports_equipment_inventory.py

class SportsEquipment:
    def __init__(self, name, quantity, price):
        """
        Initialize a SportsEquipment object.

        Args:
            name (str): Name of the equipment.
            quantity (int): Quantity of the equipment in stock.
            price (float): Price of the equipment.
        """
        self.name = name
        self.quantity = quantity
        self.price = price

    def __str__(self):
        return f"{self.name}: {self.quantity} units @ R${self.price:.2f} each"


class Inventory:
    def __init__(self):
        """
        Initialize an empty inventory.
        """
        self.equipment = {}

    def add_equipment(self, equipment):
        """
        Add equipment to the inventory.

        Args:
            equipment (SportsEquipment): Equipment to add.

        Raises:
            ValueError: If equipment with the same name already exists.
        """
        if equipment.name in self.equipment:
            raise ValueError(f"Equipment '{equipment.name}' already exists in the inventory.")
        self.equipment[equipment.name] = equipment

    def remove_equipment(self, name):
        """
        Remove equipment from the inventory.

        Args:
            name (str): Name of the equipment to remove.

        Raises:
            KeyError: If equipment does not exist in the inventory.
        """
        if name not in self.equipment:
            raise KeyError(f"Equipment '{name}' does not exist in the inventory.")
        del self.equipment[name]

    def update_quantity(self, name, quantity):
        """
        Update the quantity of equipment in the inventory.

        Args:
            name (str): Name of the equipment to update.
            quantity (int): New quantity.

        Raises:
            KeyError: If equipment does not exist in the inventory.
            ValueError: If quantity is negative.
        """
        if name not in self.equipment:
            raise KeyError(f"Equipment '{name}' does not exist in the inventory.")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self.equipment[name].quantity = quantity

    def __str__(self):
        inventory_str = "Sports Equipment Inventory:\n"
        for equipment in self.equipment.values():
            inventory_str += f"- {equipment}\n"
        return inventory_str


def main():
    # Create an inventory
    inventory = Inventory()

    try:
        # Add equipment to the inventory
        beach_volleyball = SportsEquipment("Beach Volleyball", 10, 50.0)
        basketball = SportsEquipment("Basketball", 20, 30.0)
        volleyball_net = SportsEquipment("Volleyball Net", 5, 100.0)

        inventory.add_equipment(beach_volleyball)
        inventory.add_equipment(basketball)
        inventory.add_equipment(volleyball_net)

        # Print the inventory
        print(inventory)

        # Update quantity
        inventory.update_quantity("Beach Volleyball", 15)
        print("\nUpdated Inventory:")
        print(inventory)

        # Remove equipment
        inventory.remove_equipment("Volleyball Net")
        print("\nInventory after removal:")
        print(inventory)

    except (ValueError, KeyError) as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
