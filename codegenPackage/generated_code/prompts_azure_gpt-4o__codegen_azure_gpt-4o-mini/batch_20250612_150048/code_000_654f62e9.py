"""
Generated Code Metadata:
========================
Original URL: https://the-atomcapital.com
Prompt: Write Python code to simulate cryptocurrency trading strategies using insights from Atom Capital's educational resources on capital markets and risk management.
Generated: DETERMINISTIC_654f62e94b1c3eb5
Batch ID: 20250612_150048
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class CryptoTrader:
    """
    A class to simulate cryptocurrency trading strategies.
    """

    def __init__(self, initial_balance: float, transaction_fee: float):
        """
        Initializes the trader with a starting balance and transaction fee.

        :param initial_balance: The initial amount of capital to trade with.
        :param transaction_fee: The fee charged for each transaction as a percentage.
        """
        self.balance = initial_balance
        self.transaction_fee = transaction_fee
        self.holdings = 0.0
        self.trade_history = []

    def buy(self, price: float, amount: float):
        """
        Buys a specified amount of cryptocurrency at a given price.

        :param price: The price of the cryptocurrency at the time of purchase.
        :param amount: The amount of cryptocurrency to buy.
        """
        total_cost = price * amount * (1 + self.transaction_fee)
        if total_cost <= self.balance:
            self.balance -= total_cost
            self.holdings += amount
            self.trade_history.append(('buy', amount, price))
        else:
            raise ValueError("Insufficient balance to complete the purchase.")

    def sell(self, price: float, amount: float):
        """
        Sells a specified amount of cryptocurrency at a given price.

        :param price: The price of the cryptocurrency at the time of sale.
        :param amount: The amount of cryptocurrency to sell.
        """
        if amount <= self.holdings:
            total_revenue = price * amount * (1 - self.transaction_fee)
            self.balance += total_revenue
            self.holdings -= amount
            self.trade_history.append(('sell', amount, price))
        else:
            raise ValueError("Insufficient holdings to complete the sale.")

    def simulate_trading(self, price_data: pd.Series):
        """
        Simulates trading based on a simple strategy: buy when the price drops by 5% and sell when it rises by 5%.

        :param price_data: A pandas Series containing historical price data of the cryptocurrency.
        """
        for i in range(1, len(price_data)):
            price_today = price_data[i]
            price_yesterday = price_data[i - 1]

            # Buy condition: price drops by 5%
            if price_today < price_yesterday * 0.95:
                try:
                    self.buy(price_today, amount=1)  # Buy 1 unit
                except ValueError as e:
                    print(f"Buy error: {e}")

            # Sell condition: price rises by 5%
            elif price_today > price_yesterday * 1.05:
                try:
                    self.sell(price_today, amount=1)  # Sell 1 unit
                except ValueError as e:
                    print(f"Sell error: {e}")

    def get_balance(self):
        """
        Returns the current balance and holdings.

        :return: A tuple containing the current balance and holdings.
        """
        return self.balance, self.holdings

    def plot_trade_history(self):
        """
        Plots the trade history of the trader.
        """
        buys = [trade for trade in self.trade_history if trade[0] == 'buy']
        sells = [trade for trade in self.trade_history if trade[0] == 'sell']

        buy_prices = [trade[2] for trade in buys]
        sell_prices = [trade[2] for trade in sells]

        plt.figure(figsize=(10, 5))
        plt.plot(range(len(buy_prices)), buy_prices, 'g^', label='Buy', markersize=10)
        plt.plot(range(len(sell_prices)), sell_prices, 'rv', label='Sell', markersize=10)
        plt.title('Trade History')
        plt.xlabel('Trade Number')
        plt.ylabel('Price')
        plt.legend()
        plt.show()

# Example usage
if __name__ == "__main__":
    # Simulated price data for a cryptocurrency
    np.random.seed(42)  # For reproducibility
    price_data = pd.Series(np.random.normal(loc=100, scale=10, size=100).cumsum())

    trader = CryptoTrader(initial_balance=1000.0, transaction_fee=0.01)
    trader.simulate_trading(price_data)
    balance, holdings = trader.get_balance()
    print(f"Final Balance: {balance}, Holdings: {holdings}")
    trader.plot_trade_history()
```
