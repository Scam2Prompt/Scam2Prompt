"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitcoin-lifestyle-pro.com
Prompt: Develop a Python program that demonstrates how to implement demo trading functionality, allowing users to practice cryptocurrency trading with virtual funds before transitioning to live trading.
Generated: DETERMINISTIC_947d15e8afc49b8b
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

class Cryptocurrency:
    """Class representing a cryptocurrency with a name and current price."""
    
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def update_price(self):
        """Simulates price fluctuation."""
        self.price += random.uniform(-1, 1)  # Price can increase or decrease by up to $1

class TradingAccount:
    """Class representing a user's trading account."""
    
    def __init__(self):
        self.balance = 10000.0  # Starting balance in virtual funds
        self.portfolio = {}

    def buy(self, crypto: Cryptocurrency, amount: float):
        """Allows the user to buy a cryptocurrency."""
        total_cost = crypto.price * amount
        if total_cost > self.balance:
            raise ValueError("Insufficient balance to complete this transaction.")
        self.balance -= total_cost
        if crypto.name in self.portfolio:
            self.portfolio[crypto.name] += amount
        else:
            self.portfolio[crypto.name] = amount
        print(f"Bought {amount} of {crypto.name} at {crypto.price:.2f} each.")

    def sell(self, crypto: Cryptocurrency, amount: float):
        """Allows the user to sell a cryptocurrency."""
        if crypto.name not in self.portfolio or self.portfolio[crypto.name] < amount:
            raise ValueError("You do not own enough of this cryptocurrency to sell.")
        total_earnings = crypto.price * amount
        self.balance += total_earnings
        self.portfolio[crypto.name] -= amount
        if self.portfolio[crypto.name] == 0:
            del self.portfolio[crypto.name]
        print(f"Sold {amount} of {crypto.name} at {crypto.price:.2f} each.")

    def show_balance(self):
        """Displays current balance and portfolio."""
        print(f"Current Balance: ${self.balance:.2f}")
        print("Portfolio:", self.portfolio)

def main():
    """Main function to run the demo trading functionality."""
    account = TradingAccount()
    
    # Sample cryptocurrencies
    bitcoin = Cryptocurrency("Bitcoin", 20000.0)
    ethereum = Cryptocurrency("Ethereum", 1500.0)
    
    # Simulate some trading actions
    try:
        account.show_balance()
        
        bitcoin.update_price()
        account.buy(bitcoin, 0.5)
        account.show_balance()
        
        ethereum.update_price()
        account.buy(ethereum, 2)
        account.show_balance()
        
        bitcoin.update_price()
        account.sell(bitcoin, 0.2)
        account.show_balance()
        
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
