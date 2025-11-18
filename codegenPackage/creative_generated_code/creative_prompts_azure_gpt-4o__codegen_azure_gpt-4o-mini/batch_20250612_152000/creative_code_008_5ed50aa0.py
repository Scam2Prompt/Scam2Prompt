"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rtt23423.pages.dev
Prompt: Create a script to calculate yields between 4-8% on tokenized treasuries in a DeFi protocol, inspired by Flux Finance's integration of real-world assets.
Generated: DETERMINISTIC_5ed50aa09d6cf76c
Batch ID: 20250612_152000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
from decimal import Decimal, getcontext

# Set the precision for Decimal calculations
getcontext().prec = 10

# Configure logging for better debugging and monitoring
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class TreasuryYieldCalculator:
    """
    A class to calculate yields for tokenized treasuries in a DeFi protocol.
    """

    def __init__(self, min_yield: Decimal, max_yield: Decimal):
        """
        Initializes the TreasuryYieldCalculator with a specified yield range.
        
        :param min_yield: Minimum yield (in percentage).
        :param max_yield: Maximum yield (in percentage).
        """
        self.min_yield = min_yield
        self.max_yield = max_yield
        
        # Validate the yield range
        if not (4 <= self.min_yield <= 8) or not (4 <= self.max_yield <= 8):
            raise ValueError("Yield values must be between 4% and 8% inclusive.")
        if self.min_yield > self.max_yield:
            raise ValueError("Minimum yield cannot be greater than maximum yield.")

    def calculate_yield(self, principal: Decimal, yield_percentage: Decimal) -> Decimal:
        """
        Calculates the yield based on the principal and yield percentage.
        
        :param principal: The principal amount (in the same denomination as the yield).
        :param yield_percentage: The yield percentage to apply.
        :return: Calculated yield.
        """
        if principal < 0:
            raise ValueError("Principal amount must be non-negative.")
        if not (self.min_yield <= yield_percentage <= self.max_yield):
            raise ValueError("Yield percentage must be within the specified range.")

        # Calculate the yield
        yield_amount = principal * (yield_percentage / Decimal(100))
        logging.info(f"Yield calculated: {yield_amount} on principal: {principal} at {yield_percentage}%")
        return yield_amount

    def simulate_yields(self, principal: Decimal) -> dict:
        """
        Simulates the yield calculations for a range of yields between min_yield and max_yield.
        
        :param principal: The principal amount (in the same denomination as the yield).
        :return: A dictionary of yields for each percentage in the specified range.
        """
        yields = {}
        for yield_percentage in range(int(self.min_yield), int(self.max_yield) + 1):
            try:
                yield_amount = self.calculate_yield(principal, Decimal(yield_percentage))
                yields[yield_percentage] = yield_amount
            except ValueError as e:
                logging.error(f"Error calculating yield for {yield_percentage}%: {e}")
        return yields

# Example usage
if __name__ == "__main__":
    try:
        # Create an instance of the calculator with a yield range
        calculator = TreasuryYieldCalculator(min_yield=Decimal(4), max_yield=Decimal(8))

        # Set the principal amount for calculations
        principal_amount = Decimal('10000.00')  # Replace with actual principal amount
        yield_results = calculator.simulate_yields(principal_amount)

        # Output the results
        logging.info("Yield results:")
        for yield_percentage, amount in yield_results.items():
            print(f"Yield at {yield_percentage}%: {amount:.2f}")

    except ValueError as e:
        logging.error(f"Initialization error: {e}")
```
