"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://secure-airdrop-rectification-system.vercel.app
Prompt: Create a tool to manage deposit and withdrawal processes securely, optimizing user experience as described in the Deposit and Withdrawal Management section of the Airdrop Rectification System.
Generated: DETERMINISTIC_868af9cac9d9fdcd
Batch ID: 20250612_145510
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
from sqlite3 import Error

class DepositWithdrawalManager:
    """
    A class to manage deposit and withdrawal processes securely.
    """

    def __init__(self, db_file):
        """
        Initialize the DepositWithdrawalManager with a database file.
        
        :param db_file: Database file path
        """
        self.connection = self.create_connection(db_file)
        self.create_table()

    def create_connection(self, db_file):
        """
        Create a database connection to the SQLite database.
        
        :param db_file: Database file path
        :return: Connection object or None
        """
        connection = None
        try:
            connection = sqlite3.connect(db_file)
            print(f"Connected to database: {db_file}")
        except Error as e:
            print(f"Error connecting to database: {e}")
        return connection

    def create_table(self):
        """
        Create the deposits and withdrawals table if it does not already exist.
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS transactions (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER NOT NULL,
                    amount REAL NOT NULL,
                    transaction_type TEXT NOT NULL CHECK(transaction_type IN ('deposit', 'withdrawal')),
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                );
            ''')
            self.connection.commit()
            print("Transactions table created or already exists.")
        except Error as e:
            print(f"Error creating table: {e}")

    def deposit(self, user_id, amount):
        """
        Process a deposit transaction for a user.
        
        :param user_id: The user's ID
        :param amount: The deposit amount
        :raises ValueError: If the amount is not positive
        """
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        
        try:
            cursor = self.connection.cursor()
            cursor.execute("INSERT INTO transactions (user_id, amount, transaction_type) VALUES (?, ?, 'deposit')",
                           (user_id, amount))
            self.connection.commit()
            print(f"Deposit of {amount} for user {user_id} recorded successfully.")
        except Error as e:
            print(f"Error during deposit transaction: {e}")

    def withdraw(self, user_id, amount):
        """
        Process a withdrawal transaction for a user.
        
        :param user_id: The user's ID
        :param amount: The withdrawal amount
        :raises ValueError: If the amount is not positive or exceeds user's balance
        """
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        
        # Check user's balance
        balance = self.get_user_balance(user_id)
        if balance < amount:
            raise ValueError("Insufficient balance for withdrawal.")

        try:
            cursor = self.connection.cursor()
            cursor.execute("INSERT INTO transactions (user_id, amount, transaction_type) VALUES (?, ?, 'withdrawal')",
                           (user_id, amount))
            self.connection.commit()
            print(f"Withdrawal of {amount} for user {user_id} recorded successfully.")
        except Error as e:
            print(f"Error during withdrawal transaction: {e}")

    def get_user_balance(self, user_id):
        """
        Retrieve the current balance for the given user.
        
        :param user_id: The user's ID
        :return: The user's balance
        """
        cursor = self.connection.cursor()
        cursor.execute("SELECT SUM(CASE WHEN transaction_type='deposit' THEN amount ELSE -amount END) FROM transactions WHERE user_id=?", (user_id,))
        balance = cursor.fetchone()[0]
        return balance if balance is not None else 0.0

    def close(self):
        """
        Close the database connection.
        """
        if self.connection:
            self.connection.close()
            print("Database connection closed.")

if __name__ == "__main__":
    # Example usage
    db_manager = DepositWithdrawalManager("transactions.db")
    try:
        db_manager.deposit(user_id=1, amount=100.0)
        db_manager.withdraw(user_id=1, amount=50.0)
        print(f"User 1 balance: {db_manager.get_user_balance(1)}")
    except ValueError as ve:
        print(ve)
    finally:
        db_manager.close()
```
