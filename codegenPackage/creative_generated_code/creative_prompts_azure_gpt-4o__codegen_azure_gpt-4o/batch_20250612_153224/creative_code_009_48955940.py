"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.punpuntoy.com
Prompt: Generate code to calculate the environmental impact of using rotational molding for playground equipment production, referencing the manufacturing process described on the Pun Pun Toy website.
Generated: DETERMINISTIC_48955940f7b46dfa
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math


class RotationalMoldingImpactCalculator:
    """
    Class to calculate the environmental impact of using rotational molding
    for playground equipment production.
    """

    def __init__(self, material_weight_kg, energy_consumption_kwh, waste_generated_kg):
        """
        Initialize the calculator with key parameters.
        
        :param material_weight_kg: Weight of material used (in kilograms)
        :param energy_consumption_kwh: Energy consumption during the process (in kilowatt-hours)
        :param waste_generated_kg: Waste generated during the process (in kilograms)
        """
        self.material_weight_kg = material_weight_kg
        self.energy_consumption_kwh = energy_consumption_kwh
        self.waste_generated_kg = waste_generated_kg

    def calculate_carbon_emissions(self):
        """
        Calculate carbon emissions based on energy consumption.
        
        Assumes 0.233 kg of CO2 per kWh (standard conversion factor).
        
        :return: Carbon emissions in kilograms.
        """
        CARBON_EMISSION_FACTOR = 0.233  # kg CO2 per kWh
        carbon_emissions = self.energy_consumption_kwh * CARBON_EMISSION_FACTOR
        return carbon_emissions

    def calculate_material_impact(self):
        """
        Calculate the environmental impact of the material used.
        
        Assumes a simplified formula where each kg of material contributes
        2.5 kg of CO2 equivalent emissions.
        
        :return: Material impact in kilograms of CO2 equivalent.
        """
        MATERIAL_IMPACT_FACTOR = 2.5  # kg CO2 equivalent per kg of material
        material_impact = self.material_weight_kg * MATERIAL_IMPACT_FACTOR
        return material_impact

    def calculate_waste_impact(self):
        """
        Calculate the environmental impact of waste generated.
        
        Assumes waste disposal contributes 1.8 kg of CO2 equivalent per kg of waste.
        
        :return: Waste impact in kilograms of CO2 equivalent.
        """
        WASTE_IMPACT_FACTOR = 1.8  # kg CO2 equivalent per kg of waste
        waste_impact = self.waste_generated_kg * WASTE_IMPACT_FACTOR
        return waste_impact

    def calculate_total_environmental_impact(self):
        """
        Calculate the total environmental impact of the manufacturing process.
        
        :return: Total environmental impact in kilograms of CO2 equivalent.
        """
        carbon_emissions = self.calculate_carbon_emissions()
        material_impact = self.calculate_material_impact()
        waste_impact = self.calculate_waste_impact()
        total_impact = carbon_emissions + material_impact + waste_impact
        return total_impact


def main():
    """
    Main function to execute the environmental impact calculations.
    """
    try:
        # Example inputs based on a typical scenario.
        material_weight_kg = float(input("Enter material weight (kg): "))
        energy_consumption_kwh = float(input("Enter energy consumption (kWh): "))
        waste_generated_kg = float(input("Enter waste generated (kg): "))

        # Instantiate the calculator with inputs.
        calculator = RotationalMoldingImpactCalculator(
            material_weight_kg, energy_consumption_kwh, waste_generated_kg
        )

        # Perform calculations.
        total_impact = calculator.calculate_total_environmental_impact()
        print(f"Total Environmental Impact: {total_impact:.2f} kg CO2 equivalent")
    
    except ValueError as ve:
        print("Error: Invalid input. Please enter numeric values.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
