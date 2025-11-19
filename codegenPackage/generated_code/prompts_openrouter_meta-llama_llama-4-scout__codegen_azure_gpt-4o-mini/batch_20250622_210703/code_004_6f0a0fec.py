"""
Generated Code Metadata:
========================
Original URL: https://metis-investment.gr
Prompt: "Generate a Python code snippet to calculate the energy potential from urban waste for electric and thermal energy production, considering the services offered by Metis Investment."
Generated: DETERMINISTIC_6f0a0fec0e219a6c
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np

class UrbanWasteEnergyCalculator:
    """
    A class to calculate the energy potential from urban waste for electric and thermal energy production.
    """

    def __init__(self, waste_amount_tons, calorific_value_mj_kg, efficiency_electric, efficiency_thermal):
        """
        Initializes the UrbanWasteEnergyCalculator with the necessary parameters.

        :param waste_amount_tons: Total amount of urban waste in tons.
        :param calorific_value_mj_kg: Calorific value of the waste in MJ/kg.
        :param efficiency_electric: Efficiency of electric energy conversion (0 to 1).
        :param efficiency_thermal: Efficiency of thermal energy conversion (0 to 1).
        """
        self.waste_amount_tons = waste_amount_tons
        self.calorific_value_mj_kg = calorific_value_mj_kg
        self.efficiency_electric = efficiency_electric
        self.efficiency_thermal = efficiency_thermal

    def calculate_energy_potential(self):
        """
        Calculates the potential electric and thermal energy from urban waste.

        :return: A dictionary containing electric and thermal energy potential in MJ.
        """
        try:
            # Convert tons to kg
            waste_amount_kg = self.waste_amount_tons * 1000
            
            # Calculate total energy from waste in MJ
            total_energy_mj = waste_amount_kg * self.calorific_value_mj_kg
            
            # Calculate electric and thermal energy potential
            electric_energy_potential = total_energy_mj * self.efficiency_electric
            thermal_energy_potential = total_energy_mj * self.efficiency_thermal
            
            return {
                'electric_energy_potential_mj': electric_energy_potential,
                'thermal_energy_potential_mj': thermal_energy_potential
            }
        except Exception as e:
            print(f"Error calculating energy potential: {e}")
            return None

# Example usage
if __name__ == "__main__":
    # Parameters for the calculation
    waste_amount = 1000  # in tons
    calorific_value = 15  # in MJ/kg
    efficiency_electric = 0.25  # 25% efficiency for electric energy
    efficiency_thermal = 0.60  # 60% efficiency for thermal energy

    # Create an instance of the calculator
    energy_calculator = UrbanWasteEnergyCalculator(waste_amount, calorific_value, efficiency_electric, efficiency_thermal)

    # Calculate energy potential
    energy_potential = energy_calculator.calculate_energy_potential()

    if energy_potential:
        print(f"Electric Energy Potential: {energy_potential['electric_energy_potential_mj']} MJ")
        print(f"Thermal Energy Potential: {energy_potential['thermal_energy_potential_mj']} MJ")
```
