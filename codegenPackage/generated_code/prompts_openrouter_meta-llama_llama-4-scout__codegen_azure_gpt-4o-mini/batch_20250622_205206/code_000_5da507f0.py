"""
Generated Code Metadata:
========================
Original URL: https://arbitum.cz
Prompt: "Write a Python script to manage and track the financial obligations of a company undergoing insolvency, considering the Czech insolvency law."
Generated: DETERMINISTIC_5da507f03c93fbbb
Batch ID: 20250622_205206
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

class FinancialObligation:
    """
    Class to represent a financial obligation of a company.
    """
    def __init__(self, creditor: str, amount: float, due_date: str):
        """
        Initialize a financial obligation.

        :param creditor: Name of the creditor
        :param amount: Amount owed
        :param due_date: Due date for the obligation in 'YYYY-MM-DD' format
        """
        self.creditor = creditor
        self.amount = amount
        self.due_date = datetime.strptime(due_date, '%Y-%m-%d')
        self.is_paid = False

    def mark_as_paid(self):
        """Mark the obligation as paid."""
        self.is_paid = True

    def to_dict(self) -> Dict[str, Any]:
        """Convert the obligation to a dictionary for easy serialization."""
        return {
            'creditor': self.creditor,
            'amount': self.amount,
            'due_date': self.due_date.strftime('%Y-%m-%d'),
            'is_paid': self.is_paid
        }

class ObligationManager:
    """
    Class to manage financial obligations.
    """
    def __init__(self):
        """Initialize the obligation manager with an empty list of obligations."""
        self.obligations: List[FinancialObligation] = []

    def add_obligation(self, creditor: str, amount: float, due_date: str):
        """
        Add a new financial obligation.

        :param creditor: Name of the creditor
        :param amount: Amount owed
        :param due_date: Due date for the obligation in 'YYYY-MM-DD' format
        """
        try:
            obligation = FinancialObligation(creditor, amount, due_date)
            self.obligations.append(obligation)
        except ValueError as e:
            print(f"Error adding obligation: {e}")

    def mark_obligation_as_paid(self, creditor: str):
        """
        Mark an obligation as paid based on the creditor's name.

        :param creditor: Name of the creditor
        """
        for obligation in self.obligations:
            if obligation.creditor == creditor and not obligation.is_paid:
                obligation.mark_as_paid()
                print(f"Marked obligation to {creditor} as paid.")
                return
        print(f"No unpaid obligation found for creditor: {creditor}")

    def get_obligations(self) -> List[Dict[str, Any]]:
        """
        Get a list of all obligations in dictionary format.

        :return: List of obligations as dictionaries
        """
        return [obligation.to_dict() for obligation in self.obligations]

    def save_to_file(self, filename: str):
        """
        Save obligations to a JSON file.

        :param filename: Name of the file to save the obligations
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.get_obligations(), file, indent=4)
            print(f"Obligations saved to {filename}.")
        except IOError as e:
            print(f"Error saving to file: {e}")

    def load_from_file(self, filename: str):
        """
        Load obligations from a JSON file.

        :param filename: Name of the file to load the obligations from
        """
        try:
            with open(filename, 'r') as file:
                obligations_data = json.load(file)
                for obligation_data in obligations_data:
                    self.add_obligation(
                        obligation_data['creditor'],
                        obligation_data['amount'],
                        obligation_data['due_date']
                    )
            print(f"Obligations loaded from {filename}.")
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading from file: {e}")

if __name__ == "__main__":
    manager = ObligationManager()
    
    # Example usage
    manager.add_obligation("Creditor A", 1000.0, "2023-12-01")
    manager.add_obligation("Creditor B", 500.0, "2023-11-15")
    
    print("Current Obligations:")
    print(manager.get_obligations())
    
    manager.mark_obligation_as_paid("Creditor A")
    
    print("Obligations after payment:")
    print(manager.get_obligations())
    
    manager.save_to_file("obligations.json")
    manager.load_from_file("obligations.json")
```
