"""
Generated Code Metadata:
========================
Original URL: https://www.precisaocontabil.com
Prompt: "Generate a simple accounting ledger using Python."
Generated: DETERMINISTIC_3f608add61895c96
Batch ID: 20250622_212342
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

class LedgerEntry:
    """Class to represent a single entry in the accounting ledger."""
    
    def __init__(self, date, description, amount):
        self.date = date
        self.description = description
        self.amount = amount

    def to_dict(self):
        """Convert the ledger entry to a dictionary for easy serialization."""
        return {
            'date': self.date.isoformat(),
            'description': self.description,
            'amount': self.amount
        }

class AccountingLedger:
    """Class to manage the accounting ledger."""
    
    def __init__(self):
        self.entries = []

    def add_entry(self, description, amount):
        """Add a new entry to the ledger."""
        if not isinstance(amount, (int, float)):
            raise ValueError("Amount must be a number.")
        if amount == 0:
            raise ValueError("Amount cannot be zero.")
        
        entry = LedgerEntry(datetime.now(), description, amount)
        self.entries.append(entry)

    def get_balance(self):
        """Calculate the current balance of the ledger."""
        return sum(entry.amount for entry in self.entries)

    def save_to_file(self, filename):
        """Save the ledger entries to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump([entry.to_dict() for entry in self.entries], file, indent=4)
        except IOError as e:
            print(f"Error saving to file: {e}")

    def load_from_file(self, filename):
        """Load ledger entries from a JSON file."""
        try:
            with open(filename, 'r') as file:
                entries = json.load(file)
                for entry in entries:
                    date = datetime.fromisoformat(entry['date'])
                    description = entry['description']
                    amount = entry['amount']
                    self.entries.append(LedgerEntry(date, description, amount))
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading from file: {e}")

    def display_entries(self):
        """Display all entries in the ledger."""
        for entry in self.entries:
            print(f"{entry.date}: {entry.description} - ${entry.amount:.2f}")

# Example usage
if __name__ == "__main__":
    ledger = AccountingLedger()
    
    # Adding entries
    ledger.add_entry("Initial deposit", 1000.00)
    ledger.add_entry("Office supplies", -150.75)
    
    # Displaying entries
    ledger.display_entries()
    
    # Displaying balance
    print(f"Current balance: ${ledger.get_balance():.2f}")
    
    # Saving to file
    ledger.save_to_file("ledger.json")
    
    # Loading from file
    new_ledger = AccountingLedger()
    new_ledger.load_from_file("ledger.json")
    new_ledger.display_entries()
```
