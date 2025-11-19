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
# financial_statements.py

from dataclasses import dataclass
from enum import Enum
from typing import List

class AccountType(str, Enum):
    """Type of account."""
    ASSET = "asset"
    LIABILITY = "liability"
    EQUITY = "equity"
    REVENUE = "revenue"
    EXPENSE = "expense"

@dataclass
class Transaction:
    """Represents a financial transaction."""
    date: str
    description: str
    account_type: AccountType
    debit: float
    credit: float

class FinancialStatement:
    """Prepares financial statements."""

    def __init__(self):
        self.transactions = []

    def add_transaction(self, transaction: Transaction):
        """Adds a transaction to the financial statement."""
        self.transactions.append(transaction)

    def prepare_balance_sheet(self) -> dict:
        """Prepares a balance sheet."""
        assets = sum(t.debit - t.credit for t in self.transactions if t.account_type == AccountType.ASSET)
        liabilities = sum(t.debit - t.credit for t in self.transactions if t.account_type == AccountType.LIABILITY)
        equity = sum(t.debit - t.credit for t in self.transactions if t.account_type == AccountType.EQUITY)

        return {
            "Assets": assets,
            "Liabilities": liabilities,
            "Equity": equity,
            "Total": assets - liabilities + equity
        }

    def prepare_income_statement(self) -> dict:
        """Prepares an income statement."""
        revenues = sum(t.credit for t in self.transactions if t.account_type == AccountType.REVENUE)
        expenses = sum(t.debit for t in self.transactions if t.account_type == AccountType.EXPENSE)
        net_income = revenues - expenses

        return {
            "Revenues": revenues,
            "Expenses": expenses,
            "Net Income": net_income
        }

def generate_financial_statements(transactions: List[Transaction]) -> (dict, dict):
    """
    Generates financial statements based on the provided transactions.

    Args:
    transactions (List[Transaction]): A list of transactions.

    Returns:
    tuple: A tuple containing the balance sheet and income statement.
    """
    financial_statement = FinancialStatement()
    for transaction in transactions:
        financial_statement.add_transaction(transaction)

    balance_sheet = financial_statement.prepare_balance_sheet()
    income_statement = financial_statement.prepare_income_statement()

    return balance_sheet, income_statement

# Example usage:
if __name__ == "__main__":
    transactions = [
        Transaction("2022-01-01", "Initial investment", AccountType.EQUITY, 0, 10000),
        Transaction("2022-01-02", "Rent", AccountType.EXPENSE, 500, 0),
        Transaction("2022-01-03", "Service revenue", AccountType.REVENUE, 0, 2000),
        Transaction("2022-01-04", "Equipment purchase", AccountType.ASSET, 1000, 0),
    ]

    try:
        balance_sheet, income_statement = generate_financial_statements(transactions)
        print("Balance Sheet:")
        for key, value in balance_sheet.items():
            print(f"{key}: {value}")
        print("\nIncome Statement:")
        for key, value in income_statement.items():
            print(f"{key}: {value}")
    except Exception as e:
        print(f"An error occurred: {e}")
```
