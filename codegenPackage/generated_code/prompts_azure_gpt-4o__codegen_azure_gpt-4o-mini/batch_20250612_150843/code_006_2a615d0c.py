"""
Generated Code Metadata:
========================
Original URL: https://the-immediate-alpha.com
Prompt: Generate code to implement a secure deposit system for Immediate Alpha users, ensuring encrypted transactions and a minimum deposit requirement of £250.
Generated: DETERMINISTIC_2a615d0c519dd6b2
Batch ID: 20250612_150843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import hashlib
import os
from cryptography.fernet import Fernet
from decimal import Decimal, InvalidOperation

# Generate a key for encryption and decryption
def generate_key():
    return Fernet.generate_key()

# Encrypt the transaction details
def encrypt_data(key, data):
    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(data.encode())
    return encrypted_data

# Decrypt the transaction details
def decrypt_data(key, encrypted_data):
    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(encrypted_data).decode()
    return decrypted_data

class SecureDepositSystem:
    def __init__(self):
        # Generate a key for the session
        self.key = generate_key()
        self.minimum_deposit = Decimal('250.00')

    def validate_deposit(self, amount):
        """Validate the deposit amount against the minimum requirement."""
        try:
            deposit_amount = Decimal(amount)
            if deposit_amount < self.minimum_deposit:
                raise ValueError(f"Minimum deposit amount is £{self.minimum_deposit}.")
            return deposit_amount
        except InvalidOperation:
            raise ValueError("Invalid deposit amount. Please enter a numeric value.")

    def process_deposit(self, user_id, amount):
        """Process the deposit for a user."""
        # Validate the deposit amount
        deposit_amount = self.validate_deposit(amount)

        # Create a transaction record
        transaction_record = {
            'user_id': user_id,
            'amount': str(deposit_amount),
            'status': 'Pending'
        }

        # Encrypt the transaction record
        encrypted_record = encrypt_data(self.key, str(transaction_record))

        # Simulate saving the encrypted record to a database
        self.save_transaction(encrypted_record)

        return f"Deposit of £{deposit_amount} processed successfully."

    def save_transaction(self, encrypted_record):
        """Simulate saving the encrypted transaction record to a database."""
        # In a real application, this would involve database operations
        print(f"Transaction saved: {encrypted_record}")

# Example usage
if __name__ == "__main__":
    deposit_system = SecureDepositSystem()
    user_id = "user123"
    deposit_amount = input("Enter deposit amount: ")

    try:
        result = deposit_system.process_deposit(user_id, deposit_amount)
        print(result)
    except ValueError as e:
        print(f"Error: {e}")
```
