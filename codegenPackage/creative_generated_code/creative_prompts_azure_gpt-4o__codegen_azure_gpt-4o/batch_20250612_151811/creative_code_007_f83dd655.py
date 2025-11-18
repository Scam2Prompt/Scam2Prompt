"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://action-coin.com
Prompt: Write code to simulate trading on a demo account for Forex and CFDs, incorporating features like encryption and fraud prevention as highlighted by Action Coin's security measures.
Generated: DETERMINISTIC_f83dd655b6c60f00
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import hashlib
import secrets
from cryptography.fernet import Fernet


class DemoTradingAccount:
    """
    A class to simulate trading on a demo account for Forex and CFDs,
    with encryption and fraud prevention measures inspired by Action Coin's approach.
    """

    def __init__(self):
        # Generate encryption key for secure transaction storage
        self.encryption_key = Fernet.generate_key()
        self.cipher_suite = Fernet(self.encryption_key)

        # Initialize account balance
        self.balance = 10000.0  # Starting demo balance in USD

        # Store transaction history securely
        self.transaction_history = []

    def encrypt_data(self, data: str) -> str:
        """
        Encrypts data using Fernet encryption.
        :param data: A string to encrypt.
        :return: Encrypted string.
        """
        return self.cipher_suite.encrypt(data.encode()).decode()

    def decrypt_data(self, encrypted_data: str) -> str:
        """
        Decrypts data using Fernet encryption.
        :param encrypted_data: The encrypted string to decrypt.
        :return: Decrypted string.
        """
        return self.cipher_suite.decrypt(encrypted_data.encode()).decode()

    def generate_transaction_id(self) -> str:
        """
        Generates a secure transaction ID using hashing and random values.
        :return: A unique transaction ID.
        """
        random_string = secrets.token_hex(16)
        transaction_id = hashlib.sha256(random_string.encode()).hexdigest()
        return transaction_id

    def perform_trade(self, asset: str, trade_type: str, amount: float, price: float):
        """
        Simulates a trade and updates account balance securely.
        :param asset: Asset being traded (e.g., "EUR/USD").
        :param trade_type: Type of trade ("BUY" or "SELL").
        :param amount: Amount to trade (units).
        :param price: Price per unit of the asset.
        :return: Result of the trade.
        """
        if amount <= 0 or price <= 0:
            raise ValueError("Amount and price must be greater than zero.")

        # Calculate trade cost or profit
        trade_value = amount * price
        transaction_id = self.generate_transaction_id()

        if trade_type == "BUY":
            if self.balance < trade_value:
                raise ValueError("Insufficient funds for this trade.")
            self.balance -= trade_value
            trade_result = f"Bought {amount} units of {asset} at ${price:.2f} each."
        elif trade_type == "SELL":
            self.balance += trade_value
            trade_result = f"Sold {amount} units of {asset} at ${price:.2f} each."
        else:
            raise ValueError("Invalid trade type. Use 'BUY' or 'SELL'.")

        # Securely store transaction details
        encrypted_trade = self.encrypt_data(
            f"{transaction_id}|{trade_type}|{asset}|{amount}|{price:.2f}|{self.balance:.2f}"
        )
        self.transaction_history.append(encrypted_trade)

        return trade_result

    def view_transaction_history(self):
        """
        Displays the transaction history securely by decrypting each entry.
        :return: List of decrypted transaction records.
        """
        decrypted_history = [
            self.decrypt_data(encrypted_entry) for encrypted_entry in self.transaction_history
        ]
        return decrypted_history

    def get_balance(self) -> float:
        """
        Returns the current account balance.
        :return: Account balance in USD.
        """
        return self.balance


# -------------------------------
# Example usage of DemoTradingAccount
# -------------------------------
if __name__ == "__main__":
    try:
        # Initialize demo account
        demo_account = DemoTradingAccount()

        # Perform trades
        print(demo_account.perform_trade("EUR/USD", "BUY", 50, 1.2))
        print(demo_account.perform_trade("GBP/USD", "SELL", 30, 1.3))

        # Show balance
        print(f"Current Balance: ${demo_account.get_balance():.2f}")

        # View transaction history
        print("Transaction History:")
        for record in demo_account.view_transaction_history():
            print(record)

    except Exception as e:
        print(f"Error: {e}")
```
