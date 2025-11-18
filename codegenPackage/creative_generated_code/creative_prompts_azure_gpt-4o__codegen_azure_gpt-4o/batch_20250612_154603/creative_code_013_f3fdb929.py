"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://accesslinklimited.com
Prompt: Write code to simulate the investment process, including plan selection, deposit tracking, and interest accumulation, as described on Access Link Limited's platform.
Generated: DETERMINISTIC_f3fdb92911974a4e
Batch ID: 20250612_154603
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class InvestmentPlan:
    """
    A class to represent an investment plan.
    """
    def __init__(self, name, interest_rate, duration):
        """
        Initializes the InvestmentPlan class.

        Args:
            name (str): Name of the investment plan.
            interest_rate (float): Annual interest rate (in percentage).
            duration (int): Duration of the plan in days.
        """
        self.name = name
        self.interest_rate = interest_rate
        self.duration = duration


class Investment:
    """
    A class to represent an individual investment.
    """
    def __init__(self, plan, deposit_amount):
        """
        Initializes the Investment class.

        Args:
            plan (InvestmentPlan): The investment plan selected.
            deposit_amount (float): The amount deposited for the investment.
        """
        self.plan = plan
        self.deposit_amount = deposit_amount
        self.start_date = datetime.datetime.now()
        self.end_date = self.start_date + datetime.timedelta(days=plan.duration)
        self.interest_earned = 0

    def calculate_interest(self):
        """
        Calculates the interest earned based on the investment plan and deposit.
        """
        daily_interest_rate = self.plan.interest_rate / 100 / 365
        self.interest_earned = self.deposit_amount * daily_interest_rate * self.plan.duration
        return self.interest_earned


def simulate_investment():
    """
    Simulates the investment process including plan selection, deposit tracking,
    and interest accumulation.
    """
    print("Welcome to Access Link Limited Investment Platform!")
    print("Available Investment Plans:")
    
    # Define some sample investment plans
    plans = [
        InvestmentPlan("Basic Plan", 5, 30),
        InvestmentPlan("Premium Plan", 7, 60),
        InvestmentPlan("Elite Plan", 10, 90)
    ]
    
    for idx, plan in enumerate(plans, start=1):
        print(f"{idx}. {plan.name} - Interest Rate: {plan.interest_rate}%, Duration: {plan.duration} days")
    
    # Let the user select a plan
    try:
        selected_plan_index = int(input("Select a plan by entering the corresponding number: ")) - 1
        if selected_plan_index < 0 or selected_plan_index >= len(plans):
            raise ValueError("Invalid plan selection.")
        selected_plan = plans[selected_plan_index]
    except ValueError as e:
        print(f"Error: {e}. Please restart the simulation.")
        return

    # Let the user enter a deposit amount
    try:
        deposit_amount = float(input(f"Enter deposit amount for the {selected_plan.name}: "))
        if deposit_amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")
    except ValueError as e:
        print(f"Error: {e}. Please restart the simulation.")
        return

    # Create an investment object and calculate interest
    investment = Investment(selected_plan, deposit_amount)
    interest = investment.calculate_interest()
    print("\nInvestment Summary:")
    print(f"Plan Name: {investment.plan.name}")
    print(f"Deposit Amount: ${investment.deposit_amount:.2f}")
    print(f"Start Date: {investment.start_date.strftime('%Y-%m-%d')}")
    print(f"End Date: {investment.end_date.strftime('%Y-%m-%d')}")
    print(f"Interest Earned: ${interest:.2f}")


if __name__ == "__main__":
    simulate_investment()
```
