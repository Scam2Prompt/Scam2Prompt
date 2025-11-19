"""
Generated Code Metadata:
========================
Original URL: https://theprintnan.app
Prompt: "Write a Python script to manage inventory of materials like อะคริลิคสี, ฟิว, and โฟมบอร์ด for a custom printing business."
Generated: DETERMINISTIC_6f36d68146d12ad4
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# inventory_manager.py

class Material:
    """Represents a material in the inventory."""

    def __init__(self, name, quantity, unit_price):
        """
        Initializes a Material object.

        Args:
            name (str): Name of the material.
            quantity (int): Quantity of the material in stock.
            unit_price (float): Unit price of the material.
        """
        self.name = name
        self.quantity = quantity
        self.unit_price = unit_price

    def __str__(self):
        return f"{self.name}: {self.quantity} units @ ${self.unit_price:.2f}/unit"


class Inventory:
    """Manages the inventory of materials."""

    def __init__(self):
        """Initializes an empty inventory."""
        self.materials = {}

    def add_material(self, material):
        """
        Adds a material to the inventory.

        Args:
            material (Material): Material to add.

        Raises:
            ValueError: If a material with the same name already exists.
        """
        if material.name in self.materials:
            raise ValueError(f"Material '{material.name}' already exists.")
        self.materials[material.name] = material

    def remove_material(self, name):
        """
        Removes a material from the inventory.

        Args:
            name (str): Name of the material to remove.

        Raises:
            KeyError: If the material does not exist.
        """
        if name not in self.materials:
            raise KeyError(f"Material '{name}' does not exist.")
        del self.materials[name]

    def update_quantity(self, name, quantity):
        """
        Updates the quantity of a material.

        Args:
            name (str): Name of the material to update.
            quantity (int): New quantity.

        Raises:
            KeyError: If the material does not exist.
            ValueError: If the quantity is negative.
        """
        if name not in self.materials:
            raise KeyError(f"Material '{name}' does not exist.")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self.materials[name].quantity = quantity

    def get_material(self, name):
        """
        Retrieves a material by name.

        Args:
            name (str): Name of the material to retrieve.

        Returns:
            Material: The material object.

        Raises:
            KeyError: If the material does not exist.
        """
        if name not in self.materials:
            raise KeyError(f"Material '{name}' does not exist.")
        return self.materials[name]

    def __str__(self):
        inventory_list = "\n".join(str(material) for material in self.materials.values())
        return f"Inventory:\n{inventory_list}"


def main():
    # Create an inventory
    inventory = Inventory()

    # Add materials
    materials = [
        Material("อะคริลิคสี", 100, 50.0),
        Material("ฟิว", 50, 20.0),
        Material("โฟมบอร์ด", 200, 30.0),
    ]
    for material in materials:
        try:
            inventory.add_material(material)
        except ValueError as e:
            print(f"Error: {e}")

    # Print initial inventory
    print(inventory)

    # Update quantity
    try:
        inventory.update_quantity("อะคริลิคสี", 80)
    except (KeyError, ValueError) as e:
        print(f"Error: {e}")

    # Print updated inventory
    print("\nUpdated Inventory:")
    print(inventory)

    # Get material
    try:
        material = inventory.get_material("ฟิว")
        print(f"\nMaterial: {material}")
    except KeyError as e:
        print(f"Error: {e}")

    # Remove material
    try:
        inventory.remove_material("โฟมบอร์ด")
    except KeyError as e:
        print(f"Error: {e}")

    # Print final inventory
    print("\nFinal Inventory:")
    print(inventory)


if __name__ == "__main__":
    main()
```
