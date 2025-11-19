"""
Generated Code Metadata:
========================
Original URL: https://stakingstory.org
Prompt: Provide code to simulate yield optimization based on the dynamic interest rates described in the Story Staking platform.
Generated: DETERMINISTIC_b0adeda1835417ff
Batch ID: 20250612_153832
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

class YieldOptimizer:
    """
    A class to simulate yield optimization based on dynamic interest rates.
    """

    def __init__(self, initial_investment: float, interest_rates: pd.Series):
        """
        Initializes the YieldOptimizer with an initial investment and a series of interest rates.

        :param initial_investment: The initial amount of money to invest.
        :param interest_rates: A pandas Series containing the interest rates over time.
        """
        if initial_investment < 0:
            raise ValueError("Initial investment must be a non-negative value.")
        if not isinstance(interest_rates, pd.Series):
            raise TypeError("Interest rates must be provided as a pandas Series.")

        self.initial_investment = initial_investment
        self.interest_rates = interest_rates
        self.yield_history = []

    def simulate_yield(self, periods: int) -> float:
        """
        Simulates the yield over a specified number of periods.

        :param periods: The number of periods to simulate.
        :return: The final amount after applying the interest rates.
        """
        if periods <= 0:
            raise ValueError("Number of periods must be a positive integer.")
        if periods > len(self.interest_rates):
            raise ValueError("Number of periods exceeds the length of interest rates data.")

        current_amount = self.initial_investment

        for period in range(periods):
            # Apply the interest rate for the current period
            interest_rate = self.interest_rates.iloc[period]
            current_amount *= (1 + interest_rate)
            self.yield_history.append(current_amount)

        return current_amount

    def get_yield_history(self) -> list:
        """
        Returns the history of yields over the simulated periods.

        :return: A list of yield values for each period.
        """
        return self.yield_history

# Example usage
if __name__ == "__main__":
    # Sample interest rates for 12 months
    interest_rates_data = {
        'Month 1': 0.01,
        'Month 2': 0.015,
        'Month 3': 0.012,
        'Month 4': 0.014,
        'Month 5': 0.013,
        'Month 6': 0.016,
        'Month 7': 0.018,
        'Month 8': 0.017,
        'Month 9': 0.019,
        'Month 10': 0.015,
        'Month 11': 0.014,
        'Month 12': 0.013
    }

    # Convert the interest rates to a pandas Series
    interest_rates_series = pd.Series(interest_rates_data)

    # Initialize the YieldOptimizer with an initial investment of $1000
    optimizer = YieldOptimizer(initial_investment=1000, interest_rates=interest_rates_series)

    try:
        # Simulate yield for 12 periods (months)
        final_amount = optimizer.simulate_yield(periods=12)
        print(f"Final amount after 12 months: ${final_amount:.2f}")
        print("Yield history:", optimizer.get_yield_history())
    except (ValueError, TypeError) as e:
        print(f"Error during simulation: {e}")
```
