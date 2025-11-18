"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mainecotrust.cc
Prompt: Develop a script to calculate insurance coverage for trading losses based on the insured funds model described on mainecotrust.cc.
Generated: DETERMINISTIC_1b5a386e238ec192
Batch ID: 20250612_154603
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class InsuranceCoverageCalculator:
    """
    Class to calculate insurance coverage for trading losses based on the insured funds model.
    """

    def __init__(self, insured_funds, coverage_percentage):
        """
        Initializes the InsuranceCoverageCalculator instance.

        Args:
            insured_funds (float): Total insured funds.
            coverage_percentage (float): Percentage of coverage provided by the insurance model (0-100%).
        """
        if insured_funds < 0:
            raise ValueError("Insured funds must be a non-negative value.")
        if not (0 <= coverage_percentage <= 100):
            raise ValueError("Coverage percentage must be between 0 and 100.")
        
        self.insured_funds = insured_funds
        self.coverage_percentage = coverage_percentage / 100  # Convert to decimal for calculations

    def calculate_coverage(self, trading_loss):
        """
        Calculates the insurance coverage for the given trading loss.

        Args:
            trading_loss (float): The amount of trading loss to calculate coverage for.

        Returns:
            float: The insurance coverage amount.
        """
        if trading_loss < 0:
            raise ValueError("Trading loss must be a non-negative value.")
        
        # Calculate the maximum coverage amount based on insured funds and coverage percentage
        max_coverage = self.insured_funds * self.coverage_percentage
        
        # The actual coverage is the lesser of the trading loss or the maximum coverage
        coverage = min(trading_loss, max_coverage)
        logging.info(f"Calculated coverage for trading loss ${trading_loss}: ${coverage}")
        return coverage


def main():
    """
    Main function to demonstrate the InsuranceCoverageCalculator usage.
    """
    try:
        # Example user inputs (these could be collected dynamically in a real application)
        insured_funds = 10000.0  # Example insured funds amount
        coverage_percentage = 50.0  # Example coverage percentage
        trading_loss = 8000.0  # Example trading loss amount

        # Create an instance of the InsuranceCoverageCalculator
        calculator = InsuranceCoverageCalculator(insured_funds, coverage_percentage)

        # Calculate the insurance coverage for the given trading loss
        coverage = calculator.calculate_coverage(trading_loss)

        # Output the result
        print(f"Insurance coverage for trading loss of ${trading_loss}: ${coverage}")

    except ValueError as ve:
        logging.error(f"Input error: {ve}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
