"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://skaizengroup.eu
Prompt: Create a training module for junior developers on cash management and payment systems, inspired by SKAIZen Cube's cross-skilling methodology.
Generated: DETERMINISTIC_a66065ec89e07b93
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Training Module - Cash Management and Payment Systems
Inspired by SKAIZen Cube's Cross-Skilling Methodology
This module provides a framework for junior developers to learn concepts in cash management 
and payment systems via practical, hands-on coding exercises.
"""

import logging
from typing import Dict, List

# Set up logging for debugging and monitoring
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class PaymentSystem:
    """
    A class representing a basic payment system with functionalities for cash management
    such as adding funds, making payments, and viewing account details.
    """
    def __init__(self):
        """
        Initializes the payment system with empty accounts.
        """
        self.accounts = {}  # Dictionary to store account information
        logging.info("Payment system initialized.")

    def create_account(self, account_name: str, initial_balance: float) -> None:
        """
        Creates a new account with a specified initial balance.

        :param account_name: Name of the account
        :param initial_balance: Initial balance for the account
        :raises ValueError: If account already exists or if the initial balance is invalid
        """
        if account_name in self.accounts:
            raise ValueError(f"Account '{account_name}' already exists.")
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self.accounts[account_name] = initial_balance
        logging.info(f"Account '{account_name}' created with initial balance: {initial_balance:.2f}")

    def add_funds(self, account_name: str, amount: float) -> None:
        """
        Adds funds to an existing account.

        :param account_name: Name of the account
        :param amount: Amount to be added to the account
        :raises ValueError: If account does not exist or if the amount is invalid
        """
        if account_name not in self.accounts:
            raise ValueError(f"Account '{account_name}' does not exist.")
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")
        self.accounts[account_name] += amount
        logging.info(f"Added {amount:.2f} to account '{account_name}'. New balance: {self.accounts[account_name]:.2f}")

    def make_payment(self, from_account: str, to_account: str, amount: float) -> None:
        """
        Makes a payment from one account to another.

        :param from_account: Account from which payment is made
        :param to_account: Account to which payment is made
        :param amount: Amount to be transferred
        :raises ValueError: If any account does not exist, insufficient funds, or invalid amount
        """
        if from_account not in self.accounts:
            raise ValueError(f"Source account '{from_account}' does not exist.")
        if to_account not in self.accounts:
            raise ValueError(f"Destination account '{to_account}' does not exist.")
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")
        if self.accounts[from_account] < amount:
            raise ValueError("Insufficient funds in source account.")
        
        self.accounts[from_account] -= amount
        self.accounts[to_account] += amount
        logging.info(f"Payment of {amount:.2f} made from '{from_account}' to '{to_account}'.")
        logging.info(f"New balance - '{from_account}': {self.accounts[from_account]:.2f}, '{to_account}': {self.accounts[to_account]:.2f}")

    def get_account_details(self, account_name: str) -> Dict[str, float]:
        """
        Retrieves the details of an account.

        :param account_name: Name of the account
        :return: Dictionary containing account name and balance
        :raises ValueError: If account does not exist
        """
        if account_name not in self.accounts:
            raise ValueError(f"Account '{account_name}' does not exist.")
        logging.info(f"Details for account '{account_name}' retrieved.")
        return {account_name: self.accounts[account_name]}

    def list_accounts(self) -> List[Dict[str, float]]:
        """
        Lists all accounts and their balances.

        :return: List of dictionaries containing account names and balances
        """
        logging.info("Listing all accounts.")
        return [{"account_name": name, "balance": balance} for name, balance in self.accounts.items()]


# Example usage of the PaymentSystem class
if __name__ == "__main__":
    try:
        # Initialize the payment system
        payment_system = PaymentSystem()
        
        # Create accounts
        payment_system.create_account("Alice", 500.0)
        payment_system.create_account("Bob", 300.0)
        
        # Add funds to an account
        payment_system.add_funds("Alice", 200.0)
        
        # Make a payment
        payment_system.make_payment("Alice", "Bob", 150.0)
        
        # Get account details
        alice_details = payment_system.get_account_details("Alice")
        bob_details = payment_system.get_account_details("Bob")
        
        logging.info(f"Alice's Account Details: {alice_details}")
        logging.info(f"Bob's Account Details: {bob_details}")
        
        # List all accounts
        accounts_list = payment_system.list_accounts()
        logging.info(f"All Accounts: {accounts_list}")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
