"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://greenfieldscommunityllc.com
Prompt: Write code to develop a feature for Greenfields Community Bank's online banking system that allows users to transfer funds and pay bills from their accounts.
Generated: DETERMINISTIC_92c6576ab047649c
Batch ID: 20250612_151329
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
from decimal import Decimal, InvalidOperation

class BankAccount:
    """A class representing a bank account for fund transfers and bill payments."""

    def __init__(self, account_id, balance):
        self.account_id = account_id
        self.balance = Decimal(balance)

    def transfer_funds(self, target_account, amount):
        """
        Transfer funds from this account to another account.

        Args:
            target_account (BankAccount): The target account to transfer funds to.
            amount (Decimal): The amount to transfer.

        Raises:
            ValueError: If the amount is negative or exceeds the balance.
        """
        if amount <= 0:
            raise ValueError("Transfer amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient funds for transfer.")

        # Perform the transfer
        self.balance -= amount
        target_account.balance += amount

    def pay_bill(self, bill_amount):
        """
        Pay a bill from this account.

        Args:
            bill_amount (Decimal): The amount of the bill to pay.

        Raises:
            ValueError: If the bill amount is negative or exceeds the balance.
        """
        if bill_amount <= 0:
            raise ValueError("Bill amount must be positive.")
        if bill_amount > self.balance:
            raise ValueError("Insufficient funds for bill payment.")

        # Perform the bill payment
        self.balance -= bill_amount


class Bank:
    """A class representing the bank, handling account operations."""

    def __init__(self, db_name='bank.db'):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.initialize_db()

    def initialize_db(self):
        """Initialize the database with necessary tables."""
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS accounts (
                account_id INTEGER PRIMARY KEY,
                balance REAL NOT NULL
            )
        ''')
        self.connection.commit()

    def create_account(self, initial_balance):
        """
        Create a new bank account.

        Args:
            initial_balance (Decimal): The initial balance for the new account.

        Returns:
            BankAccount: The created bank account.
        """
        self.cursor.execute('''
            INSERT INTO accounts (balance) VALUES (?)
        ''', (initial_balance,))
        self.connection.commit()
        return BankAccount(self.cursor.lastrowid, initial_balance)

    def get_account(self, account_id):
        """
        Retrieve an account by ID.

        Args:
            account_id (int): The ID of the account to retrieve.

        Returns:
            BankAccount: The requested bank account.
        """
        self.cursor.execute('SELECT * FROM accounts WHERE account_id = ?', (account_id,))
        row = self.cursor.fetchone()
        if row:
            return BankAccount(row[0], row[1])
        else:
            raise ValueError("Account not found.")

    def close(self):
        """Close the bank database connection."""
        self.connection.close()


def main():
    """Main function to demonstrate fund transfer and bill payment."""
    bank = Bank()

    # Create accounts
    account_a = bank.create_account(Decimal('500.00'))
    account_b = bank.create_account(Decimal('300.00'))

    try:
        # Transfer funds
        print(f"Initial balances: A: {account_a.balance}, B: {account_b.balance}")
        account_a.transfer_funds(account_b, Decimal('200.00'))
        print(f"Balances after transfer: A: {account_a.balance}, B: {account_b.balance}")

        # Pay a bill
        account_b.pay_bill(Decimal('50.00'))
        print(f"Balances after bill payment: A: {account_a.balance}, B: {account_b.balance}")

    except ValueError as e:
        print(f"Error: {e}")
    finally:
        bank.close()


if __name__ == "__main__":
    main()
```
