"""
Generated Code Metadata:
========================
Original URL: https://dclinvest-sa.com
Prompt: Write a script to model infrastructure investment returns, reflecting DCL Invest SA's focus on economic growth and development through infrastructure upgrades.
Generated: DETERMINISTIC_9cdf2e9950ce0395
Batch ID: 20250612_155024
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

class InfrastructureInvestmentModel:
    """
    A class to model infrastructure investment returns for DCL Invest SA.
    
    Attributes:
        initial_investment (float): The initial amount invested in infrastructure.
        annual_growth_rate (float): The expected annual growth rate of the investment.
        investment_duration (int): The duration of the investment in years.
    """

    def __init__(self, initial_investment: float, annual_growth_rate: float, investment_duration: int):
        """
        Initializes the InfrastructureInvestmentModel with the given parameters.
        
        Parameters:
            initial_investment (float): The initial investment amount.
            annual_growth_rate (float): The expected annual growth rate (as a decimal).
            investment_duration (int): The number of years the investment will be held.
        """
        if initial_investment <= 0:
            raise ValueError("Initial investment must be greater than zero.")
        if not (0 <= annual_growth_rate <= 1):
            raise ValueError("Annual growth rate must be between 0 and 1.")
        if investment_duration <= 0:
            raise ValueError("Investment duration must be greater than zero.")

        self.initial_investment = initial_investment
        self.annual_growth_rate = annual_growth_rate
        self.investment_duration = investment_duration

    def calculate_returns(self) -> pd.DataFrame:
        """
        Calculates the projected returns over the investment duration.
        
        Returns:
            pd.DataFrame: A DataFrame containing the year and the corresponding investment value.
        """
        years = np.arange(0, self.investment_duration + 1)
        values = self.initial_investment * (1 + self.annual_growth_rate) ** years
        
        return pd.DataFrame({'Year': years, 'Investment Value': values})

    def plot_investment_growth(self):
        """
        Plots the growth of the investment over the specified duration.
        """
        investment_data = self.calculate_returns()
        
        plt.figure(figsize=(10, 6))
        plt.plot(investment_data['Year'], investment_data['Investment Value'], marker='o')
        plt.title('Projected Infrastructure Investment Growth')
        plt.xlabel('Year')
        plt.ylabel('Investment Value ($)')
        plt.grid()
        plt.xticks(investment_data['Year'])
        plt.tight_layout()
        plt.show()

# Example usage
if __name__ == "__main__":
    try:
        # Initialize the investment model with example parameters
        investment_model = InfrastructureInvestmentModel(initial_investment=1000000, 
                                                         annual_growth_rate=0.05, 
                                                         investment_duration=10)
        
        # Calculate and display the returns
        returns = investment_model.calculate_returns()
        print(returns)
        
        # Plot the investment growth
        investment_model.plot_investment_growth()
        
    except ValueError as e:
        print(f"Error: {e}")
```
