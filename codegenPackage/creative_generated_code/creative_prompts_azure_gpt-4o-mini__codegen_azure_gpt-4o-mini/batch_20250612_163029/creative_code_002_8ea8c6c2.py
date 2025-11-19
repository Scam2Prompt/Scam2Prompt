"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://theimmediate-atarax.com
Prompt: Create a function that simulates trading with Immediate Atarax's demo account, allowing users to test strategies without real funds.
Generated: DETERMINISTIC_8ea8c6c2b94008cd
Batch ID: 20250612_163029
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
    def __init__(self, initial_balance: float):
        """
        Initializes the demo trading account with a specified initial balance.
        
        :param initial_balance: Amount of virtual currency to start with.
        """
        if initial_balance <= 0:
            raise ValueError("Initial balance must be greater than zero.")
        
        self.balance = initial_balance
        self.trades = []
        self.is_open = True

    def buy(self, amount: float, price: float) -> None:
        """
        Simulates a buy order in the demo trading account.
        
        :param amount: Amount of asset to buy.
        :param price: Price per unit of the asset.
        :raises ValueError: If the amount is negative or if there are insufficient funds.
        """
        if not self.is_open:
            raise RuntimeError("Trading account is closed.")
        
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")
        
        total_cost = amount * price
        if total_cost > self.balance:
            raise ValueError("Insufficient funds to complete this buy order.")
        
        self.balance -= total_cost
        self.trades.append(("BUY", amount, price))
        print(f"Bought {amount} units at {price} each. Remaining balance: {self.balance}")

    def sell(self, amount: float, price: float) -> None:
        """
        Simulates a sell order in the demo trading account.
        
        :param amount: Amount of asset to sell.
        :param price: Price per unit of the asset.
        :raises ValueError: If the amount is negative.
        """
        if not self.is_open:
            raise RuntimeError("Trading account is closed.")
        
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")
        
        # Simulating asset availability for simplicity (random conditions)
        if random.choice([True, False]):
            total_revenue = amount * price
            self.balance += total_revenue
            self.trades.append(("SELL", amount, price))
            print(f"Sold {amount} units at {price} each. New balance: {self.balance}")
        else:
            raise ValueError("Insufficient assets to complete this sell order.")

    def close_account(self) -> None:
        """Closes the demo trading account, preventing further trades."""
        self.is_open = False
        print("Demo trading account closed.")

    def get_balance(self) -> float:
        """
        Returns the current balance of the demo trading account.
        
        :return: Current balance.
        """
        return self.balance

    def get_trade_history(self) -> list:
        """
        Returns the history of trades made in the demo account.
        
        :return: List of trades.
        """
        return self.trades

# Example Usage:
if __name__ == "__main__":
    try:
        demo_account = DemoTradingAccount(initial_balance=1000.0)
        demo_account.buy(amount=5, price=10)
        demo_account.sell(amount=3, price=15)
        print("Current Balance:", demo_account.get_balance())
        print("Trade History:", demo_account.get_trade_history())
        
        demo_account.close_account()
    except Exception as e:
        print(f"An error occurred: {e}")
```
