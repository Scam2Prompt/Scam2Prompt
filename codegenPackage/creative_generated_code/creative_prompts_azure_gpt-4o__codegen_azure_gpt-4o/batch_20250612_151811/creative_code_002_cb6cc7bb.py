"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://agfinance-capitals.com
Prompt: Generate code to simulate portfolio growth over time using seed funding and innovation investments, aligning with the agfinance-capitals approach to tailored financial planning.
Generated: DETERMINISTIC_cb6cc7bb56fc53d2
Batch ID: 20250612_151811
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

class PortfolioGrowthSimulator:
    """
    A class to simulate portfolio growth over time based on seed funding
    and innovation investments following tailored financial planning principles.
    """

    def __init__(self, seed_funding, monthly_investment, growth_rate, risk_factor, months):
        """
        Initialize the portfolio simulator with parameters.

        :param seed_funding: Initial capital (float).
        :param monthly_investment: Monthly investment amount (float).
        :param growth_rate: Average annual growth rate in percentage (float).
        :param risk_factor: Risk adjustment factor (float, between 0 and 1).
        :param months: Total duration of simulation in months (int).
        """
        self.seed_funding = seed_funding
        self.monthly_investment = monthly_investment
        self.growth_rate = growth_rate / 100  # Convert percentage to decimal
        self.risk_factor = risk_factor
        self.months = months

    def simulate(self):
        """
        Simulate portfolio growth over the specified duration.

        :return: Tuple (portfolio_values, months_list)
                 portfolio_values: List of portfolio values over time.
                 months_list: List of months for simulation.
        """
        try:
            # Initialize portfolio value and growth tracking
            portfolio_values = [self.seed_funding]
            monthly_growth_rate = (1 + self.growth_rate) ** (1 / 12) - 1  # Monthly growth rate
            
            for month in range(1, self.months + 1):
                # Add monthly investment and adjust for growth and risk
                new_value = portfolio_values[-1] * (1 + monthly_growth_rate * self.risk_factor) + self.monthly_investment
                portfolio_values.append(new_value)

            months_list = list(range(self.months + 1))
            return portfolio_values, months_list

        except Exception as e:
            print(f"Error occurred during simulation: {e}")
            return [], []

    def plot_growth(self, portfolio_values, months_list):
        """
        Plot portfolio growth over time.

        :param portfolio_values: List of portfolio values over time.
        :param months_list: List of months for the simulation.
        """
        try:
            plt.figure(figsize=(10, 6))
            plt.plot(months_list, portfolio_values, label="Portfolio Value", color="blue", linewidth=2)
            plt.title("Portfolio Growth Simulation")
            plt.xlabel("Months")
            plt.ylabel("Portfolio Value ($)")
            plt.grid(True)
            plt.legend()
            plt.tight_layout()
            plt.show()
        except Exception as e:
            print(f"Error occurred during plotting: {e}")


if __name__ == "__main__":
    # Simulation parameters
    initial_seed_funding = 10000  # Starting capital ($)
    monthly_investment = 500      # Monthly investment ($)
    annual_growth_rate = 12       # Annualized growth rate (%)
    risk_adjustment_factor = 0.8  # Risk adjustment factor (between 0 and 1)
    simulation_months = 120       # Total simulation duration in months

    # Create simulator instance
    simulator = PortfolioGrowthSimulator(initial_seed_funding, monthly_investment,
                                          annual_growth_rate, risk_adjustment_factor, simulation_months)

    # Run simulation
    portfolio_values, months_list = simulator.simulate()

    # Check if simulation ran successfully before plotting
    if portfolio_values and months_list:
        simulator.plot_growth(portfolio_values, months_list)
    else:
        print("Simulation failed. Please check input parameters and try again.")
```
