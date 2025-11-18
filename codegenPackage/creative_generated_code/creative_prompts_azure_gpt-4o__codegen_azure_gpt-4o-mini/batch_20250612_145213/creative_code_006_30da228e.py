"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ledger-live-ledger.org
Prompt: Develop a script to process withdrawals and deposits securely, incorporating encryption methods similar to those mentioned for financial operations on the Vavada platform.
Generated: DETERMINISTIC_30da228e2012e3fa
Batch ID: 20250612_145213
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import json
from cryptography.fernet import Fernet
from decimal import Decimal, InvalidOperation

# Generate a new encryption key
# In a production environment, store this key securely and not hard-coded
def generate_key():
    return Fernet.generate_key()

# Load the encryption key from a secure location
def load_key(key_path):
    with open(key_path, 'rb') as key_file:
        return key_file.read()

# Encrypt a message using the provided key
def encrypt_message(message: str, key: bytes) -> str:
    fernet = Fernet(key)
    return fernet.encrypt(message.encode()).decode()

# Decrypt a message using the provided key
def decrypt_message(encrypted_message: str, key: bytes) -> str:
    fernet = Fernet(key)
    return fernet.decrypt(encrypted_message.encode()).decode()

# Account class to manage deposits and withdrawals
class Account:
    def __init__(self, account_id: str, initial_balance: Decimal = Decimal('0.00')):
        self.account_id = account_id
        self.balance = initial_balance

    def deposit(self, amount: Decimal):
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")
        self.balance += amount
        return self.balance

    def withdraw(self, amount: Decimal):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")
        if amount > self.balance:
            raise ValueError("Insufficient funds for withdrawal.")
        self.balance -= amount
        return self.balance

    def get_balance(self) -> Decimal:
        return self.balance

# Transaction processing function
def process_transaction(transaction_type: str, amount: str, account: Account, key: bytes) -> str:
    try:
        # Convert string amount to Decimal
        amount_decimal = Decimal(amount)
        
        if transaction_type == 'deposit':
            new_balance = account.deposit(amount_decimal)
            return encrypt_message(f"Deposit successful. New balance: {new_balance}", key)
        elif transaction_type == 'withdraw':
            new_balance = account.withdraw(amount_decimal)
            return encrypt_message(f"Withdrawal successful. New balance: {new_balance}", key)
        else:
            raise ValueError("Invalid transaction type. Use 'deposit' or 'withdraw'.")
    
    except (InvalidOperation, ValueError) as e:
        return encrypt_message(f"Transaction failed: {str(e)}", key)

# Example usage
if __name__ == "__main__":
    # Define path to your encryption key
    key_path = 'encryption_key.key'

    # Use an existing key or generate a new one for testing
    # key = generate_key()  # Uncomment this to generate a new key
    key = load_key(key_path)

    # Create a new account with an initial balance
    account = Account(account_id="12345678", initial_balance=Decimal('1000.00'))

    # Example transactions
    print(process_transaction('deposit', '500.00', account, key))  # Deposit example
    print(process_transaction('withdraw', '300.00', account, key))  # Withdraw example
    print(process_transaction('withdraw', '1500.00', account, key))  # Overdraw example
```
