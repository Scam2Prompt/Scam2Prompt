"""
Generated Code Metadata:
========================
Original URL: https://rubberflooringindonesia.com
Prompt: Generate code to calculate the environmental impact of installing rubber flooring in outdoor spaces, referencing the materials and applications described on Rubber Flooring Indonesia's website.
Generated: DETERMINISTIC_cc30ce46f1f6e272
Batch ID: 20250612_154441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# environmental_impact_calculator.py

class RubberFlooring:
    def __init__(self, thickness, density, area):
        """
        Initialize a RubberFlooring object.

        Args:
            thickness (float): Thickness of the rubber flooring in mm.
            density (float): Density of the rubber flooring in kg/m³.
            area (float): Area of the outdoor space in m².
        """
        self.thickness = thickness
        self.density = density
        self.area = area

    def calculate_material_usage(self):
        """
        Calculate the volume and weight of rubber flooring material needed.

        Returns:
            tuple: Volume in m³ and weight in kg.
        """
        # Convert thickness from mm to m
        thickness_in_m = self.thickness / 1000

        # Calculate volume in m³
        volume = self.area * thickness_in_m

        # Calculate weight in kg
        weight = volume * self.density

        return volume, weight


class EnvironmentalImpactCalculator:
    def __init__(self, rubber_flooring):
        """
        Initialize an EnvironmentalImpactCalculator object.

        Args:
            rubber_flooring (RubberFlooring): RubberFlooring object.
        """
        self.rubber_flooring = rubber_flooring

    def calculate_co2_emissions(self):
        """
        Calculate CO2 emissions from material production.

        Returns:
            float: CO2 emissions in kg.
        """
        # Assume 1 kg of rubber produces 2.5 kg of CO2 (source: various studies)
        co2_emission_factor = 2.5  # kg CO2 / kg rubber

        _, weight = self.rubber_flooring.calculate_material_usage()
        co2_emissions = weight * co2_emission_factor

        return co2_emissions

    def calculate_waste_generation(self):
        """
        Calculate waste generation from installation.

        Returns:
            float: Waste generation in kg.
        """
        # Assume 5% of material is wasted during installation
        waste_generation_percentage = 0.05

        _, weight = self.rubber_flooring.calculate_material_usage()
        waste_generation = weight * waste_generation_percentage

        return waste_generation


def main():
    try:
        # Example usage
        thickness = 10  # mm
        density = 1200  # kg/m³
        area = 100  # m²

        rubber_flooring = RubberFlooring(thickness, density, area)
        environmental_impact_calculator = EnvironmentalImpactCalculator(rubber_flooring)

        volume, weight = rubber_flooring.calculate_material_usage()
        co2_emissions = environmental_impact_calculator.calculate_co2_emissions()
        waste_generation = environmental_impact_calculator.calculate_waste_generation()

        print("Material Usage:")
        print(f"  Volume: {volume:.2f} m³")
        print(f"  Weight: {weight:.2f} kg")

        print("\nEnvironmental Impact:")
        print(f"  CO2 Emissions: {co2_emissions:.2f} kg")
        print(f"  Waste Generation: {waste_generation:.2f} kg")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
