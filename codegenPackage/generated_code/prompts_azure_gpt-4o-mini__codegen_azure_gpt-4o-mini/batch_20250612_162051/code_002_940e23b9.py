"""
Generated Code Metadata:
========================
Original URL: https://alwakeelacademy.com
Prompt: Write a Python script that utilizes financial accounting principles and includes features for searching solutions, inspired by alwakeelacademy.com.
Generated: DETERMINISTIC_940e23b99e8e5ed9
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class FinancialAccount:
    """
    A class to represent a financial account with basic operations.
    """

    def __init__(self, account_name, initial_balance=0.0):
        """
        Initializes a new financial account.

        :param account_name: Name of the account
        :param initial_balance: Initial balance of the account
        """
        self.account_name = account_name
        self.balance = initial_balance

    def deposit(self, amount):
        """
        Deposits a specified amount into the account.

        :param amount: Amount to deposit
        :raises ValueError: If the amount is negative
        """
        if amount < 0:
            logging.error("Deposit amount must be positive.")
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
        logging.info(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        """
        Withdraws a specified amount from the account.

        :param amount: Amount to withdraw
        :raises ValueError: If the amount is negative or exceeds the balance
        """
        if amount < 0:
            logging.error("Withdrawal amount must be positive.")
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            logging.error("Insufficient funds for withdrawal.")
            raise ValueError("Insufficient funds for withdrawal.")
        self.balance -= amount
        logging.info(f"Withdrew {amount}. New balance: {self.balance}")

    def get_balance(self):
        """
        Returns the current balance of the account.

        :return: Current balance
        """
        return self.balance


class FinancialManager:
    """
    A class to manage multiple financial accounts.
    """

    def __init__(self):
        """
        Initializes the financial manager with an empty account list.
        """
        self.accounts = {}

    def add_account(self, account_name, initial_balance=0.0):
        """
        Adds a new financial account.

        :param account_name: Name of the account
        :param initial_balance: Initial balance of the account
        :raises ValueError: If the account already exists
        """
        if account_name in self.accounts:
            logging.error("Account already exists.")
            raise ValueError("Account already exists.")
        self.accounts[account_name] = FinancialAccount(account_name, initial_balance)
        logging.info(f"Account '{account_name}' created with initial balance {initial_balance}.")

    def search_account(self, account_name):
        """
        Searches for an account by name.

        :param account_name: Name of the account to search for
        :return: FinancialAccount object if found, None otherwise
        """
        return self.accounts.get(account_name, None)

    def save_accounts(self, filename):
        """
        Saves the accounts to a JSON file.

        :param filename: Name of the file to save accounts
        """
        try:
            with open(filename, 'w') as file:
                json.dump({name: account.get_balance() for name, account in self.accounts.items()}, file)
            logging.info(f"Accounts saved to {filename}.")
        except IOError as e:
            logging.error(f"Error saving accounts: {e}")

    def load_accounts(self, filename):
        """
        Loads accounts from a JSON file.

        :param filename: Name of the file to load accounts from
        :raises IOError: If the file cannot be read
        """
        try:
            with open(filename, 'r') as file:
                accounts_data = json.load(file)
                for name, balance in accounts_data.items():
                    self.add_account(name, balance)
            logging.info(f"Accounts loaded from {filename}.")
        except IOError as e:
            logging.error(f"Error loading accounts: {e}")
        except json.JSONDecodeError as e:
            logging.error(f"Error decoding JSON: {e}")


if __name__ == "__main__":
    # Example usage of the FinancialManager
    manager = FinancialManager()
    
    # Adding accounts
    try:
        manager.add_account("Savings", 1000.0)
        manager.add_account("Checking", 500.0)
    except ValueError as e:
        logging.error(e)

    # Searching for an account
    account = manager.search_account("Savings")
    if account:
        logging.info(f"Found account: {account.account_name} with balance: {account.get_balance()}")
    else:
        logging.info("Account not found.")

    # Performing transactions
    try:
        account.deposit(200)
        account.withdraw(150)
    except ValueError as e:
        logging.error(e)

    # Saving accounts to a file
    manager.save_accounts("accounts.json")

    # Loading accounts from a file
    manager.load_accounts("accounts.json")
```
