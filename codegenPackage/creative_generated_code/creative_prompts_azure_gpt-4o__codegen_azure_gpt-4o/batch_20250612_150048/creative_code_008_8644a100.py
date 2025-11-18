"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://the-bitcoin360-ai.com
Prompt: Develop a Python program to simulate cryptocurrency trading using backtesting with historical market data, similar to the features of Bitcoin 360 AI Elite.
Generated: DETERMINISTIC_8644a10034a755f2
Batch ID: 20250612_150048
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


class CryptoBacktester:
    """
    A class to backtest cryptocurrency trading strategies using historical market data.
    """

    def __init__(self, data: pd.DataFrame, initial_balance: float = 10000.0, trading_fee: float = 0.001):
        """
        Initialize the backtester.

        :param data: Historical market data as a pandas DataFrame. Must contain 'timestamp', 'open', 'high', 'low', 'close', 'volume'.
        :param initial_balance: Starting balance for the backtest (default: $10,000).
        :param trading_fee: Trading fee percentage per transaction (default: 0.1%).
        """
        self.data = data
        self.initial_balance = initial_balance
        self.balance = initial_balance
        self.trading_fee = trading_fee
        self.position = 0  # Quantity of cryptocurrency held
        self.trades = []  # Stores trade history

    def simple_strategy(self):
        """
        Implement a simple trading strategy:
        Buy when the price increases for 3 consecutive days.
        Sell when the price decreases for 3 consecutive days.
        """
        for i in range(3, len(self.data)):
            recent_closes = self.data['close'].iloc[i-3:i]

            # Buy condition: Price increases for 3 consecutive days
            if all(np.diff(recent_closes) > 0) and self.balance > 0:
                self.buy(self.data['close'].iloc[i])

            # Sell condition: Price decreases for 3 consecutive days
            elif all(np.diff(recent_closes) < 0) and self.position > 0:
                self.sell(self.data['close'].iloc[i])

    def buy(self, price: float):
        """
        Execute a buy order at the given price.

        :param price: Price at which the buy order is executed.
        """
        # Calculate the quantity of cryptocurrency to buy after trading fees
        quantity = (self.balance * (1 - self.trading_fee)) / price
        self.position += quantity
        self.balance = 0  # Spend entire balance
        self.trades.append({'type': 'buy', 'price': price, 'quantity': quantity, 'timestamp': self.data['timestamp'].iloc[self.data.index[self.data['close'] == price][0]]})

    def sell(self, price: float):
        """
        Execute a sell order at the given price.

        :param price: Price at which the sell order is executed.
        """
        # Calculate proceeds of the sell after trading fees
        proceeds = self.position * price * (1 - self.trading_fee)
        self.balance += proceeds
        self.trades.append({'type': 'sell', 'price': price, 'quantity': self.position, 'timestamp': self.data['timestamp'].iloc[self.data.index[self.data['close'] == price][0]]})
        self.position = 0  # Clear position

    def calculate_performance(self):
        """
        Calculate the performance of the backtest.

        :return: Dictionary containing final balance, percentage return, and trade history.
        """
        final_balance = self.balance + self.position * self.data['close'].iloc[-1]
        return {
            'initial_balance': self.initial_balance,
            'final_balance': final_balance,
            'percentage_return': ((final_balance - self.initial_balance) / self.initial_balance) * 100,
            'trades': self.trades
        }


def load_data(file_path: str) -> pd.DataFrame:
    """
    Load historical market data from a CSV file.

    :param file_path: Path to the CSV file.
    :return: Pandas DataFrame containing historical market data.
    """
    try:
        data = pd.read_csv(file_path)
        required_columns = {'timestamp', 'open', 'high', 'low', 'close', 'volume'}
        if not required_columns.issubset(data.columns):
            raise ValueError(f"CSV file must contain the following columns: {required_columns}")
        data['timestamp'] = pd.to_datetime(data['timestamp'])  # Ensure timestamp is in datetime format
        return data
    except FileNotFoundError:
        raise FileNotFoundError(f"The file at path '{file_path}' was not found.")
    except ValueError as ve:
        raise ve


def main():
    """
    Main function to execute the backtesting process.
    """
    # Load historical market data (replace 'data.csv' with the path to your dataset)
    try:
        data = load_data('data.csv')
    except Exception as e:
        print(f"Error loading data: {e}")
        return

    # Initialize backtester
    backtester = CryptoBacktester(data)

    # Run the simple trading strategy
    backtester.simple_strategy()

    # Calculate and display performance metrics
    performance = backtester.calculate_performance()
    print("Backtest Performance:")
    print(f"Initial Balance: ${performance['initial_balance']:.2f}")
    print(f"Final Balance: ${performance['final_balance']:.2f}")
    print(f"Percentage Return: {performance['percentage_return']:.2f}%")
    print("Trade History:")
    for trade in performance['trades']:
        print(trade)


if __name__ == "__main__":
    main()
```
