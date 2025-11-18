"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitcoin-lifestyle-pro.com
Prompt: Write code to backtest a trading algorithm that uses historical price data, technical indicators, and chart patterns to evaluate its accuracy in predicting profitable cryptocurrency trades.
Generated: DETERMINISTIC_e3d561972a6754e5
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
import talib

class Backtester:
    def __init__(self, data: pd.DataFrame, initial_balance: float):
        """
        Initialize the backtester with historical data and an initial balance.

        :param data: A DataFrame containing historical price data with 'Date', 'Open', 'High', 'Low', 'Close', 'Volume' columns.
        :param initial_balance: Starting balance for the backtest.
        """
        self.data = data
        self.initial_balance = initial_balance
        self.balance = initial_balance
        self.position = 0  # Number of assets currently held
        self.trade_history = []

    def calculate_indicators(self):
        """
        Calculate technical indicators using TA-Lib.

        Updates the DataFrame with moving averages and RSI.
        """
        self.data['SMA_20'] = talib.SMA(self.data['Close'], timeperiod=20)
        self.data['SMA_50'] = talib.SMA(self.data['Close'], timeperiod=50)
        self.data['RSI'] = talib.RSI(self.data['Close'], timeperiod=14)

    def execute_trade(self, date: str, action: str, price: float):
        """
        Execute a trade and update the balance and position accordingly.

        :param date: The date of the trade.
        :param action: 'buy' or 'sell'.
        :param price: The price at which the trade is executed.
        """
        if action == 'buy':
            amount = self.balance / price
            self.balance = 0  # All balance is used to buy
            self.position += amount
            self.trade_history.append((date, action, price, amount))

        elif action == 'sell' and self.position > 0:
            self.balance += self.position * price
            self.trade_history.append((date, action, price, self.position))
            self.position = 0  # All assets sold
        else:
            raise ValueError("Invalid trade action or insufficient position.")

    def backtest(self):
        """
        Run the backtest on historical data to evaluate the trading strategy.
        """
        self.calculate_indicators()

        for index, row in self.data.iterrows():
            if (row['SMA_20'] > row['SMA_50']) and (row['RSI'] < 30):
                # Buy signal
                self.execute_trade(row['Date'], 'buy', row['Close'])
            elif (row['SMA_20'] < row['SMA_50']) and (row['RSI'] > 70):
                # Sell signal
                self.execute_trade(row['Date'], 'sell', row['Close'])

        # Calculate final balance after the backtest
        if self.position > 0:
            # Liquidate remaining position at last available price
            self.balance += self.position * self.data.iloc[-1]['Close']
            self.position = 0

        return self.balance

    def plot_results(self):
        """
        Plot the trade history against the price data to visualize the strategy performance.
        """
        plt.figure(figsize=(12, 6))
        plt.plot(self.data['Date'], self.data['Close'], label='Close Price', alpha=0.5)
        
        # Plot trades
        for trade in self.trade_history:
            date, action, price, amount = trade
            color = 'g' if action == 'buy' else 'r'
            plt.scatter(date, price, color=color, label=f'{action.capitalize()} at {price}', marker='o')

        plt.title('Trading Strategy Backtest Results')
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.legend()
        plt.show()

# Example usage
if __name__ == "__main__":
    # Load historical price data
    try:
        data = pd.read_csv('crypto_data.csv', parse_dates=['Date'])
        backtester = Backtester(data, initial_balance=10000)
        final_balance = backtester.backtest()
        print(f"Final Balance: ${final_balance:.2f}")
        backtester.plot_results()
    except FileNotFoundError:
        print("Error: The historical price data file was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
