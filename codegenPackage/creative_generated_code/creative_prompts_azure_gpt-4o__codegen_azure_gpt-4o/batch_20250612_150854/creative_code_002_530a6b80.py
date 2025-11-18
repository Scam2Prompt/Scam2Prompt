"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediate-peak.io
Prompt: Create a simulation platform using Python that allows users to test crypto trading strategies before applying them to live markets, inspired by Immediate Peak's offerings.
Generated: DETERMINISTIC_530a6b80cfa15af0
Batch ID: 20250612_150854
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
from datetime import datetime
import matplotlib.pyplot as plt


class CryptoTradingSimulator:
    """
    A simulation platform for testing crypto trading strategies.
    """

    def __init__(self, initial_balance=10000):
        """
        Initialize the simulator with an initial balance and empty trading history.

        :param initial_balance: Starting balance for the simulation (default: 10,000 USD).
        """
        self.initial_balance = initial_balance
        self.balance = initial_balance
        self.portfolio = {}  # Dictionary to track holdings (e.g., {'BTC': 0.5})
        self.trading_history = []  # List to track all trades
        self.data = None  # Placeholder for historical market data

    def load_market_data(self, filepath):
        """
        Load historical market data from a CSV file.

        :param filepath: Path to the CSV file containing historical data.
        The file must have columns for 'timestamp', 'symbol', 'price'.
        """
        try:
            self.data = pd.read_csv(filepath)
            self.data['timestamp'] = pd.to_datetime(self.data['timestamp'])
            self.data.sort_values(['symbol', 'timestamp'], inplace=True)
        except Exception as e:
            print(f"Error loading market data: {e}")
            self.data = None

    def simulate_strategy(self, strategy_function):
        """
        Simulate a trading strategy using loaded market data.

        :param strategy_function: A user-defined function to execute trades. 
                                  Must accept parameters: (timestamp, symbol, price).
        """
        if self.data is None:
            raise ValueError("No market data loaded. Use load_market_data() first.")

        # Iterate over the market data and simulate trading
        for _, row in self.data.iterrows():
            timestamp = row['timestamp']
            symbol = row['symbol']
            price = row['price']
            strategy_function(self, timestamp, symbol, price)

    def execute_trade(self, action, symbol, amount, price):
        """
        Execute a trade and update the portfolio and balance.

        :param action: 'buy' or 'sell'.
        :param symbol: Cryptocurrency symbol (e.g., 'BTC').
        :param amount: Amount of cryptocurrency to buy/sell.
        :param price: Current market price of the cryptocurrency.
        """
        if action not in ['buy', 'sell']:
            raise ValueError("Invalid action. Must be 'buy' or 'sell'.")

        if amount <= 0:
            raise ValueError("Trade amount must be greater than zero.")

        trade_cost = amount * price

        if action == 'buy':
            if self.balance >= trade_cost:
                self.balance -= trade_cost
                self.portfolio[symbol] = self.portfolio.get(symbol, 0) + amount
                self.trading_history.append({'action': 'buy', 'symbol': symbol, 'amount': amount, 'price': price,
                                             'timestamp': datetime.now()})
            else:
                print("Insufficient balance for the trade.")
        elif action == 'sell':
            if self.portfolio.get(symbol, 0) >= amount:
                self.balance += trade_cost
                self.portfolio[symbol] -= amount
                if self.portfolio[symbol] == 0:
                    del self.portfolio[symbol]  # Remove empty holdings
                self.trading_history.append({'action': 'sell', 'symbol': symbol, 'amount': amount, 'price': price,
                                             'timestamp': datetime.now()})
            else:
                print("Insufficient holdings for the trade.")

    def display_summary(self):
        """
        Display a summary of the portfolio and trading activity.
        """
        print(f"Initial Balance: {self.initial_balance:.2f} USD")
        print(f"Current Balance: {self.balance:.2f} USD")
        print("Portfolio:")
        for symbol, amount in self.portfolio.items():
            print(f"  {symbol}: {amount:.4f}")
        print("\nTrading History:")
        for trade in self.trading_history:
            print(trade)

    def plot_balance_over_time(self):
        """
        Plot the balance over time based on trading history.
        """
        timestamps = [trade['timestamp'] for trade in self.trading_history]
        balances = [self.initial_balance] + [
            self.initial_balance + sum(
                trade['amount'] * trade['price'] if trade['action'] == 'sell' else -trade['amount'] * trade['price']
                for trade in self.trading_history[:i]
            ) for i in range(1, len(self.trading_history) + 1)
        ]

        plt.plot(timestamps, balances, label="Balance Over Time")
        plt.xlabel("Time")
        plt.ylabel("Balance (USD)")
        plt.title("Trading Simulation Balance")
        plt.legend()
        plt.grid(True)
        plt.show()


# Example usage:
def example_strategy(simulator, timestamp, symbol, price):
    """
    Example strategy: Buy 0.01 units of cryptocurrency if the price is below 50,000 USD,
                      and sell 0.01 units if the price is above 60,000 USD.

    :param simulator: Instance of CryptoTradingSimulator.
    :param timestamp: Current timestamp.
    :param symbol: Cryptocurrency symbol.
    :param price: Current market price.
    """
    if price < 50000:
        simulator.execute_trade(action='buy', symbol=symbol, amount=0.01, price=price)
    elif price > 60000:
        simulator.execute_trade(action='sell', symbol=symbol, amount=0.01, price=price)


if __name__ == "__main__":
    simulator = CryptoTradingSimulator(initial_balance=10000)
    simulator.load_market_data("crypto_market_data.csv")  # Replace with the path to your data file
    simulator.simulate_strategy(example_strategy)
    simulator.display_summary()
    simulator.plot_balance_over_time()
```
