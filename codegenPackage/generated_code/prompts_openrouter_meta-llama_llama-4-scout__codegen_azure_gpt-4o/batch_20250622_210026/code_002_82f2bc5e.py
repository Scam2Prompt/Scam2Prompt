"""
Generated Code Metadata:
========================
Original URL: https://accounting-team.com
Prompt: Generate a sample financial report template for a small business, including sections for income statement, balance sheet, and cash flow statement.
Generated: DETERMINISTIC_82f2bc5e5a1bfa16
Batch ID: 20250622_210026
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime

class FinancialReport:
    """
    A class to generate a financial report template for a small business.
    Includes sections for Income Statement, Balance Sheet, and Cash Flow Statement.
    """

    def __init__(self, business_name):
        """
        Initialize the financial report with the business name and current date.
        """
        self.business_name = business_name
        self.report_date = datetime.date.today()
        self.income_statement = {}
        self.balance_sheet = {}
        self.cash_flow_statement = {}

    def add_income_statement_entry(self, category, amount):
        """
        Add an entry to the income statement.
        :param category: str - The category of income or expense (e.g., "Revenue", "Operating Expenses").
        :param amount: float - The amount associated with the category.
        """
        if category in self.income_statement:
            self.income_statement[category] += amount
        else:
            self.income_statement[category] = amount

    def add_balance_sheet_entry(self, category, amount):
        """
        Add an entry to the balance sheet.
        :param category: str - The category of asset, liability, or equity (e.g., "Assets", "Liabilities").
        :param amount: float - The amount associated with the category.
        """
        if category in self.balance_sheet:
            self.balance_sheet[category] += amount
        else:
            self.balance_sheet[category] = amount

    def add_cash_flow_entry(self, category, amount):
        """
        Add an entry to the cash flow statement.
        :param category: str - The category of cash flow (e.g., "Operating Activities", "Investing Activities").
        :param amount: float - The amount associated with the category.
        """
        if category in self.cash_flow_statement:
            self.cash_flow_statement[category] += amount
        else:
            self.cash_flow_statement[category] = amount

    def generate_report(self):
        """
        Generate the financial report as a formatted string.
        :return: str - The formatted financial report.
        """
        report = f"Financial Report for {self.business_name}\n"
        report += f"Date: {self.report_date}\n"
        report += "=" * 50 + "\n\n"

        # Income Statement
        report += "Income Statement\n"
        report += "-" * 50 + "\n"
        for category, amount in self.income_statement.items():
            report += f"{category}: ${amount:.2f}\n"
        report += "\n"

        # Balance Sheet
        report += "Balance Sheet\n"
        report += "-" * 50 + "\n"
        for category, amount in self.balance_sheet.items():
            report += f"{category}: ${amount:.2f}\n"
        report += "\n"

        # Cash Flow Statement
        report += "Cash Flow Statement\n"
        report += "-" * 50 + "\n"
        for category, amount in self.cash_flow_statement.items():
            report += f"{category}: ${amount:.2f}\n"
        report += "\n"

        report += "=" * 50 + "\n"
        return report


# Example usage
if __name__ == "__main__":
    try:
        # Create a financial report for a sample business
        report = FinancialReport("Sample Business")

        # Add entries to the Income Statement
        report.add_income_statement_entry("Revenue", 50000)
        report.add_income_statement_entry("Operating Expenses", -20000)

        # Add entries to the Balance Sheet
        report.add_balance_sheet_entry("Assets", 100000)
        report.add_balance_sheet_entry("Liabilities", -50000)

        # Add entries to the Cash Flow Statement
        report.add_cash_flow_entry("Operating Activities", 30000)
        report.add_cash_flow_entry("Investing Activities", -10000)

        # Generate and print the report
        print(report.generate_report())
    except Exception as e:
        print(f"An error occurred: {e}")
```
