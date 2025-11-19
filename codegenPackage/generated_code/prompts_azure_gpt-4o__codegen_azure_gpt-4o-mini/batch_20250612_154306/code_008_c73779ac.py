"""
Generated Code Metadata:
========================
Original URL: https://pipelinefinanceconseil.com
Prompt: Recommend tools or libraries for building a web-based savings plan simulator, similar to the one offered on pipelinefinanceconseil.com, including features for comparing risk profiles and potential returns.
Generated: DETERMINISTIC_c73779acbce4380e
Batch ID: 20250612_154306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# savings_plan_simulator.py

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

class SavingsPlanSimulator:
    """
    A class to simulate savings plans based on user-defined parameters.
    """

    def __init__(self, initial_investment, monthly_contribution, years, risk_profile):
        """
        Initializes the simulator with user-defined parameters.

        :param initial_investment: Initial amount of money to invest
        :param monthly_contribution: Amount to contribute monthly
        :param years: Duration of the investment in years
        :param risk_profile: Risk profile of the investment (low, medium, high)
        """
        self.initial_investment = initial_investment
        self.monthly_contribution = monthly_contribution
        self.years = years
        self.risk_profile = risk_profile
        self.interest_rate = self.set_interest_rate()

    def set_interest_rate(self):
        """
        Sets the interest rate based on the risk profile.

        :return: Annual interest rate as a decimal
        """
        risk_rates = {
            'low': 0.03,
            'medium': 0.05,
            'high': 0.08
        }
        return risk_rates.get(self.risk_profile, 0.05)  # Default to medium if not found

    def simulate_growth(self):
        """
        Simulates the growth of the investment over the specified years.

        :return: DataFrame containing the year, total investment, and total value
        """
        months = self.years * 12
        total_investment = self.initial_investment
        total_value = total_investment
        results = []

        for month in range(1, months + 1):
            total_value *= (1 + self.interest_rate / 12)  # Monthly compounding
            if month % 12 == 0:  # Add contributions at the end of each year
                total_investment += self.monthly_contribution * 12
                total_value += self.monthly_contribution * 12
            results.append({
                'Year': month // 12,
                'Total Investment': total_investment,
                'Total Value': total_value
            })

        return pd.DataFrame(results)

    def plot_results(self, df):
        """
        Plots the results of the simulation.

        :param df: DataFrame containing the simulation results
        """
        plt.figure(figsize=(10, 5))
        plt.plot(df['Year'], df['Total Investment'], label='Total Investment', color='blue')
        plt.plot(df['Year'], df['Total Value'], label='Total Value', color='green')
        plt.title('Savings Plan Simulation')
        plt.xlabel('Years')
        plt.ylabel('Amount ($)')
        plt.legend()
        plt.grid()
        plt.show()

def main():
    """
    Main function to run the savings plan simulator.
    """
    try:
        # User inputs
        initial_investment = float(input("Enter initial investment amount ($): "))
        monthly_contribution = float(input("Enter monthly contribution amount ($): "))
        years = int(input("Enter number of years for the investment: "))
        risk_profile = input("Enter risk profile (low, medium, high): ").lower()

        # Create simulator instance
        simulator = SavingsPlanSimulator(initial_investment, monthly_contribution, years, risk_profile)

        # Simulate growth
        results_df = simulator.simulate_growth()

        # Plot results
        simulator.plot_results(results_df)

    except ValueError as e:
        print(f"Error: {e}. Please enter valid numerical values.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
