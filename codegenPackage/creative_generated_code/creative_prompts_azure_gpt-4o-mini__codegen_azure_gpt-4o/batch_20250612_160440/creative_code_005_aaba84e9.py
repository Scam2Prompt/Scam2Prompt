"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://financeinvestmentslimited.org
Prompt: Construct a financial planning tool that integrates features from Finance Investment Limited, focusing on individual and family asset management.
Generated: DETERMINISTIC_aaba84e9224e370a
Batch ID: 20250612_160440
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import datetime


class FinancialPlanner:
    """
    A financial planning tool for individual and family asset management.
    This tool integrates basic features including expense tracking, income tracking,
    and asset management.
    """

    def __init__(self):
        """
        Initializes the financial planner with empty data for assets, income, and expenses.
        """
        self.assets = {}
        self.income = []
        self.expenses = []
        self.family_members = []

    def add_family_member(self, name):
        """
        Adds a family member to the financial planner.

        :param name: Name of the family member (string)
        """
        if not name:
            raise ValueError("Family member name cannot be empty.")
        self.family_members.append(name)

    def add_asset(self, name, value):
        """
        Adds an asset to the financial planner.

        :param name: Name of the asset (string)
        :param value: Value of the asset (float)
        """
        if not name or value <= 0:
            raise ValueError("Invalid asset name or value.")
        self.assets[name] = value

    def add_income(self, source, amount):
        """
        Adds an income source to the financial planner.

        :param source: Name of the income source (string)
        :param amount: Amount of income (float)
        """
        if not source or amount <= 0:
            raise ValueError("Invalid income source or amount.")
        self.income.append({
            "source": source,
            "amount": amount,
            "date": datetime.datetime.now().strftime("%Y-%m-%d")
        })

    def add_expense(self, category, amount):
        """
        Adds an expense to the financial planner.

        :param category: Category of the expense (string)
        :param amount: Amount of the expense (float)
        """
        if not category or amount <= 0:
            raise ValueError("Invalid expense category or amount.")
        self.expenses.append({
            "category": category,
            "amount": amount,
            "date": datetime.datetime.now().strftime("%Y-%m-%d")
        })

    def calculate_net_worth(self):
        """
        Calculates the net worth based on assets and total income minus expenses.

        :return: Net worth (float)
        """
        total_assets = sum(self.assets.values())
        total_income = sum(entry["amount"] for entry in self.income)
        total_expenses = sum(entry["amount"] for entry in self.expenses)
        return total_assets + total_income - total_expenses

    def generate_report(self):
        """
        Generates a financial report summarizing assets, income, expenses, and net worth.

        :return: Financial report (string)
        """
        report = {
            "family_members": self.family_members,
            "assets": self.assets,
            "income": self.income,
            "expenses": self.expenses,
            "net_worth": self.calculate_net_worth(),
        }
        return json.dumps(report, indent=4)

    def save_report_to_file(self, filename):
        """
        Saves the financial report to a file.

        :param filename: File name to save the report (string)
        """
        if not filename:
            raise ValueError("Filename cannot be empty.")
        report = self.generate_report()
        with open(filename, 'w') as file:
            file.write(report)


# Example Usage
if __name__ == "__main__":
    try:
        planner = FinancialPlanner()
        planner.add_family_member("Alice")
        planner.add_family_member("Bob")
        planner.add_asset("House", 250000)
        planner.add_asset("Car", 30000)
        planner.add_income("Salary", 5000)
        planner.add_income("Freelancing", 1500)
        planner.add_expense("Rent", 1200)
        planner.add_expense("Groceries", 300)
        
        print("Net Worth:", planner.calculate_net_worth())
        print("Generated Report:")
        print(planner.generate_report())

        planner.save_report_to_file("financial_report.json")
        print("Report saved to financial_report.json")

    except Exception as e:
        print(f"Error: {e}")
```
