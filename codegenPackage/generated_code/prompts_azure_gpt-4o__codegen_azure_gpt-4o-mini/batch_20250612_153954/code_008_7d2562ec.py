"""
Generated Code Metadata:
========================
Original URL: https://uniaircargo.id
Prompt: Create a Python script to calculate cargo insurance premiums based on Uniair Cargo’s insurance brokerage services.
Generated: DETERMINISTIC_7d2562ec29ed4b30
Batch ID: 20250612_153954
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class CargoInsuranceCalculator:
    """
    A class to calculate cargo insurance premiums based on the value of the cargo and the risk factors.
    """

    def __init__(self, base_rate: float, risk_factor: float):
        """
        Initializes the CargoInsuranceCalculator with a base rate and risk factor.

        :param base_rate: The base rate for calculating insurance premiums.
        :param risk_factor: The risk factor that affects the premium calculation.
        """
        if base_rate < 0 or risk_factor < 0:
            logging.error("Base rate and risk factor must be non-negative.")
            raise ValueError("Base rate and risk factor must be non-negative.")
        
        self.base_rate = base_rate
        self.risk_factor = risk_factor

    def calculate_premium(self, cargo_value: float) -> float:
        """
        Calculates the insurance premium for a given cargo value.

        :param cargo_value: The total value of the cargo to be insured.
        :return: The calculated insurance premium.
        """
        if cargo_value < 0:
            logging.error("Cargo value must be non-negative.")
            raise ValueError("Cargo value must be non-negative.")
        
        premium = self.base_rate * (1 + self.risk_factor) * (cargo_value / 1000)
        logging.info(f"Calculated premium: {premium} for cargo value: {cargo_value}")
        return premium

def main():
    """
    Main function to execute the cargo insurance premium calculation.
    """
    try:
        # Example parameters for the insurance calculation
        base_rate = 0.05  # Base rate per $1000 of cargo value
        risk_factor = 0.2  # 20% risk factor

        # Create an instance of the CargoInsuranceCalculator
        calculator = CargoInsuranceCalculator(base_rate, risk_factor)

        # Example cargo value
        cargo_value = 50000  # Total value of the cargo

        # Calculate the insurance premium
        premium = calculator.calculate_premium(cargo_value)
        print(f"The insurance premium for cargo value ${cargo_value} is: ${premium:.2f}")

    except ValueError as e:
        logging.error(f"Error in calculation: {e}")

if __name__ == "__main__":
    main()
```
