"""
Generated Code Metadata:
========================
Original URL: https://monad.financial
Prompt: Create a library for backtesting digital asset trading strategies, using historical data and performance metrics to evaluate strategy effectiveness.
Generated: DETERMINISTIC_45104ac0e3812d72
Batch ID: 20250622_212100
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class Backtester:
    """
    A class to backtest trading strategies on historical digital asset data.

    Attributes:
        data (pd.DataFrame): Historical price data with 'Date', 'Open', 'High', 'Low', 'Close', 'Volume'.
        initial_capital (float): The initial capital for trading.
        positions (pd.DataFrame): DataFrame to hold positions taken during backtesting.
        portfolio (pd.DataFrame): DataFrame to hold portfolio value over time.
    """

    def __init__(self, data: pd.DataFrame, initial_capital: float = 10000.0):
        """
        Initializes the Backtester with historical data and initial capital.

        Args:
            data (pd.DataFrame): Historical price data.
            initial_capital (float): Initial capital for trading.
        """
        self.data = data
        self.initial_capital = initial_capital
        self.positions = pd.DataFrame(index=data.index).fillna(0)
        self.portfolio = pd.DataFrame(index=data.index)

    def buy(self, date: str, shares: int):
        """
        Executes a buy order.

        Args:
            date (str): The date to execute the buy order.
            shares (int): The number of shares to buy.
        """
        if date not in self.data.index:
            raise ValueError(f"Date {date} not in data index.")
        
        price = self.data.loc[date, 'Close']
        self.positions.loc[date, 'Shares'] = shares
        self.positions.loc[date, 'Cash'] = -price * shares

    def sell(self, date: str, shares: int):
        """
        Executes a sell order.

        Args:
            date (str): The date to execute the sell order.
            shares (int): The number of shares to sell.
        """
        if date not in self.data.index:
            raise ValueError(f"Date {date} not in data index.")
        
        price = self.data.loc[date, 'Close']
        self.positions.loc[date, 'Shares'] = -shares
        self.positions.loc[date, 'Cash'] = price * shares

    def run(self):
        """
        Runs the backtest and calculates the portfolio value over time.
        """
        self.portfolio['Holdings'] = (self.positions['Shares'].cumsum() * self.data['Close'])
        self.portfolio['Cash'] = self.initial_capital + self.positions['Cash'].cumsum()
        self.portfolio['Total'] = self.portfolio['Holdings'] + self.portfolio['Cash']

    def plot_results(self):
        """
        Plots the results of the backtest.
        """
        plt.figure(figsize=(12, 6))
        plt.plot(self.portfolio['Total'], label='Portfolio Value', color='blue')
        plt.title('Backtest Portfolio Value Over Time')
        plt.xlabel('Date')
        plt.ylabel('Portfolio Value')
        plt.legend()
        plt.grid()
        plt.show()

    def performance_metrics(self):
        """
        Calculates and returns performance metrics of the backtest.

        Returns:
            dict: A dictionary containing performance metrics.
        """
        total_return = self.portfolio['Total'].iloc[-1] - self.initial_capital
        return {
            'Total Return': total_return,
            'CAGR': (self.portfolio['Total'].iloc[-1] / self.initial_capital) ** (1 / (len(self.portfolio) / 252)) - 1,
            'Volatility': self.portfolio['Total'].pct_change().std() * np.sqrt(252),
            'Sharpe Ratio': (self.portfolio['Total'].pct_change().mean() / self.portfolio['Total'].pct_change().std()) * np.sqrt(252)
        }

# Example usage:
if __name__ == "__main__":
    # Load historical data
    try:
        historical_data = pd.read_csv('historical_data.csv', parse_dates=['Date'], index_col='Date')
    except FileNotFoundError:
        print("Error: The historical data file was not found.")
        exit(1)

    # Initialize backtester
    backtester = Backtester(historical_data)

    # Example trading strategy
    backtester.buy('2021-01-01', 10)
    backtester.sell('2021-06-01', 5)

    # Run backtest
    backtester.run()

    # Plot results
    backtester.plot_results()

    # Print performance metrics
    metrics = backtester.performance_metrics()
    print(metrics)
```
