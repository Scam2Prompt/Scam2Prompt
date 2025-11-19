"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rateaml.com
Prompt: Explain how to manually add operations and generate tax reports using AMLBot’s features for personal use.
Generated: DETERMINISTIC_2e701ffde7e6de73
Batch ID: 20250612_163224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import json
import datetime
from typing import List, Dict, Any

class AMLBot:
    """
    A class to represent AMLBot for managing operations and generating tax reports.
    """

    def __init__(self):
        self.operations: List[Dict[str, Any]] = []
        self.tax_reports: List[Dict[str, Any]] = []

    def add_operation(self, operation: Dict[str, Any]) -> None:
        """
        Add a new operation to the AMLBot.

        Args:
            operation (Dict[str, Any]): A dictionary containing operation details.
        """
        if not self._validate_operation(operation):
            raise ValueError("Invalid operation data.")
        
        self.operations.append(operation)
        print(f"Operation added: {operation}")

    def _validate_operation(self, operation: Dict[str, Any]) -> bool:
        """
        Validate operation data.

        Args:
            operation (Dict[str, Any]): A dictionary containing operation details.

        Returns:
            bool: True if operation data is valid, otherwise False.
        """
        required_keys = ['id', 'amount', 'date', 'category']
        return all(key in operation for key in required_keys)

    def generate_tax_report(self, year: int) -> Dict[str, Any]:
        """
        Generate a tax report for a specified year.

        Args:
            year (int): The year for which the tax report is generated.

        Returns:
            Dict[str, Any]: A dictionary containing the tax report data.
        """
        report = {
            'year': year,
            'total_income': 0,
            'total_expense': 0,
            'operations': []
        }

        for operation in self.operations:
            operation_date = datetime.datetime.strptime(operation['date'], '%Y-%m-%d')
            if operation_date.year == year:
                if operation['category'] == 'income':
                    report['total_income'] += operation['amount']
                elif operation['category'] == 'expense':
                    report['total_expense'] += operation['amount']
                report['operations'].append(operation)

        self.tax_reports.append(report)
        print(f"Tax report generated for {year}: {report}")
        return report

    def save_operations(self, filename: str) -> None:
        """
        Save operations to a JSON file.

        Args:
            filename (str): The name of the file to save operations.
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.operations, file, indent=4)
            print(f"Operations saved to {filename}.")
        except IOError as e:
            print(f"Error saving operations: {e}")

    def load_operations(self, filename: str) -> None:
        """
        Load operations from a JSON file.

        Args:
            filename (str): The name of the file to load operations from.
        """
        try:
            with open(filename, 'r') as file:
                self.operations = json.load(file)
            print(f"Operations loaded from {filename}.")
        except IOError as e:
            print(f"Error loading operations: {e}")
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")

# Example usage
if __name__ == "__main__":
    bot = AMLBot()

    # Adding operations
    try:
        bot.add_operation({'id': 1, 'amount': 1500, 'date': '2023-03-15', 'category': 'income'})
        bot.add_operation({'id': 2, 'amount': 500, 'date': '2023-06-20', 'category': 'expense'})
    except ValueError as e:
        print(e)

    # Generating tax report for 2023
    report = bot.generate_tax_report(2023)

    # Saving operations
    bot.save_operations('operations.json')

    # Loading operations
    bot.load_operations('operations.json')
```
