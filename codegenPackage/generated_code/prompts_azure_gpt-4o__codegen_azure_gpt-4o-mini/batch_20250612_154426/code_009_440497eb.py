"""
Generated Code Metadata:
========================
Original URL: https://genesisicu.com
Prompt: Create a program to track and manage small-to-medium business investments, inspired by Genesis Investment Credit Union's business services offerings.
Generated: DETERMINISTIC_440497eb9e86ab87
Batch ID: 20250612_154426
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

class Investment:
    """Class to represent an investment."""
    
    def __init__(self, name, amount, date, description):
        """
        Initialize an investment instance.

        :param name: Name of the investment
        :param amount: Amount invested
        :param date: Date of the investment
        :param description: Description of the investment
        """
        self.name = name
        self.amount = amount
        self.date = datetime.strptime(date, '%Y-%m-%d')
        self.description = description

    def to_dict(self):
        """Convert the investment instance to a dictionary."""
        return {
            'name': self.name,
            'amount': self.amount,
            'date': self.date.strftime('%Y-%m-%d'),
            'description': self.description
        }

class InvestmentManager:
    """Class to manage a collection of investments."""
    
    def __init__(self, filename='investments.json'):
        """
        Initialize the investment manager.

        :param filename: The filename to store investments
        """
        self.filename = filename
        self.investments = self.load_investments()

    def load_investments(self):
        """Load investments from a JSON file."""
        try:
            with open(self.filename, 'r') as file:
                investments_data = json.load(file)
                return [Investment(**data) for data in investments_data]
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            print("Error: Could not decode JSON from the file.")
            return []

    def save_investments(self):
        """Save investments to a JSON file."""
        with open(self.filename, 'w') as file:
            json.dump([investment.to_dict() for investment in self.investments], file, indent=4)

    def add_investment(self, name, amount, date, description):
        """Add a new investment to the collection."""
        new_investment = Investment(name, amount, date, description)
        self.investments.append(new_investment)
        self.save_investments()

    def list_investments(self):
        """List all investments."""
        for investment in self.investments:
            print(f"Name: {investment.name}, Amount: {investment.amount}, Date: {investment.date.strftime('%Y-%m-%d')}, Description: {investment.description}")

def main():
    """Main function to run the investment manager."""
    manager = InvestmentManager()

    while True:
        print("\nInvestment Manager")
        print("1. Add Investment")
        print("2. List Investments")
        print("3. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            name = input("Enter investment name: ")
            amount = float(input("Enter investment amount: "))
            date = input("Enter investment date (YYYY-MM-DD): ")
            description = input("Enter investment description: ")
            manager.add_investment(name, amount, date, description)
            print("Investment added successfully.")
        elif choice == '2':
            manager.list_investments()
        elif choice == '3':
            print("Exiting the Investment Manager.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```
