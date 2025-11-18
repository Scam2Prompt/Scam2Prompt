"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uniaircargo.id
Prompt: Create a Python script to calculate cargo insurance premiums based on Uniair Cargo’s insurance brokerage services.
Generated: DETERMINISTIC_7d2562ec29ed4b30
Batch ID: 20250612_153954
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging to output to console
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class CargoInsuranceCalculator:
    """Class to calculate cargo insurance premiums based on weight and value of the cargo."""

    def __init__(self, base_rate: float, weight_rate: float, value_rate: float):
        """
        Initialize the CargoInsuranceCalculator with base rate, weight rate, and value rate.

        :param base_rate: Fixed base insurance rate
        :param weight_rate: Rate per weight unit (e.g. per kg)
        :param value_rate: Rate per value unit (e.g. per $1000 of cargo value)
        """
        self.base_rate = base_rate
        self.weight_rate = weight_rate
        self.value_rate = value_rate

    def calculate_premium(self, weight: float, value: float) -> float:
        """
        Calculate the total insurance premium based on weight and value of the cargo.

        :param weight: Weight of the cargo in kg
        :param value: Value of the cargo in monetary units
        :return: Total insurance premium
        """
        if weight < 0 or value < 0:
            logging.error("Weight and value must be non-negative.")
            raise ValueError("Weight and value must be non-negative.")

        # Calculate premium components
        weight_premium = self.weight_rate * weight
        value_premium = (value / 1000) * self.value_rate
        
        # Total premium calculation
        total_premium = self.base_rate + weight_premium + value_premium
        
        logging.info(f"Calculated premium: Base: {self.base_rate}, "
                     f"Weight: {weight_premium}, Value: {value_premium}, "
                     f"Total: {total_premium}")
        
        return total_premium

def main():
    """Main function to run the cargo insurance premium calculation."""
    # Example rates (these would typically be fetched from a configuration or database)
    BASE_RATE = 50.0  # Base rate for insurance
    WEIGHT_RATE = 2.0  # Rate per kg
    VALUE_RATE = 5.0  # Rate per $1000 of value
    
    # Create an instance of the calculator
    calculator = CargoInsuranceCalculator(BASE_RATE, WEIGHT_RATE, VALUE_RATE)

    # Example cargo details (these could be input dynamically)
    cargo_weight = 100.0  # Weight of cargo in kg
    cargo_value = 50000.0  # Value of cargo in monetary units

    try:
        # Calculate and display the insurance premium
        premium = calculator.calculate_premium(cargo_weight, cargo_value)
        print(f"The cargo insurance premium is: ${premium:.2f}")
    except ValueError as e:
        logging.error(f"Error calculating premium: {e}")

if __name__ == "__main__":
    main()
```
