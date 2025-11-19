"""
Generated Code Metadata:
========================
Original URL: https://panchsheelbank.com
Prompt: Write code to generate eStatements for savings accounts, referencing the banking services offered by Panchsheel Mercantile Co-op. Bank Ltd.
Generated: DETERMINISTIC_0640837a58c0c11b
Batch ID: 20250612_150615
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# eStatement Generator for Savings Accounts
# Panchsheel Mercantile Co-op. Bank Ltd.

import datetime
from dataclasses import dataclass
from enum import Enum
from typing import List

class TransactionType(Enum):
    """Transaction types for savings account"""
    DEPOSIT = 1
    WITHDRAWAL = 2
    TRANSFER = 3

@dataclass
class Transaction:
    """Represents a transaction in the savings account"""
    date: datetime.date
    type: TransactionType
    amount: float
    description: str

@dataclass
class SavingsAccount:
    """Represents a savings account"""
    account_number: str
    account_holder: str
    balance: float
    transactions: List[Transaction]

class eStatementGenerator:
    """Generates eStatements for savings accounts"""
    def __init__(self, account: SavingsAccount):
        self.account = account

    def generate_statement(self, start_date: datetime.date, end_date: datetime.date) -> str:
        """Generates eStatement for the given date range"""
        try:
            # Filter transactions by date range
            transactions = [t for t in self.account.transactions if start_date <= t.date <= end_date]

            # Calculate statement balance
            statement_balance = self.account.balance
            for t in transactions:
                if t.type == TransactionType.DEPOSIT:
                    statement_balance += t.amount
                elif t.type == TransactionType.WITHDRAWAL:
                    statement_balance -= t.amount
                elif t.type == TransactionType.TRANSFER:
                    statement_balance -= t.amount

            # Generate eStatement
            eStatement = f"eStatement for Savings Account {self.account.account_number}\n"
            eStatement += f"Account Holder: {self.account.account_holder}\n"
            eStatement += f"Date Range: {start_date} to {end_date}\n"
            eStatement += f"Initial Balance: {self.account.balance:.2f}\n"
            eStatement += "Transactions:\n"
            for t in transactions:
                eStatement += f"{t.date}: {t.type.name} - {t.amount:.2f} ({t.description})\n"
            eStatement += f"Statement Balance: {statement_balance:.2f}\n"

            return eStatement
        except Exception as e:
            # Handle any exceptions during eStatement generation
            return f"Error generating eStatement: {str(e)}"

# Example usage
if __name__ == "__main__":
    # Create savings account with transactions
    account = SavingsAccount(
        account_number="SAV12345",
        account_holder="John Doe",
        balance=1000.0,
        transactions=[
            Transaction(datetime.date(2022, 1, 1), TransactionType.DEPOSIT, 500.0, "Payroll deposit"),
            Transaction(datetime.date(2022, 1, 15), TransactionType.WITHDRAWAL, 200.0, "ATM withdrawal"),
            Transaction(datetime.date(2022, 2, 1), TransactionType.TRANSFER, 300.0, "Transfer to checking")
        ]
    )

    # Generate eStatement
    generator = eStatementGenerator(account)
    start_date = datetime.date(2022, 1, 1)
    end_date = datetime.date(2022, 1, 31)
    eStatement = generator.generate_statement(start_date, end_date)
    print(eStatement)
```
