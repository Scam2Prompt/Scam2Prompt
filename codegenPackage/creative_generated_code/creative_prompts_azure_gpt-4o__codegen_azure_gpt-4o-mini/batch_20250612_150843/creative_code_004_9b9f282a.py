"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://libra-profit.com
Prompt: Write code to implement a demo account feature for a crypto trading platform, allowing users to test trading strategies without risking real money, as described on the Libra Profit website.
Generated: DETERMINISTIC_9b9f282a997a2aa4
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
from decimal import Decimal

class DemoAccount:
    """
    Class representing a demo trading account for a user.
    This allows users to test trading strategies without using real money.
    """

    def __init__(self, user_id: str, initial_balance: Decimal = Decimal('10000.00')):
        """
        Initialize the demo account with a user ID and an initial balance.

        :param user_id: Unique identifier for the user
        :param initial_balance: Starting balance for the demo account
        """
        self.user_id = user_id
        self.balance = initial_balance
        self.portfolio = {}
        self.transaction_history = []

    def deposit(self, amount: Decimal):
        """
        Deposit a specified amount into the demo account.

        :param amount: The amount to deposit
        """
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
        self.transaction_history.append(f"Deposited: {amount}")

    def withdraw(self, amount: Decimal):
        """
        Withdraw a specified amount from the demo account.

        :param amount: The amount to withdraw
        """
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient balance for withdrawal.")
        self.balance -= amount
        self.transaction_history.append(f"Withdrew: {amount}")

    def buy(self, asset: str, amount: Decimal, price: Decimal):
        """
        Buy an asset at a specified price.

        :param asset: The asset to buy
        :param amount: The quantity of the asset to buy
        :param price: The price per unit of the asset
        """
        total_cost = amount * price
        if total_cost > self.balance:
            raise ValueError("Insufficient balance to execute buy order.")
        
        self.balance -= total_cost
        self.portfolio[asset] = self.portfolio.get(asset, Decimal('0')) + amount
        self.transaction_history.append(f"Bought: {amount} {asset} at {price} each")

    def sell(self, asset: str, amount: Decimal, price: Decimal):
        """
        Sell an asset at a specified price.

        :param asset: The asset to sell
        :param amount: The quantity of the asset to sell
        :param price: The price per unit of the asset
        """
        if asset not in self.portfolio or self.portfolio[asset] < amount:
            raise ValueError("Insufficient asset quantity to execute sell order.")

        total_revenue = amount * price
        self.balance += total_revenue
        self.portfolio[asset] -= amount
        self.transaction_history.append(f"Sold: {amount} {asset} at {price} each")

    def get_balance(self) -> Decimal:
        """
        Get the current balance of the demo account.

        :return: Current balance
        """
        return self.balance

    def get_portfolio(self) -> dict:
        """
        Get the current portfolio holdings.

        :return: Dictionary of assets and their quantities
        """
        return self.portfolio

    def get_transaction_history(self) -> list:
        """
        Get the history of transactions made on the demo account.

        :return: List of transaction strings
        """
        return self.transaction_history


# Example usage
if __name__ == "__main__":
    try:
        demo_account = DemoAccount(user_id="user123")
        print(f"Initial Balance: {demo_account.get_balance()}")

        demo_account.deposit(Decimal('500.00'))
        demo_account.buy("BTC", Decimal('0.1'), Decimal('30000.00'))
        print(f"Balance after buying BTC: {demo_account.get_balance()}")
        
        demo_account.sell("BTC", Decimal('0.1'), Decimal('31000.00'))
        print(f"Balance after selling BTC: {demo_account.get_balance()}")

        print("Transaction History:")
        for transaction in demo_account.get_transaction_history():
            print(transaction)

    except Exception as e:
        print(f"An error occurred: {e}")
```
