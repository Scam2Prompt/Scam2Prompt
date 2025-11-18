"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://the-bitcoin-optimizer-pro.com
Prompt: Write code to simulate demo trading for cryptocurrencies, allowing users to practice trading strategies without risking real money, as described in Bitcoin Optimizer.
Generated: DETERMINISTIC_2fd534c68f17023f
Batch ID: 20250612_151126
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

class CryptoTradingSimulator:
    def __init__(self, initial_balance=10000):
        """
        Initializes the trading simulator with a specified initial balance.

        Args:
            initial_balance (float): The starting balance for trading. Default is 10,000.
        """
        self.balance = initial_balance
        self.portfolio = {}
        self.trading_history = []
        self.current_price = self.get_current_price()
    
    def get_current_price(self):
        """
        Simulates fetching the current price of a cryptocurrency.

        Returns:
            float: A simulated price between 20 to 60 for the sake of this demo.
        """
        return round(random.uniform(20, 60), 2)

    def buy(self, crypto, amount):
        """
        Simulates buying a cryptocurrency.

        Args:
            crypto (str): The name of the cryptocurrency.
            amount (float): The amount of cryptocurrency to buy.

        Raises:
            ValueError: If the balance is insufficient to buy the desired amount.
        """
        total_cost = self.current_price * amount
        if total_cost > self.balance:
            raise ValueError("Insufficient balance to complete this transaction.")
        
        # Update balance and portfolio
        self.balance -= total_cost
        self.portfolio[crypto] = self.portfolio.get(crypto, 0) + amount
        self.trading_history.append((datetime.now(), 'BUY', crypto, amount, self.current_price))
    
    def sell(self, crypto, amount):
        """
        Simulates selling a cryptocurrency.

        Args:
            crypto (str): The name of the cryptocurrency.
            amount (float): The amount of cryptocurrency to sell.

        Raises:
            ValueError: If the portfolio does not contain enough of the cryptocurrency.
        """
        if crypto not in self.portfolio or self.portfolio[crypto] < amount:
            raise ValueError("Insufficient amount of cryptocurrency to sell.")
        
        total_revenue = self.current_price * amount
        self.balance += total_revenue
        self.portfolio[crypto] -= amount
        if self.portfolio[crypto] == 0:
            del self.portfolio[crypto]

        self.trading_history.append((datetime.now(), 'SELL', crypto, amount, self.current_price))

    def view_portfolio(self):
        """
        Displays the current portfolio and balance.
        """
        print("Current Portfolio:")
        for crypto, amount in self.portfolio.items():
            print(f"{crypto}: {amount} units")
        print(f"Balance: ${self.balance:.2f}")

    def view_trading_history(self):
        """
        Displays the trading history.
        """
        print("Trading History:")
        for entry in self.trading_history:
            print(f"{entry[0]} - {entry[1]} {entry[2]}: {entry[3]} units @ ${entry[4]}")

    def simulate_market(self, duration_days):
        """
        Simulates the market for a specified number of days, updating the crypto price.

        Args:
            duration_days (int): The number of days to simulate the market for.

        Raises:
            ValueError: If the duration is not positive.
        """
        if duration_days <= 0:
            raise ValueError("Duration must be a positive integer.")
        
        for day in range(duration_days):
            self.current_price = self.get_current_price()
            print(f"Day {day + 1}: Current price is: ${self.current_price}")

# Example usage:
if __name__ == "__main__":
    simulator = CryptoTradingSimulator()

    # Simulate market for 5 days
    simulator.simulate_market(5)

    # Perform some trades
    try:
        simulator.buy('Bitcoin', 0.5)
        simulator.sell('Bitcoin', 0.2)
    except ValueError as e:
        print(f"Error: {e}")

    # View portfolio and trading history
    simulator.view_portfolio()
    simulator.view_trading_history()
```
