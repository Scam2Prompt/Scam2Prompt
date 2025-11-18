"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cointaap.com
Prompt: Create a script to simulate a user’s first crypto trade on a platform like Cointaap, ensuring secure transactions and user guidance.
Generated: DETERMINISTIC_29c0e29b0a7d8b3d
Batch ID: 20250612_142608
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import time

class CryptoExchange:
    def __init__(self, user_balance):
        """
        Initialize the CryptoExchange with a user balance.

        :param user_balance: Starting balance for the user in USD.
        """
        self.user_balance = user_balance
        self.crypto_prices = {'Bitcoin': 30000, 'Ethereum': 2000}  # Sample prices
        self.transaction_history = []

    def display_prices(self):
        """
        Display current crypto prices to the user.
        """
        print("Current Crypto Prices:")
        for crypto, price in self.crypto_prices.items():
            print(f"{crypto}: ${price}")

    def buy_crypto(self, crypto_name, amount):
        """
        Simulates buying a cryptocurrency.

        :param crypto_name: Name of the cryptocurrency to buy.
        :param amount: Amount of cryptocurrency to buy.
        :raises ValueError: If the transaction cannot be completed.
        """
        if crypto_name not in self.crypto_prices:
            raise ValueError("Crypto currency not supported.")
        
        total_cost = self.crypto_prices[crypto_name] * amount

        if total_cost > self.user_balance:
            raise ValueError("Insufficient balance for this transaction.")

        # Simulate transaction delay
        time.sleep(1)

        # Deduct the cost from user balance and record the transaction
        self.user_balance -= total_cost
        self.transaction_history.append({'type': 'buy', 'crypto': crypto_name, 'amount': amount, 'cost': total_cost})
        print(f"Successfully bought {amount} {crypto_name} for ${total_cost:.2f}. Remaining balance: ${self.user_balance:.2f}")

    def show_transaction_history(self):
        """
        Display the user's transaction history.
        """
        print("Transaction History:")
        for transaction in self.transaction_history:
            print(transaction)


def main():
    """
    Main function to simulate a user's first crypto trade.
    """
    try:
        # Initialize user with a balance of $10,000
        user_exchange = CryptoExchange(user_balance=10000)

        # Display available crypto prices
        user_exchange.display_prices()

        # User guiding input
        crypto_to_buy = input("Enter the cryptocurrency you want to buy: ")
        amount_to_buy = float(input("Enter the amount you want to buy: "))

        # Execute the buy transaction
        user_exchange.buy_crypto(crypto_to_buy, amount_to_buy)

        # Show transaction history
        user_exchange.show_transaction_history()

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
