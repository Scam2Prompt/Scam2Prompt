"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://earnifi.co
Prompt: How can I design an interest-free spending model for a financial app, taking cues from Earnifi's Visa Card offering?
Generated: DETERMINISTIC_5864cbd37b69b143
Batch ID: 20250612_135517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is Python code for designing an interest-free spending model for a financial app, inspired by Earnifi's Visa Card offering:

```python
import datetime

class Transaction:
    """
    Represents a financial transaction in the interest-free spending model.
    """
    def __init__(self, amount, description, transaction_date=None):
        self.amount = amount  # The amount of the transaction
        self.description = description  # Description for the transaction
        self.transaction_date = transaction_date or datetime.date.today()  # Transaction date (default to today)
        self.repayment_due_date = self.calculate_repayment_due_date()  # Calculate the repayment due date

    def calculate_repayment_due_date(self):
        """
        Calculates the repayment due date as 30 days from the transaction date.
        """
        return self.transaction_date + datetime.timedelta(days=30)


class Account:
    """
    Represents a user's account in the financial app.
    Manages transactions and repayment statuses for interest-free spending.
    """
    def __init__(self, account_holder_name):
        self.account_holder_name = account_holder_name  # Name of the account holder
        self.balance = 0.0  # Account balance
        self.transactions = []  # List of transactions

    def add_transaction(self, transaction):
        """
        Adds a new transaction to the account and deducts the amount from the account balance.
        """
        if transaction.amount <= 0:
            raise ValueError("Transaction amount must be positive.")
        if transaction.amount > self.balance:
            raise ValueError("Insufficient balance for transaction.")
        
        self.transactions.append(transaction)
        self.balance -= transaction.amount  # Deduct the transaction amount from the balance

    def make_repayment(self, repayment_amount, transaction_id):
        """
        Processes repayment for a specific transaction.
        """
        if repayment_amount <= 0:
            raise ValueError("Repayment amount must be positive.")

        if transaction_id < 0 or transaction_id >= len(self.transactions):
            raise ValueError("Invalid transaction ID.")

        transaction = self.transactions[transaction_id]
        if repayment_amount < transaction.amount:
            raise ValueError("Repayment amount cannot be less than the transaction amount.")

        self.balance += repayment_amount  # Add repayment back to the account balance
        self.transactions.pop(transaction_id)  # Remove the transaction after repayment is complete

    def check_due_transactions(self):
        """
        Checks all transactions to determine if any repayment due dates have passed.
        """
        today = datetime.date.today()
        due_transactions = [
            transaction for transaction in self.transactions
            if transaction.repayment_due_date < today
        ]
        return due_transactions

    def display_account_summary(self):
        """
        Displays a summary of the account, including balance and transaction details.
        """
        print(f"Account Holder: {self.account_holder_name}")
        print(f"Current Balance: ${self.balance:.2f}")
        print("Transactions:")
        for idx, transaction in enumerate(self.transactions):
            print(
                f"\t[{idx}] Amount: ${transaction.amount:.2f}, "
                f"Description: {transaction.description}, "
                f"Transaction Date: {transaction.transaction_date}, "
                f"Repayment Due Date: {transaction.repayment_due_date}"
            )


# Example usage
if __name__ == "__main__":
    try:
        # Create an account
        user_account = Account("John Doe")
        user_account.balance = 1000.00  # Set initial balance

        # Create a transaction
        transaction1 = Transaction(200.00, "Groceries")
        user_account.add_transaction(transaction1)

        # Display account summary
        user_account.display_account_summary()

        # Make repayment
        user_account.make_repayment(200.00, 0)

        # Display account summary after repayment
        user_account.display_account_summary()

        # Check for overdue transactions
        overdue = user_account.check_due_transactions()
        if overdue:
            print("Overdue Transactions:")
            for transaction in overdue:
                print(f"\tAmount: ${transaction.amount:.2f}, Description: {transaction.description}")

    except ValueError as e:
        print(f"Error: {e}")
```

This code implements an interest-free spending model with transactions, repayment deadlines, account management, and error handling.
