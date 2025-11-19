"""
Generated Code Metadata:
========================
Original URL: https://cgbokhald.is
Prompt: Create a function that handles accounts payable and receivable management, inspired by the services listed on CGBókhald's website.
Generated: DETERMINISTIC_a16d0af9cd800bdd
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Account:
    """
    A class to represent a financial account for accounts payable and receivable.
    """

    def __init__(self, account_name: str):
        """
        Initializes an account with a name and empty transactions.

        :param account_name: The name of the account.
        """
        self.account_name = account_name
        self.transactions = []

    def add_transaction(self, amount: float, transaction_type: str, description: str = ""):
        """
        Adds a transaction to the account.

        :param amount: The amount of the transaction (positive for receivable, negative for payable).
        :param transaction_type: The type of transaction ('receivable' or 'payable').
        :param description: A brief description of the transaction.
        :raises ValueError: If the transaction type is invalid.
        """
        if transaction_type not in ['receivable', 'payable']:
            raise ValueError("Transaction type must be 'receivable' or 'payable'.")

        transaction = {
            'amount': amount,
            'type': transaction_type,
            'description': description
        }
        self.transactions.append(transaction)

    def get_balance(self) -> float:
        """
        Calculates the current balance of the account.

        :return: The current balance (positive for receivables, negative for payables).
        """
        balance = sum(
            t['amount'] if t['type'] == 'receivable' else -t['amount'
            for t in self.transactions
        )
        return balance

    def get_transaction_history(self):
        """
        Returns the transaction history of the account.

        :return: A list of transactions.
        """
        return self.transactions

    def clear_transactions(self):
        """
        Clears all transactions from the account.
        """
        self.transactions.clear()


# Example usage
if __name__ == "__main__":
    try:
        # Create an account for managing accounts payable and receivable
        account = Account("Business Account")

        # Add some transactions
        account.add_transaction(1000.0, 'receivable', 'Invoice #001')
        account.add_transaction(500.0, 'payable', 'Bill #001')
        account.add_transaction(200.0, 'receivable', 'Invoice #002')

        # Print the current balance
        print(f"Current Balance: {account.get_balance()}")

        # Print transaction history
        print("Transaction History:")
        for transaction in account.get_transaction_history():
            print(transaction)

        # Clear transactions if needed
        # account.clear_transactions()

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
