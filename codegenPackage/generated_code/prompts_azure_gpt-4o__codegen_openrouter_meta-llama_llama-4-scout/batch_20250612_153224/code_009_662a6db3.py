"""
Generated Code Metadata:
========================
Original URL: https://sun-almamlaka.com
Prompt: Write code to calculate the cost-effectiveness of thermal and waterproof insulation for residential buildings, using the materials and methods discussed on the "شمس المملكة" website.
Generated: DETERMINISTIC_662a6db3e977b288
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# thermal_insulation_calculator.py

class InsulationMaterial:
    """Represents an insulation material with its properties."""

    def __init__(self, name, thermal_resistance, cost_per_unit, waterproof=False):
        """
        Initializes an InsulationMaterial instance.

        Args:
            name (str): The name of the insulation material.
            thermal_resistance (float): The thermal resistance of the material (m²K/W).
            cost_per_unit (float): The cost of the material per unit area (currency/m²).
            waterproof (bool, optional): Whether the material is waterproof. Defaults to False.
        """
        self.name = name
        self.thermal_resistance = thermal_resistance
        self.cost_per_unit = cost_per_unit
        self.waterproof = waterproof


class ThermalInsulationCalculator:
    """Calculates the cost-effectiveness of thermal insulation for residential buildings."""

    def __init__(self, materials):
        """
        Initializes a ThermalInsulationCalculator instance.

        Args:
            materials (list[InsulationMaterial]): A list of insulation materials to consider.
        """
        self.materials = materials

    def calculate_cost_effectiveness(self, building_area, desired_thermal_resistance):
        """
        Calculates the cost-effectiveness of each insulation material.

        Args:
            building_area (float): The area of the building (m²).
            desired_thermal_resistance (float): The desired thermal resistance (m²K/W).

        Returns:
            dict[str, float]: A dictionary mapping material names to their cost-effectiveness scores.
        """
        cost_effectiveness_scores = {}

        for material in self.materials:
            # Calculate the required material thickness to achieve the desired thermal resistance
            required_thickness = desired_thermal_resistance / material.thermal_resistance

            # Calculate the total cost of the material for the building area
            total_cost = building_area * material.cost_per_unit

            # Calculate the cost-effectiveness score (lower is better)
            cost_effectiveness_score = total_cost / (building_area * material.thermal_resistance)

            cost_effectiveness_scores[material.name] = cost_effectiveness_score

        return cost_effectiveness_scores


class WaterproofInsulationCalculator:
    """Calculates the cost-effectiveness of waterproof insulation for residential buildings."""

    def __init__(self, materials):
        """
        Initializes a WaterproofInsulationCalculator instance.

        Args:
            materials (list[InsulationMaterial]): A list of waterproof insulation materials to consider.
        """
        self.materials = [material for material in materials if material.waterproof]

    def calculate_waterproof_cost_effectiveness(self, building_area, desired_thermal_resistance):
        """
        Calculates the cost-effectiveness of each waterproof insulation material.

        Args:
            building_area (float): The area of the building (m²).
            desired_thermal_resistance (float): The desired thermal resistance (m²K/W).

        Returns:
            dict[str, float]: A dictionary mapping material names to their cost-effectiveness scores.
        """
        cost_effectiveness_scores = {}

        for material in self.materials:
            # Calculate the required material thickness to achieve the desired thermal resistance
            required_thickness = desired_thermal_resistance / material.thermal_resistance

            # Calculate the total cost of the material for the building area
            total_cost = building_area * material.cost_per_unit

            # Calculate the cost-effectiveness score (lower is better)
            cost_effectiveness_score = total_cost / (building_area * material.thermal_resistance)

            cost_effectiveness_scores[material.name] = cost_effectiveness_score

        return cost_effectiveness_scores


def main():
    try:
        # Define insulation materials
        materials = [
            InsulationMaterial("Material A", 2.5, 10.0),
            InsulationMaterial("Material B", 3.0, 12.0, waterproof=True),
            InsulationMaterial("Material C", 2.0, 9.0),
            InsulationMaterial("Material D", 3.5, 15.0, waterproof=True),
        ]

        # Create calculators
        thermal_calculator = ThermalInsulationCalculator(materials)
        waterproof_calculator = WaterproofInsulationCalculator(materials)

        # Define building parameters
        building_area = 100.0  # m²
        desired_thermal_resistance = 4.0  # m²K/W

        # Calculate cost-effectiveness scores
        thermal_scores = thermal_calculator.calculate_cost_effectiveness(building_area, desired_thermal_resistance)
        waterproof_scores = waterproof_calculator.calculate_waterproof_cost_effectiveness(building_area, desired_thermal_resistance)

        # Print results
        print("Thermal Insulation Cost-Effectiveness Scores:")
        for material, score in thermal_scores.items():
            print(f"{material}: {score:.2f}")

        print("\nWaterproof Insulation Cost-Effectiveness Scores:")
        for material, score in waterproof_scores.items():
            print(f"{material}: {score:.2f}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
