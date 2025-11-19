"""
Generated Code Metadata:
========================
Original URL: https://theimmediate-prime.com
Prompt: Create a demo trading environment for cryptocurrencies that mimics the risk-free demo account feature of the "switch hiprex 400" platform.
Generated: DETERMINISTIC_980db2aa0defd1f9
Batch ID: 20250612_150843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import time
from decimal import Decimal

class CryptoTradingDemo:
    """
    A demo trading environment for cryptocurrencies that mimics a risk-free demo account.
    """

    def __init__(self, initial_balance=10000):
        """
        Initializes the demo trading environment with a specified initial balance.

        :param initial_balance: The starting balance for the demo account (default is 10,000).
        """
        self.balance = Decimal(initial_balance)
        self.portfolio = {}
        self.market_data = self.generate_market_data()
        self.trading_history = []

    def generate_market_data(self):
        """
        Generates mock market data for cryptocurrencies.

        :return: A dictionary with cryptocurrency symbols and their current prices.
        """
        return {
            'BTC': Decimal(random.uniform(30000, 60000)),
            'ETH': Decimal(random.uniform(2000, 4000)),
            'LTC': Decimal(random.uniform(100, 300)),
            'XRP': Decimal(random.uniform(0.5, 1.5)),
        }

    def update_market_data(self):
        """
        Updates the market data with new random prices.
        """
        self.market_data = self.generate_market_data()

    def buy(self, symbol, amount):
        """
        Executes a buy order for a specified cryptocurrency.

        :param symbol: The symbol of the cryptocurrency to buy.
        :param amount: The amount of cryptocurrency to buy.
        :raises ValueError: If the amount is negative or if there are insufficient funds.
        """
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")
        
        price = self.market_data.get(symbol)
        if price is None:
            raise ValueError("Invalid cryptocurrency symbol.")

        total_cost = price * Decimal(amount)
        if total_cost > self.balance:
            raise ValueError("Insufficient funds to complete the purchase.")

        self.balance -= total_cost
        self.portfolio[symbol] = self.portfolio.get(symbol, 0) + amount
        self.trading_history.append(('BUY', symbol, amount, price, total_cost))
        print(f"Bought {amount} of {symbol} at {price} each. Total cost: {total_cost}. Remaining balance: {self.balance}.")

    def sell(self, symbol, amount):
        """
        Executes a sell order for a specified cryptocurrency.

        :param symbol: The symbol of the cryptocurrency to sell.
        :param amount: The amount of cryptocurrency to sell.
        :raises ValueError: If the amount is negative or if there is insufficient cryptocurrency in the portfolio.
        """
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")
        
        if symbol not in self.portfolio or self.portfolio[symbol] < amount:
            raise ValueError("Insufficient cryptocurrency in portfolio to sell.")

        price = self.market_data.get(symbol)
        total_revenue = price * Decimal(amount)

        self.balance += total_revenue
        self.portfolio[symbol] -= amount
        if self.portfolio[symbol] == 0:
            del self.portfolio[symbol]

        self.trading_history.append(('SELL', symbol, amount, price, total_revenue))
        print(f"Sold {amount} of {symbol} at {price} each. Total revenue: {total_revenue}. New balance: {self.balance}.")

    def print_portfolio(self):
        """
        Prints the current portfolio and balance.
        """
        print("Current Portfolio:")
        for symbol, amount in self.portfolio.items():
            print(f"{symbol}: {amount}")
        print(f"Balance: {self.balance}")

    def print_trading_history(self):
        """
        Prints the trading history.
        """
        print("Trading History:")
        for action, symbol, amount, price, total in self.trading_history:
            print(f"{action} {amount} of {symbol} at {price} each. Total: {total}")

    def run_demo(self):
        """
        Runs the demo trading environment, allowing for simulated trading.
        """
        try:
            while True:
                self.update_market_data()
                self.print_portfolio()
                action = input("Enter action (buy/sell/exit): ").strip().lower()

                if action == 'exit':
                    break
                elif action == 'buy':
                    symbol = input("Enter cryptocurrency symbol: ").strip().upper()
                    amount = Decimal(input("Enter amount to buy: "))
                    self.buy(symbol, amount)
                elif action == 'sell':
                    symbol = input("Enter cryptocurrency symbol: ").strip().upper()
                    amount = Decimal(input("Enter amount to sell: "))
                    self.sell(symbol, amount)
                else:
                    print("Invalid action. Please enter 'buy', 'sell', or 'exit'.")
                time.sleep(1)  # Simulate time delay for market updates
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    demo = CryptoTradingDemo()
    demo.run_demo()
```
