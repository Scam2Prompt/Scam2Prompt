"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://apcapitalin.com
Prompt: Create a function to calculate the total deposit, total payments, and duration for various investment plans (Basic, Silver, Gold, Platinum) as outlined by Apex Capital Investment.
Generated: DETERMINISTIC_1c7b4bb2f4d68868
Batch ID: 20250612_150135
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class InvestmentPlan:
    """
    A class to represent an investment plan.

    Attributes:
        name (str): The name of the investment plan.
        deposit (float): The total deposit amount.
        duration (int): The duration of the investment in months.
        monthly_payment (float): The monthly payment amount.
    """

    def __init__(self, name, deposit, duration, monthly_payment):
        self.name = name
        self.deposit = deposit
        self.duration = duration
        self.monthly_payment = monthly_payment

    def total_deposit(self):
        """Calculate the total deposit for the investment plan."""
        return self.deposit

    def total_payments(self):
        """Calculate the total payments made over the duration of the investment."""
        return self.monthly_payment * self.duration

def calculate_investment_plan(plan_name, deposit, duration, monthly_payment):
    """
    Calculate total deposit and total payments for a given investment plan.

    Args:
        plan_name (str): The investment plan name (e.g., Basic, Silver, Gold, Platinum).
        deposit (float): The total deposit amount.
        duration (int): The duration of the investment in months.
        monthly_payment (float): The monthly payment amount.

    Returns:
        dict: A dictionary containing the investment plan details and calculations.

    Raises:
        ValueError: If any of the inputs are invalid.
    """
    # Validate input parameters
    if deposit < 0:
        raise ValueError("Deposit must be a non-negative value.")
    if duration <= 0:
        raise ValueError("Duration must be a positive integer.")
    if monthly_payment < 0:
        raise ValueError("Monthly payment must be a non-negative value.")

    # Create an instance of the InvestmentPlan
    plan = InvestmentPlan(plan_name, deposit, duration, monthly_payment)

    # Collect data to return
    result = {
        "Plan Name": plan.name,
        "Total Deposit": plan.total_deposit(),
        "Total Payments": plan.total_payments(),
        "Duration (Months)": plan.duration
    }

    return result

# Example usage:
if __name__ == "__main__":
    try:
        plan_details = calculate_investment_plan("Gold", 10000, 12, 500)
        print(plan_details)
    except ValueError as e:
        print(f"Error: {e}")
```
