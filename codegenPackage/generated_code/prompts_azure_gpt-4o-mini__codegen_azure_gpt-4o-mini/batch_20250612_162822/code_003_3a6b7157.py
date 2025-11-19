"""
Generated Code Metadata:
========================
Original URL: https://reckonmexico.com
Prompt: Develop a library function that automates the preparation of financial statements, reflecting the accounting optimization services provided by Reckon Business Consulting.
Generated: DETERMINISTIC_3a6b7157b86a4355
Batch ID: 20250612_162822
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
from typing import List, Dict

class FinancialStatementGenerator:
    """
    A class to automate the preparation of financial statements.
    This class reflects the accounting optimization services provided by Reckon Business Consulting.
    """

    def __init__(self, transactions: List[Dict[str, float]]):
        """
        Initializes the FinancialStatementGenerator with a list of transactions.

        :param transactions: A list of dictionaries containing transaction data.
        """
        self.transactions = transactions
        self.df = pd.DataFrame(transactions)

    def validate_transactions(self):
        """
        Validates the transaction data to ensure it contains the necessary fields.
        Raises ValueError if validation fails.
        """
        required_fields = {'date', 'description', 'amount', 'type'}
        if not all(field in self.df.columns for field in required_fields):
            raise ValueError("Transactions must contain 'date', 'description', 'amount', and 'type' fields.")

    def generate_income_statement(self) -> pd.DataFrame:
        """
        Generates an income statement from the transactions.

        :return: A DataFrame representing the income statement.
        """
        self.validate_transactions()
        
        # Filter income and expenses
        income = self.df[self.df['type'] == 'income']
        expenses = self.df[self.df['type'] == 'expense']

        # Calculate total income and total expenses
        total_income = income['amount'].sum()
        total_expenses = expenses['amount'].sum()
        net_income = total_income - total_expenses

        # Create income statement DataFrame
        income_statement = pd.DataFrame({
            'Description': ['Total Income', 'Total Expenses', 'Net Income'],
            'Amount': [total_income, total_expenses, net_income]
        })

        return income_statement

    def generate_balance_sheet(self) -> pd.DataFrame:
        """
        Generates a balance sheet from the transactions.

        :return: A DataFrame representing the balance sheet.
        """
        self.validate_transactions()

        # Assuming assets and liabilities are categorized in the 'type' field
        assets = self.df[self.df['type'] == 'asset']
        liabilities = self.df[self.df['type'] == 'liability']

        # Calculate total assets and total liabilities
        total_assets = assets['amount'].sum()
        total_liabilities = liabilities['amount'].sum()
        equity = total_assets - total_liabilities

        # Create balance sheet DataFrame
        balance_sheet = pd.DataFrame({
            'Description': ['Total Assets', 'Total Liabilities', 'Equity'],
            'Amount': [total_assets, total_liabilities, equity]
        })

        return balance_sheet

# Example usage:
if __name__ == "__main__":
    # Sample transaction data
    transactions = [
        {'date': '2023-01-01', 'description': 'Sale of goods', 'amount': 1000.0, 'type': 'income'},
        {'date': '2023-01-02', 'description': 'Purchase of materials', 'amount': 300.0, 'type': 'expense'},
        {'date': '2023-01-03', 'description': 'Office Supplies', 'amount': 150.0, 'type': 'expense'},
        {'date': '2023-01-04', 'description': 'Cash', 'amount': 500.0, 'type': 'asset'},
        {'date': '2023-01-05', 'description': 'Loan', 'amount': 200.0, 'type': 'liability'},
    ]

    # Create an instance of the FinancialStatementGenerator
    generator = FinancialStatementGenerator(transactions)

    # Generate and print financial statements
    try:
        income_statement = generator.generate_income_statement()
        print("Income Statement:")
        print(income_statement)

        balance_sheet = generator.generate_balance_sheet()
        print("\nBalance Sheet:")
        print(balance_sheet)
    except ValueError as e:
        print(f"Error: {e}")
```
