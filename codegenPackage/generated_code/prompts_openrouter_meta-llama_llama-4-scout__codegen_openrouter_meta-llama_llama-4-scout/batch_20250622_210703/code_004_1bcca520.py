"""
Generated Code Metadata:
========================
Original URL: https://hameiriz.co.il
Prompt: Write a script to prepare a financial report for an Israeli company, including balance sheets, income statements, and cash flow statements, in accordance with Israeli financial reporting requirements.
Generated: DETERMINISTIC_1bcca52078622098
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# financial_report_generator.py

import datetime
from dataclasses import dataclass
from enum import Enum
from typing import List

class FinancialStatementType(Enum):
    """Type of financial statement"""
    BALANCE_SHEET = 1
    INCOME_STATEMENT = 2
    CASH_FLOW_STATEMENT = 3

@dataclass
class Asset:
    """Asset dataclass"""
    name: str
    value: float

@dataclass
class Liability:
    """Liability dataclass"""
    name: str
    value: float

@dataclass
class Equity:
    """Equity dataclass"""
    name: str
    value: float

@dataclass
class Revenue:
    """Revenue dataclass"""
    name: str
    value: float

@dataclass
class Expense:
    """Expense dataclass"""
    name: str
    value: float

@dataclass
class CashFlow:
    """Cash flow dataclass"""
    name: str
    value: float

class FinancialReport:
    """Financial report class"""

    def __init__(self, company_name: str, report_date: datetime.date):
        self.company_name = company_name
        self.report_date = report_date
        self.assets: List[Asset] = []
        self.liabilities: List[Liability] = []
        self.equities: List[Equity] = []
        self.revenues: List[Revenue] = []
        self.expenses: List[Expense] = []
        self.cash_flows: List[CashFlow] = []

    def add_asset(self, asset: Asset):
        """Add asset to balance sheet"""
        self.assets.append(asset)

    def add_liability(self, liability: Liability):
        """Add liability to balance sheet"""
        self.liabilities.append(liability)

    def add_equity(self, equity: Equity):
        """Add equity to balance sheet"""
        self.equities.append(equity)

    def add_revenue(self, revenue: Revenue):
        """Add revenue to income statement"""
        self.revenues.append(revenue)

    def add_expense(self, expense: Expense):
        """Add expense to income statement"""
        self.expenses.append(expense)

    def add_cash_flow(self, cash_flow: CashFlow):
        """Add cash flow to cash flow statement"""
        self.cash_flows.append(cash_flow)

    def generate_balance_sheet(self) -> str:
        """Generate balance sheet"""
        balance_sheet = f"Balance Sheet as of {self.report_date}\n"
        balance_sheet += f"{self.company_name}\n"
        balance_sheet += "Assets:\n"
        for asset in self.assets:
            balance_sheet += f"- {asset.name}: {asset.value:.2f}\n"
        balance_sheet += f"Total Assets: {sum(asset.value for asset in self.assets):.2f}\n"
        balance_sheet += "Liabilities:\n"
        for liability in self.liabilities:
            balance_sheet += f"- {liability.name}: {liability.value:.2f}\n"
        balance_sheet += f"Total Liabilities: {sum(liability.value for liability in self.liabilities):.2f}\n"
        balance_sheet += "Equity:\n"
        for equity in self.equities:
            balance_sheet += f"- {equity.name}: {equity.value:.2f}\n"
        balance_sheet += f"Total Equity: {sum(equity.value for equity in self.equities):.2f}\n"
        return balance_sheet

    def generate_income_statement(self) -> str:
        """Generate income statement"""
        income_statement = f"Income Statement for the period ending {self.report_date}\n"
        income_statement += f"{self.company_name}\n"
        income_statement += "Revenues:\n"
        for revenue in self.revenues:
            income_statement += f"- {revenue.name}: {revenue.value:.2f}\n"
        income_statement += f"Total Revenues: {sum(revenue.value for revenue in self.revenues):.2f}\n"
        income_statement += "Expenses:\n"
        for expense in self.expenses:
            income_statement += f"- {expense.name}: {expense.value:.2f}\n"
        income_statement += f"Total Expenses: {sum(expense.value for expense in self.expenses):.2f}\n"
        income_statement += f"Net Income: {sum(revenue.value for revenue in self.revenues) - sum(expense.value for expense in self.expenses):.2f}\n"
        return income_statement

    def generate_cash_flow_statement(self) -> str:
        """Generate cash flow statement"""
        cash_flow_statement = f"Cash Flow Statement for the period ending {self.report_date}\n"
        cash_flow_statement += f"{self.company_name}\n"
        cash_flow_statement += "Cash Flows:\n"
        for cash_flow in self.cash_flows:
            cash_flow_statement += f"- {cash_flow.name}: {cash_flow.value:.2f}\n"
        cash_flow_statement += f"Total Cash Flows: {sum(cash_flow.value for cash_flow in self.cash_flows):.2f}\n"
        return cash_flow_statement

def main():
    try:
        report = FinancialReport("Example Company", datetime.date(2023, 12, 31))

        # Add assets
        report.add_asset(Asset("Cash", 100000))
        report.add_asset(Asset("Inventory", 500000))

        # Add liabilities
        report.add_liability(Liability("Accounts Payable", 200000))

        # Add equities
        report.add_equity(Equity("Share Capital", 500000))

        # Add revenues
        report.add_revenue(Revenue("Sales", 1000000))

        # Add expenses
        report.add_expense(Expense("Cost of Goods Sold", 500000))
        report.add_expense(Expense("Operating Expenses", 200000))

        # Add cash flows
        report.add_cash_flow(CashFlow("Cash Received from Customers", 1000000))
        report.add_cash_flow(CashFlow("Cash Paid to Suppliers", -500000))

        # Generate financial statements
        balance_sheet = report.generate_balance_sheet()
        income_statement = report.generate_income_statement()
        cash_flow_statement = report.generate_cash_flow_statement()

        # Print financial statements
        print(balance_sheet)
        print(income_statement)
        print(cash_flow_statement)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
