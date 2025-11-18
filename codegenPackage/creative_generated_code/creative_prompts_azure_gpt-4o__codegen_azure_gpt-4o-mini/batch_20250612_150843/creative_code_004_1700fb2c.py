"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://theimmediateifexai.com
Prompt: Implement a demo account feature in a cryptocurrency trading application that allows users to test strategies in a risk-free environment, similar to Immediate Ifex Ai's demo account offering.
Generated: DETERMINISTIC_1700fb2cf94ff464
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
import uuid
from datetime import datetime, timedelta

class DemoAccount:
    """A class to represent a demo account for cryptocurrency trading."""

    def __init__(self, user_id):
        """
        Initialize a new demo account.

        Args:
            user_id (str): The unique identifier of the user.
        """
        self.user_id = user_id
        self.balance = 100000  # Starting balance for the demo account
        self.portfolio = {}
        self.trading_history = []
        self.account_id = str(uuid.uuid4())  # Unique ID for the demo account
        self.is_active = True
        self.created_at = datetime.now()
        self.expiration_date = self.created_at + timedelta(days=30)  # Valid for 30 days

    def buy(self, symbol, amount, price):
        """
        Buy a cryptocurrency.

        Args:
            symbol (str): The ticker symbol of the cryptocurrency.
            amount (float): The amount of cryptocurrency to buy.
            price (float): The price per unit of cryptocurrency.

        Raises:
            ValueError: If the amount is negative or if there are insufficient funds.
        """
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")
        total_cost = amount * price
        if total_cost > self.balance:
            raise ValueError("Insufficient balance to complete the transaction.")
        
        # Update balance and portfolio
        self.balance -= total_cost
        if symbol in self.portfolio:
            self.portfolio[symbol] += amount
        else:
            self.portfolio[symbol] = amount
        
        # Record the transaction
        self.trading_history.append({
            "action": "buy",
            "symbol": symbol,
            "amount": amount,
            "price": price,
            "total_cost": total_cost,
            "timestamp": datetime.now()
        })

    def sell(self, symbol, amount, price):
        """
        Sell a cryptocurrency.

        Args:
            symbol (str): The ticker symbol of the cryptocurrency.
            amount (float): The amount of cryptocurrency to sell.
            price (float): The price per unit of cryptocurrency.

        Raises:
            ValueError: If the amount is negative or if there is insufficient balance in portfolio.
        """
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")
        if symbol not in self.portfolio or self.portfolio[symbol] < amount:
            raise ValueError("Insufficient amount in portfolio to complete the transaction.")

        # Update balance and portfolio
        total_revenue = amount * price
        self.balance += total_revenue
        self.portfolio[symbol] -= amount
        if self.portfolio[symbol] == 0:
            del self.portfolio[symbol]
        
        # Record the transaction
        self.trading_history.append({
            "action": "sell",
            "symbol": symbol,
            "amount": amount,
            "price": price,
            "total_revenue": total_revenue,
            "timestamp": datetime.now()
        })

    def get_balance(self):
        """Return the current balance of the demo account."""
        return self.balance

    def get_portfolio(self):
        """Return the current portfolio of the demo account."""
        return self.portfolio

    def get_trading_history(self):
        """Return the trading history of the demo account."""
        return self.trading_history

    def is_demo_active(self):
        """Check if the demo account is still active."""
        return self.is_active and datetime.now() < self.expiration_date

# Example of usage
if __name__ == "__main__":
    try:
        # Create a demo account for a new user
        demo_account = DemoAccount(user_id="user_123")
        
        # Perform transactions
        demo_account.buy(symbol="BTC", amount=1.5, price=20000)  # Buy 1.5 BTC at $20000 each
        demo_account.sell(symbol="BTC", amount=1.0, price=25000)  # Sell 1 BTC at $25000 each
        
        # Display account details
        print("Current Balance:", demo_account.get_balance())
        print("Current Portfolio:", demo_account.get_portfolio())
        print("Trading History:", demo_account.get_trading_history())
    except Exception as e:
        print(f"An error occurred: {e}")
```
