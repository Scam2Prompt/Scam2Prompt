"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://theimmediategp.com
Prompt: Generate code to simulate Immediate GP's demo trading account functionality, allowing users to practice cryptocurrency trading without risking real money.
Generated: DETERMINISTIC_1e12e67fcd490913
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

class DemoTradingAccount:
    """
    A class to simulate a demo trading account for cryptocurrency trading.
    Users can practice trading without risking real money.
    """

    def __init__(self, initial_balance=10000.00):
        """
        Initializes a new demo trading account.

        :param initial_balance: The initial balance of the demo account.
        """
        self.balance = initial_balance
        self.positions = {}  # Stores open positions
        self.market_data = self.generate_market_data()  # Simulated market data

    def generate_market_data(self):
        """
        Generates simulated market data for cryptocurrencies.

        :return: A dictionary containing simulated prices for various cryptocurrencies.
        """
        return {
            'BTC': round(random.uniform(30000, 60000), 2),
            'ETH': round(random.uniform(1000, 4000), 2),
            'XRP': round(random.uniform(0.5, 2), 2)
        }

    def get_balance(self):
        """
        Returns the current balance of the demo trading account.

        :return: Current balance.
        """
        return self.balance

    def buy(self, crypto, amount):
        """
        Executes a buy order for the specified cryptocurrency.

        :param crypto: The cryptocurrency to buy.
        :param amount: The amount of cryptocurrency to buy.
        :raises ValueError: If the amount exceeds available balance.
        """
        price = self.market_data.get(crypto)
        if price is None:
            raise ValueError(f"Invalid cryptocurrency: {crypto}")
        
        total_cost = price * amount
        if total_cost > self.balance:
            raise ValueError("Insufficient balance to complete the purchase.")
        
        self.balance -= total_cost  # Deduct total cost from balance
        self.positions[crypto] = self.positions.get(crypto, 0) + amount  # Update positions
        print(f"Bought {amount} {crypto} at ${price} each. Total cost: ${total_cost}. Remaining balance: ${self.balance}.")

    def sell(self, crypto, amount):
        """
        Executes a sell order for the specified cryptocurrency.

        :param crypto: The cryptocurrency to sell.
        :param amount: The amount of cryptocurrency to sell.
        :raises ValueError: If the amount exceeds owned position or invalid cryptocurrency.
        """
        if crypto not in self.positions:
            raise ValueError(f"No positions for cryptocurrency: {crypto}")
        
        if amount > self.positions[crypto]:
            raise ValueError("Insufficient amount to sell.")
        
        price = self.market_data.get(crypto)
        total_revenue = price * amount
        self.balance += total_revenue  # Add revenue to balance
        self.positions[crypto] -= amount  # Deduct from positions
        
        if self.positions[crypto] == 0:
            del self.positions[crypto]  # Remove crypto if all sold
        
        print(f"Sold {amount} {crypto} at ${price} each. Total revenue: ${total_revenue}. New balance: ${self.balance}.")

    def show_positions(self):
        """
        Displays the current open positions in the demo trading account.

        :return: Current positions.
        """
        return self.positions

    def refresh_market_data(self):
        """
        Refreshes the market data to simulate new prices.
        """
        self.market_data = self.generate_market_data()
        print("Market data refreshed.")

# Example usage of the DemoTradingAccount class
if __name__ == "__main__":
    demo_account = DemoTradingAccount()

    # Display initial balance
    print(f"Initial balance: ${demo_account.get_balance()}")

    # Simulate buying and selling
    try:
        demo_account.buy('BTC', 0.1)
        demo_account.sell('BTC', 0.05)
        demo_account.refresh_market_data()
        print(f"Current positions: {demo_account.show_positions()}")
    except ValueError as e:
        print(f"Error: {e}")
```
