"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitcoin-evista-software.com
Prompt: Generate code to simulate a demo account for cryptocurrency trading, incorporating features like enhanced security with cryptography and borderless transactions as described on Bitcoin Evista.
Generated: DETERMINISTIC_a5fab408b6073e61
Batch ID: 20250612_150048
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib
import hmac
import json
import os
import random
import string
import time
from datetime import datetime

# ----------------------------
# A simple cryptocurrency demo trading simulation
# ----------------------------

class CryptoDemoAccount:
    def __init__(self, username, initial_balance=10000):
        """
        Initialize the demo account for cryptocurrency trading.

        :param username: The username of the account holder.
        :param initial_balance: Starting balance of the demo account in USD.
        """
        self.username = username
        self.wallet_id = self.generate_wallet_id()
        self.secret_key = self.generate_secret_key()
        self.balance = initial_balance
        self.transactions = []

    @staticmethod
    def generate_wallet_id():
        """
        Generate a unique wallet ID for the user.
        """
        return hashlib.sha256(os.urandom(32)).hexdigest()

    @staticmethod
    def generate_secret_key():
        """
        Generate a secret key for enhanced security.
        """
        return ''.join(random.choices(string.ascii_letters + string.digits, k=64))

    def authenticate_transaction(self, transaction_data, signature):
        """
        Authenticate a transaction using HMAC.

        :param transaction_data: The data of the transaction to be verified.
        :param signature: The signature to verify the transaction.
        :return: True if the transaction is authenticated, False otherwise.
        """
        generated_signature = hmac.new(
            self.secret_key.encode(),
            transaction_data.encode(),
            hashlib.sha256
        ).hexdigest()
        return hmac.compare_digest(generated_signature, signature)

    def make_transaction(self, amount, crypto, action):
        """
        Simulate a cryptocurrency transaction (buy or sell).

        :param amount: The amount in USD to trade.
        :param crypto: Cryptocurrency being traded (e.g., Bitcoin, Ethereum).
        :param action: Type of action - 'buy' or 'sell'.
        :return: A transaction receipt.
        """
        if amount <= 0:
            raise ValueError("Transaction amount must be greater than zero.")
        if action not in ['buy', 'sell']:
            raise ValueError("Action must be either 'buy' or 'sell'.")
        if action == 'buy' and amount > self.balance:
            raise ValueError("Insufficient funds to complete the purchase.")

        crypto_price = self.get_crypto_price(crypto)
        if crypto_price is None:
            raise ValueError(f"Unable to fetch price for {crypto}.")

        timestamp = datetime.now().isoformat()
        crypto_amount = amount / crypto_price if action == 'buy' else -amount / crypto_price
        transaction = {
            'id': hashlib.sha256(f'{time.time()}-{self.username}'.encode()).hexdigest(),
            'crypto': crypto,
            'action': action,
            'crypto_amount': crypto_amount,
            'amount_usd': amount,
            'price_usd': crypto_price,
            'timestamp': timestamp
        }
        self.transactions.append(transaction)

        if action == 'buy':
            self.balance -= amount
        elif action == 'sell':
            self.balance += amount

        return transaction

    @staticmethod
    def get_crypto_price(crypto):
        """
        Simulate fetching the current price of cryptocurrency.
        In production, this would call a real API like CoinGecko or Binance.

        :param crypto: The cryptocurrency to fetch the price for.
        :return: The price in USD.
        """
        mock_prices = {
            'Bitcoin': 30000,
            'Ethereum': 2000,
            'Cardano': 0.3
        }
        return mock_prices.get(crypto, None)

    def get_transaction_history(self):
        """
        Retrieve the transaction history for the account.
        """
        return self.transactions

    def get_account_balance(self):
        """
        Retrieve the current account balance.
        """
        return self.balance


# Example usage
if __name__ == "__main__":
    # Initialize a demo account
    account = CryptoDemoAccount(username="demo_user")

    print("Account created successfully!")
    print(f"Wallet ID: {account.wallet_id}")
    print(f"Initial Balance: ${account.get_account_balance()}")

    # Simulate a transaction
    try:
        print("\nAttempting to buy $5000 worth of Bitcoin...")
        transaction = account.make_transaction(amount=5000, crypto="Bitcoin", action="buy")
        print("Transaction successful!")
        print(json.dumps(transaction, indent=4))
    except ValueError as e:
        print(f"Transaction failed: {e}")

    # Check balance
    print(f"\nBalance: ${account.get_account_balance()}")

    # Retrieve transaction history
    print("\nTransaction History:")
    print(json.dumps(account.get_transaction_history(), indent=4))
```
