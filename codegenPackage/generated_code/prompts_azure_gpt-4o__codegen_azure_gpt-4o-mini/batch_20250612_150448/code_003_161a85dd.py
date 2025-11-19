"""
Generated Code Metadata:
========================
Original URL: https://assettrackr.app
Prompt: Create a Python script to model private equity investment returns based on risk aversion and timing, similar to the approach outlined by Grade World Investment Limited.
Generated: DETERMINISTIC_161a85dd35a0240e
Batch ID: 20250612_150448
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
import matplotlib.pyplot as plt

class PrivateEquityInvestmentModel:
    """
    A class to model private equity investment returns based on risk aversion and timing.
    """

    def __init__(self, initial_investment, risk_aversion, investment_period):
        """
        Initializes the investment model with the given parameters.

        :param initial_investment: Initial amount invested in the private equity.
        :param risk_aversion: A float representing the investor's risk aversion (0 to 1).
        :param investment_period: Duration of the investment in years.
        """
        self.initial_investment = initial_investment
        self.risk_aversion = risk_aversion
        self.investment_period = investment_period
        self.returns = []

    def simulate_returns(self):
        """
        Simulates the investment returns over the investment period based on risk aversion.
        """
        np.random.seed(42)  # For reproducibility
        for year in range(self.investment_period):
            # Simulate return based on risk aversion
            market_return = np.random.normal(loc=0.08, scale=0.15)  # Average market return
            adjusted_return = market_return * (1 - self.risk_aversion)
            self.returns.append(adjusted_return)

    def calculate_final_value(self):
        """
        Calculates the final value of the investment after the investment period.

        :return: Final value of the investment.
        """
        final_value = self.initial_investment
        for annual_return in self.returns:
            final_value *= (1 + annual_return)
        return final_value

    def plot_returns(self):
        """
        Plots the annual returns of the investment over the investment period.
        """
        years = np.arange(1, self.investment_period + 1)
        plt.figure(figsize=(10, 5))
        plt.plot(years, self.returns, marker='o', linestyle='-', color='b')
        plt.title('Annual Returns of Private Equity Investment')
        plt.xlabel('Year')
        plt.ylabel('Annual Return')
        plt.grid()
        plt.xticks(years)
        plt.axhline(0, color='red', linestyle='--')
        plt.show()

def main():
    """
    Main function to execute the investment model simulation.
    """
    try:
        # Parameters for the investment model
        initial_investment = 100000  # Initial investment amount
        risk_aversion = 0.5           # Risk aversion level (0 = no risk aversion, 1 = high risk aversion)
        investment_period = 10         # Investment period in years

        # Create an instance of the investment model
        investment_model = PrivateEquityInvestmentModel(initial_investment, risk_aversion, investment_period)

        # Simulate returns and calculate final value
        investment_model.simulate_returns()
        final_value = investment_model.calculate_final_value()

        # Output the final value
        print(f"Final value of the investment after {investment_period} years: ${final_value:,.2f}")

        # Plot the annual returns
        investment_model.plot_returns()

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
