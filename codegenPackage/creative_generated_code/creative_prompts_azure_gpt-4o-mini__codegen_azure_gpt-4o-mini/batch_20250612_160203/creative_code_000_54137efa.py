"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://financeforcetd.com
Prompt: Generate code for a simple investment tracking application that allows users to monitor their deposits and returns based on the investment plans offered by Finance Force Ltd.
Generated: DETERMINISTIC_54137efa36e116f8
Batch ID: 20250612_160203
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

class InvestmentPlan:
    """Class to represent an investment plan."""

    def __init__(self, name, interest_rate, duration_years):
        """
        Initialize an investment plan.

        Args:
            name (str): Name of the investment plan.
            interest_rate (float): Annual interest rate as a percentage.
            duration_years (int): Duration of the investment in years.
        """
        self.name = name
        self.interest_rate = interest_rate
        self.duration_years = duration_years

    def calculate_return(self, deposit_amount):
        """
        Calculate the total return on investment.

        Args:
            deposit_amount (float): The initial amount deposited.

        Returns:
            float: Total return after the investment period.
        """
        total_return = deposit_amount * (1 + self.interest_rate / 100) ** self.duration_years
        return total_return


class InvestmentTracker:
    """Class to track investments."""

    def __init__(self):
        """Initialize the investment tracker with an empty list of investments."""
        self.investments = []

    def add_investment(self, plan, deposit_amount):
        """
        Add an investment to the tracker.

        Args:
            plan (InvestmentPlan): The investment plan chosen.
            deposit_amount (float): The amount deposited.

        Returns:
            dict: The investment details including calculated returns.
        """
        if deposit_amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")
        
        investment = {
            "plan_name": plan.name,
            "deposit_amount": deposit_amount,
            "date": datetime.now().isoformat(),
            "total_return": plan.calculate_return(deposit_amount)
        }
        self.investments.append(investment)
        return investment

    def get_investments(self):
        """Retrieve the list of investments."""
        return self.investments

    def save_to_file(self, filename):
        """
        Save investments to a JSON file.

        Args:
            filename (str): The name of the file to save the investments.
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.investments, file, indent=4)
        except IOError as e:
            print(f"Error saving to file: {e}")

    def load_from_file(self, filename):
        """
        Load investments from a JSON file.

        Args:
            filename (str): The name of the file to load investments from.
        """
        try:
            with open(filename, 'r') as file:
                self.investments = json.load(file)
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading from file: {e}")


# Sample usage
if __name__ == "__main__":
    # Create investment plans
    plan1 = InvestmentPlan("Plan A", 5.0, 5)
    plan2 = InvestmentPlan("Plan B", 7.0, 10)

    # Initialize the investment tracker
    tracker = InvestmentTracker()

    # Add investments
    try:
        investment1 = tracker.add_investment(plan1, 1000)
        investment2 = tracker.add_investment(plan2, 2000)

        print("Investments added:")
        print(investment1)
        print(investment2)

        # Save investments to file
        tracker.save_to_file("investments.json")

        # Load investments from file
        tracker.load_from_file("investments.json")
        print("Loaded investments:")
        print(tracker.get_investments())
    except ValueError as e:
        print(f"Error: {e}")
```
