"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://assettrackr.app
Prompt: Create a Python script to model private equity investment returns based on risk aversion and timing, similar to the approach outlined by Grade World Investment Limited.
Generated: DETERMINISTIC_161a85dd35a0240e
Batch ID: 20250612_150448
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np
import matplotlib.pyplot as plt

class PrivateEquityInvestment:
    """
    Class to model private equity investment returns based on risk aversion and timing.
    """

    def __init__(self, initial_investment, risk_aversion, years, expected_return=0.12, volatility=0.2):
        """
        Initialize the investment model.

        :param initial_investment: The initial amount invested (float).
        :param risk_aversion: Risk aversion factor (float: 0.0 < risk_aversion <= 1.0).
        :param years: Investment period in years (int).
        :param expected_return: Expected annual return (float, default=0.12 for 12%).
        :param volatility: Annual volatility (float, default=0.2 for 20%).
        """
        if not (0.0 < risk_aversion <= 1.0):
            raise ValueError("Risk aversion must be between 0 and 1 (exclusive).")
        if years <= 0:
            raise ValueError("Investment period must be greater than zero.")

        self.initial_investment = initial_investment
        self.risk_aversion = risk_aversion
        self.years = years
        self.expected_return = expected_return
        self.volatility = volatility

    def simulate_returns(self):
        """
        Simulate investment returns over the given period using a geometric Brownian motion model.

        :return: A numpy array of portfolio values over time.
        """
        # Number of time steps (monthly granularity)
        time_steps = self.years * 12
        dt = 1 / 12  # Monthly time step size

        # Modify expected return based on risk aversion
        adjusted_return = self.expected_return * (1 - self.risk_aversion)

        # Generate random returns using geometric Brownian motion
        random_shocks = np.random.normal(
            loc=0, scale=self.volatility * np.sqrt(dt), size=time_steps
        )
        growth_rates = adjusted_return * dt + random_shocks
        portfolio_values = self.initial_investment * np.exp(np.cumsum(growth_rates))

        return portfolio_values

    def plot_returns(self, portfolio_values):
        """
        Plot the simulated portfolio values over time.

        :param portfolio_values: Numpy array of portfolio values over time.
        """
        plt.figure(figsize=(10, 6))
        plt.plot(portfolio_values, label="Portfolio Value")
        plt.title("Private Equity Investment Returns")
        plt.xlabel("Months")
        plt.ylabel("Portfolio Value")
        plt.legend()
        plt.grid(True)
        plt.show()

def main():
    """
    Main function to execute the private equity investment model.
    """
    try:
        # Parameters
        initial_investment = 100000  # $100,000
        risk_aversion = 0.3  # Moderate risk aversion
        years = 10  # 10-year investment horizon

        # Create investment model instance
        investment_model = PrivateEquityInvestment(
            initial_investment=initial_investment,
            risk_aversion=risk_aversion,
            years=years
        )

        # Simulate returns
        portfolio_values = investment_model.simulate_returns()

        # Plot results
        investment_model.plot_returns(portfolio_values)

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
