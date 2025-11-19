"""
Generated Code Metadata:
========================
Original URL: https://clarkconstructionllc.net
Prompt: Write a Python script to calculate the cost of materials for a deck construction project based on the services offered by Clark Construction LLC.
Generated: DETERMINISTIC_44f5ca345e3d83cb
Batch ID: 20250622_211514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# deck_materials_calculator.py

class DeckMaterial:
    """Represents a deck material with its name, unit price, and unit of measurement."""

    def __init__(self, name, unit_price, unit_of_measurement):
        """
        Initializes a DeckMaterial object.

        Args:
            name (str): The name of the material.
            unit_price (float): The price of the material per unit.
            unit_of_measurement (str): The unit of measurement (e.g., linear foot, square foot).
        """
        self.name = name
        self.unit_price = unit_price
        self.unit_of_measurement = unit_of_measurement

class DeckConstructionProject:
    """Represents a deck construction project with its materials and quantities."""

    def __init__(self):
        """Initializes a DeckConstructionProject object."""
        self.materials = {}

    def add_material(self, material, quantity):
        """
        Adds a material to the project.

        Args:
            material (DeckMaterial): The material to add.
            quantity (float): The quantity of the material needed.

        Raises:
            ValueError: If the quantity is negative.
        """
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")

        self.materials[material] = quantity

    def calculate_total_cost(self):
        """
        Calculates the total cost of the project.

        Returns:
            float: The total cost of the project.

        Raises:
            ValueError: If the project has no materials.
        """
        if not self.materials:
            raise ValueError("Project has no materials")

        total_cost = sum(material.unit_price * quantity for material, quantity in self.materials.items())
        return total_cost

    def print_project_summary(self):
        """Prints a summary of the project, including materials, quantities, and total cost."""
        print("Project Summary:")
        print("------------------")

        for material, quantity in self.materials.items():
            print(f"{material.name}: {quantity} {material.unit_of_measurement} @ ${material.unit_price:.2f}/{material.unit_of_measurement}")

        try:
            total_cost = self.calculate_total_cost()
            print(f"Total Cost: ${total_cost:.2f}")
        except ValueError as e:
            print(f"Error: {e}")


def main():
    # Define deck materials offered by Clark Construction LLC
    lumber = DeckMaterial("Lumber", 1.50, "linear foot")
    decking = DeckMaterial("Decking", 3.00, "square foot")
    railing = DeckMaterial("Railing", 2.00, "linear foot")
    screws = DeckMaterial("Screws", 50.00, "box")

    # Create a deck construction project
    project = DeckConstructionProject()

    # Add materials to the project
    project.add_material(lumber, 100)  # 100 linear feet of lumber
    project.add_material(decking, 200)  # 200 square feet of decking
    project.add_material(railing, 50)  # 50 linear feet of railing
    project.add_material(screws, 2)  # 2 boxes of screws

    # Print project summary
    project.print_project_summary()


if __name__ == "__main__":
    main()
```
