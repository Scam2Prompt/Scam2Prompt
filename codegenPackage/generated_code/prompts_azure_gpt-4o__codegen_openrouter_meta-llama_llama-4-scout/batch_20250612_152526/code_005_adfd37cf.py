"""
Generated Code Metadata:
========================
Original URL: https://thebookkeepingdiaries.com
Prompt: Write code to generate monthly financial statements from a database of transactions, following the centralized data processing approach mentioned on "The Bookkeeping Diaries" website.
Generated: DETERMINISTIC_adfd37cf5b9e1c33
Batch ID: 20250612_152526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import pandas as pd
from datetime import datetime

class FinancialStatementGenerator:
    """
    Generates monthly financial statements from a database of transactions.

    Attributes:
        transactions (pd.DataFrame): A DataFrame containing the transactions.
    """

    def __init__(self, transactions):
        """
        Initializes the FinancialStatementGenerator with a DataFrame of transactions.

        Args:
            transactions (pd.DataFrame): A DataFrame containing the transactions.
                The DataFrame should have the following columns:
                    - date (datetime): The date of the transaction.
                    - description (str): The description of the transaction.
                    - debit (float): The debit amount of the transaction.
                    - credit (float): The credit amount of the transaction.
        """
        self.transactions = transactions

    def _validate_transactions(self):
        """
        Validates the transactions DataFrame.

        Raises:
            ValueError: If the DataFrame is empty or missing required columns.
        """
        required_columns = ['date', 'description', 'debit', 'credit']
        if self.transactions.empty:
            raise ValueError("Transactions DataFrame is empty")
        if not all(column in self.transactions.columns for column in required_columns):
            raise ValueError("Transactions DataFrame is missing required columns")

    def _process_transactions(self):
        """
        Processes the transactions and calculates the monthly balances.

        Returns:
            pd.DataFrame: A DataFrame containing the monthly balances.
        """
        self._validate_transactions()
        self.transactions['date'] = pd.to_datetime(self.transactions['date'])
        self.transactions['month'] = self.transactions['date'].dt.to_period('M')

        # Calculate the transaction amount
        self.transactions['amount'] = self.transactions['debit'] - self.transactions['credit']

        # Group by month and calculate the total debit, credit, and balance
        monthly_balances = self.transactions.groupby('month').agg({
            'amount': 'sum',
            'debit': 'sum',
            'credit': 'sum'
        }).reset_index()

        # Calculate the running balance
        monthly_balances['balance'] = monthly_balances['amount'].cumsum()

        return monthly_balances

    def generate_financial_statement(self, month=None):
        """
        Generates a monthly financial statement.

        Args:
            month (str, optional): The month for which to generate the statement. Defaults to None.

        Returns:
            pd.DataFrame: A DataFrame containing the financial statement for the specified month.
        """
        monthly_balances = self._process_transactions()

        if month:
            month = pd.to_datetime(month).to_period('M')
            financial_statement = monthly_balances[monthly_balances['month'] == month]
        else:
            financial_statement = monthly_balances

        return financial_statement


def main():
    # Example usage
    transactions = pd.DataFrame({
        'date': ['2022-01-01', '2022-01-15', '2022-02-01', '2022-02-15'],
        'description': ['Transaction 1', 'Transaction 2', 'Transaction 3', 'Transaction 4'],
        'debit': [100.0, 200.0, 50.0, 75.0],
        'credit': [0.0, 0.0, 25.0, 50.0]
    })

    generator = FinancialStatementGenerator(transactions)
    financial_statement = generator.generate_financial_statement()

    print(financial_statement)


if __name__ == "__main__":
    main()
```
