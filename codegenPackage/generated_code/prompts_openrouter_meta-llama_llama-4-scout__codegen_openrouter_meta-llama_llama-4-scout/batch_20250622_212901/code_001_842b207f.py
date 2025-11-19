"""
Generated Code Metadata:
========================
Original URL: https://unitramabrazz.blogspot.com
Prompt: Generate a Python code snippet to manage an inventory of visual communication materials, including chapas de ACM, lonas unibanner, and vinil auto adesivo.
Generated: DETERMINISTIC_842b207f75e72f69
Batch ID: 20250622_212901
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# inventory_manager.py

class VisualCommunicationMaterial:
    """Base class for visual communication materials."""

    def __init__(self, name, quantity, unit_price):
        """
        Initialize a visual communication material.

        Args:
            name (str): Material name.
            quantity (int): Material quantity.
            unit_price (float): Material unit price.
        """
        self.name = name
        self.quantity = quantity
        self.unit_price = unit_price

    def get_total_value(self):
        """Calculate the total value of the material."""
        return self.quantity * self.unit_price

    def __str__(self):
        return f"{self.name}: {self.quantity} units @ R${self.unit_price:.2f}/unit"


class ChapasDeACM(VisualCommunicationMaterial):
    """Chapas de ACM material."""

    def __init__(self, quantity, unit_price, size):
        """
        Initialize a Chapas de ACM material.

        Args:
            quantity (int): Material quantity.
            unit_price (float): Material unit price.
            size (str): Material size.
        """
        super().__init__("Chapas de ACM", quantity, unit_price)
        self.size = size

    def __str__(self):
        return super().__str__() + f", Size: {self.size}"


class LonasUnibanner(VisualCommunicationMaterial):
    """Lonas Unibanner material."""

    def __init__(self, quantity, unit_price, width, height):
        """
        Initialize a Lonas Unibanner material.

        Args:
            quantity (int): Material quantity.
            unit_price (float): Material unit price.
            width (float): Material width.
            height (float): Material height.
        """
        super().__init__("Lonas Unibanner", quantity, unit_price)
        self.width = width
        self.height = height

    def get_area(self):
        """Calculate the area of the material."""
        return self.width * self.height

    def __str__(self):
        return super().__str__() + f", Size: {self.width}m x {self.height}m"


class VinilAutoAdesivo(VisualCommunicationMaterial):
    """Vinil Auto Adesivo material."""

    def __init__(self, quantity, unit_price, roll_size):
        """
        Initialize a Vinil Auto Adesivo material.

        Args:
            quantity (int): Material quantity.
            unit_price (float): Material unit price.
            roll_size (float): Material roll size.
        """
        super().__init__("Vinil Auto Adesivo", quantity, unit_price)
        self.roll_size = roll_size

    def __str__(self):
        return super().__str__() + f", Roll Size: {self.roll_size}m"


class Inventory:
    """Inventory of visual communication materials."""

    def __init__(self):
        self.materials = []

    def add_material(self, material):
        """
        Add a material to the inventory.

        Args:
            material (VisualCommunicationMaterial): Material to add.
        """
        self.materials.append(material)

    def remove_material(self, material_name):
        """
        Remove a material from the inventory.

        Args:
            material_name (str): Name of the material to remove.

        Raises:
            ValueError: If the material is not found.
        """
        for material in self.materials:
            if material.name == material_name:
                self.materials.remove(material)
                return
        raise ValueError(f"Material '{material_name}' not found.")

    def get_total_inventory_value(self):
        """Calculate the total value of the inventory."""
        return sum(material.get_total_value() for material in self.materials)

    def __str__(self):
        inventory_str = "Inventory:\n"
        for material in self.materials:
            inventory_str += f"- {material}\n"
        inventory_str += f"Total Value: R${self.get_total_inventory_value():.2f}"
        return inventory_str


def main():
    try:
        inventory = Inventory()

        chapas_de_acm = ChapasDeACM(10, 50.0, "2x3m")
        lonas_unibanner = LonasUnibanner(5, 200.0, 4, 6)
        vinil_auto_adesivo = VinilAutoAdesivo(20, 30.0, 100)

        inventory.add_material(chapas_de_acm)
        inventory.add_material(lonas_unibanner)
        inventory.add_material(vinil_auto_adesivo)

        print(inventory)

        inventory.remove_material("Lonas Unibanner")

        print("\nAfter removing Lonas Unibanner:")
        print(inventory)

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
