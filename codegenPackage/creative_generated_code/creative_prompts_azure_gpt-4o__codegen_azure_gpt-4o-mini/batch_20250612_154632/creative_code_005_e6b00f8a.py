"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cornerstoneprimesinvestment.com
Prompt: Write a program to manage user investment accounts, including features for selecting a plan, tracking profits, and ensuring privacy as described on the Corner Stone Investment website.
Generated: DETERMINISTIC_e6b00f8a39ecdd10
Batch ID: 20250612_154632
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict

class InvestmentAccount:
    """
    A class to represent an investment account for a user.

    Attributes
    ----------
    user_id : str
        Unique identifier for the user
    plan : str
        Selected investment plan
    investments : List[float]
        List of investments made by the user
    profits : float
        Total profits earned by the user

    Methods
    -------
    select_plan(plan: str):
        Allows the user to select an investment plan.
        
    add_investment(amount: float):
        Adds a new investment amount to the account.
        
    calculate_profits() -> float:
        Calculates total profits based on investments.
        
    save_account() -> None:
        Saves the account details to a JSON file.
    """

    def __init__(self, user_id: str):
        self.user_id = user_id
        self.plan = None
        self.investments = []
        self.profits = 0.0

    def select_plan(self, plan: str):
        """Selects an investment plan for the account."""
        valid_plans = ['Basic', 'Silver', 'Gold', 'Platinum']
        if plan not in valid_plans:
            raise ValueError(f"Invalid plan selected. Choose from: {valid_plans}")
        self.plan = plan

    def add_investment(self, amount: float):
        """Adds a new investment amount to the account."""
        if amount <= 0:
            raise ValueError("Investment amount must be greater than zero.")
        self.investments.append(amount)
        self.profits = self.calculate_profits()

    def calculate_profits(self) -> float:
        """Calculates total profits based on investments."""
        # Simple profit calculation - can be adjusted based on specific rules
        return sum(self.investments) * 0.1  # Example: 10% profit

    def save_account(self) -> None:
        """Saves the account details to a JSON file."""
        account_data = {
            'user_id': self.user_id,
            'plan': self.plan,
            'investments': self.investments,
            'profits': self.profits
        }
        try:
            with open(f"{self.user_id}_account.json", 'w') as file:
                json.dump(account_data, file)
        except IOError as e:
            raise Exception(f"Error saving account data: {e}")

def main():
    """Main function to demonstrate the InvestmentAccount class functionality."""
    user_id = input("Enter your user ID: ")
    account = InvestmentAccount(user_id)

    try:
        plan = input("Select an investment plan (Basic, Silver, Gold, Platinum): ")
        account.select_plan(plan)

        while True:
            amount = float(input("Enter investment amount (or -1 to finish): "))
            if amount == -1:
                break
            account.add_investment(amount)

        account.save_account()
        print(f"Account for {user_id} saved successfully.")
        print(f"Total Profits: {account.profits:.2f}")

    except ValueError as ve:
        print(f"Value Error: {ve}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
