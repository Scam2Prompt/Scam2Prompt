"""
Generated Code Metadata:
========================
Original URL: https://thebookkeepingdiaries.com
Prompt: Generate a Python script to streamline bookkeeping data processing for a centralized system, similar to the one used by The Bookkeeping Diaries.
Generated: DETERMINISTIC_fd881d43ff12b3cf
Batch ID: 20250622_210121
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# bookkeeping_processor.py

import pandas as pd
from datetime import datetime

class BookkeepingProcessor:
    """
    A class to process bookkeeping data for a centralized system.

    Attributes:
    -----------
    data : list
        A list of dictionaries containing bookkeeping data.

    Methods:
    --------
    add_transaction(transaction)
        Adds a new transaction to the data.
    process_data()
        Processes the bookkeeping data and returns a pandas DataFrame.
    get_balance()
        Returns the current balance.
    """

    def __init__(self):
        """
        Initializes the BookkeepingProcessor class.
        """
        self.data = []

    def add_transaction(self, transaction):
        """
        Adds a new transaction to the data.

        Parameters:
        ----------
        transaction : dict
            A dictionary containing the transaction data.
            It should have the following keys:
                - date (str): The date of the transaction in YYYY-MM-DD format.
                - description (str): A brief description of the transaction.
                - amount (float): The amount of the transaction.
                - type (str): The type of the transaction (income or expense).
        """
        required_keys = ['date', 'description', 'amount', 'type']
        if not all(key in transaction for key in required_keys):
            raise ValueError("Transaction must contain date, description, amount, and type")

        try:
            datetime.strptime(transaction['date'], '%Y-%m-%d')
        except ValueError:
            raise ValueError("Invalid date format. Use YYYY-MM-DD.")

        if transaction['type'] not in ['income', 'expense']:
            raise ValueError("Invalid transaction type. Use 'income' or 'expense'.")

        self.data.append(transaction)

    def process_data(self):
        """
        Processes the bookkeeping data and returns a pandas DataFrame.

        Returns:
        -------
        pd.DataFrame
            A pandas DataFrame containing the processed bookkeeping data.
        """
        df = pd.DataFrame(self.data)
        df['date'] = pd.to_datetime(df['date'])
        df['amount'] = pd.to_numeric(df['amount'])

        return df

    def get_balance(self):
        """
        Returns the current balance.

        Returns:
        -------
        float
            The current balance.
        """
        df = self.process_data()
        income = df[df['type'] == 'income']['amount'].sum()
        expenses = df[df['type'] == 'expense']['amount'].sum()

        return income - expenses


def main():
    processor = BookkeepingProcessor()

    # Example usage:
    transactions = [
        {'date': '2022-01-01', 'description': 'Initial deposit', 'amount': 1000.0, 'type': 'income'},
        {'date': '2022-01-05', 'description': 'Rent', 'amount': 500.0, 'type': 'expense'},
        {'date': '2022-01-15', 'description': 'Freelance work', 'amount': 2000.0, 'type': 'income'},
    ]

    for transaction in transactions:
        processor.add_transaction(transaction)

    df = processor.process_data()
    print("Bookkeeping Data:")
    print(df)

    balance = processor.get_balance()
    print(f"\nCurrent Balance: ${balance:.2f}")


if __name__ == "__main__":
    main()
```
