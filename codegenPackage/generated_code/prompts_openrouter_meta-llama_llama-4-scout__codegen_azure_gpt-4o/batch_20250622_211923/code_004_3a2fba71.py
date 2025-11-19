"""
Generated Code Metadata:
========================
Original URL: https://fiboex.com
Prompt: Generate code to create a simple Fibonacci-based trading strategy backtester using Python and relevant libraries.
Generated: DETERMINISTIC_3a2fba718c073906
Batch ID: 20250622_211923
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

# Define the Fibonacci-based trading strategy backtester
class FibonacciBacktester:
    def __init__(self, data, initial_balance=10000):
        """
        Initialize the backtester with market data and initial balance.

        :param data: A pandas DataFrame with 'Date' and 'Close' columns.
        :param initial_balance: Starting capital for the backtest.
        """
        self.data = data.copy()
        self.initial_balance = initial_balance
        self.balance = initial_balance
        self.position = 0  # Current position (number of shares held)
        self.trades = []  # List to store trade details
        self.data['Signal'] = 0  # Column to store buy/sell signals

    def calculate_fibonacci_levels(self, window=14):
        """
        Calculate Fibonacci retracement levels based on a rolling window.

        :param window: Lookback period for high and low prices.
        """
        self.data['High'] = self.data['Close'].rolling(window=window).max()
        self.data['Low'] = self.data['Close'].rolling(window=window).min()
        self.data['Fib_0.236'] = self.data['High'] - 0.236 * (self.data['High'] - self.data['Low'])
        self.data['Fib_0.382'] = self.data['High'] - 0.382 * (self.data['High'] - self.data['Low'])
        self.data['Fib_0.618'] = self.data['High'] - 0.618 * (self.data['High'] - self.data['Low'])

    def generate_signals(self):
        """
        Generate buy/sell signals based on Fibonacci levels.
        Buy when price crosses above the 0.618 level.
        Sell when price crosses below the 0.382 level.
        """
        for i in range(1, len(self.data)):
            if self.data['Close'].iloc[i] > self.data['Fib_0.618'].iloc[i] and \
                    self.data['Close'].iloc[i - 1] <= self.data['Fib_0.618'].iloc[i - 1]:
                self.data.at[i, 'Signal'] = 1  # Buy signal
            elif self.data['Close'].iloc[i] < self.data['Fib_0.382'].iloc[i] and \
                    self.data['Close'].iloc[i - 1] >= self.data['Fib_0.382'].iloc[i - 1]:
                self.data.at[i, 'Signal'] = -1  # Sell signal

    def execute_trades(self):
        """
        Execute trades based on generated signals and update balance.
        """
        for i, row in self.data.iterrows():
            if row['Signal'] == 1:  # Buy signal
                if self.position == 0:  # Only buy if no position is held
                    self.position = self.balance // row['Close']
                    self.balance -= self.position * row['Close']
                    self.trades.append({'Date': row['Date'], 'Type': 'Buy', 'Price': row['Close'], 'Shares': self.position})
            elif row['Signal'] == -1:  # Sell signal
                if self.position > 0:  # Only sell if a position is held
                    self.balance += self.position * row['Close']
                    self.trades.append({'Date': row['Date'], 'Type': 'Sell', 'Price': row['Close'], 'Shares': self.position})
                    self.position = 0

    def calculate_performance(self):
        """
        Calculate the final portfolio value and return on investment (ROI).
        """
        final_balance = self.balance + (self.position * self.data['Close'].iloc[-1])
        roi = (final_balance - self.initial_balance) / self.initial_balance * 100
        return final_balance, roi

    def plot_results(self):
        """
        Plot the price chart with buy/sell signals.
        """
        plt.figure(figsize=(12, 6))
        plt.plot(self.data['Date'], self.data['Close'], label='Close Price', color='blue')
        buy_signals = self.data[self.data['Signal'] == 1]
        sell_signals = self.data[self.data['Signal'] == -1]
        plt.scatter(buy_signals['Date'], buy_signals['Close'], label='Buy Signal', marker='^', color='green')
        plt.scatter(sell_signals['Date'], sell_signals['Close'], label='Sell Signal', marker='v', color='red')
        plt.title('Fibonacci Trading Strategy Backtest')
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.legend()
        plt.show()

    def run_backtest(self, window=14):
        """
        Run the full backtest process.

        :param window: Lookback period for Fibonacci levels.
        """
        self.calculate_fibonacci_levels(window)
        self.generate_signals()
        self.execute_trades()
        final_balance, roi = self.calculate_performance()
        print(f"Final Portfolio Value: ${final_balance:.2f}")
        print(f"Return on Investment (ROI): {roi:.2f}%")
        self.plot_results()


# Example usage
if __name__ == "__main__":
    # Generate example data (replace with real market data)
    dates = pd.date_range(start="2022-01-01", end="2022-12-31", freq="D")
    prices = np.cumsum(np.random.randn(len(dates)) * 2 + 0.1) + 100  # Simulated price data
    market_data = pd.DataFrame({'Date': dates, 'Close': prices})

    # Initialize and run the backtester
    backtester = FibonacciBacktester(market_data)
    backtester.run_backtest(window=14)
```
