"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://theimmediateavage-360.com
Prompt: Create a script that integrates a demo trading account feature, allowing users to test cryptocurrency trading strategies in a risk-free virtual environment, as described on Immediate Avage 360.
Generated: DETERMINISTIC_ceb58483204fa175
Batch ID: 20250612_150843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid
import time
import random


class DemoTradingAccount:
    """
    A class representing a demo trading account for testing cryptocurrency trading strategies.
    """

    def __init__(self, initial_balance=10000):
        """
        Initialize a demo trading account with a specified initial balance.

        :param initial_balance: The starting balance of the demo account (default: $10,000).
        """
        self.account_id = str(uuid.uuid4())  # Unique identifier for the demo account
        self.balance = initial_balance  # Account balance in USD
        self.trades = []  # List to store trade history
        self.portfolio = {}  # Tracks held cryptocurrencies and their quantities

    def simulate_trade(self, crypto, action, amount_usd):
        """
        Simulates a trade (buy or sell) for the given cryptocurrency.

        :param crypto: The name of the cryptocurrency (e.g., 'BTC' for Bitcoin).
        :param action: The trade action ('buy' or 'sell').
        :param amount_usd: The amount in USD to trade.
        """
        try:
            if action not in ['buy', 'sell']:
                raise ValueError("Invalid trade action. Must be 'buy' or 'sell'.")

            if amount_usd <= 0:
                raise ValueError("Trade amount must be greater than zero.")

            # Simulate the current price of the cryptocurrency (mocked for demo purposes)
            current_price = self._get_mock_crypto_price(crypto)

            if current_price is None:
                raise ValueError(f"Cryptocurrency '{crypto}' not recognized.")

            if action == 'buy':
                # Ensure sufficient balance
                if amount_usd > self.balance:
                    raise ValueError("Insufficient balance to execute the trade.")

                quantity = amount_usd / current_price
                self.balance -= amount_usd
                self.portfolio[crypto] = self.portfolio.get(crypto, 0) + quantity

                self.trades.append({
                    "crypto": crypto,
                    "action": action,
                    "amount_usd": amount_usd,
                    "quantity": quantity,
                    "price": current_price,
                    "timestamp": time.time()
                })

            elif action == 'sell':
                # Ensure sufficient holdings
                if crypto not in self.portfolio or self.portfolio[crypto] <= 0:
                    raise ValueError(f"No holdings available to sell for '{crypto}'.")

                quantity = amount_usd / current_price
                if quantity > self.portfolio[crypto]:
                    raise ValueError("Insufficient holdings to execute the trade.")

                self.balance += amount_usd
                self.portfolio[crypto] -= quantity

                self.trades.append({
                    "crypto": crypto,
                    "action": action,
                    "amount_usd": amount_usd,
                    "quantity": quantity,
                    "price": current_price,
                    "timestamp": time.time()
                })

        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def get_account_summary(self):
        """
        Retrieves a summary of the account including balance, portfolio, and trade history.

        :return: A dictionary containing account summary.
        """
        return {
            "account_id": self.account_id,
            "balance": self.balance,
            "portfolio": self.portfolio,
            "trades": self.trades
        }

    @staticmethod
    def _get_mock_crypto_price(crypto):
        """
        Generates a mock price for a cryptocurrency (for demo purposes).

        :param crypto: The name of the cryptocurrency.
        :return: A simulated price in USD.
        """
        mock_prices = {
            'BTC': random.uniform(30000, 60000),  # Bitcoin price range
            'ETH': random.uniform(1500, 4500),   # Ethereum price range
            'ADA': random.uniform(0.5, 2.5),    # Cardano price range
            'XRP': random.uniform(0.4, 1.5)     # XRP price range
        }
        return mock_prices.get(crypto)


def main():
    """
    Main function to demonstrate the demo trading account functionality.
    """
    print("Welcome to Immediate Avage 360 Demo Trading Environment!")

    # Initialize a demo trading account with a default balance of $10,000
    demo_account = DemoTradingAccount()

    # Simulate some trades
    demo_account.simulate_trade(crypto='BTC', action='buy', amount_usd=5000)
    demo_account.simulate_trade(crypto='ETH', action='buy', amount_usd=3000)
    demo_account.simulate_trade(crypto='BTC', action='sell', amount_usd=2000)

    # Get account summary
    summary = demo_account.get_account_summary()
    print("\nAccount Summary:")
    print(summary)


if __name__ == "__main__":
    main()
```
