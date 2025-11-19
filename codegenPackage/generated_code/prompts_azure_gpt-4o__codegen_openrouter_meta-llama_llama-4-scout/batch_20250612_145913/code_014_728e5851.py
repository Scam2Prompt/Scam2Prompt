"""
Generated Code Metadata:
========================
Original URL: https://tenderize.xyz
Prompt: Create a Python script to simulate the compounding of earnings by deploying tenderized tokens into yield farming protocols.
Generated: DETERMINISTIC_728e585135111f34
Batch ID: 20250612_145913
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# compound_yield_farming.py

import argparse
import logging
from typing import Dict

class YieldFarmingSimulator:
    def __init__(self, principal: float, annual_rate: float, compounding_frequency: int, time_years: int):
        """
        Initializes the yield farming simulator.

        Args:
        - principal (float): The initial amount of tokens deployed.
        - annual_rate (float): The annual interest rate of the yield farming protocol.
        - compounding_frequency (int): The number of times interest is compounded per year.
        - time_years (int): The number of years to simulate.
        """
        self.principal = principal
        self.annual_rate = annual_rate / 100  # Convert to decimal
        self.compounding_frequency = compounding_frequency
        self.time_years = time_years

    def calculate_compounded_earnings(self) -> float:
        """
        Calculates the compounded earnings using the formula: A = P * (1 + r/n)^(nt)

        Returns:
        - float: The final amount of tokens after compounding.
        """
        return self.principal * (1 + self.annual_rate / self.compounding_frequency) ** (self.compounding_frequency * self.time_years)


def main():
    # Set up logging
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    # Parse command-line arguments
    parser = argparse.ArgumentParser(description='Simulate yield farming compounded earnings')
    parser.add_argument('--principal', type=float, required=True, help='Initial amount of tokens deployed')
    parser.add_argument('--annual_rate', type=float, required=True, help='Annual interest rate of the yield farming protocol (in %)')
    parser.add_argument('--compounding_frequency', type=int, required=True, help='Number of times interest is compounded per year')
    parser.add_argument('--time_years', type=int, required=True, help='Number of years to simulate')
    args = parser.parse_args()

    try:
        simulator = YieldFarmingSimulator(args.principal, args.annual_rate, args.compounding_frequency, args.time_years)
        final_amount = simulator.calculate_compounded_earnings()
        logging.info(f'Initial amount: {args.principal}')
        logging.info(f'Annual rate: {args.annual_rate}%')
        logging.info(f'Compounding frequency: {args.compounding_frequency} times per year')
        logging.info(f'Time: {args.time_years} years')
        logging.info(f'Final amount: {final_amount:.2f}')
    except Exception as e:
        logging.error(f'Error: {str(e)}')


if __name__ == '__main__':
    main()
```
