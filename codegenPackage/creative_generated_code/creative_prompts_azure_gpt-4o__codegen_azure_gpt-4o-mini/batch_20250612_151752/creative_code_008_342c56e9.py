"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethereumprofit.org
Prompt: Generate code to simulate the trading of forked cryptocurrencies, such as Ethereum Classic and Bitcoin Cash, including mechanisms for handling hard and soft forks, as described on Auto Profit Hub.
Generated: DETERMINISTIC_342c56e9729a33cf
Batch ID: 20250612_151752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
from datetime import datetime, timedelta

class ForkedCryptocurrency:
    """
    A class to represent a forked cryptocurrency with mechanisms to handle hard and soft forks.
    """

    def __init__(self, name, price):
        """
        Initialize the cryptocurrency with a name and initial price.
        
        :param name: The name of the cryptocurrency.
        :param price: The current price of the cryptocurrency.
        """
        self.name = name
        self.price = price
        self.history = [(datetime.now(), price)]
        self.forks = []

    def update_price(self, new_price):
        """
        Update the cryptocurrency price and log the change.
        
        :param new_price: The new price of the cryptocurrency.
        """
        if new_price < 0:
            raise ValueError("Price cannot be negative.")
        self.price = new_price
        self.history.append((datetime.now(), new_price))

    def handle_fork(self, fork_type, fork_value):
        """
        Handle a cryptocurrency fork (hard or soft).

        :param fork_type: The type of fork ('hard' or 'soft').
        :param fork_value: The value to apply from the fork.
        """
        if fork_type not in ['hard', 'soft']:
            raise ValueError("Fork type must be either 'hard' or 'soft'.")

        # Simulate the impact of a fork on the cryptocurrency
        if fork_type == 'hard':
            self.price += fork_value
        else:  # soft fork
            self.price *= (1 + fork_value)

        self.forks.append((datetime.now(), fork_type, fork_value))
        self.history.append((datetime.now(), self.price))

    def get_price_history(self):
        """
        Retrieve the price history of the cryptocurrency.

        :return: List of tuples containing timestamps and prices.
        """
        return self.history

class TradingSimulator:
    """
    A class to simulate trading operations with forked cryptocurrencies.
    """

    def __init__(self):
        self.portfolio = {}

    def add_to_portfolio(self, crypto, amount):
        """
        Add a cryptocurrency to the trading portfolio.

        :param crypto: The ForkedCryptocurrency object to add.
        :param amount: The amount to add.
        """
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")
        self.portfolio[crypto.name] = self.portfolio.get(crypto.name, 0) + amount

    def simulate_trade(self, crypto, amount):
        """
        Simulate a trade for a specific cryptocurrency.

        :param crypto: The ForkedCryptocurrency object for the trade.
        :param amount: The amount to trade.
        """
        if crypto.name not in self.portfolio:
            raise ValueError(f"{crypto.name} not in portfolio.")
        if self.portfolio[crypto.name] < amount:
            raise ValueError("Insufficient funds in portfolio.")

        # Simulate trading
        trade_outcome = random.choice(['profit', 'loss'])
        price_change = random.uniform(-0.1, 0.1)  # Random price change
        new_price = crypto.price * (1 + price_change)

        if trade_outcome == 'profit':
            self.portfolio[crypto.name] -= amount
            crypto.update_price(new_price)
            print(f"Traded {amount} of {crypto.name} at profit! New price: {new_price}")
        else:
            print(f"Traded {amount} of {crypto.name} at loss! Price remains: {crypto.price}")

    def get_portfolio_value(self):
        """
        Calculate the total value of the portfolio based on current prices.

        :return: Total portfolio value.
        """
        total_value = 0
        for crypto_name, amount in self.portfolio.items():
            if crypto_name in crypto_registry:
                crypto = crypto_registry[crypto_name]
                total_value += crypto.price * amount
        return total_value

# Create a registry of cryptocurrencies
crypto_registry = {
    "Ethereum Classic": ForkedCryptocurrency("Ethereum Classic", 30.00),
    "Bitcoin Cash": ForkedCryptocurrency("Bitcoin Cash", 200.00)
}

# Example usage
if __name__ == "__main__":
    simulator = TradingSimulator()

    # Add cryptocurrencies to portfolio
    simulator.add_to_portfolio(crypto_registry["Ethereum Classic"], 10)
    simulator.add_to_portfolio(crypto_registry["Bitcoin Cash"], 5)

    # Simulate trades
    try:
        simulator.simulate_trade(crypto_registry["Ethereum Classic"], 2)
        simulator.simulate_trade(crypto_registry["Bitcoin Cash"], 3)
    except ValueError as e:
        print(f"Error: {e}")

    # Handle a soft fork
    crypto_registry["Bitcoin Cash"].handle_fork('soft', 0.05)

    # Get total portfolio value
    print(f"Total portfolio value: ${simulator.get_portfolio_value():.2f}")
```
