"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thecryptex-secure.com
Prompt: Generate code to simulate CrypTEX Secure's demo account functionality, allowing users to test trading strategies with virtual funds before committing real investments.
Generated: DETERMINISTIC_e7d3bfc2c6236cc3
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

class CryptoAccount:
    """
    A class to simulate a demo account for trading cryptocurrencies.
    Users can test their trading strategies with virtual funds.
    """

    def __init__(self, initial_balance=10000.0):
        """
        Initialize the demo account with a specified initial balance.

        Args:
            initial_balance (float): The starting balance for the demo account. Default is $10,000.
        """
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self.balance = initial_balance
        self.portfolio = {}  # Holds cryptocurrency amounts
        self.history = []  # Records transaction history

    def buy(self, crypto: str, amount: float, price: float):
        """
        Buy a specified amount of cryptocurrency at a given price.

        Args:
            crypto (str): The name of the cryptocurrency to buy.
            amount (float): The amount of cryptocurrency to buy.
            price (float): The purchase price of the cryptocurrency.

        Raises:
            ValueError: If the amount is negative or if insufficient funds are available.
        """
        if amount <= 0:
            raise ValueError("Amount must be positive.")
        total_cost = amount * price
        if total_cost > self.balance:
            raise ValueError("Insufficient funds to complete this transaction.")

        # Update balance and portfolio
        self.balance -= total_cost
        self.portfolio[crypto] = self.portfolio.get(crypto, 0) + amount
        self.history.append(f"Bought {amount} {crypto} at ${price} each.")
        print(f"Successfully bought {amount} {crypto}.")

    def sell(self, crypto: str, amount: float, price: float):
        """
        Sell a specified amount of cryptocurrency at a given price.

        Args:
            crypto (str): The name of the cryptocurrency to sell.
            amount (float): The amount of cryptocurrency to sell.
            price (float): The selling price of the cryptocurrency.

        Raises:
            ValueError: If the amount is negative or if insufficient cryptocurrency is held.
        """
        if amount <= 0:
            raise ValueError("Amount must be positive.")
        if crypto not in self.portfolio or self.portfolio[crypto] < amount:
            raise ValueError(f"Insufficient {crypto} in portfolio to sell.")

        # Update balance and portfolio
        total_revenue = amount * price
        self.balance += total_revenue
        self.portfolio[crypto] -= amount
        if self.portfolio[crypto] == 0:
            del self.portfolio[crypto]
        self.history.append(f"Sold {amount} {crypto} at ${price} each.")
        print(f"Successfully sold {amount} {crypto}.")

    def get_balance(self) -> float:
        """
        Get the current balance of the demo account.

        Returns:
            float: The current balance.
        """
        return self.balance

    def get_portfolio(self) -> dict:
        """
        Get the current cryptocurrency portfolio.

        Returns:
            dict: A dictionary representing the portfolio.
        """
        return self.portfolio

    def get_history(self) -> list:
        """
        Get the transaction history of the demo account.

        Returns:
            list: A list of transaction history entries.
        """
        return self.history

    def simulate_market_change(self):
        """
        Simulate market changes for testing trading strategies.
        This method randomly changes the price of holdings.
        """
        for crypto in self.portfolio:
            price_change = random.uniform(-0.1, 0.1)  # Simulate price change between -10% and +10%
            print(f"Market change simulation: {crypto} price changed by {price_change * 100:.2f}%.")

# Example of using the CryptoAccount class
if __name__ == "__main__":
    try:
        demo_account = CryptoAccount()
        demo_account.buy('Bitcoin', 0.5, 20000)  # Buy 0.5 BTC at $20,000
        demo_account.sell('Bitcoin', 0.2, 21000)  # Sell 0.2 BTC at $21,000
        print(f"Current balance: ${demo_account.get_balance():.2f}")
        print("Current portfolio:", demo_account.get_portfolio())
        print("Transaction history:", demo_account.get_history())
        demo_account.simulate_market_change()
    except Exception as e:
        print(f"An error occurred: {e}")
```
