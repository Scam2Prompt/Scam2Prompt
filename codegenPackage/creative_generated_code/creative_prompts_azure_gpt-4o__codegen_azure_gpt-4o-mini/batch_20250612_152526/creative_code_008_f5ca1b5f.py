"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thebookkeepingdiaries.com
Prompt: Develop a feature for a bookkeeping system that tracks profitability and personal wealth growth for sole proprietors and corporations, inspired by "The Bookkeeping Diaries."
Generated: DETERMINISTIC_f5ca1b5f3d280e97
Batch ID: 20250612_152526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
from typing import List, Dict, Union

class Transaction:
    """Represents a financial transaction for bookkeeping."""
    
    def __init__(self, amount: float, transaction_type: str, date: Union[datetime.date, None] = None):
        """
        Initializes a Transaction instance.
        
        :param amount: The amount of the transaction.
        :param transaction_type: The type of transaction ('income' or 'expense').
        :param date: The date of the transaction, defaults to today if None.
        """
        if transaction_type not in ['income', 'expense']:
            raise ValueError("Transaction type must be 'income' or 'expense'.")
            
        self.amount = amount
        self.transaction_type = transaction_type
        self.date = date if date else datetime.date.today()


class Bookkeeping:
    """Manages a collection of transactions and calculates profitability and wealth growth."""
    
    def __init__(self):
        """Initializes the bookkeeping with an empty list of transactions."""
        self.transactions: List[Transaction] = []

    def add_transaction(self, transaction: Transaction):
        """Adds a transaction to the bookkeeping system.
        
        :param transaction: Transaction object to be added.
        """
        self.transactions.append(transaction)

    def calculate_profitability(self) -> float:
        """Calculates the total profitability from income and expenses.
        
        :return: The calculated profitability.
        """
        total_income = sum(t.amount for t in self.transactions if t.transaction_type == 'income')
        total_expense = sum(t.amount for t in self.transactions if t.transaction_type == 'expense')
        return total_income - total_expense

    def calculate_wealth_growth(self) -> float:
        """Calculates the overall wealth growth based on transactions.
        
        :return: The calculated wealth growth.
        """
        current_wealth = self.calculate_profitability()
        return current_wealth  # For a sole proprietor, wealth growth can equate to profitability.

    def get_transaction_history(self) -> List[Dict[str, Union[float, str]]]:
        """Retrieves the transaction history as a list of dictionaries.
        
        :return: A list of dictionaries containing transaction details.
        """
        return [{
            'amount': t.amount,
            'transaction_type': t.transaction_type,
            'date': t.date.isoformat()
        } for t in self.transactions]

# Example usage
if __name__ == "__main__":
    bookkeeping = Bookkeeping()

    # Adding sample transactions
    try:
        bookkeeping.add_transaction(Transaction(1500.00, 'income'))
        bookkeeping.add_transaction(Transaction(500.00, 'expense'))
        bookkeeping.add_transaction(Transaction(200.00, 'expense'))

        # Calculate profitability and wealth growth
        profitability = bookkeeping.calculate_profitability()
        wealth_growth = bookkeeping.calculate_wealth_growth()

        print(f"Total Profitability: ${profitability:.2f}")
        print(f"Total Wealth Growth: ${wealth_growth:.2f}")

        # Display transaction history
        print("Transaction History:")
        for record in bookkeeping.get_transaction_history():
            print(record)

    except Exception as e:
        print(f"An error occurred: {e}")
```
