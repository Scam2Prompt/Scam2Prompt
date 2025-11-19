"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://suistrategies.com
Prompt: Construct a library function that simulates the performance of the investment strategy over the specified quarters, focusing on SUI's role in the portfolio.
Generated: DETERMINISTIC_f23489a642d30cad
Batch ID: 20250612_155449
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import numpy as np

class InvestmentStrategySimulator:
    """
    A class to simulate the performance of an investment strategy over specified quarters,
    focusing on the role of SUI in the portfolio.
    """

    def __init__(self, initial_investment, sut_allocation_ratio):
        """
        Initializes the simulator with an initial investment and SUI allocation ratio.

        :param initial_investment: Initial amount to invest.
        :param sut_allocation_ratio: Percentage of the investment allocated to SUI (0 to 1).
        """
        if not (0 <= sut_allocation_ratio <= 1):
            raise ValueError("SUI allocation ratio must be between 0 and 1.")
        
        self.initial_investment = initial_investment
        self.sui_allocation_ratio = sut_allocation_ratio
        self.portfolio_value = initial_investment

    def simulate_quarters(self, quarters, sui_return_rate):
        """
        Simulates the portfolio performance over a specified number of quarters.

        :param quarters: Number of quarters to simulate.
        :param sui_return_rate: Expected return rate for SUI over each quarter (as a decimal).
        :return: Final portfolio value after the specified quarters.
        """
        if quarters < 0:
            raise ValueError("Number of quarters must be a non-negative integer.")

        # Calculate allocation to SUI and other investments
        sui_investment = self.initial_investment * self.sui_allocation_ratio
        other_investment = self.initial_investment * (1 - self.sui_allocation_ratio)

        # Simulate the performance over the quarters
        for quarter in range(quarters):
            # Update SUI investment value
            sui_investment *= (1 + sui_return_rate)
            # Other investments can have a different return rate, assumed to be 0 for simplicity
            other_investment *= 1  # Placeholder for future investments

            # Update total portfolio value
            self.portfolio_value = sui_investment + other_investment

        return self.portfolio_value

# Example usage:
if __name__ == "__main__":
    try:
        initial_investment = 10000  # Example initial investment
        sui_allocation_ratio = 0.7   # 70% allocated to SUI
        quarters = 4                  # Simulate for 4 quarters
        sui_return_rate = 0.05        # 5% return rate for SUI

        simulator = InvestmentStrategySimulator(initial_investment, sui_allocation_ratio)
        final_value = simulator.simulate_quarters(quarters, sui_return_rate)

        print(f"Final portfolio value after {quarters} quarters: ${final_value:.2f}")

    except Exception as e:
        print(f"An error occurred: {e}")
```
