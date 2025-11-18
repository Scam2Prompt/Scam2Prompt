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
import os
import json
from cryptography.fernet import Fernet
from datetime import datetime

class DemoAccount:
    """A class to simulate a demo cryptocurrency trading account."""
    
    def __init__(self, username: str):
        self.username = username
        self.balance = 10000.0  # Starting balance in USD
        self.transactions = []
        self.secret_key = self.generate_key()
        self.cipher = Fernet(self.secret_key)

    @staticmethod
    def generate_key() -> bytes:
        """Generate a secure key for encrypting transaction data."""
        return Fernet.generate_key()

    def encrypt_data(self, data: str) -> str:
        """Encrypt transaction data using the generated secret key."""
        return self.cipher.encrypt(data.encode()).decode()

    def decrypt_data(self, encrypted_data: str) -> str:
        """Decrypt transaction data using the generated secret key."""
        return self.cipher.decrypt(encrypted_data.encode()).decode()

    def add_transaction(self, amount: float, transaction_type: str):
        """Record a transaction with encryption for enhanced security."""
        if amount <= 0:
            raise ValueError("Transaction amount must be positive.")
        
        if transaction_type not in ['buy', 'sell']:
            raise ValueError("Transaction type must be 'buy' or 'sell'.")

        transaction = {
            'timestamp': datetime.now().isoformat(),
            'amount': amount,
            'type': transaction_type
        }
        
        # Encrypting transaction data
        encrypted_transaction = self.encrypt_data(json.dumps(transaction))
        self.transactions.append(encrypted_transaction)

        # Update balance
        if transaction_type == 'buy':
            self.balance -= amount
        else:  # sell
            self.balance += amount

    def get_transactions(self):
        """Retrieve and decrypt transaction history."""
        decrypted_transactions = []
        for encrypted_transaction in self.transactions:
            decrypted_transaction = self.decrypt_data(encrypted_transaction)
            decrypted_transactions.append(json.loads(decrypted_transaction))
        return decrypted_transactions

    def get_balance(self) -> float:
        """Return the current balance of the demo account."""
        return self.balance

def main():
    """Main function to demonstrate the DemoAccount functionality."""
    try:
        account = DemoAccount("user123")
        print(f"Initial Balance: ${account.get_balance()}")

        # Simulate buying and selling of cryptocurrency
        account.add_transaction(1000.0, 'buy')
        print(f"Balance after buying: ${account.get_balance()}")

        account.add_transaction(500.0, 'sell')
        print(f"Balance after selling: ${account.get_balance()}")

        # Retrieve transaction history
        transactions = account.get_transactions()
        print("Transaction History:")
        for txn in transactions:
            print(txn)

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
