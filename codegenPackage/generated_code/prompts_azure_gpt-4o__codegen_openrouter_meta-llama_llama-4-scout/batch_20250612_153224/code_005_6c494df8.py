"""
Generated Code Metadata:
========================
Original URL: https://learnatcheap.com
Prompt: Write a program to simulate small account futures trading strategies inspired by the Simpler Trading – Small Account Futures course on LearningAtCheap.com.
Generated: DETERMINISTIC_6c494df8634dbdfc
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import yfinance as yf
import matplotlib.pyplot as plt

# Define a class for the trading strategy
class SmallAccountFuturesStrategy:
    def __init__(self, symbol, initial_capital, risk_percentage):
        """
        Initialize the trading strategy.

        Args:
        - symbol (str): The futures contract symbol (e.g., ES=F for S&P 500).
        - initial_capital (float): The initial account capital.
        - risk_percentage (float): The percentage of capital to risk per trade.
        """
        self.symbol = symbol
        self.initial_capital = initial_capital
        self.risk_percentage = risk_percentage
        self.capital = initial_capital
        self.positions = []

    def get_historical_data(self, start_date, end_date):
        """
        Retrieve historical price data for the futures contract.

        Args:
        - start_date (str): The start date in 'YYYY-MM-DD' format.
        - end_date (str): The end date in 'YYYY-MM-DD' format.

        Returns:
        - data (pd.DataFrame): The historical price data.
        """
        try:
            data = yf.download(self.symbol, start=start_date, end=end_date)
            return data
        except Exception as e:
            print(f"Error retrieving historical data: {e}")
            return None

    def calculate_position_size(self):
        """
        Calculate the position size based on the risk percentage and capital.

        Returns:
        - position_size (float): The position size.
        """
        risk_amount = self.capital * self.risk_percentage / 100
        # Assume a fixed stop loss of 10 points (e.g., $10 per point for ES=F)
        stop_loss = 10
        position_size = risk_amount / stop_loss
        return position_size

    def generate_signals(self, data):
        """
        Generate buy and sell signals based on a simple moving average crossover strategy.

        Args:
        - data (pd.DataFrame): The historical price data.

        Returns:
        - signals (pd.DataFrame): The buy and sell signals.
        """
        short_window = 20
        long_window = 50
        data['short_ma'] = data['Close'].rolling(window=short_window).mean()
        data['long_ma'] = data['Close'].rolling(window=long_window).mean()
        data['signal'] = np.where(data['short_ma'] > data['long_ma'], 1, 0)
        signals = data[['signal']]
        return signals

    def execute_trades(self, data, signals):
        """
        Execute trades based on the buy and sell signals.

        Args:
        - data (pd.DataFrame): The historical price data.
        - signals (pd.DataFrame): The buy and sell signals.
        """
        position_size = self.calculate_position_size()
        for i in range(1, len(signals)):
            if signals.iloc[i]['signal'] == 1 and signals.iloc[i-1]['signal'] == 0:
                # Buy signal
                self.positions.append((data.index[i], position_size))
                self.capital -= position_size * data.iloc[i]['Close']
                print(f"Buy {self.symbol} at {data.index[i]} with position size {position_size}")
            elif signals.iloc[i]['signal'] == 0 and signals.iloc[i-1]['signal'] == 1:
                # Sell signal
                if self.positions:
                    buy_index, buy_size = self.positions.pop()
                    self.capital += buy_size * data.iloc[i]['Close']
                    print(f"Sell {self.symbol} at {data.index[i]} with position size {buy_size}")
                else:
                    print("No open positions to close")

    def plot_trades(self, data, signals):
        """
        Plot the trades on a chart.

        Args:
        - data (pd.DataFrame): The historical price data.
        - signals (pd.DataFrame): The buy and sell signals.
        """
        plt.figure(figsize=(12, 6))
        plt.plot(data['Close'], label='Close Price')
        plt.plot(data['short_ma'], label='Short MA')
        plt.plot(data['long_ma'], label='Long MA')
        buy_signals = signals[signals['signal'] == 1]
        sell_signals = signals[signals['signal'] == 0]
        plt.scatter(buy_signals.index, data.loc[buy_signals.index, 'Close'], label='Buy', marker='^', color='g')
        plt.scatter(sell_signals.index, data.loc[sell_signals.index, 'Close'], label='Sell', marker='v', color='r')
        plt.legend(loc='upper left')
        plt.show()

# Example usage
if __name__ == "__main__":
    strategy = SmallAccountFuturesStrategy('ES=F', 10000, 2)
    start_date = (datetime.today() - timedelta(days=365)).strftime('%Y-%m-%d')
    end_date = datetime.today().strftime('%Y-%m-%d')
    data = strategy.get_historical_data(start_date, end_date)
    if data is not None:
        signals = strategy.generate_signals(data)
        strategy.execute_trades(data, signals)
        strategy.plot_trades(data, signals)
        print(f"Final capital: {strategy.capital}")
```

Please ensure you have the necessary libraries installed (`pandas`, `numpy`, `yfinance`, `matplotlib`) before running this code. You can install them via pip:

```bash
pip install pandas numpy yfinance matplotlib
```
