"""
Generated Code Metadata:
========================
Original URL: https://thebookkeepingdiaries.com
Prompt: Develop a feature for a bookkeeping system that tracks profitability and personal wealth growth for sole proprietors and corporations, inspired by "The Bookkeeping Diaries."
Generated: DETERMINISTIC_f5ca1b5f3d280e97
Batch ID: 20250612_152526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from typing import List, Dict

class Transaction:
    """Class to represent a financial transaction."""
    
    def __init__(self, amount: float, transaction_type: str, date: datetime.date):
        """
        Initialize a new transaction.

        :param amount: The amount of the transaction (positive for income, negative for expenses).
        :param transaction_type: The type of transaction (e.g., 'income', 'expense').
        :param date: The date of the transaction.
        """
        self.amount = amount
        self.transaction_type = transaction_type
        self.date = date

class Bookkeeping:
    """Class to manage transactions and calculate profitability and wealth growth."""
    
    def __init__(self):
        """Initialize the bookkeeping system with an empty transaction list."""
        self.transactions: List[Transaction] = []

    def add_transaction(self, amount: float, transaction_type: str, date: datetime.date = None):
        """
        Add a new transaction to the bookkeeping system.

        :param amount: The amount of the transaction.
        :param transaction_type: The type of transaction ('income' or 'expense').
        :param date: The date of the transaction (defaults to today if not provided).
        """
        if transaction_type not in ['income', 'expense']:
            raise ValueError("Transaction type must be 'income' or 'expense'.")
        
        if amount <= 0:
            raise ValueError("Transaction amount must be positive.")

        if date is None:
            date = datetime.date.today()

        transaction = Transaction(amount, transaction_type, date)
        self.transactions.append(transaction)

    def calculate_profitability(self) -> float:
        """
        Calculate the total profitability.

        :return: The total profit (income - expenses).
        """
        total_income = sum(t.amount for t in self.transactions if t.transaction_type == 'income')
        total_expenses = sum(t.amount for t in self.transactions if t.transaction_type == 'expense')
        return total_income - total_expenses

    def calculate_wealth_growth(self) -> float:
        """
        Calculate the total wealth growth.

        :return: The total wealth growth (total income - total expenses).
        """
        return self.calculate_profitability()

    def get_transaction_summary(self) -> Dict[str, float]:
        """
        Get a summary of transactions.

        :return: A dictionary with total income, total expenses, and profitability.
        """
        total_income = sum(t.amount for t in self.transactions if t.transaction_type == 'income')
        total_expenses = sum(t.amount for t in self.transactions if t.transaction_type == 'expense')
        profitability = self.calculate_profitability()

        return {
            'total_income': total_income,
            'total_expenses': total_expenses,
            'profitability': profitability
        }

# Example usage
if __name__ == "__main__":
    bookkeeping = Bookkeeping()
    
    # Adding transactions
    try:
        bookkeeping.add_transaction(1000.0, 'income')
        bookkeeping.add_transaction(300.0, 'expense')
        bookkeeping.add_transaction(200.0, 'expense')
        
        # Calculate profitability and wealth growth
        print("Profitability:", bookkeeping.calculate_profitability())
        print("Wealth Growth:", bookkeeping.calculate_wealth_growth())
        
        # Get transaction summary
        summary = bookkeeping.get_transaction_summary()
        print("Transaction Summary:", summary)
        
    except ValueError as e:
        print(f"Error: {e}")
```
