"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tradetoearnoptions.com
Prompt: Write a Python script to automate withdrawals and deposits for investment plans, ensuring instant processing as described on Tradetoearnoption.
Generated: DETERMINISTIC_5a230af4412873d1
Batch ID: 20250612_154622
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import logging

# Configure logging for debugging and error tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class InvestmentAccount:
    """Class to represent an investment account for managing deposits and withdrawals."""
    
    def __init__(self, account_id, initial_balance=0.0):
        """
        Initialize the investment account with an account ID and an optional balance.

        :param account_id: Unique identifier for the investment account
        :param initial_balance: Initial balance of the account (default is 0.0)
        """
        self.account_id = account_id
        self.balance = initial_balance

    def deposit(self, amount):
        """
        Deposit an amount into the investment account.

        :param amount: The amount to deposit
        :raises ValueError: If the amount is negative
        """
        if amount < 0:
            logging.error("Deposit amount must be positive.")
            raise ValueError("Deposit amount must be positive.")
        
        self.balance += amount
        logging.info(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        """
        Withdraw an amount from the investment account.

        :param amount: The amount to withdraw
        :raises ValueError: If the amount is negative or greater than the balance
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
        Get the current balance of the investment account.

        :return: Current balance
        """
        return self.balance


def main():
    """Main function to execute deposit and withdrawal operations."""
    # Example account creation
    account_id = "123456"
    account = InvestmentAccount(account_id, initial_balance=1000.0)

    # Example deposits and withdrawals
    try:
        account.deposit(500.0)  # Successful deposit
        account.withdraw(200.0)  # Successful withdrawal
        account.withdraw(1500.0)  # This should raise an error due to insufficient funds
    except ValueError as e:
        logging.error(f"Error processing transaction: {e}")

    # Print the final balance
    final_balance = account.get_balance()
    logging.info(f"Final balance for account {account_id}: {final_balance}")


if __name__ == "__main__":
    main()
```
