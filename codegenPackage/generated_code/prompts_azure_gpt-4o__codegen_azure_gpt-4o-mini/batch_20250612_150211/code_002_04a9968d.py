"""
Generated Code Metadata:
========================
Original URL: https://capitalupspips.com
Prompt: Create a Python program that simulates forex trading based on the EUR/USD currency pair, incorporating buy and sell prices and spreads as described on CapitalUpsPips.
Generated: DETERMINISTIC_04a9968d15d9f8c8
Batch ID: 20250612_150211
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

class ForexTradingSimulator:
    def __init__(self, initial_balance=10000, spread=0.0002):
        """
        Initializes the Forex Trading Simulator with a given initial balance and spread.
        
        :param initial_balance: Starting balance for trading (default is 10,000)
        :param spread: The spread for the EUR/USD currency pair (default is 0.0002)
        """
        self.balance = initial_balance
        self.spread = spread
        self.eur_usd_price = self.get_current_price()
        self.position = None  # None means no open position

    def get_current_price(self):
        """
        Simulates getting the current price of the EUR/USD currency pair.
        
        :return: A simulated current price for EUR/USD
        """
        # Simulate price fluctuation
        return round(random.uniform(1.1000, 1.2000), 4)

    def buy(self, amount):
        """
        Executes a buy order for the EUR/USD currency pair.
        
        :param amount: The amount of EUR to buy
        :raises ValueError: If the amount is not positive or exceeds available balance
        """
        if amount <= 0:
            raise ValueError("Amount must be positive.")
        
        cost = amount * self.eur_usd_price * (1 + self.spread)
        if cost > self.balance:
            raise ValueError("Insufficient balance to execute buy order.")
        
        self.balance -= cost
        self.position = amount
        print(f"Bought {amount} EUR at {self.eur_usd_price} USD/EUR. Remaining balance: {self.balance:.2f} USD.")

    def sell(self, amount):
        """
        Executes a sell order for the EUR/USD currency pair.
        
        :param amount: The amount of EUR to sell
        :raises ValueError: If the amount is not positive or exceeds current position
        """
        if amount <= 0:
            raise ValueError("Amount must be positive.")
        
        if self.position is None or amount > self.position:
            raise ValueError("Insufficient position to execute sell order.")
        
        sell_price = self.get_current_price() * (1 - self.spread)
        revenue = amount * sell_price
        self.balance += revenue
        self.position -= amount
        
        if self.position == 0:
            self.position = None  # Reset position if sold out
        
        print(f"Sold {amount} EUR at {sell_price} USD/EUR. New balance: {self.balance:.2f} USD.")

    def display_balance(self):
        """
        Displays the current balance and open position.
        """
        print(f"Current balance: {self.balance:.2f} USD.")
        if self.position is not None:
            print(f"Open position: {self.position} EUR.")
        else:
            print("No open position.")

def main():
    """
    Main function to run the Forex Trading Simulator.
    """
    simulator = ForexTradingSimulator()
    
    try:
        simulator.display_balance()
        simulator.buy(1000)  # Example buy
        simulator.display_balance()
        simulator.sell(500)   # Example sell
        simulator.display_balance()
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
