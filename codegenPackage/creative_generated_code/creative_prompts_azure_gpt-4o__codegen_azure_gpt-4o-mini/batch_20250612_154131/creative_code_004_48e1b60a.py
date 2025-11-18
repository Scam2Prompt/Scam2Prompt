"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app.extra-fl.io
Prompt: Create a Python script to calculate APR rewards for liquidity providers in Extra Finance's lending pools, factoring in $EXTRA token emissions and borrowing interest rates.
Generated: DETERMINISTIC_48e1b60ad2136a0e
Batch ID: 20250612_154131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import requests
import logging
from decimal import Decimal, InvalidOperation

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class APRCalculator:
    """
    A class to calculate the APR rewards for liquidity providers in Extra Finance's lending pools.
    """

    def __init__(self, emissions_per_block: Decimal, blocks_per_year: int, borrowing_interest_rate: Decimal):
        """
        Initializes the APRCalculator with necessary parameters.

        :param emissions_per_block: The amount of $EXTRA tokens emitted per block.
        :param blocks_per_year: The total number of blocks mined in a year.
        :param borrowing_interest_rate: The borrowing interest rate as a decimal (e.g., 0.05 for 5%).
        """
        self.emissions_per_block = emissions_per_block
        self.blocks_per_year = blocks_per_year
        self.borrowing_interest_rate = borrowing_interest_rate

    def calculate_annual_rewards(self) -> Decimal:
        """
        Calculates the annual rewards based on emissions and blocks per year.

        :return: Annual rewards in $EXTRA tokens.
        """
        annual_rewards = self.emissions_per_block * self.blocks_per_year
        logging.info(f"Annual rewards calculated: {annual_rewards} $EXTRA tokens.")
        return annual_rewards

    def calculate_apr(self) -> Decimal:
        """
        Calculates the APR for liquidity providers.

        :return: APR as a decimal.
        """
        try:
            annual_rewards = self.calculate_annual_rewards()
            apr = annual_rewards / (annual_rewards + self.borrowing_interest_rate)
            apr_percentage = apr * Decimal(100)  # Convert to percentage
            logging.info(f"APR calculated: {apr_percentage:.2f}%")
            return apr_percentage
        except ZeroDivisionError:
            logging.error("Error calculating APR: Division by zero.")
            return Decimal(0)
        except Exception as e:
            logging.error(f"An unexpected error occurred: {e}")
            return Decimal(0)

def main():
    """
    Main function to execute the APR calculation with example parameters.
    """
    # Example parameters
    emissions_per_block = Decimal('0.1')  # Example: 0.1 $EXTRA per block
    blocks_per_year = 10512000  # Approximate number of blocks per year for Ethereum
    borrowing_interest_rate = Decimal('0.05')  # Example: 5% annual borrowing interest rate

    # Create an instance of APRCalculator
    apr_calculator = APRCalculator(emissions_per_block, blocks_per_year, borrowing_interest_rate)

    # Calculate and display the APR
    apr = apr_calculator.calculate_apr()
    print(f"The calculated APR for liquidity providers is: {apr:.2f}%")

if __name__ == "__main__":
    main()
```
