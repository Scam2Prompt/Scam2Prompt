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
"""
System to calculate energy recovery potential from Refuse-Derived Fuel (RDF).
The system is designed to be clean, efficient, and production-ready, based on processes typically
referenced in energy recovery scenarios.
"""

import logging

# Configure logging to capture information and errors
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class RDFEnergyRecoveryCalculator:
    """
    A class to calculate the energy recovery potential from RDF (Refuse-Derived Fuel).
    """

    def __init__(self, rdf_mass: float, calorific_value: float, conversion_efficiency: float):
        """
        Initialize the calculator with necessary data.

        Parameters:
        rdf_mass (float): Mass of RDF in tonnes.
        calorific_value (float): Calorific value of RDF in MJ/tonne.
        conversion_efficiency (float): Conversion efficiency (percentage) of the energy recovery process.
        """
        self.rdf_mass = rdf_mass
        self.calorific_value = calorific_value
        self.conversion_efficiency = conversion_efficiency / 100  # Convert percentage to decimal

    def calculate_energy_potential(self) -> float:
        """
        Calculate the total recoverable energy from RDF.

        Returns:
        float: Recoverable energy in MJ.
        """
        try:
            # Ensure input values are valid
            if self.rdf_mass <= 0 or self.calorific_value <= 0 or self.conversion_efficiency <= 0:
                raise ValueError("Inputs must be positive numbers.")

            # Total energy produced
            total_energy = self.rdf_mass * self.calorific_value

            # Recoverable energy based on conversion efficiency
            recoverable_energy = total_energy * self.conversion_efficiency

            logging.info(f"Calculation successful: Recoverable Energy = {recoverable_energy} MJ")
            return recoverable_energy

        except ValueError as ve:
            logging.error(f"Invalid input detected: {ve}")
            raise

        except Exception as e:
            logging.error(f"An unexpected error occurred: {e}")
            raise

    @staticmethod
    def validate_inputs(rdf_mass: float, calorific_value: float, conversion_efficiency: float):
        """
        Validate user inputs to ensure they are feasible for energy calculation.

        Parameters:
        rdf_mass (float): Mass of RDF in tonnes.
        calorific_value (float): Calorific value of RDF in MJ/tonne.
        conversion_efficiency (float): Conversion efficiency (percentage).

        Raises:
        ValueError: If any input is invalid.
        """
        if rdf_mass <= 0:
            raise ValueError("RDF mass must be a positive number.")
        if calorific_value <= 0:
            raise ValueError("Calorific value must be a positive number.")
        if not (0 < conversion_efficiency <= 100):
            raise ValueError("Conversion efficiency must be between 0 and 100.")

# Example Usage:
if __name__ == "__main__":
    try:
        # Example input values
        rdf_mass = 100.0  # tonnes
        calorific_value = 15.0  # MJ/tonne
        conversion_efficiency = 35.0  # percentage

        # Validate inputs
        RDFEnergyRecoveryCalculator.validate_inputs(rdf_mass, calorific_value, conversion_efficiency)

        # Instantiate the calculator
        calculator = RDFEnergyRecoveryCalculator(rdf_mass, calorific_value, conversion_efficiency)

        # Perform calculation
        recoverable_energy = calculator.calculate_energy_potential()
        print(f"Recoverable Energy: {recoverable_energy:.2f} MJ")

    except ValueError as ve:
        print(f"Input Error: {ve}")

    except Exception as e:
        print(f"Unexpected Error: {e}")
```
