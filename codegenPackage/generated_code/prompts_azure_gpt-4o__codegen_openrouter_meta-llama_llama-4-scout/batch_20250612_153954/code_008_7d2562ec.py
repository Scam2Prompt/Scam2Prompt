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
# cargo_insurance_calculator.py

"""
Calculates cargo insurance premiums based on Uniair Cargo's insurance brokerage services.

Author: [Your Name]
Date: [Today's Date]
"""

import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class CargoInsuranceCalculator:
    """
    Calculates cargo insurance premiums.

    Attributes:
        cargo_value (float): The value of the cargo.
        cargo_weight (float): The weight of the cargo in kilograms.
        insurance_rate (float): The insurance rate as a decimal.
        minimum_premium (float): The minimum insurance premium.
    """

    def __init__(self, cargo_value, cargo_weight, insurance_rate, minimum_premium):
        """
        Initializes a CargoInsuranceCalculator instance.

        Args:
            cargo_value (float): The value of the cargo.
            cargo_weight (float): The weight of the cargo in kilograms.
            insurance_rate (float): The insurance rate as a decimal.
            minimum_premium (float): The minimum insurance premium.

        Raises:
            ValueError: If cargo_value, cargo_weight, insurance_rate, or minimum_premium is not a positive number.
        """
        if cargo_value <= 0 or cargo_weight <= 0 or insurance_rate <= 0 or minimum_premium <= 0:
            raise ValueError("All input values must be positive numbers.")

        self.cargo_value = cargo_value
        self.cargo_weight = cargo_weight
        self.insurance_rate = insurance_rate
        self.minimum_premium = minimum_premium

    def calculate_premium(self):
        """
        Calculates the cargo insurance premium.

        Returns:
            float: The calculated insurance premium.
        """
        # Calculate premium based on cargo value and weight
        premium = max(self.cargo_value * self.insurance_rate, self.cargo_weight * 0.01 * self.insurance_rate)

        # Apply minimum premium
        return max(premium, self.minimum_premium)


def main():
    try:
        # Example usage
        cargo_value = 10000.0  # Cargo value in dollars
        cargo_weight = 500.0  # Cargo weight in kilograms
        insurance_rate = 0.005  # Insurance rate as a decimal
        minimum_premium = 50.0  # Minimum insurance premium

        calculator = CargoInsuranceCalculator(cargo_value, cargo_weight, insurance_rate, minimum_premium)
        premium = calculator.calculate_premium()

        logging.info(f"Cargo Insurance Premium: ${premium:.2f}")
        print(f"Cargo Insurance Premium: ${premium:.2f}")

    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
```
