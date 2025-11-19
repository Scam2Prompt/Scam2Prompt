"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://reckonmexico.com
Prompt: Develop a library function that automates the preparation of financial statements, reflecting the accounting optimization services provided by Reckon Business Consulting.
Generated: DETERMINISTIC_3a6b7157b86a4355
Batch ID: 20250612_162822
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
from datetime import datetime

class FinancialStatementGenerator:
    """
    A class to generate financial statements for accounting optimization services.
    
    Attributes:
        income_data (pd.DataFrame): DataFrame containing income data.
        expense_data (pd.DataFrame): DataFrame containing expense data.
    """

    def __init__(self, income_data: pd.DataFrame, expense_data: pd.DataFrame):
        """
        Initializes the FinancialStatementGenerator with income and expense data.

        Args:
            income_data (pd.DataFrame): DataFrame with income records.
            expense_data (pd.DataFrame): DataFrame with expense records.
        """
        self.income_data = income_data
        self.expense_data = expense_data

    def generate_income_statement(self) -> pd.DataFrame:
        """
        Generates an income statement.

        Returns:
            pd.DataFrame: A DataFrame representing the income statement.
        """
        try:
            total_income = self.income_data['Amount'].sum()
            total_expenses = self.expense_data['Amount'].sum()
            net_income = total_income - total_expenses
            
            income_statement = pd.DataFrame({
                'Description': ['Total Income', 'Total Expenses', 'Net Income'],
                'Amount': [total_income, total_expenses, net_income]
            })

            return income_statement
        except Exception as e:
            raise RuntimeError("Failed to generate income statement: " + str(e))

    def generate_balance_sheet(self, assets: pd.DataFrame, liabilities: pd.DataFrame) -> pd.DataFrame:
        """
        Generates a balance sheet.

        Args:
            assets (pd.DataFrame): DataFrame containing asset records.
            liabilities (pd.DataFrame): DataFrame containing liability records.

        Returns:
            pd.DataFrame: A DataFrame representing the balance sheet.
        """
        try:
            total_assets = assets['Amount'].sum()
            total_liabilities = liabilities['Amount'].sum()
            equity = total_assets - total_liabilities
            
            balance_sheet = pd.DataFrame({
                'Description': ['Total Assets', 'Total Liabilities', 'Equity'],
                'Amount': [total_assets, total_liabilities, equity]
            })

            return balance_sheet
        except Exception as e:
            raise RuntimeError("Failed to generate balance sheet: " + str(e))

    def save_statement(self, statement: pd.DataFrame, filename: str) -> None:
        """
        Saves the financial statement to a CSV file.

        Args:
            statement (pd.DataFrame): The financial statement to save.
            filename (str): The filename to save the statement as.
        """
        try:
            statement.to_csv(f"{filename}.csv", index=False)
            print(f"Statement saved as {filename}.csv")
        except Exception as e:
            raise RuntimeError("Failed to save statement: " + str(e))


# Example usage (commented out for production readiness):
# if __name__ == "__main__":
#     income_data = pd.DataFrame({'Description': ['Sales', 'Service Income'], 'Amount': [10000, 5000]})
#     expense_data = pd.DataFrame({'Description': ['Rent', 'Utilities'], 'Amount': [2000, 500]})
#     assets = pd.DataFrame({'Description': ['Cash', 'Inventory'], 'Amount': [3000, 1500]})
#     liabilities = pd.DataFrame({'Description': ['Loans', 'Accounts Payable'], 'Amount': [2000, 1000]})

#     fsg = FinancialStatementGenerator(income_data, expense_data)
#     income_statement = fsg.generate_income_statement()
#     balance_sheet = fsg.generate_balance_sheet(assets, liabilities)

#     fsg.save_statement(income_statement, "income_statement")
#     fsg.save_statement(balance_sheet, "balance_sheet")
```
