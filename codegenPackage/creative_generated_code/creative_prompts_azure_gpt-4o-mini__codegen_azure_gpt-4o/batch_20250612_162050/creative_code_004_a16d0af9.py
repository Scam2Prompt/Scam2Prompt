"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cgbokhald.is
Prompt: Create a function that handles accounts payable and receivable management, inspired by the services listed on CGBókhald's website.
Generated: DETERMINISTIC_a16d0af9cd800bdd
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime


class Transaction:
    """
    A class to represent a financial transaction (payable or receivable).
    """

    def __init__(self, transaction_id, amount, description, transaction_type, due_date):
        """
        Initialize a transaction object.

        :param transaction_id: Unique ID for the transaction (str)
        :param amount: Amount of money involved in the transaction (float)
        :param description: Description of the transaction (str)
        :param transaction_type: Type of transaction ('payable' or 'receivable') (str)
        :param due_date: Due date for the transaction (datetime)
        """
        self.transaction_id = transaction_id
        self.amount = amount
        self.description = description
        self.transaction_type = transaction_type
        self.due_date = due_date
        self.status = "Pending"  # Default status for all transactions

    def mark_as_paid(self):
        """
        Mark the transaction as paid.
        """
        self.status = "Paid"


class AccountManager:
    """
    A class to manage accounts payable and receivable.
    """

    def __init__(self):
        """
        Initialize the AccountManager with empty lists for payables and receivables.
        """
        self.payables = []
        self.receivables = []

    def add_transaction(self, transaction):
        """
        Add a transaction to the appropriate list (payables or receivables).

        :param transaction: Transaction object to be added
        :raises ValueError: If transaction_type is invalid
        """
        if transaction.transaction_type == "payable":
            self.payables.append(transaction)
        elif transaction.transaction_type == "receivable":
            self.receivables.append(transaction)
        else:
            raise ValueError("Invalid transaction type. Must be 'payable' or 'receivable'.")

    def get_due_transactions(self, transaction_type, current_date=None):
        """
        Get a list of transactions that are due on or before the current date.

        :param transaction_type: Type of transaction ('payable' or 'receivable') (str)
        :param current_date: Date to check for due transactions. Defaults to today. (datetime)
        :return: List of due transactions
        :raises ValueError: If transaction_type is invalid
        """
        current_date = current_date or datetime.now()
        if transaction_type == "payable":
            return [t for t in self.payables if t.due_date <= current_date and t.status == "Pending"]
        elif transaction_type == "receivable":
            return [t for t in self.receivables if t.due_date <= current_date and t.status == "Pending"]
        else:
            raise ValueError("Invalid transaction type. Must be 'payable' or 'receivable'.")

    def mark_transaction_as_paid(self, transaction_id, transaction_type):
        """
        Mark a specific transaction as paid.

        :param transaction_id: The ID of the transaction to mark as paid (str)
        :param transaction_type: Type of transaction ('payable' or 'receivable') (str)
        :raises ValueError: If transaction_type is invalid or transaction does not exist
        """
        transactions = self.payables if transaction_type == "payable" else self.receivables
        for transaction in transactions:
            if transaction.transaction_id == transaction_id:
                transaction.mark_as_paid()
                return
        raise ValueError(f"Transaction with ID {transaction_id} not found in {transaction_type}s.")

    def summary(self):
        """
        Generate a summary of accounts payable and receivable.

        :return: Dictionary containing summary information
        """
        return {
            "total_payables": sum(t.amount for t in self.payables),
            "total_receivables": sum(t.amount for t in self.receivables),
            "pending_payables": sum(t.amount for t in self.payables if t.status == "Pending"),
            "pending_receivables": sum(t.amount for t in self.receivables if t.status == "Pending"),
        }


# Example usage:
if __name__ == "__main__":
    manager = AccountManager()

    # Adding transactions
    transaction1 = Transaction(
        transaction_id="T001", 
        amount=500.0, 
        description="Office Rent", 
        transaction_type="payable", 
        due_date=datetime(2023, 11, 30)
    )
    transaction2 = Transaction(
        transaction_id="T002", 
        amount=1200.0, 
        description="Client Invoice", 
        transaction_type="receivable", 
        due_date=datetime(2023, 11, 15)
    )

    manager.add_transaction(transaction1)
    manager.add_transaction(transaction2)

    # Check due transactions
    print("Due Payables:", [t.transaction_id for t in manager.get_due_transactions("payable")])
    print("Due Receivables:", [t.transaction_id for t in manager.get_due_transactions("receivable")])

    # Mark a transaction as paid
    manager.mark_transaction_as_paid("T001", "payable")

    # Print summary
    print("Summary:", manager.summary())
```
