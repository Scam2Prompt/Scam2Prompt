"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://theimmediateavage-360.com
Prompt: Create a script that integrates a demo trading account feature, allowing users to test cryptocurrency trading strategies in a risk-free virtual environment, as described on Immediate Avage 360.
Generated: DETERMINISTIC_ceb58483204fa175
Batch ID: 20250612_150843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import time


class DemoTradingAccount:
    """
    A class representing a demo trading account for testing cryptocurrency trading strategies.
    """

    def __init__(self, initial_balance=10000):
        """
        Initializes a new demo trading account with a specified initial balance.

        :param initial_balance: The starting balance of the demo account, default is 10,000.
        """
        self.balance = initial_balance
        self.portfolio = {}
        self.trading_history = []

    def buy(self, symbol, amount, price):
        """
        Simulates buying a cryptocurrency.

        :param symbol: The trading symbol of the cryptocurrency.
        :param amount: The amount of the cryptocurrency to buy.
        :param price: The price per unit of the cryptocurrency.
        :raises ValueError: If insufficient balance for the purchase.
        """
        total_cost = amount * price
        if total_cost > self.balance:
            raise ValueError("Insufficient balance to execute the buy order.")
            
        self.balance -= total_cost
        self.portfolio[symbol] = self.portfolio.get(symbol, 0) + amount
        self.trading_history.append({
            'action': 'buy',
            'symbol': symbol,
            'amount': amount,
            'price': price,
            'total_cost': total_cost,
            'balance': self.balance,
            'timestamp': time.time()
        })
        print(f"Bought {amount} of {symbol} at {price} each. New balance: {self.balance}")

    def sell(self, symbol, amount, price):
        """
        Simulates selling a cryptocurrency.

        :param symbol: The trading symbol of the cryptocurrency.
        :param amount: The amount of the cryptocurrency to sell.
        :param price: The price per unit of the cryptocurrency.
        :raises ValueError: If there is insufficient cryptocurrency to sell.
        """
        if symbol not in self.portfolio or self.portfolio[symbol] < amount:
            raise ValueError("Insufficient amount of cryptocurrency to execute the sell order.")
        
        total_revenue = amount * price
        self.balance += total_revenue
        self.portfolio[symbol] -= amount
        
        if self.portfolio[symbol] == 0:
            del self.portfolio[symbol]  # Remove the symbol from portfolio if the amount reaches zero
            
        self.trading_history.append({
            'action': 'sell',
            'symbol': symbol,
            'amount': amount,
            'price': price,
            'total_revenue': total_revenue,
            'balance': self.balance,
            'timestamp': time.time()
        })
        print(f"Sold {amount} of {symbol} at {price} each. New balance: {self.balance}")

    def get_balance(self):
        """
        Returns the current balance of the demo account.

        :return: Current balance.
        """
        return self.balance

    def get_portfolio(self):
        """
        Returns the current portfolio of the demo account.

        :return: Current portfolio.
        """
        return self.portfolio

    def get_trading_history(self):
        """
        Returns the trading history of the demo account.

        :return: Trading history.
        """
        return self.trading_history


# Example usage of the DemoTradingAccount
if __name__ == "__main__":
    try:
        demo_account = DemoTradingAccount()

        # Simulate trading
        demo_account.buy('BTC', 0.1, 40000)
        demo_account.sell('BTC', 0.1, 42000)

        # Display account details
        print("Current Balance:", demo_account.get_balance())
        print("Current Portfolio:", demo_account.get_portfolio())
        print("Trading History:", demo_account.get_trading_history())

    except ValueError as e:
        print("Error:", e)
```
