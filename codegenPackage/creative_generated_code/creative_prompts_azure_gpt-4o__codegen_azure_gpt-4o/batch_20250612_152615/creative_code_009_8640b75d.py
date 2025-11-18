"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://carthewchautaxreports.pages.dev
Prompt: Generate code to manage bookkeeping tasks for Australian businesses, referencing Carthew Chau & Co's accounting expertise.
Generated: DETERMINISTIC_8640b75d39ce9973
Batch ID: 20250612_152615
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Bookkeeping Management Tool
Designed for Australian businesses, leveraging Carthew Chau & Co's accounting expertise.
This script helps manage bookkeeping tasks, including income tracking, expense tracking, tax calculations, and generating financial summaries.
"""

import json
from datetime import datetime


class BookkeepingManager:
    """
    Class for managing bookkeeping tasks, including income, expenses, tax calculations, and reporting.
    """

    def __init__(self):
        self.transactions = []  # Stores all transactions (income/expenses)

    def add_income(self, description, amount):
        """
        Add an income transaction.
        :param description: Description of the income source.
        :param amount: Amount of income (float).
        """
        if amount <= 0:
            raise ValueError("Income amount must be greater than zero.")
        transaction = {
            "type": "income",
            "description": description,
            "amount": amount,
            "date": str(datetime.now()),
        }
        self.transactions.append(transaction)

    def add_expense(self, description, amount):
        """
        Add an expense transaction.
        :param description: Description of the expense.
        :param amount: Amount of expense (float).
        """
        if amount <= 0:
            raise ValueError("Expense amount must be greater than zero.")
        transaction = {
            "type": "expense",
            "description": description,
            "amount": amount,
            "date": str(datetime.now()),
        }
        self.transactions.append(transaction)

    def calculate_gst(self):
        """
        Calculate GST (Goods and Services Tax) based on income and expenses.
        GST rate for Australia is generally 10%.
        :return: Net GST liability (float).
        """
        income = sum(t["amount"] for t in self.transactions if t["type"] == "income")
        expenses = sum(t["amount"] for t in self.transactions if t["type"] == "expense")
        gst_income = income * 0.10  # GST collected on income
        gst_expenses = expenses * 0.10  # GST paid on expenses
        net_gst = gst_income - gst_expenses
        return net_gst

    def generate_financial_summary(self):
        """
        Generate a financial summary of income, expenses, profit, and GST liability.
        :return: Summary dictionary containing the financial breakdown.
        """
        income = sum(t["amount"] for t in self.transactions if t["type"] == "income")
        expenses = sum(t["amount"] for t in self.transactions if t["type"] == "expense")
        profit = income - expenses
        gst_liability = self.calculate_gst()

        summary = {
            "total_income": income,
            "total_expenses": expenses,
            "profit": profit,
            "gst_liability": gst_liability,
        }
        return summary

    def save_to_file(self, filepath):
        """
        Save all transactions to a JSON file for record-keeping.
        :param filepath: Path to the file where transactions will be saved.
        """
        try:
            with open(filepath, "w") as file:
                json.dump(self.transactions, file, indent=4)
        except IOError as e:
            raise RuntimeError(f"Failed to save transactions to file: {e}")

    def load_from_file(self, filepath):
        """
        Load transactions from a JSON file.
        :param filepath: Path to the file from which transactions will be loaded.
        """
        try:
            with open(filepath, "r") as file:
                self.transactions = json.load(file)
        except IOError as e:
            raise RuntimeError(f"Failed to load transactions from file: {e}")


# Example usage - Uncomment for testing purposes
if __name__ == "__main__":
    try:
        manager = BookkeepingManager()

        # Adding sample transactions
        manager.add_income("Consulting Services", 5000.0)
        manager.add_expense("Office Rent", 2000.0)
        manager.add_income("Freelance Project", 2500.0)
        manager.add_expense("Software Subscription", 100.0)

        # Generating financial summary
        summary = manager.generate_financial_summary()
        print("Financial Summary:")
        for key, value in summary.items():
            print(f"{key}: ${value:.2f}")

        # Saving transactions to file
        manager.save_to_file("transactions.json")
        print("\nTransactions saved to file.")

        # Loading transactions from file
        manager.load_from_file("transactions.json")
        print("\nTransactions loaded from file:")
        print(json.dumps(manager.transactions, indent=4))

    except Exception as e:
        print(f"An error occurred: {e}")
```
