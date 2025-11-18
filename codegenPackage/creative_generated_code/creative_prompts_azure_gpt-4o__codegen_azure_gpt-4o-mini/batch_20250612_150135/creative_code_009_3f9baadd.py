"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://globalfinessetrade.com
Prompt: Create a program to rank and display the performance of trading strategies across multiple asset classes, similar to the reporting tools provided by Global Finesse Trade.
Generated: DETERMINISTIC_3f9baaddf0fd7d17
Batch ID: 20250612_150135
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class TradingStrategy:
    """Class to represent a trading strategy and its performance metrics."""

    def __init__(self, name, returns):
        """
        Initializes the TradingStrategy with a name and returns.

        Args:
            name (str): The name of the trading strategy.
            returns (pd.Series): A Series of returns for the strategy.
        """
        self.name = name
        self.returns = returns

    def calculate_performance_metrics(self):
        """Calculate and return performance metrics for the strategy."""
        metrics = {
            'Cumulative Return': self.get_cumulative_return(),
            'Annualized Return': self.get_annualized_return(),
            'Annualized Volatility': self.get_annualized_volatility(),
            'Sharpe Ratio': self.get_sharpe_ratio()
        }
        return metrics

    def get_cumulative_return(self):
        """Calculate cumulative return of the strategy."""
        return (1 + self.returns).cumprod()[-1] - 1

    def get_annualized_return(self):
        """Calculate annualized return of the strategy."""
        return self.returns.mean() * 252  # Assuming 252 trading days in a year

    def get_annualized_volatility(self):
        """Calculate annualized volatility of the strategy."""
        return self.returns.std() * np.sqrt(252)

    def get_sharpe_ratio(self, risk_free_rate=0.01):
        """Calculate Sharpe Ratio of the strategy.

        Args:
            risk_free_rate (float): The risk-free rate for Sharpe Ratio calculation.
        """
        excess_returns = self.returns - risk_free_rate / 252
        return excess_returns.mean() / excess_returns.std()

def rank_strategies(strategies):
    """Rank trading strategies based on performance metrics.

    Args:
        strategies (list of TradingStrategy): List containing TradingStrategy instances.
    
    Returns:
        pd.DataFrame: DataFrame containing the performance metrics ranked by Sharpe Ratio.
    """
    performance_df = pd.DataFrame()

    for strategy in strategies:
        performance_df = performance_df.append(strategy.calculate_performance_metrics(), ignore_index=True)

    performance_df.index = [strategy.name for strategy in strategies]
    performance_df = performance_df.sort_values(by='Sharpe Ratio', ascending=False)
    
    return performance_df

def display_performance(performance_df):
    """Display the performance metrics of trading strategies.

    Args:
        performance_df (pd.DataFrame): DataFrame containing strategy performance metrics.
    """
    print(performance_df)

def main():
    """Main function to execute the trading strategy ranking."""
    try:
        # Sample data for demonstration; replace with actual returns.
        np.random.seed(42)
        strategies = [
            TradingStrategy("Strategy A", pd.Series(np.random.normal(0.001, 0.02, 1000))),
            TradingStrategy("Strategy B", pd.Series(np.random.normal(0.0005, 0.015, 1000))),
            TradingStrategy("Strategy C", pd.Series(np.random.normal(0.0015, 0.025, 1000))),
        ]
        
        # Rank strategies based on their performance metrics.
        performance_df = rank_strategies(strategies)

        # Display the ranked performance metrics.
        display_performance(performance_df)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
