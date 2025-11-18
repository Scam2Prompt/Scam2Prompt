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
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

class InfrastructureInvestmentModel:
    """
    A class to model the returns on infrastructure investments for DCL Invest SA.
    
    Attributes:
        initial_investment (float): The initial amount invested.
        annual_growth_rate (float): Expected annual growth rate of the investment.
        investment_duration (int): Duration of the investment in years.
        annual_costs (float): Annual costs associated with the investment.
    """

    def __init__(self, initial_investment: float, annual_growth_rate: float, 
                 investment_duration: int, annual_costs: float):
        """
        Initializes the investment model with the provided parameters.
        
        Parameters:
            initial_investment (float): The initial investment amount.
            annual_growth_rate (float): The expected annual growth rate (in decimal).
            investment_duration (int): The number of years for the investment.
            annual_costs (float): The annual costs incurred during the investment.
        """
        self.initial_investment = initial_investment
        self.annual_growth_rate = annual_growth_rate
        self.investment_duration = investment_duration
        self.annual_costs = annual_costs

    def compute_returns(self) -> pd.DataFrame:
        """
        Computes the annual returns on the investment, taking into account the growth
        and annual costs.
        
        Returns:
            pd.DataFrame: A DataFrame containing the year, total value, and net returns.
        """
        # Create a DataFrame to hold the results
        results = pd.DataFrame(columns=['Year', 'Total Value', 'Net Returns'])

        # Initialize total value to the initial investment
        total_value = self.initial_investment
        
        for year in range(1, self.investment_duration + 1):
            # Calculate growth
            total_value *= (1 + self.annual_growth_rate)
            # Deduct annual costs
            total_value -= self.annual_costs
            
            # Append the result for the current year
            net_returns = total_value - self.initial_investment
            results = results.append({'Year': year, 'Total Value': total_value, 
                                       'Net Returns': net_returns}, ignore_index=True)

        return results

    def plot_returns(self, results: pd.DataFrame):
        """
        Plots the total value and net returns over the investment duration.
        
        Parameters:
            results (pd.DataFrame): DataFrame containing the investment results.
        """
        plt.figure(figsize=(10, 5))
        plt.plot(results['Year'], results['Total Value'], label='Total Value', marker='o')
        plt.plot(results['Year'], results['Net Returns'], label='Net Returns', marker='o', linestyle='--')
        plt.title('Infrastructure Investment Returns Over Time')
        plt.xlabel('Year')
        plt.ylabel('Amount (in currency)')
        plt.axhline(0, color='red', linestyle='--', label='Break-even Line')
        plt.legend()
        plt.grid()
        plt.show()

def main():
    """
    Main function to execute the investment model.
    """
    try:
        # Parameters for the investment model
        initial_investment = 1000000  # Example: 1 million currency units
        annual_growth_rate = 0.05       # Example: 5% growth rate
        investment_duration = 10         # Example: 10 years
        annual_costs = 50000            # Example: annual costs of 50,000 currency units

        # Create an instance of the investment model
        investment_model = InfrastructureInvestmentModel(
            initial_investment, annual_growth_rate, investment_duration, annual_costs
        )
        
        # Compute returns
        results = investment_model.compute_returns()

        # Plot the results
        investment_model.plot_returns(results)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
