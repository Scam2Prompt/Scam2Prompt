"""
Generated Code Metadata:
========================
Original URL: https://metis-investment.gr
Prompt: "How can biomass be used for electric and thermal energy production in agricultural applications?"
Generated: DETERMINISTIC_af8e35487cca6145
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Biomass Energy Simulation for Agricultural Applications

This script demonstrates how biomass can be used for electric and thermal energy production
in agricultural applications. It simulates the process of converting biomass into energy
and calculates the energy output based on input parameters.

Requirements:
- Python 3.x
"""

import logging

# Configure logging for error handling and debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class BiomassEnergyProduction:
    """
    A class to simulate biomass energy production for agricultural applications.
    """

    def __init__(self, biomass_mass_kg, energy_conversion_efficiency=0.35):
        """
        Initialize the biomass energy production system.

        :param biomass_mass_kg: Mass of biomass in kilograms (float)
        :param energy_conversion_efficiency: Efficiency of energy conversion (default: 35%)
        """
        if biomass_mass_kg <= 0:
            raise ValueError("Biomass mass must be greater than zero.")
        if not (0 < energy_conversion_efficiency <= 1):
            raise ValueError("Energy conversion efficiency must be between 0 and 1.")

        self.biomass_mass_kg = biomass_mass_kg
        self.energy_conversion_efficiency = energy_conversion_efficiency

    def calculate_energy_output(self):
        """
        Calculate the energy output from biomass.

        :return: Tuple containing electric energy (kWh) and thermal energy (kWh)
        """
        # Energy content of biomass (kWh per kg) - approximate value
        energy_content_per_kg = 4.5

        # Total energy available from biomass
        total_energy_kWh = self.biomass_mass_kg * energy_content_per_kg

        # Electric energy output (based on conversion efficiency)
        electric_energy_kWh = total_energy_kWh * self.energy_conversion_efficiency

        # Thermal energy output (remaining energy after electric conversion)
        thermal_energy_kWh = total_energy_kWh - electric_energy_kWh

        return electric_energy_kWh, thermal_energy_kWh

    def display_energy_output(self):
        """
        Display the calculated energy output.
        """
        try:
            electric_energy, thermal_energy = self.calculate_energy_output()
            logging.info(f"Electric Energy Output: {electric_energy:.2f} kWh")
            logging.info(f"Thermal Energy Output: {thermal_energy:.2f} kWh")
        except Exception as e:
            logging.error(f"Error calculating energy output: {e}")


def main():
    """
    Main function to simulate biomass energy production.
    """
    try:
        # Example input: Biomass mass in kilograms
        biomass_mass = float(input("Enter the biomass mass in kilograms: "))

        # Create an instance of BiomassEnergyProduction
        biomass_energy_system = BiomassEnergyProduction(biomass_mass)

        # Display the energy output
        biomass_energy_system.display_energy_output()

    except ValueError as ve:
        logging.error(f"Invalid input: {ve}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
