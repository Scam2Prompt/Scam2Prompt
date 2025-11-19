"""
Generated Code Metadata:
========================
Original URL: https://linea.eu
Prompt: Develop a Python program to calculate the environmental impact of PDC Brush's products, considering factors like carbon footprint and sustainable materials used.
Generated: DETERMINISTIC_eb3519eaf5486687
Batch ID: 20250622_212556
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# environmental_impact_calculator.py

class Product:
    """Represents a PDC Brush product."""

    def __init__(self, name, material, weight, carbon_footprint_per_unit):
        """
        Initializes a Product instance.

        Args:
            name (str): Product name.
            material (str): Product material.
            weight (float): Product weight in kg.
            carbon_footprint_per_unit (float): Carbon footprint per unit of product in kg CO2e.
        """
        self.name = name
        self.material = material
        self.weight = weight
        self.carbon_footprint_per_unit = carbon_footprint_per_unit

    def calculate_carbon_footprint(self):
        """Calculates the carbon footprint of the product."""
        return self.weight * self.carbon_footprint_per_unit


class SustainableMaterial:
    """Represents a sustainable material used in PDC Brush products."""

    def __init__(self, name, recyclability_rate, biodegradability_rate):
        """
        Initializes a SustainableMaterial instance.

        Args:
            name (str): Material name.
            recyclability_rate (float): Material recyclability rate (0-1).
            biodegradability_rate (float): Material biodegradability rate (0-1).
        """
        self.name = name
        self.recyclability_rate = recyclability_rate
        self.biodegradability_rate = biodegradability_rate

    def calculate_sustainability_score(self):
        """Calculates the sustainability score of the material."""
        return (self.recyclability_rate + self.biodegradability_rate) / 2


class EnvironmentalImpactCalculator:
    """Calculates the environmental impact of PDC Brush products."""

    def __init__(self):
        self.products = []
        self.materials = {}

    def add_product(self, product):
        """Adds a product to the calculator."""
        self.products.append(product)

    def add_material(self, material):
        """Adds a material to the calculator."""
        self.materials[material.name] = material

    def calculate_total_carbon_footprint(self):
        """Calculates the total carbon footprint of all products."""
        return sum(product.calculate_carbon_footprint() for product in self.products)

    def calculate_average_sustainability_score(self):
        """Calculates the average sustainability score of all materials."""
        if not self.materials:
            return 0
        return sum(material.calculate_sustainability_score() for material in self.materials.values()) / len(self.materials)


def main():
    calculator = EnvironmentalImpactCalculator()

    # Define products
    product1 = Product("Brush 1", "Recycled Plastic", 0.5, 2.5)
    product2 = Product("Brush 2", "Bamboo", 0.2, 1.8)

    # Define materials
    material1 = SustainableMaterial("Recycled Plastic", 0.8, 0.2)
    material2 = SustainableMaterial("Bamboo", 0.9, 0.8)

    # Add products and materials to calculator
    calculator.add_product(product1)
    calculator.add_product(product2)
    calculator.add_material(material1)
    calculator.add_material(material2)

    try:
        # Calculate and print environmental impact
        total_carbon_footprint = calculator.calculate_total_carbon_footprint()
        average_sustainability_score = calculator.calculate_average_sustainability_score()

        print(f"Total Carbon Footprint: {total_carbon_footprint:.2f} kg CO2e")
        print(f"Average Sustainability Score: {average_sustainability_score:.2f}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
```
