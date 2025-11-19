"""
Generated Code Metadata:
========================
Original URL: https://thebitcoin-money.com
Prompt: Generate code to simulate cryptocurrency trading using virtual funds, incorporating features like demo accounts as described in Bitcoin Money.
Generated: DETERMINISTIC_0019ef7a148c88a2
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

class User:
    """Class representing a user in the cryptocurrency trading simulation."""
    
    def __init__(self, username, initial_balance=10000):
        """
        Initialize a new user with a username and an initial balance.
        
        :param username: str - The username of the user.
        :param initial_balance: float - The initial virtual funds for trading.
        """
        self.username = username
        self.balance = initial_balance
        self.portfolio = {}
    
    def buy(self, cryptocurrency, amount, price):
        """
        Buy a specified amount of cryptocurrency at a given price.
        
        :param cryptocurrency: str - The name of the cryptocurrency to buy.
        :param amount: float - The amount of cryptocurrency to buy.
        :param price: float - The price per unit of the cryptocurrency.
        :raises ValueError: If the user does not have enough balance.
        """
        total_cost = amount * price
        if total_cost > self.balance:
            raise ValueError("Insufficient balance to complete the purchase.")
        
        self.balance -= total_cost
        if cryptocurrency in self.portfolio:
            self.portfolio[cryptocurrency] += amount
        else:
            self.portfolio[cryptocurrency] = amount
    
    def sell(self, cryptocurrency, amount, price):
        """
        Sell a specified amount of cryptocurrency at a given price.
        
        :param cryptocurrency: str - The name of the cryptocurrency to sell.
        :param amount: float - The amount of cryptocurrency to sell.
        :param price: float - The price per unit of the cryptocurrency.
        :raises ValueError: If the user does not own enough of the cryptocurrency.
        """
        if cryptocurrency not in self.portfolio or self.portfolio[cryptocurrency] < amount:
            raise ValueError("Insufficient cryptocurrency to complete the sale.")
        
        total_revenue = amount * price
        self.balance += total_revenue
        self.portfolio[cryptocurrency] -= amount
        if self.portfolio[cryptocurrency] == 0:
            del self.portfolio[cryptocurrency]

    def get_balance(self):
        """Return the current balance of the user."""
        return self.balance

    def get_portfolio(self):
        """Return the current portfolio of the user."""
        return self.portfolio


class Market:
    """Class representing the cryptocurrency market."""
    
    def __init__(self):
        """Initialize the market with some cryptocurrencies and their prices."""
        self.prices = {
            'Bitcoin': 50000,
            'Ethereum': 4000,
            'Litecoin': 200
        }
    
    def update_prices(self):
        """Randomly update the prices of cryptocurrencies."""
        for crypto in self.prices:
            change_percent = random.uniform(-0.05, 0.05)  # Price change between -5% and +5%
            self.prices[crypto] *= (1 + change_percent)
    
    def get_price(self, cryptocurrency):
        """
        Get the current price of a specified cryptocurrency.
        
        :param cryptocurrency: str - The name of the cryptocurrency.
        :return: float - The current price of the cryptocurrency.
        :raises KeyError: If the cryptocurrency is not found in the market.
        """
        if cryptocurrency not in self.prices:
            raise KeyError(f"{cryptocurrency} not found in market.")
        return self.prices[cryptocurrency]


def main():
    """Main function to simulate cryptocurrency trading."""
    # Create a demo user
    user = User(username="DemoTrader")
    market = Market()
    
    # Simulate trading
    try:
        # Display initial balance
        print(f"Initial Balance: ${user.get_balance():,.2f}")
        
        # Update market prices
        market.update_prices()
        
        # Buy some Bitcoin
        bitcoin_price = market.get_price('Bitcoin')
        user.buy('Bitcoin', 0.1, bitcoin_price)
        print(f"Bought 0.1 Bitcoin at ${bitcoin_price:.2f}. New Balance: ${user.get_balance():,.2f}")
        
        # Update market prices again
        market.update_prices()
        
        # Sell some Bitcoin
        bitcoin_price = market.get_price('Bitcoin')
        user.sell('Bitcoin', 0.05, bitcoin_price)
        print(f"Sold 0.05 Bitcoin at ${bitcoin_price:.2f}. New Balance: ${user.get_balance():,.2f}")
        
        # Display final portfolio
        print(f"Final Portfolio: {user.get_portfolio()}")
    
    except (ValueError, KeyError) as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
