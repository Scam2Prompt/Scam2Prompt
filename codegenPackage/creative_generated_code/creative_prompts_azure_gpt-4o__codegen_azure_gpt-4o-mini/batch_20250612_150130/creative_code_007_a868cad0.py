"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://financeforcetd.com
Prompt: Generate a Python script to simulate the withdrawal process for Finance Force Ltd, ensuring that all withdrawals are processed within 24 hours. Include functionality to validate the withdrawal amount against the user's account balance.
Generated: DETERMINISTIC_a868cad0f2d930b1
Batch ID: 20250612_150130
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import threading
from datetime import datetime, timedelta

class Account:
    """Class representing a bank account."""

    def __init__(self, account_number, balance):
        """
        Initializes a new account with the given account number and balance.

        :param account_number: The unique identifier for the account.
        :param balance: The initial balance of the account.
        """
        self.account_number = account_number
        self.balance = balance

    def validate_withdrawal(self, amount):
        """
        Validates if the withdrawal amount is less than or equal to the current balance.

        :param amount: The amount to withdraw.
        :return: True if the withdrawal is valid, False otherwise.
        """
        return amount <= self.balance

    def withdraw(self, amount):
        """
        Withdraws the specified amount from the account if valid.

        :param amount: The amount to withdraw.
        :raises ValueError: If the withdrawal amount exceeds the account balance.
        """
        if not self.validate_withdrawal(amount):
            raise ValueError("Insufficient funds for withdrawal.")
        self.balance -= amount
        return self.balance


class WithdrawalProcessor:
    """Class for processing withdrawal requests."""

    def __init__(self, account):
        """
        Initializes the withdrawal processor for a specific account.

        :param account: The Account object associated with this processor.
        """
        self.account = account
        self.withdrawal_requests = []

    def request_withdrawal(self, amount):
        """
        Requests a withdrawal and processes it in a separate thread.

        :param amount: The amount to withdraw.
        """
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        
        self.withdrawal_requests.append(amount)
        threading.Thread(target=self.process_withdrawal, args=(amount,)).start()

    def process_withdrawal(self, amount):
        """
        Processes the withdrawal request, simulating a delay of 24 hours.

        :param amount: The amount to withdraw.
        """
        # Simulate processing time (here we use a shorter delay for demonstration)
        time.sleep(2)  # Replace this with 86400 for actual 24 hours
        try:
            new_balance = self.account.withdraw(amount)
            print(f"Withdrawal of {amount} processed successfully. New balance: {new_balance}.")
        except ValueError as e:
            print(f"Withdrawal of {amount} failed: {e}.")


def main():
    # Initialize account with a balance of 1000
    account = Account(account_number="123456", balance=1000)

    # Create a withdrawal processor for the account
    processor = WithdrawalProcessor(account)

    # Simulate withdrawal requests
    try:
        processor.request_withdrawal(200)  # Valid withdrawal
        processor.request_withdrawal(500)  # Valid withdrawal
        processor.request_withdrawal(400)  # Exceeds balance
    except ValueError as e:
        print(f"Error: {e}")

    # Wait for threads to finish (for demonstration purposes)
    time.sleep(5)


if __name__ == "__main__":
    main()
```
