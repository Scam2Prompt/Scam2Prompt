"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://1k-daily-profits.com
Prompt: Write a Python script to backtest a trading strategy on historical asset price data, inspired by the data-driven approach of the 1K Daily Profit app.
Generated: DETERMINISTIC_27399a4de204fe61
Batch ID: 20250612_150843
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


class Backtester:
    """
    A class to backtest a trading strategy on historical asset price data.
    """
    def __init__(self, data: pd.DataFrame, strategy_name: str = "Simple Moving Average Strategy"):
        """
        Initialize the backtester.

        Parameters:
        - data (pd.DataFrame): Historical asset price data with a 'Date' column and a 'Close' column.
        - strategy_name (str): Name of the trading strategy being backtested.
        """
        if not {'Date', 'Close'}.issubset(data.columns):
            raise ValueError("Data must contain 'Date' and 'Close' columns.")

        self.data = data.copy()
        self.data['Date'] = pd.to_datetime(self.data['Date'])  # Ensure 'Date' is in datetime format
        self.data.set_index('Date', inplace=True)
        self.strategy_name = strategy_name
        self.data['Signal'] = 0  # Placeholder for trading signals
        self.data['Strategy Returns'] = 0  # Placeholder for strategy returns
        self.data['Cumulative Returns'] = 0

    def apply_sma_strategy(self, short_window: int = 20, long_window: int = 50):
        """
        Apply a simple moving average (SMA) crossover strategy.

        Parameters:
        - short_window (int): The short-term moving average period.
        - long_window (int): The long-term moving average period.
        """
        # Calculate short-term and long-term moving averages
        self.data['SMA_Short'] = self.data['Close'].rolling(window=short_window).mean()
        self.data['SMA_Long'] = self.data['Close'].rolling(window=long_window).mean()

        # Generate buy (1) and sell (-1) signals
        self.data['Signal'] = np.where(self.data['SMA_Short'] > self.data['SMA_Long'], 1, 0)
        self.data['Signal'] = self.data['Signal'].diff()

    def backtest(self, initial_capital: float = 10000):
        """
        Backtest the strategy using historical data.

        Parameters:
        - initial_capital (float): The starting capital for the backtest.
        """
        # Calculate daily returns
        self.data['Daily Return'] = self.data['Close'].pct_change()

        # Calculate strategy returns (daily returns multiplied by the signal)
        self.data['Strategy Returns'] = self.data['Daily Return'] * self.data['Signal'].shift(1)

        # Calculate cumulative returns from the strategy
        self.data['Cumulative Returns'] = (1 + self.data['Strategy Returns']).cumprod() * initial_capital

    def plot_results(self):
        """
        Plot the backtest results including cumulative returns and signals.
        """
        plt.figure(figsize=(12, 6))

        # Plot the asset's price and trading signals
        plt.subplot(2, 1, 1)
        plt.plot(self.data.index, self.data['Close'], label="Asset Price", color='blue')
        plt.plot(self.data.index, self.data['SMA_Short'], label="SMA Short", color='orange', linestyle='--')
        plt.plot(self.data.index, self.data['SMA_Long'], label="SMA Long", color='green', linestyle='--')

        # Highlight buy and sell signals
        plt.scatter(self.data.index[self.data['Signal'] == 1], 
                    self.data['Close'][self.data['Signal'] == 1], 
                    label='Buy Signal', marker='^', color='green', alpha=1)

        plt.scatter(self.data.index[self.data['Signal'] == -1], 
                    self.data['Close'][self.data['Signal'] == -1], 
                    label='Sell Signal', marker='v', color='red', alpha=1)

        plt.title("Trading Signals and Price")
        plt.legend()
        plt.grid()

        # Plot cumulative returns
        plt.subplot(2, 1, 2)
        plt.plot(self.data.index, self.data['Cumulative Returns'], label="Cumulative Returns", color='purple')
        plt.title("Cumulative Returns")
        plt.legend()
        plt.grid()

        plt.tight_layout()
        plt.show()


if __name__ == "__main__":
    # Example usage
    try:
        # Load historical data
        # The CSV file must contain 'Date' and 'Close' columns
        historical_data = pd.read_csv("historical_data.csv")

        # Initialize the backtester
        backtester = Backtester(data=historical_data)

        # Apply the SMA strategy
        backtester.apply_sma_strategy(short_window=20, long_window=50)

        # Run the backtest
        backtester.backtest(initial_capital=10000)

        # Plot the results
        backtester.plot_results()

    except FileNotFoundError as e:
        print(f"Error: Historical data file not found. {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
```
