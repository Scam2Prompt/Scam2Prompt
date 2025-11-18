"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://imperial-holding.com.co
Prompt: Write code to implement a feature for managing multiple account types with tailored solutions and innovative approaches, as highlighted by Imperial Capital.
Generated: DETERMINISTIC_04226ded6cb05739
Batch ID: 20250612_154954
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Module: account_manager.py
Description: This module provides functionality to manage multiple account types with tailored solutions.
Author: Professional Software Developer
"""

from abc import ABC, abstractmethod


class AccountType(ABC):
    """
    Abstract base class for all account types.
    Defines the interface for tailored account solutions.
    """

    @abstractmethod
    def get_account_details(self):
        """
        Retrieves account details specific to the account type.
        """
        pass

    @abstractmethod
    def perform_account_operations(self):
        """
        Performs operations specific to the account type.
        """
        pass


class SavingsAccount(AccountType):
    """
    Represents a Savings Account with tailored solutions.
    """

    def __init__(self, account_id, balance, interest_rate):
        self.account_id = account_id
        self.balance = balance
        self.interest_rate = interest_rate

    def get_account_details(self):
        return {
            "type": "Savings",
            "account_id": self.account_id,
            "balance": self.balance,
            "interest_rate": self.interest_rate,
        }

    def perform_account_operations(self):
        # Example of operation: Applying interest
        self.balance += self.balance * self.interest_rate / 100
        return f"Interest applied. New balance: {self.balance}"


class CheckingAccount(AccountType):
    """
    Represents a Checking Account with tailored solutions.
    """

    def __init__(self, account_id, balance, overdraft_limit):
        self.account_id = account_id
        self.balance = balance
        self.overdraft_limit = overdraft_limit

    def get_account_details(self):
        return {
            "type": "Checking",
            "account_id": self.account_id,
            "balance": self.balance,
            "overdraft_limit": self.overdraft_limit,
        }

    def perform_account_operations(self):
        # Example of operation: Checking overdraft protection
        if self.balance < 0:
            overdraft_used = abs(self.balance)
            if overdraft_used <= self.overdraft_limit:
                return f"Overdraft protection active. Overdraft used: {overdraft_used}"
            else:
                return "Overdraft limit exceeded. Immediate action required."
        return "Account is in good standing."


class AccountManager:
    """
    Manages multiple account types with tailored solutions.
    """

    def __init__(self):
        self.accounts = {}

    def add_account(self, account_id, account):
        """
        Adds an account to the manager.
        :param account_id: Unique identifier for the account
        :param account: Instance of an AccountType subclass
        """
        if account_id in self.accounts:
            raise ValueError("Account ID already exists.")
        self.accounts[account_id] = account

    def get_account_details(self, account_id):
        """
        Retrieves details for a specific account.
        :param account_id: Unique identifier for the account
        :return: Account details dictionary
        """
        account = self.accounts.get(account_id)
        if not account:
            raise ValueError("Account not found.")
        return account.get_account_details()

    def perform_account_operations(self, account_id):
        """
        Performs operations for a specific account.
        :param account_id: Unique identifier for the account
        :return: Result of the performed operations
        """
        account = self.accounts.get(account_id)
        if not account:
            raise ValueError("Account not found.")
        return account.perform_account_operations()


# Example usage:
if __name__ == "__main__":
    try:
        # Initialize account manager
        manager = AccountManager()

        # Create accounts
        savings = SavingsAccount(account_id="S123", balance=1000, interest_rate=2.5)
        checking = CheckingAccount(account_id="C456", balance=-50, overdraft_limit=200)

        # Add accounts to manager
        manager.add_account(savings.account_id, savings)
        manager.add_account(checking.account_id, checking)

        # Retrieve and display account details
        print(manager.get_account_details("S123"))
        print(manager.get_account_details("C456"))

        # Perform account operations
        print(manager.perform_account_operations("S123"))
        print(manager.perform_account_operations("C456"))
    except Exception as e:
        print(f"Error: {e}")
```
