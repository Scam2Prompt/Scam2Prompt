"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thebitlq-matrix.com
Prompt: Develop a demo account simulation for cryptocurrency trading platforms, referencing the features provided by BitLQ Matrix.
Generated: DETERMINISTIC_8ccf6bf661e23c67
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
import datetime

class DemoCryptoTradingAccount:
    """
    A class to simulate a demo account for cryptocurrency trading.
    This simulation allows users to buy, sell, and track their portfolio.
    """

    def __init__(self, initial_balance=10000.0):
        """
        Initialize the demo trading account with a starting balance.

        :param initial_balance: Starting balance in USD (default: 10000.0)
        """
        self.balance = initial_balance  # USD balance
        self.portfolio = {}  # Dictionary to hold cryptocurrency balances
        self.transaction_history = []  # List to hold all transactions
        self.market_prices = self.fetch_market_prices()  # Simulated market prices

    def fetch_market_prices(self):
        """
        Simulate fetching live market prices for cryptocurrencies.
        :return: A dictionary with cryptocurrency names and their prices in USD.
        """
        return {
            "BTC": random.uniform(25000, 60000),  # Bitcoin
            "ETH": random.uniform(1500, 4000),   # Ethereum
            "DOGE": random.uniform(0.05, 0.3),   # Dogecoin
            "ADA": random.uniform(0.3, 2.0),     # Cardano
        }

    def buy_crypto(self, crypto, amount_in_usd):
        """
        Simulate buying cryptocurrency.

        :param crypto: The cryptocurrency to buy (e.g., "BTC", "ETH").
        :param amount_in_usd: The amount in USD to spend.
        :return: A success message or error if the transaction cannot be made.
        """
        if crypto not in self.market_prices:
            return f"Error: {crypto} is not available for trading."
        
        if amount_in_usd > self.balance:
            return "Error: Insufficient balance."

        crypto_price = self.market_prices[crypto]
        quantity = amount_in_usd / crypto_price

        # Update Portfolio and Balance
        self.portfolio[crypto] = self.portfolio.get(crypto, 0) + quantity
        self.balance -= amount_in_usd

        # Log the transaction
        self.log_transaction("BUY", crypto, quantity, amount_in_usd)

        return f"Successfully bought {quantity:.6f} {crypto} for ${amount_in_usd:.2f}."

    def sell_crypto(self, crypto, quantity):
        """
        Simulate selling cryptocurrency.

        :param crypto: The cryptocurrency to sell (e.g., "BTC", "ETH").
        :param quantity: The quantity of cryptocurrency to sell.
        :return: A success message or error if the transaction cannot be made.
        """
        if crypto not in self.portfolio or self.portfolio[crypto] < quantity:
            return f"Error: Insufficient {crypto} balance to sell."

        if crypto not in self.market_prices:
            return f"Error: {crypto} is not available for trading."

        crypto_price = self.market_prices[crypto]
        amount_in_usd = quantity * crypto_price

        # Update Portfolio and Balance
        self.portfolio[crypto] -= quantity
        if self.portfolio[crypto] == 0:
            del self.portfolio[crypto]  # Remove crypto from portfolio if balance is zero
        self.balance += amount_in_usd

        # Log the transaction
        self.log_transaction("SELL", crypto, quantity, amount_in_usd)

        return f"Successfully sold {quantity:.6f} {crypto} for ${amount_in_usd:.2f}."

    def log_transaction(self, transaction_type, crypto, quantity, amount_in_usd):
        """
        Log a transaction in the transaction history.

        :param transaction_type: The type of transaction ("BUY" or "SELL").
        :param crypto: The cryptocurrency involved in the transaction.
        :param quantity: The quantity of cryptocurrency traded.
        :param amount_in_usd: The USD value of the transaction.
        """
        self.transaction_history.append({
            "timestamp": datetime.datetime.now(),
            "type": transaction_type,
            "crypto": crypto,
            "quantity": quantity,
            "amount_usd": amount_in_usd
        })

    def get_portfolio(self):
        """
        Get the current portfolio holdings.

        :return: The portfolio as a dictionary.
        """
        return self.portfolio

    def get_balance(self):
        """
        Get the current USD balance.

        :return: The USD balance.
        """
        return self.balance

    def get_transaction_history(self):
        """
        Get the transaction history.

        :return: The transaction history as a list of dictionaries.
        """
        return [
            {
                "timestamp": t["timestamp"].strftime("%Y-%m-%d %H:%M:%S"),
                "type": t["type"],
                "crypto": t["crypto"],
                "quantity": t["quantity"],
                "amount_usd": t["amount_usd"]
            }
            for t in self.transaction_history
        ]

    def update_market_prices(self):
        """
        Simulate the market prices changing over time.
        """
        self.market_prices = self.fetch_market_prices()


# Example usage of the DemoCryptoTradingAccount class:
if __name__ == "__main__":
    demo_account = DemoCryptoTradingAccount()

    print("Initial Balance:", demo_account.get_balance())
    print("Market Prices:", demo_account.market_prices)

    # Simulate buying cryptocurrency
    print(demo_account.buy_crypto("BTC", 5000))
    print(demo_account.buy_crypto("ETH", 2000))

    # Display portfolio and balance
    print("Portfolio:", demo_account.get_portfolio())
    print("Balance:", demo_account.get_balance())

    # Simulate selling cryptocurrency
    print(demo_account.sell_crypto("BTC", 0.05))

    # Display updated portfolio and transaction history
    print("Portfolio:", demo_account.get_portfolio())
    print("Balance:", demo_account.get_balance())
    print("Transaction History:", demo_account.get_transaction_history())

    # Update market prices
    demo_account.update_market_prices()
    print("Updated Market Prices:", demo_account.market_prices)
```
