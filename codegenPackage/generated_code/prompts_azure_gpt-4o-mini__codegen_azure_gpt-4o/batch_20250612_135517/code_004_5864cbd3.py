"""
Generated Code Metadata:
========================
Original URL: https://earnifi.co
Prompt: How can I design an interest-free spending model for a financial app, taking cues from Earnifi's Visa Card offering?
Generated: DETERMINISTIC_5864cbd37b69b143
Batch ID: 20250612_135517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Below is a Python implementation of an interest-free spending model for a financial app. The code is clean, well-documented, and follows best practices.

```python
import datetime

class InterestFreeSpendingModel:
    """
    A class to represent an interest-free spending model for a financial app.
    """

    def __init__(self, spending_limit: float, repayment_period_days: int):
        """
        Initialize the spending model.

        :param spending_limit: Maximum amount the user can spend interest-free.
        :param repayment_period_days: Number of days within which the user must repay to avoid penalties.
        """
        if spending_limit <= 0:
            raise ValueError("Spending limit must be greater than zero.")
        if repayment_period_days <= 0:
            raise ValueError("Repayment period must be greater than zero.")

        self.spending_limit = spending_limit
        self.repayment_period_days = repayment_period_days
        self.transactions = []  # List to store transactions
        self.balance = 0.0  # Current balance owed by the user

    def add_transaction(self, amount: float, description: str):
        """
        Add a transaction to the spending model.

        :param amount: The amount spent in the transaction.
        :param description: A brief description of the transaction.
        :raises ValueError: If the transaction exceeds the spending limit or if the amount is invalid.
        """
        if amount <= 0:
            raise ValueError("Transaction amount must be greater than zero.")
        if self.balance + amount > self.spending_limit:
            raise ValueError("Transaction exceeds the spending limit.")

        transaction = {
            "amount": amount,
            "description": description,
            "date": datetime.datetime.now()
        }
        self.transactions.append(transaction)
        self.balance += amount
        print(f"Transaction added: {description} - ${amount:.2f}")

    def repay_balance(self, amount: float):
        """
        Repay the balance owed.

        :param amount: The amount to repay.
        :raises ValueError: If the repayment amount is invalid.
        """
        if amount <= 0:
            raise ValueError("Repayment amount must be greater than zero.")
        if amount > self.balance:
            raise ValueError("Repayment amount exceeds the current balance.")

        self.balance -= amount
        print(f"Repayment successful: ${amount:.2f}")
        if self.balance == 0:
            print("All dues cleared!")

    def check_due_date(self):
        """
        Check if any transactions are past the repayment period.

        :return: List of overdue transactions.
        """
        overdue_transactions = []
        current_date = datetime.datetime.now()

        for transaction in self.transactions:
            transaction_date = transaction["date"]
            days_since_transaction = (current_date - transaction_date).days
            if days_since_transaction > self.repayment_period_days:
                overdue_transactions.append(transaction)

        return overdue_transactions

    def get_summary(self):
        """
        Get a summary of the user's spending and balance.

        :return: A dictionary containing the spending summary.
        """
        return {
            "spending_limit": self.spending_limit,
            "current_balance": self.balance,
            "transactions": self.transactions
        }


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the model with a $1000 spending limit and a 30-day repayment period
        spending_model = InterestFreeSpendingModel(spending_limit=1000.0, repayment_period_days=30)

        # Add transactions
        spending_model.add_transaction(amount=200.0, description="Groceries")
        spending_model.add_transaction(amount=150.0, description="Electricity Bill")

        # Repay part of the balance
        spending_model.repay_balance(amount=100.0)

        # Check for overdue transactions
        overdue = spending_model.check_due_date()
        if overdue:
            print("Overdue transactions:")
            for transaction in overdue:
                print(transaction)
        else:
            print("No overdue transactions.")

        # Get spending summary
        summary = spending_model.get_summary()
        print("Spending Summary:", summary)

    except Exception as e:
        print(f"Error: {e}")
```

This code provides a robust implementation of an interest-free spending model, complete with error handling, transaction tracking, repayment functionality, and overdue transaction checks.
