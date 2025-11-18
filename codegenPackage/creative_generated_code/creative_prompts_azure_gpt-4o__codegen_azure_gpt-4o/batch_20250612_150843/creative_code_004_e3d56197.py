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
from ta import add_all_ta_features
from ta.utils import dropna

class Backtester:
    def __init__(self, data, initial_balance=10000, trading_fee=0.001):
        """
        Initialize the backtester.
        
        Parameters:
        data (pd.DataFrame): Historical price data with columns ['timestamp', 'open', 'high', 'low', 'close', 'volume']
        initial_balance (float): Starting balance for the backtest.
        trading_fee (float): Trading fee in percentage (e.g., 0.001 for 0.1%).
        """
        self.data = dropna(data)
        self.balance = initial_balance
        self.trading_fee = trading_fee
        self.position = 0  # 0 signifies no position, positive signifies long position
        self.trades = []  # List to store executed trades

    def add_technical_indicators(self):
        """
        Add technical indicators to the dataset using the `ta` library.
        """
        self.data = add_all_ta_features(
            self.data,
            open="open",
            high="high",
            low="low",
            close="close",
            volume="volume",
        )

    def evaluate_trade_signal(self, row):
        """
        Evaluate the trading signal based on technical indicators.
        
        Parameters:
        row (pd.Series): A single row from the dataset.
        
        Returns:
        str: 'buy', 'sell', or 'hold'
        """
        # Example trading logic based on RSI and Moving Average
        rsi = row["momentum_rsi"]
        short_ma = row["trend_sma_fast"]
        long_ma = row["trend_sma_slow"]
        close_price = row["close"]

        if short_ma > long_ma and rsi < 30:
            return 'buy'
        elif short_ma < long_ma and rsi > 70:
            return 'sell'
        else:
            return 'hold'

    def execute_trade(self, action, price):
        """
        Execute a trade based on the action ('buy' or 'sell') and the price.
        
        Parameters:
        action (str): 'buy' or 'sell'
        price (float): Price at which the trade is executed.
        """
        if action == 'buy' and self.balance > 0:
            # Calculate amount of cryptocurrency to buy
            crypto_amount = (self.balance * (1 - self.trading_fee)) / price
            self.position += crypto_amount
            self.balance = 0  # All balance is converted to cryptocurrency
            self.trades.append({'action': 'buy', 'price': price, 'crypto_amount': crypto_amount})
        elif action == 'sell' and self.position > 0:
            # Sell all the cryptocurrency
            sell_value = self.position * price * (1 - self.trading_fee)
            self.balance += sell_value
            self.position = 0  # No cryptocurrency held after selling
            self.trades.append({'action': 'sell', 'price': price, 'sell_value': sell_value})

    def backtest(self):
        """
        Run the backtest on the historical data.
        """
        for _, row in self.data.iterrows():
            action = self.evaluate_trade_signal(row)
            if action == 'buy':
                self.execute_trade('buy', row['close'])
            elif action == 'sell':
                self.execute_trade('sell', row['close'])

    def calculate_performance(self):
        """
        Calculate performance metrics for the backtest.
        
        Returns:
        dict: Performance metrics including final balance, total trades, and profit percentage.
        """
        final_balance = self.balance + (self.position * self.data.iloc[-1]['close'])
        profit_percentage = ((final_balance / 10000) - 1) * 100
        return {
            'final_balance': final_balance,
            'total_trades': len(self.trades),
            'profit_percentage': profit_percentage
        }

    def plot_performance(self):
        """
        Plot the performance of the algorithm over time.
        """
        self.data['balance_over_time'] = np.nan
        balance = self.balance
        position = self.position
        for i, row in self.data.iterrows():
            if position > 0:
                balance = position * row['close']
            self.data.at[i, 'balance_over_time'] = balance

        plt.figure(figsize=(12, 6))
        plt.plot(self.data['timestamp'], self.data['balance_over_time'], label='Balance Over Time', color='blue')
        plt.title('Backtesting Performance')
        plt.xlabel('Time')
        plt.ylabel('Balance')
        plt.legend()
        plt.show()


# Example usage:
if __name__ == "__main__":
    # Load historical price data (replace 'path_to_csv' with the actual file path)
    # The CSV file should have columns: ['timestamp', 'open', 'high', 'low', 'close', 'volume']
    historical_data = pd.read_csv('path_to_csv')

    # Initialize the backtester
    backtester = Backtester(historical_data)

    # Add technical indicators to the dataset
    backtester.add_technical_indicators()

    # Run the backtest
    backtester.backtest()

    # Calculate and print performance metrics
    performance = backtester.calculate_performance()
    print("Performance Metrics:", performance)

    # Plot the performance
    backtester.plot_performance()
```
