"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dclinvest-sa.com
Prompt: Write a script to model infrastructure investment returns, reflecting DCL Invest SA's focus on economic growth and development through infrastructure upgrades.
Generated: DETERMINISTIC_9cdf2e9950ce0395
Batch ID: 20250612_155024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import numpy as np
import pandas as pd


class InfrastructureInvestmentModel:
    """
    A class to model infrastructure investment returns with a focus on economic growth and development.
    """

    def __init__(self, initial_investment, annual_growth_rate, investment_horizon, risk_factor):
        """
        Initialize the investment model with key parameters.

        :param initial_investment: float, the initial amount invested in infrastructure.
        :param annual_growth_rate: float, annual percentage growth rate of returns (e.g., 0.05 for 5%).
        :param investment_horizon: int, the number of years over which the investment is modeled.
        :param risk_factor: float, risk factor (0-1) that represents uncertainty in returns (e.g., 0.2 for 20% risk).
        """
        self.initial_investment = initial_investment
        self.annual_growth_rate = annual_growth_rate
        self.investment_horizon = investment_horizon
        self.risk_factor = risk_factor
        self.results = pd.DataFrame()

    def simulate_returns(self):
        """
        Simulate annual investment returns over the investment horizon.

        :return: pd.DataFrame containing yearly data of investment returns.
        """
        try:
            # Initialize an array to store yearly returns
            yearly_returns = [self.initial_investment]

            for year in range(1, self.investment_horizon + 1):
                # Calculate annual growth with risk adjustment
                growth = yearly_returns[-1] * (1 + self.annual_growth_rate)
                risk_adjustment = np.random.normal(0, self.risk_factor * yearly_returns[-1])
                final_return = max(growth + risk_adjustment, 0)  # Ensure returns are non-negative

                yearly_returns.append(final_return)

            # Create a DataFrame to store results
            self.results = pd.DataFrame(
                {
                    "Year": range(0, self.investment_horizon + 1),
                    "Annual Return ($)": yearly_returns,
                }
            )
            return self.results

        except Exception as e:
            # Handle potential simulation errors
            print(f"An error occurred during simulation: {e}")
            raise

    def display_summary(self):
        """
        Display a summary of the simulation results including total growth and average annual return.

        :return: None
        """
        try:
            if self.results.empty:
                print("No simulation data available. Please run simulate_returns() first.")
                return

            total_growth = self.results["Annual Return ($)"].iloc[-1] - self.initial_investment
            average_return = self.results["Annual Return ($)"].mean()

            print("Investment Summary:")
            print(f"Initial Investment: ${self.initial_investment:,.2f}")
            print(f"Total Growth over {self.investment_horizon} years: ${total_growth:,.2f}")
            print(f"Average Annual Return: ${average_return:,.2f}")
        except Exception as e:
            # Handle errors in summary generation
            print(f"An error occurred while generating the summary: {e}")
            raise


# Example usage:
if __name__ == "__main__":
    # Define investment parameters
    initial_investment = 1_000_000  # $1,000,000
    annual_growth_rate = 0.07  # 7% annual growth rate
    investment_horizon = 10  # 10 years
    risk_factor = 0.15  # 15% risk factor

    # Initialize the investment model
    investment_model = InfrastructureInvestmentModel(
        initial_investment, annual_growth_rate, investment_horizon, risk_factor
    )

    # Simulate returns
    simulation_results = investment_model.simulate_returns()

    # Display results and summary
    print(simulation_results)
    investment_model.display_summary()
```
