"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://minebnb.pro
Prompt: Write a Python script to simulate cloud mining using the tariff plans described on the MineBNB website, including calculations for ROI based on deposit amounts and durations.
Generated: DETERMINISTIC_70548ac00c7c677a
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

class CloudMiningPlan:
    """Class representing a cloud mining tariff plan."""
    
    def __init__(self, name, daily_rate, min_deposit, max_deposit, duration_days):
        """
        Initializes a CloudMiningPlan object.

        Args:
            name (str): The name of the plan.
            daily_rate (float): Daily earnings rate (percentage).
            min_deposit (float): Minimum deposit required for the plan.
            max_deposit (float): Maximum deposit allowed for the plan.
            duration_days (int): Duration of the plan in days.
        """
        self.name = name
        self.daily_rate = daily_rate
        self.min_deposit = min_deposit
        self.max_deposit = max_deposit
        self.duration_days = duration_days

    def calculate_earnings(self, deposit):
        """
        Calculates total earnings based on the deposit and duration.

        Args:
            deposit (float): The amount deposited.

        Returns:
            float: Total earnings after the specified duration.
        """
        if deposit < self.min_deposit or deposit > self.max_deposit:
            raise ValueError(f"Deposit must be between {self.min_deposit} and {self.max_deposit}.")

        total_earnings = deposit * (self.daily_rate / 100) * self.duration_days
        return total_earnings

    def calculate_roi(self, deposit):
        """
        Calculates the return on investment (ROI).

        Args:
            deposit (float): The amount deposited.

        Returns:
            float: ROI percentage based on the deposit and earnings.
        """
        earnings = self.calculate_earnings(deposit)
        roi = (earnings / deposit) * 100
        return roi


def main():
    """Main function to simulate cloud mining."""
    
    # Define cloud mining plans (example data)
    plans = [
        CloudMiningPlan("Basic Plan", daily_rate=1.5, min_deposit=100, max_deposit=1000, duration_days=30),
        CloudMiningPlan("Standard Plan", daily_rate=2.0, min_deposit=1000, max_deposit=5000, duration_days=60),
        CloudMiningPlan("Premium Plan", daily_rate=2.5, min_deposit=5000, max_deposit=20000, duration_days=90)
    ]

    # User input for simulation
    try:
        plan_name = input("Enter the plan name (Basic Plan, Standard Plan, Premium Plan): ")
        deposit = float(input("Enter your deposit amount: "))

        # Find the selected plan
        selected_plan = next((plan for plan in plans if plan.name == plan_name), None)
        if selected_plan is None:
            raise ValueError("Invalid plan name entered.")

        # Calculate earnings and ROI
        earnings = selected_plan.calculate_earnings(deposit)
        roi = selected_plan.calculate_roi(deposit)

        # Display results
        print(f"Selected Plan: {selected_plan.name}")
        print(f"Total Earnings after {selected_plan.duration_days} days: {earnings:.2f}")
        print(f"Return on Investment (ROI): {roi:.2f}%")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
```
