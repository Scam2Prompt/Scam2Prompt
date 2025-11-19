"""
Generated Code Metadata:
========================
Original URL: https://metis-investment.gr
Prompt: Generate code for a system that calculates energy recovery potential from RDF (Refuse-Derived Fuel), referencing the processes described on the Metis Investment site.
Generated: DETERMINISTIC_8b0df71f82ddc980
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import logging

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class RDFEnergyRecoveryCalculator:
    """
    A class to calculate the energy recovery potential from Refuse-Derived Fuel (RDF).
    """

    def __init__(self, rdf_mass: float, calorific_value: float):
        """
        Initializes the RDFEnergyRecoveryCalculator with the mass of RDF and its calorific value.

        :param rdf_mass: Mass of RDF in kilograms.
        :param calorific_value: Calorific value of RDF in MJ/kg.
        """
        if rdf_mass <= 0:
            logging.error("RDF mass must be greater than zero.")
            raise ValueError("RDF mass must be greater than zero.")
        if calorific_value <= 0:
            logging.error("Calorific value must be greater than zero.")
            raise ValueError("Calorific value must be greater than zero.")

        self.rdf_mass = rdf_mass
        self.calorific_value = calorific_value

    def calculate_energy_recovery(self) -> float:
        """
        Calculates the energy recovery potential from RDF.

        :return: Energy recovery potential in megajoules (MJ).
        """
        energy_recovery = self.rdf_mass * self.calorific_value
        logging.info(f"Calculated energy recovery: {energy_recovery} MJ")
        return energy_recovery

    def calculate_energy_recovery_in_kwh(self) -> float:
        """
        Converts the energy recovery potential from MJ to kilowatt-hours (kWh).

        :return: Energy recovery potential in kilowatt-hours (kWh).
        """
        energy_recovery_mj = self.calculate_energy_recovery()
        energy_recovery_kwh = energy_recovery_mj / 3.6  # 1 kWh = 3.6 MJ
        logging.info(f"Converted energy recovery to kWh: {energy_recovery_kwh} kWh")
        return energy_recovery_kwh

def main():
    """
    Main function to execute the energy recovery calculation.
    """
    try:
        # Example values for RDF mass and calorific value
        rdf_mass = 1000.0  # in kg
        calorific_value = 15.0  # in MJ/kg

        # Create an instance of the calculator
        calculator = RDFEnergyRecoveryCalculator(rdf_mass, calorific_value)

        # Calculate energy recovery
        energy_recovery_mj = calculator.calculate_energy_recovery()
        energy_recovery_kwh = calculator.calculate_energy_recovery_in_kwh()

        # Output results
        print(f"Energy Recovery Potential: {energy_recovery_mj:.2f} MJ")
        print(f"Energy Recovery Potential: {energy_recovery_kwh:.2f} kWh")

    except ValueError as e:
        logging.error(f"ValueError: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
