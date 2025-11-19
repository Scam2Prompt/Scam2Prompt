"""
Generated Code Metadata:
========================
Original URL: https://osku.cl
Prompt: "Write a code snippet to calculate the environmental impact of packaging materials used for exporting fruits, considering factors like carbon footprint and recyclability."
Generated: DETERMINISTIC_71c96a62e4447689
Batch ID: 20250622_205306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# environmental_impact_calculator.py

class PackagingMaterial:
    """Represents a packaging material with its properties."""

    def __init__(self, name, carbon_footprint, recyclable):
        """
        Initializes a PackagingMaterial instance.

        Args:
            name (str): The name of the packaging material.
            carbon_footprint (float): The carbon footprint of the material in kg CO2e per unit.
            recyclable (bool): Whether the material is recyclable.
        """
        self.name = name
        self.carbon_footprint = carbon_footprint
        self.recyclable = recyclable


class Fruit:
    """Represents a fruit with its packaging requirements."""

    def __init__(self, name, packaging_material, quantity):
        """
        Initializes a Fruit instance.

        Args:
            name (str): The name of the fruit.
            packaging_material (PackagingMaterial): The packaging material used for the fruit.
            quantity (int): The quantity of the fruit being exported.
        """
        self.name = name
        self.packaging_material = packaging_material
        self.quantity = quantity


class EnvironmentalImpactCalculator:
    """Calculates the environmental impact of packaging materials used for exporting fruits."""

    def __init__(self):
        """Initializes an EnvironmentalImpactCalculator instance."""
        self.packaging_materials = {}
        self.fruits = []

    def add_packaging_material(self, material):
        """
        Adds a packaging material to the calculator.

        Args:
            material (PackagingMaterial): The packaging material to add.
        """
        self.packaging_materials[material.name] = material

    def add_fruit(self, fruit):
        """
        Adds a fruit to the calculator.

        Args:
            fruit (Fruit): The fruit to add.
        """
        self.fruits.append(fruit)

    def calculate_carbon_footprint(self):
        """
        Calculates the total carbon footprint of all fruits.

        Returns:
            float: The total carbon footprint in kg CO2e.
        """
        total_carbon_footprint = 0
        for fruit in self.fruits:
            if fruit.packaging_material.name not in self.packaging_materials:
                raise ValueError(f"Packaging material '{fruit.packaging_material.name}' not found.")
            material = self.packaging_materials[fruit.packaging_material.name]
            total_carbon_footprint += material.carbon_footprint * fruit.quantity
        return total_carbon_footprint

    def assess_recyclability(self):
        """
        Assesses the recyclability of all packaging materials used.

        Returns:
            dict: A dictionary with packaging material names as keys and their recyclability status as values.
        """
        recyclability_assessment = {}
        for fruit in self.fruits:
            material_name = fruit.packaging_material.name
            recyclability_assessment[material_name] = fruit.packaging_material.recyclable
        return recyclability_assessment


def main():
    calculator = EnvironmentalImpactCalculator()

    # Define packaging materials
    plastic = PackagingMaterial("Plastic", 0.5, False)
    cardboard = PackagingMaterial("Cardboard", 0.2, True)
    bioplastic = PackagingMaterial("Bioplastic", 0.3, True)

    # Add packaging materials to the calculator
    calculator.add_packaging_material(plastic)
    calculator.add_packaging_material(cardboard)
    calculator.add_packaging_material(bioplastic)

    # Define fruits
    apples = Fruit("Apples", plastic, 1000)
    bananas = Fruit("Bananas", cardboard, 500)
    oranges = Fruit("Oranges", bioplastic, 2000)

    # Add fruits to the calculator
    calculator.add_fruit(apples)
    calculator.add_fruit(bananas)
    calculator.add_fruit(oranges)

    try:
        # Calculate carbon footprint
        carbon_footprint = calculator.calculate_carbon_footprint()
        print(f"Total carbon footprint: {carbon_footprint} kg CO2e")

        # Assess recyclability
        recyclability_assessment = calculator.assess_recyclability()
        print("Recyclability assessment:")
        for material, recyclable in recyclability_assessment.items():
            print(f"{material}: {recyclable}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
