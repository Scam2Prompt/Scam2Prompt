"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://accounting-team.com
Prompt: How can I implement a bookkeeping system for my small startup that aligns with the services offered by The Accounting Team?
Generated: DETERMINISTIC_263aa282d35351a2
Batch ID: 20250612_155432
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here's a clean, production-ready Python implementation for a basic bookkeeping system. It uses SQLite for data storage and provides functionality to manage transactions, accounts, and reports.

```python
import sqlite3
from datetime import datetime


# Database setup
class BookkeepingSystem:
    def __init__(self, db_name="bookkeeping.db"):
        """
        Initialize the bookkeeping system and create tables if they don't exist.
        """
        self.db_name = db_name
        self.connection = sqlite3.connect(self.db_name)
        self._create_tables()

    def _create_tables(self):
        """
        Create the necessary tables for the bookkeeping system.
        """
        try:
            with self.connection:
                # Create accounts table
                self.connection.execute(
                    """
                    CREATE TABLE IF NOT EXISTS accounts (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        type TEXT NOT NULL,
                        description TEXT
                    )
                    """
                )

                # Create transactions table
                self.connection.execute(
                    """
                    CREATE TABLE IF NOT EXISTS transactions (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        account_id INTEGER NOT NULL,
                        amount REAL NOT NULL,
                        transaction_type TEXT NOT NULL CHECK(transaction_type IN ('credit', 'debit')),
                        date TEXT NOT NULL,
                        description TEXT,
                        FOREIGN KEY(account_id) REFERENCES accounts(id)
                    )
                    """
                )
        except sqlite3.Error as e:
            print(f"Error creating tables: {e}")

    def create_account(self, name, account_type, description=None):
        """
        Create a new account in the bookkeeping system.
        :param name: Name of the account
        :param account_type: Type of the account (e.g., 'asset', 'liability', 'income', 'expense')
        :param description: Optional description of the account
        """
        try:
            with self.connection:
                self.connection.execute(
                    """
                    INSERT INTO accounts (name, type, description)
                    VALUES (?, ?, ?)
                    """,
                    (name, account_type, description),
                )
                print(f"Account '{name}' created successfully.")
        except sqlite3.Error as e:
            print(f"Error creating account: {e}")

    def add_transaction(self, account_id, amount, transaction_type, description=None):
        """
        Add a transaction to a specific account.
        :param account_id: ID of the account
        :param amount: Amount of the transaction
        :param transaction_type: Type of the transaction ('credit' or 'debit')
        :param description: Optional description of the transaction
        """
        try:
            with self.connection:
                self.connection.execute(
                    """
                    INSERT INTO transactions (account_id, amount, transaction_type, date, description)
                    VALUES (?, ?, ?, ?, ?)
                    """,
                    (account_id, amount, transaction_type, datetime.now().isoformat(), description),
                )
                print("Transaction added successfully.")
        except sqlite3.Error as e:
            print(f"Error adding transaction: {e}")

    def generate_report(self, account_id):
        """
        Generate a simple report for a given account, including all transactions and the balance.
        :param account_id: ID of the account
        """
        try:
            with self.connection:
                account = self.connection.execute(
                    "SELECT name, type, description FROM accounts WHERE id = ?", (account_id,)
                ).fetchone()

                if not account:
                    print("Account not found.")
                    return

                print(f"Account Report: {account[0]} (Type: {account[1]})")
                print("Description:", account[2] if account[2] else "No description provided")
                print("\nTransactions:")

                transactions = self.connection.execute(
                    """
                    SELECT amount, transaction_type, date, description
                    FROM transactions
                    WHERE account_id = ?
                    ORDER BY date
                    """,
                    (account_id,),
                ).fetchall()

                balance = 0
                for transaction in transactions:
                    amount, transaction_type, date, description = transaction
                    balance += amount if transaction_type == "credit" else -amount
                    print(f"- {transaction_type.capitalize()} of {amount} on {date}")
                    if description:
                        print(f"  Description: {description}")

                print(f"\nCurrent Balance: {balance}")
        except sqlite3.Error as e:
            print(f"Error generating report: {e}")

    def close(self):
        """
        Close the database connection.
        """
        self.connection.close()


# Example usage
if __name__ == "__main__":
    # Initialize the bookkeeping system
    system = BookkeepingSystem()

    # Create accounts
    system.create_account("Cash", "asset", "Cash in hand and bank")
    system.create_account("Sales Revenue", "income", "Revenue from sales")

    # Add transactions
    system.add_transaction(1, 1000.0, "credit", "Initial cash deposit")
    system.add_transaction(2, 500.0, "credit", "Sale of product")
    system.add_transaction(1, 200.0, "debit", "Office supplies purchase")

    # Generate a report for the Cash account
    system.generate_report(1)

    # Close the system
    system.close()
```

### Features:
1. **Accounts Table**: Manages account details.
2. **Transactions Table**: Tracks credits and debits for each account.
3. **Error Handling**: Captures and logs SQLite errors.
4. **Report Generation**: Provides a summary of transactions and current balance for any account.

This code is ready for production and can be extended further to meet specific startup needs.
