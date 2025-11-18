"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.superstep.org
Prompt: Create a script to compare investment paths for silver bullion and gold, inspired by the analysis provided on Superstep.org.
Generated: DETERMINISTIC_c8176d1d99936ebc
Batch ID: 20250612_151948
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

class InvestmentComparison:
    def __init__(self, gold_prices: pd.Series, silver_prices: pd.Series):
        """
        Initializes the InvestmentComparison class with gold and silver price data.

        :param gold_prices: A Pandas Series containing historical gold prices.
        :param silver_prices: A Pandas Series containing historical silver prices.
        """
        self.gold_prices = gold_prices
        self.silver_prices = silver_prices
        self.investment_data = pd.DataFrame({'Gold': self.gold_prices, 'Silver': self.silver_prices})

    def calculate_returns(self) -> pd.DataFrame:
        """
        Calculates the daily returns of gold and silver investments.

        :return: A Pandas DataFrame containing the daily returns of gold and silver.
        """
        returns = self.investment_data.pct_change().dropna()
        return returns

    def cumulative_returns(self) -> pd.DataFrame:
        """
        Calculates the cumulative returns for gold and silver investments.

        :return: A Pandas DataFrame containing the cumulative returns of gold and silver.
        """
        cumulative_returns = (1 + self.calculate_returns()).cumprod() - 1
        return cumulative_returns

    def plot_investment_paths(self):
        """
        Plots the investment paths for gold and silver.
        """
        cumulative_returns = self.cumulative_returns()
        
        plt.figure(figsize=(12, 6))
        plt.plot(cumulative_returns.index, cumulative_returns['Gold'], label='Gold', color='gold')
        plt.plot(cumulative_returns.index, cumulative_returns['Silver'], label='Silver', color='silver')
        plt.title('Cumulative Returns of Gold and Silver Investments')
        plt.xlabel('Date')
        plt.ylabel('Cumulative Return')
        plt.legend()
        plt.grid()
        plt.tight_layout()
        plt.show()

def load_data(gold_file: str, silver_file: str) -> (pd.Series, pd.Series):
    """
    Loads gold and silver price data from CSV files.

    :param gold_file: Path to the CSV file containing gold prices.
    :param silver_file: Path to the CSV file containing silver prices.
    :return: Two Pandas Series containing the historical prices of gold and silver.
    """
    try:
        gold_data = pd.read_csv(gold_file, parse_dates=['Date'], index_col='Date')
        silver_data = pd.read_csv(silver_file, parse_dates=['Date'], index_col='Date')
        
        return gold_data['Price'], silver_data['Price']
    except Exception as e:
        print(f"Error loading data: {e}")
        raise e

if __name__ == "__main__":
    # Example file paths (replace with actual file paths)
    gold_file_path = 'gold_prices.csv'
    silver_file_path = 'silver_prices.csv'

    try:
        # Load the historical price data for gold and silver
        gold_prices, silver_prices = load_data(gold_file_path, silver_file_path)

        # Create an instance of the InvestmentComparison class
        investment_comparison = InvestmentComparison(gold_prices, silver_prices)

        # Plot the investment paths for gold and silver
        investment_comparison.plot_investment_paths()
    except Exception as e:
        print(f"Failed to run investment comparison: {e}")
```
