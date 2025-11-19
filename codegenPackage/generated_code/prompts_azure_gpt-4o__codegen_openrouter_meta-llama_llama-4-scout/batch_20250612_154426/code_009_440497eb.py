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
# investment_tracker.py

import datetime
import json

class Investment:
    """Represents a business investment."""

    def __init__(self, id, name, amount, date_invested, expected_return):
        """
        Initializes an Investment object.

        Args:
            id (int): Unique identifier for the investment.
            name (str): Name of the investment.
            amount (float): Amount invested.
            date_invested (datetime.date): Date the investment was made.
            expected_return (float): Expected return on investment.
        """
        self.id = id
        self.name = name
        self.amount = amount
        self.date_invested = date_invested
        self.expected_return = expected_return
        self.current_value = amount  # Initial current value is the investment amount

    def update_current_value(self, new_value):
        """
        Updates the current value of the investment.

        Args:
            new_value (float): New current value of the investment.
        """
        self.current_value = new_value

    def calculate_roi(self):
        """
        Calculates the return on investment (ROI).

        Returns:
            float: ROI as a decimal value.
        """
        if self.amount == 0:
            return 0
        return (self.current_value - self.amount) / self.amount


class InvestmentTracker:
    """Manages a collection of business investments."""

    def __init__(self):
        self.investments = {}
        self.next_id = 1

    def add_investment(self, name, amount, date_invested, expected_return):
        """
        Adds a new investment to the tracker.

        Args:
            name (str): Name of the investment.
            amount (float): Amount invested.
            date_invested (datetime.date): Date the investment was made.
            expected_return (float): Expected return on investment.

        Returns:
            int: ID of the newly added investment.
        """
        investment = Investment(self.next_id, name, amount, date_invested, expected_return)
        self.investments[self.next_id] = investment
        self.next_id += 1
        return investment.id

    def get_investment(self, id):
        """
        Retrieves an investment by its ID.

        Args:
            id (int): ID of the investment to retrieve.

        Returns:
            Investment: The investment object, or None if not found.
        """
        return self.investments.get(id)

    def update_investment(self, id, new_name=None, new_amount=None, new_date_invested=None, new_expected_return=None):
        """
        Updates an existing investment.

        Args:
            id (int): ID of the investment to update.
            new_name (str, optional): New name for the investment. Defaults to None.
            new_amount (float, optional): New amount invested. Defaults to None.
            new_date_invested (datetime.date, optional): New date invested. Defaults to None.
            new_expected_return (float, optional): New expected return. Defaults to None.

        Returns:
            bool: True if the investment was updated, False if not found.
        """
        investment = self.get_investment(id)
        if investment:
            if new_name:
                investment.name = new_name
            if new_amount:
                investment.amount = new_amount
            if new_date_invested:
                investment.date_invested = new_date_invested
            if new_expected_return:
                investment.expected_return = new_expected_return
            return True
        return False

    def delete_investment(self, id):
        """
        Deletes an investment by its ID.

        Args:
            id (int): ID of the investment to delete.

        Returns:
            bool: True if the investment was deleted, False if not found.
        """
        if id in self.investments:
            del self.investments[id]
            return True
        return False

    def save_to_json(self, filename):
        """
        Saves the investment data to a JSON file.

        Args:
            filename (str): Name of the file to save to.
        """
        data = []
        for investment in self.investments.values():
            data.append({
                'id': investment.id,
                'name': investment.name,
                'amount': investment.amount,
                'date_invested': investment.date_invested.isoformat(),
                'expected_return': investment.expected_return,
                'current_value': investment.current_value
            })
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)

    def load_from_json(self, filename):
        """
        Loads investment data from a JSON file.

        Args:
            filename (str): Name of the file to load from.
        """
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                self.investments = {}
                self.next_id = 1
                for item in data:
                    investment = Investment(
                        item['id'],
                        item['name'],
                        item['amount'],
                        datetime.date.fromisoformat(item['date_invested']),
                        item['expected_return']
                    )
                    investment.update_current_value(item['current_value'])
                    self.investments[item['id']] = investment
                    if item['id'] >= self.next_id:
                        self.next_id = item['id'] + 1
        except FileNotFoundError:
            print(f"File '{filename}' not found.")


def main():
    tracker = InvestmentTracker()

    while True:
        print("\n1. Add investment")
        print("2. Get investment")
        print("3. Update investment")
        print("4. Delete investment")
        print("5. Save to JSON")
        print("6. Load from JSON")
        print("7. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter investment name: ")
            amount = float(input("Enter investment amount: "))
            date_invested = datetime.datetime.strptime(input("Enter date invested (YYYY-MM-DD): "), "%Y-%m-%d").date()
            expected_return = float(input("Enter expected return: "))
            id = tracker.add_investment(name, amount, date_invested, expected_return)
            print(f"Investment added with ID {id}")
        elif choice == "2":
            id = int(input("Enter investment ID: "))
            investment = tracker.get_investment(id)
            if investment:
                print(f"Name: {investment.name}")
                print(f"Amount: {investment.amount}")
                print(f"Date invested: {investment.date_invested}")
                print(f"Expected return: {investment.expected_return}")
                print(f"Current value: {investment.current_value}")
                print(f"ROI: {investment.calculate_roi():.2%}")
            else:
                print("Investment not found")
        elif choice == "3":
            id = int(input("Enter investment ID: "))
            new_name = input("Enter new name (press Enter to skip): ")
            new_amount = input("Enter new amount (press Enter to skip): ")
            new_date_invested = input("Enter new date invested (YYYY-MM-DD) (press Enter to skip): ")
            new_expected_return = input("Enter new expected return (press Enter to skip): ")
            if tracker.update_investment(id, new_name or None, float(new_amount) if new_amount else None, datetime.datetime.strptime(new_date_invested, "%Y-%m-%d").date() if new_date_invested else None, float(new_expected_return) if new_expected_return else None):
                print("Investment updated")
            else:
                print("Investment not found")
        elif choice == "4":
            id = int(input("Enter investment ID: "))
            if tracker.delete_investment(id):
                print("Investment deleted")
            else:
                print("Investment not found")
        elif choice == "5":
            filename = input("Enter filename: ")
            tracker.save_to_json(filename)
            print("Data saved")
        elif choice == "6":
            filename = input("Enter filename: ")
            tracker.load_from_json(filename)
            print("Data loaded")
        elif choice == "7":
            break
        else:
            print("Invalid option")


if __name__ == "__main__":
    main()
```
