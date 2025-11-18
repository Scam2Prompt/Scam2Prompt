"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://theimmediate-prime.com
Prompt: Create a demo trading environment for cryptocurrencies that mimics the risk-free demo account feature of the "switch hiprex 400" platform.
Generated: DETERMINISTIC_980db2aa0defd1f9
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
from datetime import datetime

class DemoTradingEnvironment:
    """
    A class to simulate a risk-free demo trading environment for cryptocurrencies.
    """

    def __init__(self, initial_balance=10000):
        """
        Initializes the trading environment with an initial balance.
        Args:
            initial_balance (float): Starting amount in the demo account.
        """
        self.balance = initial_balance
        self.portfolio = {}
        self.transaction_history = []
        self.prices = {
            "Bitcoin": 50000,
            "Ethereum": 3500,
            "Cardano": 2.5,
            "Solana": 150,
        }

    def get_prices(self):
        """
        Simulates fetching live cryptocurrency prices.
        Returns:
            dict: A dictionary of cryptocurrency prices.
        """
        # Simulate price fluctuations
        for coin in self.prices:
            self.prices[coin] = round(self.prices[coin] * random.uniform(0.95, 1.05), 2)
        return self.prices

    def buy(self, crypto, amount):
        """
        Buys a cryptocurrency for the given amount.
        Args:
            crypto (str): The name of the cryptocurrency.
            amount (float): The amount to invest.
        Returns:
            str: Confirmation of the transaction or error message.
        """
        if crypto not in self.prices:
            return f"Error: {crypto} is not available for trading."

        current_price = self.prices[crypto]
        quantity = amount / current_price

        if amount > self.balance:
            return "Error: Insufficient balance."

        self.balance -= amount
        self.portfolio[crypto] = self.portfolio.get(crypto, 0) + quantity
        self.transaction_history.append({
            "type": "BUY",
            "crypto": crypto,
            "amount": amount,
            "quantity": quantity,
            "price": current_price,
            "timestamp": datetime.now()
        })
        return f"Successfully bought {quantity:.6f} {crypto} for ${amount:.2f}."

    def sell(self, crypto, quantity):
        """
        Sells a cryptocurrency for the given quantity.
        Args:
            crypto (str): The name of the cryptocurrency.
            quantity (float): The quantity to sell.
        Returns:
            str: Confirmation of the transaction or error message.
        """
        if crypto not in self.portfolio or self.portfolio[crypto] < quantity:
            return f"Error: Insufficient {crypto} holdings."

        current_price = self.prices[crypto]
        proceeds = quantity * current_price

        self.portfolio[crypto] -= quantity
        if self.portfolio[crypto] == 0:
            del self.portfolio[crypto]

        self.balance += proceeds
        self.transaction_history.append({
            "type": "SELL",
            "crypto": crypto,
            "amount": proceeds,
            "quantity": quantity,
            "price": current_price,
            "timestamp": datetime.now()
        })
        return f"Successfully sold {quantity:.6f} {crypto} for ${proceeds:.2f}."

    def show_balance(self):
        """
        Displays the current balance and portfolio.
        Returns:
            str: A summary of the balance and portfolio.
        """
        portfolio_summary = "\n".join([f"{crypto}: {quantity:.6f}" for crypto, quantity in self.portfolio.items()])
        return f"Balance: ${self.balance:.2f}\nPortfolio:\n{portfolio_summary or 'Empty'}"

    def show_transaction_history(self):
        """
        Displays the transaction history.
        Returns:
            str: A summary of all transactions.
        """
        history = "\n".join([
            f"{t['timestamp']} - {t['type']} {t['crypto']} - ${t['amount']:.2f} ({t['quantity']:.6f} @ ${t['price']:.2f})"
            for t in self.transaction_history
        ])
        return history or "No transactions yet."


# Demo usage
if __name__ == "__main__":
    # Initialize the demo trading environment
    demo_env = DemoTradingEnvironment()

    # Display initial balance and portfolio
    print(demo_env.show_balance())

    # Fetch and display prices
    print("Current Prices:", demo_env.get_prices())

    # Perform a buy transaction
    print(demo_env.buy("Bitcoin", 5000))

    # Perform a sell transaction
    print(demo_env.sell("Bitcoin", 0.05))

    # Display updated balance and portfolio
    print(demo_env.show_balance())

    # Display transaction history
    print("Transaction History:")
    print(demo_env.show_transaction_history())
```
