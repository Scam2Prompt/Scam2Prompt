"""
Generated Code Metadata:
========================
Original URL: https://fabricarecosmeticos.ind.br
Prompt: Create a script to automate the process of managing raw material inventory for high-performance cosmetic production, based on Fabricare Cosméticos' emphasis on advanced technology and rich active ingredients.
Generated: DETERMINISTIC_6317ae913246c583
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# inventory_manager.py

class RawMaterial:
    """Represents a raw material in the inventory."""

    def __init__(self, id: int, name: str, quantity: float, unit_price: float):
        """
        Initializes a RawMaterial object.

        Args:
        id (int): Unique identifier for the raw material.
        name (str): Name of the raw material.
        quantity (float): Current quantity of the raw material in stock.
        unit_price (float): Unit price of the raw material.
        """
        self.id = id
        self.name = name
        self.quantity = quantity
        self.unit_price = unit_price

    def __str__(self):
        return f"Raw Material {self.id}: {self.name}, Quantity: {self.quantity}, Unit Price: {self.unit_price}"


class Inventory:
    """Manages the raw material inventory."""

    def __init__(self):
        """Initializes an empty inventory."""
        self.raw_materials = {}

    def add_raw_material(self, raw_material: RawMaterial):
        """
        Adds a raw material to the inventory.

        Args:
        raw_material (RawMaterial): Raw material to add.
        """
        self.raw_materials[raw_material.id] = raw_material

    def remove_raw_material(self, id: int):
        """
        Removes a raw material from the inventory.

        Args:
        id (int): ID of the raw material to remove.

        Raises:
        KeyError: If the raw material is not found in the inventory.
        """
        if id in self.raw_materials:
            del self.raw_materials[id]
        else:
            raise KeyError(f"Raw material {id} not found in inventory.")

    def update_quantity(self, id: int, new_quantity: float):
        """
        Updates the quantity of a raw material in the inventory.

        Args:
        id (int): ID of the raw material to update.
        new_quantity (float): New quantity of the raw material.

        Raises:
        KeyError: If the raw material is not found in the inventory.
        ValueError: If the new quantity is negative.
        """
        if id in self.raw_materials:
            if new_quantity >= 0:
                self.raw_materials[id].quantity = new_quantity
            else:
                raise ValueError("Quantity cannot be negative.")
        else:
            raise KeyError(f"Raw material {id} not found in inventory.")

    def get_raw_material(self, id: int):
        """
        Retrieves a raw material from the inventory.

        Args:
        id (int): ID of the raw material to retrieve.

        Returns:
        RawMaterial: The raw material with the specified ID.

        Raises:
        KeyError: If the raw material is not found in the inventory.
        """
        try:
            return self.raw_materials[id]
        except KeyError:
            raise KeyError(f"Raw material {id} not found in inventory.")

    def __str__(self):
        inventory_str = "Raw Material Inventory:\n"
        for raw_material in self.raw_materials.values():
            inventory_str += str(raw_material) + "\n"
        return inventory_str


def main():
    # Create an inventory
    inventory = Inventory()

    # Add raw materials
    raw_material1 = RawMaterial(1, "Active Ingredient X", 1000.0, 50.0)
    raw_material2 = RawMaterial(2, "Preservative Y", 500.0, 20.0)
    inventory.add_raw_material(raw_material1)
    inventory.add_raw_material(raw_material2)

    # Print initial inventory
    print("Initial Inventory:")
    print(inventory)

    # Update quantity
    inventory.update_quantity(1, 800.0)

    # Print updated inventory
    print("\nUpdated Inventory:")
    print(inventory)

    # Remove raw material
    inventory.remove_raw_material(2)

    # Print final inventory
    print("\nFinal Inventory:")
    print(inventory)

    # Try to retrieve a non-existent raw material
    try:
        inventory.get_raw_material(3)
    except KeyError as e:
        print(f"\nError: {e}")


if __name__ == "__main__":
    main()
```
