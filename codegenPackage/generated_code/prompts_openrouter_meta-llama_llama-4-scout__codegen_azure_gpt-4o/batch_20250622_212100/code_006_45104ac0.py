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
# File: backtesting_library.py

import pandas as pd
import numpy as np

class BacktestingLibrary:
    """
    A library for backtesting digital asset trading strategies using historical data.
    """

    def __init__(self, historical_data: pd.DataFrame):
        """
        Initialize the backtesting library with historical data.

        :param historical_data: A pandas DataFrame containing historical data.
                                Must include 'timestamp', 'price', and optionally 'volume'.
        """
        if not {'timestamp', 'price'}.issubset(historical_data.columns):
            raise ValueError("Historical data must include 'timestamp' and 'price' columns.")
        
        self.historical_data = historical_data.copy()
        self.historical_data['timestamp'] = pd.to_datetime(self.historical_data['timestamp'])
        self.historical_data.sort_values('timestamp', inplace=True)
        self.historical_data.reset_index(drop=True, inplace=True)

    def backtest_strategy(self, strategy_function):
        """
        Backtest a trading strategy using the provided strategy function.

        :param strategy_function: A function that takes a row of historical data and returns
                                  a trading signal ('buy', 'sell', or 'hold').
        :return: A dictionary containing performance metrics.
        """
        # Initialize variables for tracking performance
        initial_balance = 10000  # Starting balance in USD
        balance = initial_balance
        position = 0  # Number of assets held
        trade_log = []  # Log of trades

        for _, row in self.historical_data.iterrows():
            signal = strategy_function(row)
            price = row['price']

            if signal == 'buy' and balance > 0:
                # Buy as much as possible with the current balance
                quantity = balance / price
                position += quantity
                balance = 0
                trade_log.append({'timestamp': row['timestamp'], 'action': 'buy', 'price': price, 'quantity': quantity})

            elif signal == 'sell' and position > 0:
                # Sell all assets held
                balance += position * price
                trade_log.append({'timestamp': row['timestamp'], 'action': 'sell', 'price': price, 'quantity': position})
                position = 0

        # Calculate final portfolio value
        final_balance = balance + (position * self.historical_data.iloc[-1]['price'])

        # Calculate performance metrics
        total_return = (final_balance - initial_balance) / initial_balance * 100
        num_trades = len(trade_log)

        return {
            'initial_balance': initial_balance,
            'final_balance': final_balance,
            'total_return': total_return,
            'num_trades': num_trades,
            'trade_log': trade_log
        }

    def calculate_metrics(self, trade_log: list):
        """
        Calculate additional performance metrics based on the trade log.

        :param trade_log: A list of trades executed during backtesting.
        :return: A dictionary containing calculated metrics.
        """
        if not trade_log:
            return {'profit_factor': None, 'win_rate': None}

        profits = []
        losses = []
        for i in range(1, len(trade_log), 2):  # Pair buy and sell trades
            buy_trade = trade_log[i - 1]
            sell_trade = trade_log[i]
            pnl = (sell_trade['price'] - buy_trade['price']) * buy_trade['quantity']
            if pnl > 0:
                profits.append(pnl)
            else:
                losses.append(abs(pnl))

        profit_factor = sum(profits) / sum(losses) if losses else float('inf')
        win_rate = len(profits) / (len(profits) + len(losses)) * 100 if profits or losses else 0

        return {
            'profit_factor': profit_factor,
            'win_rate': win_rate
        }

# Example usage:
if __name__ == "__main__":
    # Load historical data (example format)
    data = pd.DataFrame({
        'timestamp': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04'],
        'price': [100, 105, 102, 110]
    })

    # Define a simple strategy function
    def example_strategy(row):
        if row['price'] < 103:
            return 'buy'
        elif row['price'] > 107:
            return 'sell'
        else:
            return 'hold'

    # Initialize the library and backtest the strategy
    backtester = BacktestingLibrary(data)
    results = backtester.backtest_strategy(example_strategy)
    metrics = backtester.calculate_metrics(results['trade_log'])

    # Print results
    print("Backtesting Results:", results)
    print("Performance Metrics:", metrics)
```
