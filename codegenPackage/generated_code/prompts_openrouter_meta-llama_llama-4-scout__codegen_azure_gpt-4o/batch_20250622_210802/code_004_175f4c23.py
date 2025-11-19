"""
Generated Code Metadata:
========================
Original URL: https://lkinc.co.za
Prompt: Generate a sample financial plan for a business, incorporating Lund & Kieck's financial planning services and expertise in South African financial regulations.
Generated: DETERMINISTIC_175f4c237313a6df
Batch ID: 20250622_210802
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime

class FinancialPlan:
    """
    A class to represent a financial plan for a business.
    Incorporates Lund & Kieck's financial planning services and expertise in South African financial regulations.
    """

    def __init__(self, business_name, start_date, end_date, initial_budget):
        """
        Initialize the financial plan.

        :param business_name: Name of the business
        :param start_date: Start date of the financial plan (YYYY-MM-DD)
        :param end_date: End date of the financial plan (YYYY-MM-DD)
        :param initial_budget: Initial budget allocated for the plan
        """
        self.business_name = business_name
        self.start_date = self._validate_date(start_date)
        self.end_date = self._validate_date(end_date)
        self.initial_budget = initial_budget
        self.expenses = []
        self.revenue_sources = []

    def _validate_date(self, date_str):
        """
        Validate and parse a date string.

        :param date_str: Date string in the format YYYY-MM-DD
        :return: Parsed datetime.date object
        :raises ValueError: If the date format is invalid
        """
        try:
            return datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError(f"Invalid date format: {date_str}. Expected format: YYYY-MM-DD")

    def add_expense(self, description, amount):
        """
        Add an expense to the financial plan.

        :param description: Description of the expense
        :param amount: Amount of the expense
        :raises ValueError: If the amount is negative
        """
        if amount < 0:
            raise ValueError("Expense amount cannot be negative.")
        self.expenses.append({"description": description, "amount": amount})

    def add_revenue_source(self, description, amount):
        """
        Add a revenue source to the financial plan.

        :param description: Description of the revenue source
        :param amount: Amount of the revenue
        :raises ValueError: If the amount is negative
        """
        if amount < 0:
            raise ValueError("Revenue amount cannot be negative.")
        self.revenue_sources.append({"description": description, "amount": amount})

    def calculate_net_budget(self):
        """
        Calculate the net budget after accounting for expenses and revenue.

        :return: Net budget
        """
        total_expenses = sum(expense["amount"] for expense in self.expenses)
        total_revenue = sum(revenue["amount"] for revenue in self.revenue_sources)
        return self.initial_budget + total_revenue - total_expenses

    def generate_report(self):
        """
        Generate a financial report summarizing the plan.

        :return: A string containing the financial report
        """
        report = f"Financial Plan Report for {self.business_name}\n"
        report += f"Plan Duration: {self.start_date} to {self.end_date}\n"
        report += f"Initial Budget: R{self.initial_budget:.2f}\n\n"

        report += "Expenses:\n"
        for expense in self.expenses:
            report += f"  - {expense['description']}: R{expense['amount']:.2f}\n"
        report += f"Total Expenses: R{sum(expense['amount'] for expense in self.expenses):.2f}\n\n"

        report += "Revenue Sources:\n"
        for revenue in self.revenue_sources:
            report += f"  - {revenue['description']}: R{revenue['amount']:.2f}\n"
        report += f"Total Revenue: R{sum(revenue['amount'] for revenue in self.revenue_sources):.2f}\n\n"

        report += f"Net Budget: R{self.calculate_net_budget():.2f}\n"
        return report


# Example usage
if __name__ == "__main__":
    try:
        # Create a financial plan
        plan = FinancialPlan(
            business_name="ABC Enterprises",
            start_date="2023-01-01",
            end_date="2023-12-31",
            initial_budget=500000.00
        )

        # Add expenses
        plan.add_expense("Office Rent", 120000.00)
        plan.add_expense("Utilities", 30000.00)
        plan.add_expense("Employee Salaries", 250000.00)

        # Add revenue sources
        plan.add_revenue_source("Product Sales", 400000.00)
        plan.add_revenue_source("Service Contracts", 150000.00)

        # Generate and print the financial report
        print(plan.generate_report())

    except Exception as e:
        print(f"Error: {e}")
```
