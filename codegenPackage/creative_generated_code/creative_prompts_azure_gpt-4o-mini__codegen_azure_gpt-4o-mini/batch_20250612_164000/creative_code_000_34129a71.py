"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://buylibracoins.com
Prompt: How can I implement a secure wallet system for online slot games that allows for quick deposits and withdrawals?
Generated: DETERMINISTIC_34129a71d106d205
Batch ID: 20250612_164000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
from hashlib import sha256
from uuid import uuid4
import os

class WalletSystem:
    def __init__(self, db_name='wallets.db'):
        """
        Initializes the WalletSystem with a connection to the SQLite database.
        Creates the wallets table if it doesn't exist.
        """
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_wallets_table()

    def create_wallets_table(self):
        """
        Creates a wallets table in the database if it doesn't already exist.
        """
        create_table_query = """
        CREATE TABLE IF NOT EXISTS wallets (
            id TEXT PRIMARY KEY,
            user_id TEXT NOT NULL,
            balance REAL NOT NULL CHECK (balance >= 0)
        )
        """
        self.cursor.execute(create_table_query)
        self.connection.commit()

    def create_wallet(self, user_id):
        """
        Creates a new wallet for the given user_id.
        :param user_id: Unique identifier for the user.
        :raises ValueError: If the wallet already exists.
        """
        wallet_id = str(uuid4())
        self.cursor.execute("SELECT * FROM wallets WHERE user_id = ?", (user_id,))
        if self.cursor.fetchone() is not None:
            raise ValueError("Wallet already exists for this user.")

        self.cursor.execute("INSERT INTO wallets (id, user_id, balance) VALUES (?, ?, ?)",
                            (wallet_id, user_id, 0.0))
        self.connection.commit()

    def deposit(self, user_id, amount):
        """
        Deposits the specified amount into the user's wallet.
        :param user_id: Unique identifier for the user.
        :param amount: Amount to deposit.
        :raises ValueError: If the amount is invalid.
        """
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")

        self.cursor.execute("UPDATE wallets SET balance = balance + ? WHERE user_id = ?", (amount, user_id))
        if self.cursor.rowcount == 0:
            raise ValueError("No wallet found for this user.")

        self.connection.commit()

    def withdraw(self, user_id, amount):
        """
        Withdraws the specified amount from the user's wallet.
        :param user_id: Unique identifier for the user.
        :param amount: Amount to withdraw.
        :raises ValueError: If the amount is invalid or exceeds the balance.
        """
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")

        self.cursor.execute("SELECT balance FROM wallets WHERE user_id = ?", (user_id,))
        result = self.cursor.fetchone()
        if result is None:
            raise ValueError("No wallet found for this user.")
        
        balance = result[0]
        if amount > balance:
            raise ValueError("Insufficient funds for withdrawal.")

        self.cursor.execute("UPDATE wallets SET balance = balance - ? WHERE user_id = ?", (amount, user_id))
        self.connection.commit()

    def get_balance(self, user_id):
        """
        Retrieves the current balance of the user's wallet.
        :param user_id: Unique identifier for the user.
        :return: User's balance.
        :raises ValueError: If the wallet does not exist.
        """
        self.cursor.execute("SELECT balance FROM wallets WHERE user_id = ?", (user_id,))
        result = self.cursor.fetchone()
        if result is None:
            raise ValueError("No wallet found for this user.")
        return result[0]

    def close(self):
        """
        Closes the database connection.
        """
        self.connection.close()

if __name__ == "__main__":
    # Example usage of the WalletSystem
    wallet_system = WalletSystem()
    user_id = 'user123'
    
    try:
        wallet_system.create_wallet(user_id)
        print("Wallet created successfully.")
        
        wallet_system.deposit(user_id, 100.0)
        print("Deposit successful. New balance:", wallet_system.get_balance(user_id))
        
        wallet_system.withdraw(user_id, 50.0)
        print("Withdrawal successful. New balance:", wallet_system.get_balance(user_id))
        
    except ValueError as e:
        print("Error:", e)
    finally:
        wallet_system.close()
```
