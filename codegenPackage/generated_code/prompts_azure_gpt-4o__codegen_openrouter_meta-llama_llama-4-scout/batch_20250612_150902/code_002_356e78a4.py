"""
Generated Code Metadata:
========================
Original URL: https://clibiya.com
Prompt: Generate code to calculate the environmental impact of recycling organic waste into protein, using Clibiya's recycling model as a reference.
Generated: DETERMINISTIC_356e78a455874afd
Batch ID: 20250612_150902
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# environmental_impact_calculator.py

"""
Calculates the environmental impact of recycling organic waste into protein using Clibiya's recycling model.

Author: [Your Name]
Date: [Today's Date]
"""

import math

class EnvironmentalImpactCalculator:
    def __init__(self, 
                 organic_waste_tonnes: float, 
                 protein_production_efficiency: float, 
                 energy_consumption_per_tonne: float, 
                 water_consumption_per_tonne: float,
                 co2_emission_per_tonne: float):
        """
        Initializes the EnvironmentalImpactCalculator.

        Args:
        - organic_waste_tonnes (float): The amount of organic waste in tonnes.
        - protein_production_efficiency (float): The efficiency of protein production from organic waste (0-1).
        - energy_consumption_per_tonne (float): The energy consumption per tonne of organic waste in kWh.
        - water_consumption_per_tonne (float): The water consumption per tonne of organic waste in litres.
        - co2_emission_per_tonne (float): The CO2 emission per tonne of organic waste in kg.
        """

        self.organic_waste_tonnes = organic_waste_tonnes
        self.protein_production_efficiency = protein_production_efficiency
        self.energy_consumption_per_tonne = energy_consumption_per_tonne
        self.water_consumption_per_tonne = water_consumption_per_tonne
        self.co2_emission_per_tonne = co2_emission_per_tonne

    def calculate_protein_production(self) -> float:
        """
        Calculates the amount of protein produced from the organic waste.

        Returns:
        - protein_production (float): The amount of protein produced in tonnes.
        """
        protein_production = self.organic_waste_tonnes * self.protein_production_efficiency
        return protein_production

    def calculate_energy_consumption(self) -> float:
        """
        Calculates the total energy consumption for recycling the organic waste.

        Returns:
        - energy_consumption (float): The total energy consumption in kWh.
        """
        energy_consumption = self.organic_waste_tonnes * self.energy_consumption_per_tonne
        return energy_consumption

    def calculate_water_consumption(self) -> float:
        """
        Calculates the total water consumption for recycling the organic waste.

        Returns:
        - water_consumption (float): The total water consumption in litres.
        """
        water_consumption = self.organic_waste_tonnes * self.water_consumption_per_tonne
        return water_consumption

    def calculate_co2_emission(self) -> float:
        """
        Calculates the total CO2 emission for recycling the organic waste.

        Returns:
        - co2_emission (float): The total CO2 emission in kg.
        """
        co2_emission = self.organic_waste_tonnes * self.co2_emission_per_tonne
        return co2_emission

    def calculate_environmental_impact(self) -> dict:
        """
        Calculates the environmental impact of recycling organic waste into protein.

        Returns:
        - environmental_impact (dict): A dictionary containing the environmental impact metrics.
        """
        protein_production = self.calculate_protein_production()
        energy_consumption = self.calculate_energy_consumption()
        water_consumption = self.calculate_water_consumption()
        co2_emission = self.calculate_co2_emission()

        environmental_impact = {
            "protein_production": protein_production,
            "energy_consumption": energy_consumption,
            "water_consumption": water_consumption,
            "co2_emission": co2_emission
        }

        return environmental_impact


def main():
    try:
        # Example usage
        calculator = EnvironmentalImpactCalculator(
            organic_waste_tonnes=1000,
            protein_production_efficiency=0.8,
            energy_consumption_per_tonne=50,
            water_consumption_per_tonne=1000,
            co2_emission_per_tonne=200
        )

        environmental_impact = calculator.calculate_environmental_impact()

        print("Environmental Impact Metrics:")
        print(f"Protein Production: {environmental_impact['protein_production']} tonnes")
        print(f"Energy Consumption: {environmental_impact['energy_consumption']} kWh")
        print(f"Water Consumption: {environmental_impact['water_consumption']} litres")
        print(f"CO2 Emission: {environmental_impact['co2_emission']} kg")

    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
```
