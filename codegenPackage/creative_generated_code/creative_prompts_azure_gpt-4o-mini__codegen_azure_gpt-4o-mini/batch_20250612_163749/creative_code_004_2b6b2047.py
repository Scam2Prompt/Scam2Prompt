"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://front-1.pointech.cloud
Prompt: Describe how to securely store cryptocurrencies using PointPay's multi-account security features in a code example.
Generated: DETERMINISTIC_2b6b2047a4c9d476
Batch ID: 20250612_163749
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import cryptography
from cryptography.fernet import Fernet
import json

class CryptoAccountManager:
    """
    A class to securely manage cryptocurrency accounts using multi-account security features.
    """

    def __init__(self, master_key: bytes):
        """
        Initialize the CryptoAccountManager with a master key for encryption and decryption.

        :param master_key: A bytes object representing the master key.
        """
        self.master_key = master_key
        self.cipher = Fernet(master_key)
        self.accounts = {}

    def create_account(self, account_name: str, password: str):
        """
        Create a new cryptocurrency account with a secure password.

        :param account_name: The name of the cryptocurrency account.
        :param password: The password for the cryptocurrency account.
        :raises ValueError: If the account already exists or if the account name is invalid.
        """
        if account_name in self.accounts:
            raise ValueError("Account already exists.")
        
        if not account_name.isalnum():
            raise ValueError("Account name must be alphanumeric.")

        # Encrypt the password before storing it
        encrypted_password = self.cipher.encrypt(password.encode())
        self.accounts[account_name] = encrypted_password

    def get_account_password(self, account_name: str) -> str:
        """
        Retrieve the decrypted password for a cryptocurrency account.

        :param account_name: The name of the cryptocurrency account.
        :raises ValueError: If the account does not exist.
        :return: The decrypted password for the account.
        """
        if account_name not in self.accounts:
            raise ValueError("Account not found.")

        encrypted_password = self.accounts[account_name]
        return self.cipher.decrypt(encrypted_password).decode()

    def export_accounts(self, file_path: str):
        """
        Export all accounts to a JSON file securely.

        :param file_path: The path to the file where accounts will be saved.
        :raises IOError: If there is an issue writing to the file.
        """
        try:
            with open(file_path, 'w') as file:
                json.dump(self.accounts, file)
        except IOError as e:
            raise IOError(f"Failed to write to file: {e}")

    def import_accounts(self, file_path: str):
        """
        Import accounts from a JSON file securely.

        :param file_path: The path to the file from which accounts will be loaded.
        :raises IOError: If there is an issue reading the file.
        :raises ValueError: If the file contains invalid data.
        """
        try:
            with open(file_path, 'r') as file:
                self.accounts = json.load(file)
                if not isinstance(self.accounts, dict):
                    raise ValueError("Invalid data format.")
        except IOError as e:
            raise IOError(f"Failed to read from file: {e}")

# Example usage:
if __name__ == "__main__":
    # Generate a master key for encryption and decryption
    master_key = Fernet.generate_key()
    manager = CryptoAccountManager(master_key)

    # Create a new cryptocurrency account
    try:
        manager.create_account("my_crypto_account", "secure_password_123")
        print("Account created successfully.")

        # Retrieve the password for the account
        password = manager.get_account_password("my_crypto_account")
        print(f"Retrieved password: {password}")

        # Export accounts to a file
        manager.export_accounts("accounts.json")
        print("Accounts exported successfully.")

        # Import accounts from a file
        manager.import_accounts("accounts.json")
        print("Accounts imported successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
```
