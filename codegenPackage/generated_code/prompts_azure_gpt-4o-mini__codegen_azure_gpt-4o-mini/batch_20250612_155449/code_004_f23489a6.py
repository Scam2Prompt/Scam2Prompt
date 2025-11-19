"""
Generated Code Metadata:
========================
Original URL: https://suistrategies.com
Prompt: Construct a library function that simulates the performance of the investment strategy over the specified quarters, focusing on SUI's role in the portfolio.
Generated: DETERMINISTIC_f23489a642d30cad
Batch ID: 20250612_155449
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import pandas as pd

class InvestmentStrategy:
    """
    A class to simulate the performance of an investment strategy over specified quarters.
    This class focuses on the role of SUI (assumed to be a stock or asset) in the portfolio.
    """

    def __init__(self, initial_investment: float, quarterly_returns: pd.Series):
        """
        Initializes the InvestmentStrategy with an initial investment and quarterly returns.

        :param initial_investment: The initial amount of money to invest.
        :param quarterly_returns: A pandas Series containing the quarterly returns of the investment.
        """
        if initial_investment <= 0:
            raise ValueError("Initial investment must be greater than zero.")
        if not isinstance(quarterly_returns, pd.Series):
            raise TypeError("Quarterly returns must be a pandas Series.")

        self.initial_investment = initial_investment
        self.quarterly_returns = quarterly_returns

    def simulate_performance(self, quarters: int) -> float:
        """
        Simulates the performance of the investment strategy over a specified number of quarters.

        :param quarters: The number of quarters to simulate.
        :return: The final value of the investment after the specified quarters.
        """
        if quarters <= 0:
            raise ValueError("Number of quarters must be greater than zero.")
        if quarters > len(self.quarterly_returns):
            raise ValueError("Number of quarters exceeds the length of quarterly returns data.")

        # Initialize the investment value
        investment_value = self.initial_investment

        # Simulate the investment performance over the specified quarters
        for i in range(quarters):
            investment_value *= (1 + self.quarterly_returns.iloc[i])

        return investment_value

# Example usage:
if __name__ == "__main__":
    # Sample quarterly returns for SUI (as a pandas Series)
    sample_returns = pd.Series([0.05, 0.03, -0.02, 0.04, 0.06])

    # Initialize the investment strategy
    strategy = InvestmentStrategy(initial_investment=10000, quarterly_returns=sample_returns)

    # Simulate performance over 4 quarters
    try:
        final_value = strategy.simulate_performance(quarters=4)
        print(f"Final investment value after 4 quarters: ${final_value:.2f}")
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")
```
