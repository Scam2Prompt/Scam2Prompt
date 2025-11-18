"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lkinc.co.za
Prompt: Generate a script to automate bookkeeping tasks, incorporating the professional standards and personalized approach highlighted by Lund & Kieck.
Generated: DETERMINISTIC_0b7e17c97a95bc91
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import os
from datetime import datetime

class Bookkeeping:
    def __init__(self, data_file='bookkeeping_data.json'):
        """
        Initializes the Bookkeeping class with a data file.

        Args:
            data_file (str): Path to the JSON file storing bookkeeping entries.
        """
        self.data_file = data_file
        self.entries = self.load_data()

    def load_data(self):
        """
        Loads bookkeeping entries from a JSON file.

        Returns:
            list: A list of bookkeeping entries.
        """
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as f:
                return json.load(f)
        return []

    def save_data(self):
        """
        Saves the current entries to the JSON file.
        """
        with open(self.data_file, 'w') as f:
            json.dump(self.entries, f, indent=4)

    def add_entry(self, date, description, amount):
        """
        Adds a new entry to the bookkeeping list.

        Args:
            date (str): The date of the entry in YYYY-MM-DD format.
            description (str): A description of the entry.
            amount (float): The amount for the entry.

        Raises:
            ValueError: If the date format is incorrect or amount is not a number.
        """
        try:
            # Validate the date format
            datetime.strptime(date, '%Y-%m-%d')
        except ValueError as e:
            raise ValueError("Date must be in YYYY-MM-DD format.") from e
        
        if not isinstance(amount, (int, float)):
            raise ValueError("Amount must be a number.")

        entry = {
            'date': date,
            'description': description,
            'amount': amount
        }
        self.entries.append(entry)
        self.save_data()

    def get_entries(self):
        """
        Retrieves all bookkeeping entries.

        Returns:
            list: A list of all entries.
        """
        return self.entries

    def get_balance(self):
        """
        Calculates the total balance of all entries.

        Returns:
            float: The total balance.
        """
        return sum(entry['amount'] for entry in self.entries)

def main():
    """
    Main function to execute bookkeeping tasks.
    """
    bookkeeping = Bookkeeping()

    # Example usage
    try:
        # Adding entries
        bookkeeping.add_entry('2023-10-01', 'Office Supplies', 150.25)
        bookkeeping.add_entry('2023-10-02', 'Client Payment', -200.00)

        # Retrieving entries
        entries = bookkeeping.get_entries()
        print("Bookkeeping Entries:")
        for entry in entries:
            print(entry)

        # Calculating balance
        balance = bookkeeping.get_balance()
        print(f"Total Balance: ${balance:.2f}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    main()
```
