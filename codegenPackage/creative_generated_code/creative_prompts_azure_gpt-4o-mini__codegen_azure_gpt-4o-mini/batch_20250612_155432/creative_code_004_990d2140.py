"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://accounting-team.com
Prompt: How can I create a financial record organization system based on the tailored services provided by The Accounting Team?
Generated: DETERMINISTIC_990d2140e4f91e15
Batch ID: 20250612_155432
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from datetime import datetime
from typing import List, Dict, Any

class FinancialRecord:
    """Class to represent a financial record."""
    
    def __init__(self, date: str, amount: float, description: str):
        self.date = self.validate_date(date)
        self.amount = self.validate_amount(amount)
        self.description = description

    @staticmethod
    def validate_date(date_str: str) -> str:
        """Validates and returns the date in ISO format."""
        try:
            parsed_date = datetime.strptime(date_str, '%Y-%m-%d')
            return parsed_date.date().isoformat()
        except ValueError:
            raise ValueError("Date must be in YYYY-MM-DD format")

    @staticmethod
    def validate_amount(amount: float) -> float:
        """Validates and returns the amount as a positive float."""
        if amount < 0:
            raise ValueError("Amount must be a positive number")
        return amount

    def to_dict(self) -> Dict[str, Any]:
        """Converts the financial record to a dictionary."""
        return {
            "date": self.date,
            "amount": self.amount,
            "description": self.description
        }

class FinancialRecordManager:
    """Class to manage a collection of financial records."""
    
    def __init__(self, filename: str):
        self.filename = filename
        self.records: List[FinancialRecord] = []
        self.load_records()

    def load_records(self) -> None:
        """Loads financial records from a JSON file."""
        try:
            with open(self.filename, 'r') as file:
                records_data = json.load(file)
                self.records = [FinancialRecord(**record) for record in records_data]
        except FileNotFoundError:
            print("No existing records found. Starting fresh.")
        except json.JSONDecodeError:
            print("Error decoding JSON data. Starting fresh.")

    def save_records(self) -> None:
        """Saves financial records to a JSON file."""
        try:
            with open(self.filename, 'w') as file:
                json.dump([record.to_dict() for record in self.records], file, indent=4)
        except IOError as e:
            print(f"An error occurred while writing to the file: {e}")

    def add_record(self, date: str, amount: float, description: str) -> None:
        """Adds a new financial record and saves it."""
        record = FinancialRecord(date, amount, description)
        self.records.append(record)
        self.save_records()

    def get_records(self) -> List[FinancialRecord]:
        """Returns a list of financial records."""
        return self.records

def main():
    """Main function to demonstrate the financial record organization system."""
    manager = FinancialRecordManager('financial_records.json')

    # Example usage: Add a record
    try:
        manager.add_record('2023-10-05', 250.75, 'Consulting services')
        manager.add_record('2023-10-06', -100, 'Refund request')  # This will raise an error
    except ValueError as ve:
        print(f"Error: {ve}")

    # Print all records
    records = manager.get_records()
    for record in records:
        print(record.to_dict())

if __name__ == '__main__':
    main()
```
