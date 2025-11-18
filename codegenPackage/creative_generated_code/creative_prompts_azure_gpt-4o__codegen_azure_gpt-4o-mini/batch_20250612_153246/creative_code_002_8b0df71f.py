"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metis-investment.gr
Prompt: Generate code for a system that calculates energy recovery potential from RDF (Refuse-Derived Fuel), referencing the processes described on the Metis Investment site.
Generated: DETERMINISTIC_8b0df71f82ddc980
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class RDFEnergyRecoveryCalculator:
    """
    A class to calculate the energy recovery potential from Refuse-Derived Fuel (RDF).
    """

    def __init__(self, calorific_value: float, mass: float):
        """
        Initialize the RDF Energy Recovery Calculator.

        :param calorific_value: The calorific value of RDF in MJ/kg.
        :param mass: The mass of RDF in kilograms.
        """
        if calorific_value <= 0:
            logging.error("Calorific value must be greater than zero.")
            raise ValueError("Calorific value must be greater than zero.")
        
        if mass <= 0:
            logging.error("Mass must be greater than zero.")
            raise ValueError("Mass must be greater than zero.")

        self.calorific_value = calorific_value  # in MJ/kg
        self.mass = mass  # in kg

    def calculate_energy_recovery(self) -> float:
        """
        Calculate the total energy recovery potential.

        :return: Total energy recovery potential in MJ.
        """
        energy_recovery = self.calorific_value * self.mass
        logging.info(f"Calculated energy recovery: {energy_recovery} MJ")
        return energy_recovery

    def calculate_energy_recovery_per_ton(self) -> float:
        """
        Calculate energy recovery potential per ton of RDF.

        :return: Energy recovery potential per ton in MJ.
        """
        energy_recovery_per_ton = (self.calorific_value * 1000)  # Convert kg to tons
        logging.info(f"Calculated energy recovery per ton: {energy_recovery_per_ton} MJ")
        return energy_recovery_per_ton


if __name__ == "__main__":
    try:
        # Example values for calorific value and mass
        calorific_value_input = 15.0  # MJ/kg
        mass_input = 1000.0  # kg

        # Create an instance of the RDFEnergyRecoveryCalculator
        rdf_calculator = RDFEnergyRecoveryCalculator(calorific_value_input, mass_input)

        # Calculate total energy recovery
        total_energy_recovery = rdf_calculator.calculate_energy_recovery()
        logging.info(f"Total Energy Recovery: {total_energy_recovery} MJ")

        # Calculate energy recovery per ton
        energy_recovery_per_ton = rdf_calculator.calculate_energy_recovery_per_ton()
        logging.info(f"Energy Recovery per Ton: {energy_recovery_per_ton} MJ")

    except ValueError as e:
        logging.error(f"Error occurred: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
```
