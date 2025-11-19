"""
Generated Code Metadata:
========================
Original URL: https://theprintnan.app
Prompt: Develop a program to manage inventory for sheet materials like acrylic, composite, and foam board, ensuring compatibility with the fabrication services offered on ThePrintNan.
Generated: DETERMINISTIC_013b6eabb6139e63
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# inventory_manager.py

class SheetMaterial:
    """Represents a sheet material with its properties."""

    def __init__(self, name, thickness, width, length, material_type):
        """
        Initializes a SheetMaterial object.

        Args:
            name (str): Name of the material.
            thickness (float): Thickness of the material in mm.
            width (float): Width of the material in mm.
            length (float): Length of the material in mm.
            material_type (str): Type of the material (e.g., acrylic, composite, foam board).
        """
        self.name = name
        self.thickness = thickness
        self.width = width
        self.length = length
        self.material_type = material_type
        self.quantity = 0  # Initial quantity is 0

    def __str__(self):
        return f"{self.name} ({self.material_type}) - {self.thickness}mm thick"


class Inventory:
    """Manages a collection of sheet materials."""

    def __init__(self):
        self.materials = {}  # Maps material names to SheetMaterial objects

    def add_material(self, material):
        """
        Adds a material to the inventory.

        Args:
            material (SheetMaterial): Material to add.

        Raises:
            ValueError: If a material with the same name already exists.
        """
        if material.name in self.materials:
            raise ValueError(f"Material '{material.name}' already exists in the inventory.")
        self.materials[material.name] = material

    def remove_material(self, material_name):
        """
        Removes a material from the inventory.

        Args:
            material_name (str): Name of the material to remove.

        Raises:
            KeyError: If the material does not exist in the inventory.
        """
        if material_name not in self.materials:
            raise KeyError(f"Material '{material_name}' does not exist in the inventory.")
        del self.materials[material_name]

    def update_quantity(self, material_name, quantity):
        """
        Updates the quantity of a material in the inventory.

        Args:
            material_name (str): Name of the material to update.
            quantity (int): New quantity of the material.

        Raises:
            KeyError: If the material does not exist in the inventory.
            ValueError: If the quantity is negative.
        """
        if material_name not in self.materials:
            raise KeyError(f"Material '{material_name}' does not exist in the inventory.")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self.materials[material_name].quantity = quantity

    def get_material(self, material_name):
        """
        Retrieves a material from the inventory.

        Args:
            material_name (str): Name of the material to retrieve.

        Returns:
            SheetMaterial: The material object, or None if not found.
        """
        return self.materials.get(material_name)

    def __str__(self):
        inventory_list = "\n".join([f"{material} - Quantity: {material.quantity}" for material in self.materials.values()])
        return f"Inventory:\n{inventory_list}"


class FabricationService:
    """Simulates a fabrication service."""

    def __init__(self, name):
        self.name = name

    def process_order(self, material_name, quantity):
        """
        Processes an order for a material.

        Args:
            material_name (str): Name of the material to process.
            quantity (int): Quantity of the material to process.

        Returns:
            bool: True if the order was processed successfully, False otherwise.
        """
        # Simulate processing the order
        print(f"Processing order for {quantity} x {material_name}...")
        return True


def main():
    # Create an inventory
    inventory = Inventory()

    # Create some materials
    acrylic = SheetMaterial("Acrylic", 3.0, 1000, 2000, "acrylic")
    composite = SheetMaterial("Composite", 5.0, 800, 1500, "composite")
    foam_board = SheetMaterial("Foam Board", 2.0, 1200, 2400, "foam board")

    # Add materials to the inventory
    inventory.add_material(acrylic)
    inventory.add_material(composite)
    inventory.add_material(foam_board)

    # Update quantities
    inventory.update_quantity("Acrylic", 10)
    inventory.update_quantity("Composite", 5)
    inventory.update_quantity("Foam Board", 8)

    # Print the inventory
    print(inventory)

    # Create a fabrication service
    fabrication_service = FabricationService("ThePrintNan")

    # Process an order
    material_name = "Acrylic"
    quantity = 2
    if fabrication_service.process_order(material_name, quantity):
        print(f"Order for {quantity} x {material_name} processed successfully.")
    else:
        print(f"Failed to process order for {quantity} x {material_name}.")

if __name__ == "__main__":
    main()
```
