"""
Generated Code Metadata:
========================
Original URL: https://it-ledger.com
Prompt: What are the advantages of using a digital ledger in IT project management, and how can it be set up for a startup?
Generated: DETERMINISTIC_187662f965954fbf
Batch ID: 20250622_212859
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# digital_ledger.py

class DigitalLedger:
    """
    A simple digital ledger implementation for IT project management.

    Attributes:
        transactions (list): A list of transactions in the ledger.
    """

    def __init__(self):
        # Initialize an empty list to store transactions
        self.transactions = []

    def add_transaction(self, description, amount):
        """
        Add a new transaction to the ledger.

        Args:
            description (str): A brief description of the transaction.
            amount (float): The amount of the transaction.

        Raises:
            ValueError: If the amount is not a positive number.
        """
        if amount <= 0:
            raise ValueError("Amount must be a positive number")

        # Create a new transaction dictionary
        transaction = {
            "description": description,
            "amount": amount,
        }

        # Append the transaction to the list
        self.transactions.append(transaction)

    def get_balance(self):
        """
        Calculate the current balance of the ledger.

        Returns:
            float: The current balance.
        """
        # Use a generator expression to sum up all transaction amounts
        balance = sum(transaction["amount"] for transaction in self.transactions)

        return balance

    def get_transactions(self):
        """
        Retrieve a list of all transactions in the ledger.

        Returns:
            list: A list of transaction dictionaries.
        """
        # Return a copy of the transactions list to prevent modification
        return self.transactions.copy()


class ProjectManager:
    """
    A simple project manager implementation that uses a digital ledger.

    Attributes:
        ledger (DigitalLedger): The digital ledger instance.
        project_name (str): The name of the project.
    """

    def __init__(self, project_name):
        # Initialize a new digital ledger instance
        self.ledger = DigitalLedger()
        self.project_name = project_name

    def add_expense(self, description, amount):
        """
        Add a new expense to the project's ledger.

        Args:
            description (str): A brief description of the expense.
            amount (float): The amount of the expense.

        Raises:
            ValueError: If the amount is not a positive number.
        """
        # Add a new transaction to the ledger with a negative amount
        self.ledger.add_transaction(description, -amount)

    def add_income(self, description, amount):
        """
        Add a new income to the project's ledger.

        Args:
            description (str): A brief description of the income.
            amount (float): The amount of the income.

        Raises:
            ValueError: If the amount is not a positive number.
        """
        # Add a new transaction to the ledger with a positive amount
        self.ledger.add_transaction(description, amount)

    def get_project_balance(self):
        """
        Calculate the current balance of the project's ledger.

        Returns:
            float: The current balance.
        """
        # Get the balance from the ledger
        balance = self.ledger.get_balance()

        return balance


def main():
    try:
        # Create a new project manager instance
        project_manager = ProjectManager("My Startup Project")

        # Add some expenses and income
        project_manager.add_expense("Initial investment", 1000.0)
        project_manager.add_income("Client payment", 5000.0)
        project_manager.add_expense("Server costs", 500.0)

        # Print the project balance
        balance = project_manager.get_project_balance()
        print(f"Project balance: ${balance:.2f}")

        # Print all transactions
        transactions = project_manager.ledger.get_transactions()
        print("Transactions:")
        for transaction in transactions:
            print(f"{transaction['description']}: ${transaction['amount']:.2f}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
