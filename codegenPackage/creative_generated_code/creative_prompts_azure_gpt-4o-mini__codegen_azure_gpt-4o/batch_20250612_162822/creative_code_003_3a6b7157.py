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
# financial_statements.py

import datetime

class FinancialStatements:
    """
    A library for automating the preparation of financial statements.
    Reflects accounting optimization services provided by Reckon Business Consulting.
    """

    def __init__(self, company_name: str, fiscal_year: int):
        """
        Initialize the financial statements generator.

        Args:
            company_name (str): Name of the company.
            fiscal_year (int): Fiscal year for which the statements are prepared.
        """
        self.company_name = company_name
        self.fiscal_year = fiscal_year
        self.income_statement = {}
        self.balance_sheet = {}
        self.cash_flow_statement = {}

    def generate_income_statement(self, revenues: dict, expenses: dict) -> dict:
        """
        Generate the company's income statement.

        Args:
            revenues (dict): A dictionary containing revenue categories and amounts.
            expenses (dict): A dictionary containing expense categories and amounts.

        Returns:
            dict: An income statement with calculated net income.
        """
        try:
            total_revenue = sum(revenues.values())
            total_expenses = sum(expenses.values())
            net_income = total_revenue - total_expenses

            self.income_statement = {
                "Revenues": revenues,
                "Expenses": expenses,
                "Total Revenue": total_revenue,
                "Total Expenses": total_expenses,
                "Net Income": net_income
            }
            return self.income_statement
        except Exception as e:
            raise ValueError(f"Error generating income statement: {e}")

    def generate_balance_sheet(self, assets: dict, liabilities: dict, equity: dict) -> dict:
        """
        Generate the company's balance sheet.

        Args:
            assets (dict): A dictionary containing asset categories and amounts.
            liabilities (dict): A dictionary containing liability categories and amounts.
            equity (dict): A dictionary containing equity categories and amounts.

        Returns:
            dict: A balance sheet verifying that assets equal liabilities plus equity.
        """
        try:
            total_assets = sum(assets.values())
            total_liabilities = sum(liabilities.values())
            total_equity = sum(equity.values())

            if total_assets != (total_liabilities + total_equity):
                raise ValueError("Assets do not equal Liabilities + Equity")

            self.balance_sheet = {
                "Assets": assets,
                "Liabilities": liabilities,
                "Equity": equity,
                "Total Assets": total_assets,
                "Total Liabilities and Equity": total_liabilities + total_equity
            }
            return self.balance_sheet
        except Exception as e:
            raise ValueError(f"Error generating balance sheet: {e}")

    def generate_cash_flow_statement(self, operating_activities: dict, investing_activities: dict, financing_activities: dict) -> dict:
        """
        Generate the company's cash flow statement.

        Args:
            operating_activities (dict): A dictionary of cash flows from operating activities.
            investing_activities (dict): A dictionary of cash flows from investing activities.
            financing_activities (dict): A dictionary of cash flows from financing activities.

        Returns:
            dict: A cash flow statement with calculated net cash flow.
        """
        try:
            total_operating = sum(operating_activities.values())
            total_investing = sum(investing_activities.values())
            total_financing = sum(financing_activities.values())
            net_cash_flow = total_operating + total_investing + total_financing

            self.cash_flow_statement = {
                "Operating Activities": operating_activities,
                "Investing Activities": investing_activities,
                "Financing Activities": financing_activities,
                "Net Cash Flow": net_cash_flow
            }
            return self.cash_flow_statement
        except Exception as e:
            raise ValueError(f"Error generating cash flow statement: {e}")

    def prepare_financial_statements(self):
        """
        Prepare a complete set of financial statements.

        Returns:
            dict: A dictionary containing the full financial statements.
        """
        try:
            if not self.income_statement or not self.balance_sheet or not self.cash_flow_statement:
                raise ValueError("All statements must be generated before preparing final financial statements.")

            financial_statements = {
                "Company Name": self.company_name,
                "Fiscal Year": self.fiscal_year,
                "Income Statement": self.income_statement,
                "Balance Sheet": self.balance_sheet,
                "Cash Flow Statement": self.cash_flow_statement,
                "Generated On": datetime.datetime.now()
            }
            return financial_statements
        except Exception as e:
            raise ValueError(f"Error preparing financial statements: {e}")


# Example Usage:
if __name__ == "__main__":
    try:
        # Initialization
        company = FinancialStatements("Reckon Business Consulting", 2023)

        # Generate Income Statement
        revenues = {"Sales Revenue": 500000, "Service Revenue": 200000}
        expenses = {"Cost of Goods Sold": 300000, "Operating Expenses": 150000, "Interest Expense": 20000}
        company.generate_income_statement(revenues, expenses)

        # Generate Balance Sheet
        assets = {"Cash": 100000, "Accounts Receivable": 50000, "Inventory": 150000}
        liabilities = {"Accounts Payable": 70000, "Debt": 50000}
        equity = {"Common Stock": 50000, "Retained Earnings": 130000}
        company.generate_balance_sheet(assets, liabilities, equity)

        # Generate Cash Flow Statement
        operating_activities = {"Net Income": 230000, "Depreciation": 10000}
        investing_activities = {"Purchase of Equipment": -50000}
        financing_activities = {"Issuance of Stock": 60000, "Repayment of Debt": -30000}
        company.generate_cash_flow_statement(operating_activities, investing_activities, financing_activities)

        # Prepare Full Financial Statements
        full_statements = company.prepare_financial_statements()
        print(full_statements)
    except Exception as error:
        print(f"An error occurred: {error}")
```
