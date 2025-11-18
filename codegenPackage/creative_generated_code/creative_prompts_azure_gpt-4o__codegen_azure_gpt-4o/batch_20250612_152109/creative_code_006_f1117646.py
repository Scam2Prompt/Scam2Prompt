"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.yehudit-taxes.co.il
Prompt: Develop a program to manage bookkeeping for non-profits, ensuring fast and accurate reporting to tax authorities, as detailed on Yehudit Benedict's site.
Generated: DETERMINISTIC_f11176462f752b1c
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Bookkeeping Management System for Non-Profits

This program helps non-profits manage their finances efficiently and generate 
accurate reports for tax authorities. It supports income and expense tracking, 
report generation, and basic error handling.

Author: [Your Name]
"""

import datetime
import json
import os

# Constants
DATA_FILE = "bookkeeping_data.json"
DEFAULT_CURRENCY = "USD"

class BookkeepingManager:
    """Class to manage bookkeeping for a non-profit organization."""

    def __init__(self):
        """Initialize bookkeeping manager and load data."""
        self.data = {"income": [], "expenses": []}
        self.load_data()

    def load_data(self):
        """Load bookkeeping data from a file."""
        if os.path.exists(DATA_FILE):
            try:
                with open(DATA_FILE, "r") as file:
                    self.data = json.load(file)
            except json.JSONDecodeError:
                print("Error: Corrupted data file. Starting with empty data.")
            except Exception as e:
                print(f"Error loading data file: {e}")

    def save_data(self):
        """Save bookkeeping data to a file."""
        try:
            with open(DATA_FILE, "w") as file:
                json.dump(self.data, file, indent=4)
        except Exception as e:
            print(f"Error saving data file: {e}")

    def add_income(self, amount, source, date=None):
        """Add an income record."""
        if amount <= 0:
            raise ValueError("Income amount must be positive.")
        date = date or datetime.date.today().isoformat()
        self.data["income"].append({"amount": amount, "source": source, "date": date})
        self.save_data()

    def add_expense(self, amount, description, date=None):
        """Add an expense record."""
        if amount <= 0:
            raise ValueError("Expense amount must be positive.")
        date = date or datetime.date.today().isoformat()
        self.data["expenses"].append({"amount": amount, "description": description, "date": date})
        self.save_data()

    def generate_report(self):
        """Generate a financial report."""
        total_income = sum(item["amount"] for item in self.data["income"])
        total_expenses = sum(item["amount"] for item in self.data["expenses"])
        net_balance = total_income - total_expenses

        report = {
            "total_income": f"{total_income} {DEFAULT_CURRENCY}",
            "total_expenses": f"{total_expenses} {DEFAULT_CURRENCY}",
            "net_balance": f"{net_balance} {DEFAULT_CURRENCY}",
            "generated_on": datetime.datetime.now().isoformat(),
        }

        return report

    def export_report_to_file(self, filename="financial_report.json"):
        """Export the financial report to a file."""
        report = self.generate_report()
        try:
            with open(filename, "w") as file:
                json.dump(report, file, indent=4)
            print(f"Report successfully exported to {filename}")
        except Exception as e:
            print(f"Error exporting report: {e}")

# Main function to demonstrate usage
def main():
    """Main function demonstrating the bookkeeping manager."""
    manager = BookkeepingManager()

    # Add sample data
    try:
        manager.add_income(5000, "Donation from Organization X")
        manager.add_expense(1200, "Office Supplies")
        manager.add_income(2500, "Government Grant")
        manager.add_expense(800, "Event Catering")
    except ValueError as e:
        print(f"Error adding transaction: {e}")

    # Generate and display report
    report = manager.generate_report()
    print("Financial Report:")
    for key, value in report.items():
        print(f"{key}: {value}")

    # Export report to file
    manager.export_report_to_file()

if __name__ == "__main__":
    main()
```
