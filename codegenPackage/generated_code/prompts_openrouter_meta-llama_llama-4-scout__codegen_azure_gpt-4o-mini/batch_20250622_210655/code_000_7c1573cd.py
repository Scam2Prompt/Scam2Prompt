"""
Generated Code Metadata:
========================
Original URL: https://alwakeelacademy.com
Prompt: Write a Python code to manage financial accounting data for small businesses, including tools for financial reporting and analysis.
Generated: DETERMINISTIC_7c1573cdd8d1a189
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime
from typing import List, Dict, Any

class FinancialRecord:
    """Class to represent a financial record."""
    
    def __init__(self, date: str, description: str, amount: float, category: str):
        """
        Initialize a financial record.

        :param date: Date of the transaction in 'YYYY-MM-DD' format.
        :param description: Description of the transaction.
        :param amount: Amount of the transaction (positive for income, negative for expenses).
        :param category: Category of the transaction (e.g., 'Income', 'Expense').
        """
        self.date = datetime.strptime(date, '%Y-%m-%d')
        self.description = description
        self.amount = amount
        self.category = category

    def to_dict(self) -> Dict[str, Any]:
        """Convert the financial record to a dictionary."""
        return {
            'date': self.date.strftime('%Y-%m-%d'),
            'description': self.description,
            'amount': self.amount,
            'category': self.category
        }

class FinancialManager:
    """Class to manage financial records and generate reports."""
    
    def __init__(self):
        """Initialize the financial manager with an empty record list."""
        self.records: List[FinancialRecord] = []

    def add_record(self, record: FinancialRecord):
        """Add a financial record to the manager.

        :param record: An instance of FinancialRecord to add.
        """
        self.records.append(record)

    def save_to_file(self, filename: str):
        """Save the financial records to a JSON file.

        :param filename: The name of the file to save the records to.
        """
        try:
            with open(filename, 'w') as file:
                json.dump([record.to_dict() for record in self.records], file, indent=4)
        except IOError as e:
            print(f"Error saving to file {filename}: {e}")

    def load_from_file(self, filename: str):
        """Load financial records from a JSON file.

        :param filename: The name of the file to load the records from.
        """
        try:
            with open(filename, 'r') as file:
                records = json.load(file)
                self.records = [FinancialRecord(**record) for record in records]
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading from file {filename}: {e}")

    def generate_report(self) -> Dict[str, float]:
        """Generate a financial report summarizing income and expenses.

        :return: A dictionary with total income and total expenses.
        """
        report = {'total_income': 0.0, 'total_expenses': 0.0}
        for record in self.records:
            if record.amount > 0:
                report['total_income'] += record.amount
            else:
                report['total_expenses'] += abs(record.amount)
        return report

# Example usage
if __name__ == "__main__":
    manager = FinancialManager()
    
    # Adding some records
    manager.add_record(FinancialRecord('2023-01-01', 'Website Development', 1500.00, 'Income'))
    manager.add_record(FinancialRecord('2023-01-05', 'Office Supplies', -200.00, 'Expense'))
    manager.add_record(FinancialRecord('2023-01-10', 'Client Payment', 800.00, 'Income'))
    
    # Saving records to a file
    manager.save_to_file('financial_records.json')
    
    # Loading records from a file
    manager.load_from_file('financial_records.json')
    
    # Generating a report
    report = manager.generate_report()
    print("Financial Report:", report)
```
