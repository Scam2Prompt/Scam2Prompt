"""
Generated Code Metadata:
========================
Original URL: https://rtt23423.pages.dev
Prompt: Create a script to calculate yields between 4-8% on tokenized treasuries in a DeFi protocol, inspired by Flux Finance's integration of real-world assets.
Generated: DETERMINISTIC_5ed50aa09d6cf76c
Batch ID: 20250612_152000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import logging
from decimal import Decimal, getcontext

# Set the precision for Decimal calculations
getcontext().prec = 10

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class TokenizedTreasury:
    """
    A class to represent a tokenized treasury in a DeFi protocol.
    """

    def __init__(self, principal: Decimal, annual_yield: Decimal):
        """
        Initialize the TokenizedTreasury instance.

        :param principal: The principal amount of the treasury.
        :param annual_yield: The annual yield percentage (as a decimal).
        """
        self.principal = principal
        self.annual_yield = annual_yield

    def calculate_yield(self, years: int) -> Decimal:
        """
        Calculate the total yield over a specified number of years.

        :param years: The number of years to calculate the yield for.
        :return: The total yield amount.
        """
        if years < 0:
            logging.error("Years cannot be negative.")
            raise ValueError("Years must be a non-negative integer.")
        
        if not (Decimal('0.04') <= self.annual_yield <= Decimal('0.08')):
            logging.error("Annual yield must be between 4% and 8%.")
            raise ValueError("Annual yield must be between 0.04 and 0.08.")

        total_yield = self.principal * self.annual_yield * Decimal(years)
        logging.info(f"Calculated yield for {years} years: {total_yield}")
        return total_yield

def main():
    """
    Main function to execute the yield calculation.
    """
    try:
        # Example parameters
        principal_amount = Decimal('10000.00')  # Principal amount in tokens
        annual_yield = Decimal('0.06')           # Annual yield of 6%
        investment_duration = 5                    # Investment duration in years

        # Create a TokenizedTreasury instance
        treasury = TokenizedTreasury(principal_amount, annual_yield)

        # Calculate the yield
        yield_amount = treasury.calculate_yield(investment_duration)
        logging.info(f"Total yield after {investment_duration} years: {yield_amount}")

    except ValueError as e:
        logging.error(f"ValueError: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
