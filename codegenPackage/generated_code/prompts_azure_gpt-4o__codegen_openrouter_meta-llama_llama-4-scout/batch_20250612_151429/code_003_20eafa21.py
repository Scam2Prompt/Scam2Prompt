"""
Generated Code Metadata:
========================
Original URL: https://somcivil.com
Prompt: Create a script to calculate the material requirements for structural steel fabrication, considering SOM Civil Engineers' emphasis on cost-effective and recyclable steel solutions.
Generated: DETERMINISTIC_20eafa216aca8df4
Batch ID: 20250612_151429
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# material_calculator.py

class SteelMaterial:
    """Represents a steel material with its properties."""

    def __init__(self, name, density, unit_cost, recyclability_factor):
        """
        Initializes a SteelMaterial object.

        Args:
            name (str): Name of the steel material.
            density (float): Density of the steel material in kg/m^3.
            unit_cost (float): Unit cost of the steel material in $/kg.
            recyclability_factor (float): Recyclability factor of the steel material (0-1).
        """
        self.name = name
        self.density = density
        self.unit_cost = unit_cost
        self.recyclability_factor = recyclability_factor

    def calculate_cost(self, volume):
        """
        Calculates the cost of the steel material for a given volume.

        Args:
            volume (float): Volume of the steel material in m^3.

        Returns:
            float: Cost of the steel material.
        """
        mass = self.density * volume
        return mass * self.unit_cost

    def calculate_recyclability_score(self):
        """
        Calculates the recyclability score of the steel material.

        Returns:
            float: Recyclability score of the steel material.
        """
        return self.recyclability_factor


class StructuralSteelFabrication:
    """Represents a structural steel fabrication project."""

    def __init__(self):
        self.materials = {}

    def add_material(self, material, quantity):
        """
        Adds a steel material to the project.

        Args:
            material (SteelMaterial): Steel material to add.
            quantity (float): Quantity of the steel material in m^3.
        """
        self.materials[material] = quantity

    def calculate_total_cost(self):
        """
        Calculates the total cost of the project.

        Returns:
            float: Total cost of the project.
        """
        total_cost = 0
        for material, quantity in self.materials.items():
            total_cost += material.calculate_cost(quantity)
        return total_cost

    def calculate_total_recyclability_score(self):
        """
        Calculates the total recyclability score of the project.

        Returns:
            float: Total recyclability score of the project.
        """
        total_recyclability_score = 0
        total_quantity = 0
        for material, quantity in self.materials.items():
            total_recyclability_score += material.calculate_recyclability_score() * quantity
            total_quantity += quantity
        return total_recyclability_score / total_quantity if total_quantity > 0 else 0


def main():
    try:
        # Create steel materials
        material1 = SteelMaterial("Steel Beam", 7850, 1.2, 0.8)
        material2 = SteelMaterial("Steel Plate", 7850, 1.0, 0.9)

        # Create a structural steel fabrication project
        project = StructuralSteelFabrication()
        project.add_material(material1, 10)  # 10 m^3 of Steel Beam
        project.add_material(material2, 5)   # 5 m^3 of Steel Plate

        # Calculate and print project costs and recyclability scores
        total_cost = project.calculate_total_cost()
        total_recyclability_score = project.calculate_total_recyclability_score()

        print(f"Total Cost: ${total_cost:.2f}")
        print(f"Total Recyclability Score: {total_recyclability_score:.2f}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
