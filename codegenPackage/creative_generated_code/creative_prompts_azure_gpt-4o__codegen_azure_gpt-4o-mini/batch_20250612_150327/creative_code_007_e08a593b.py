"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamaskcoins.com
Prompt: Write code to simulate the growth of an investment portfolio over time using Meta Mask Coins' profit percentages and trade durations.
Generated: DETERMINISTIC_e08a593b2971f01e
Batch ID: 20250612_150327
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

class InvestmentPortfolio:
    """
    A class to simulate the growth of an investment portfolio over time.
    
    Attributes:
        initial_investment (float): The initial amount of money invested.
        profit_percentages (list): A list containing the profit percentages for each trade.
        trade_durations (list): A list containing the durations in years for each trade.
    """
    
    def __init__(self, initial_investment, profit_percentages, trade_durations):
        """
        Initializes the InvestmentPortfolio with the initial investment, profit percentages, and trade durations.
        
        Args:
            initial_investment (float): The initial amount of money invested.
            profit_percentages (list): A list of profit percentages (e.g., [0.1, 0.05]).
            trade_durations (list): A list of durations in years (e.g., [1, 2]).
        """
        if initial_investment <= 0:
            raise ValueError("Initial investment must be greater than zero.")
        if len(profit_percentages) != len(trade_durations):
            raise ValueError("Profit percentages and trade durations must have the same length.")
        
        self.initial_investment = initial_investment
        self.profit_percentages = profit_percentages
        self.trade_durations = trade_durations

    def simulate_growth(self):
        """
        Simulates the growth of the investment portfolio over the given trade durations.
        
        Returns:
            DataFrame: A Pandas DataFrame containing the year-wise growth of the portfolio.
        """
        # Initialize an array to hold the portfolio values over time
        portfolio_values = [self.initial_investment]
        
        for profit, duration in zip(self.profit_percentages, self.trade_durations):
            # Calculate the value growth over the trade duration
            for year in range(duration):
                current_value = portfolio_values[-1] * (1 + profit)
                portfolio_values.append(current_value)
        
        # Create a DataFrame to hold the results
        years = np.arange(0, len(portfolio_values))
        portfolio_df = pd.DataFrame({'Year': years, 'Portfolio Value': portfolio_values})
        
        return portfolio_df

    def plot_growth(self, portfolio_df):
        """
        Plots the growth of the investment portfolio.
        
        Args:
            portfolio_df (DataFrame): A DataFrame containing the year-wise portfolio values.
        """
        plt.figure(figsize=(10, 6))
        plt.plot(portfolio_df['Year'], portfolio_df['Portfolio Value'], marker='o')
        plt.title('Investment Portfolio Growth Over Time', fontsize=16)
        plt.xlabel('Year', fontsize=14)
        plt.ylabel('Portfolio Value ($)', fontsize=14)
        plt.grid()
        plt.xticks(portfolio_df['Year'])
        plt.show()

# Example usage
if __name__ == "__main__":
    try:
        # Define the initial investment amount, profit percentages, and trade durations
        initial_investment = 1000.0  # Example: $1000
        profit_percentages = [0.1, 0.05, 0.2]  # Example: 10%, 5%, 20%
        trade_durations = [1, 2, 1]  # Example: 1 year, 2 years, 1 year

        # Create an instance of InvestmentPortfolio
        portfolio = InvestmentPortfolio(initial_investment, profit_percentages, trade_durations)

        # Simulate the growth of the portfolio
        portfolio_df = portfolio.simulate_growth()

        # Plot the growth of the investment portfolio
        portfolio.plot_growth(portfolio_df)

    except ValueError as e:
        print(f"Error: {e}")
```
