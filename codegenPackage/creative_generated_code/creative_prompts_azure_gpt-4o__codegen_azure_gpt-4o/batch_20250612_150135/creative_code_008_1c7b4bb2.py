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
from typing import Dict, Tuple, Union

# Define a dictionary to hold investment plan details
investment_plans = {
    "Basic": {"rate": 0.05, "duration": 6},  # 5% rate per month, 6 months duration
    "Silver": {"rate": 0.07, "duration": 12},  # 7% rate per month, 12 months duration
    "Gold": {"rate": 0.1, "duration": 18},  # 10% rate per month, 18 months duration
    "Platinum": {"rate": 0.15, "duration": 24},  # 15% rate per month, 24 months duration
}

def calculate_investment(plan_name: str, monthly_deposit: Union[int, float]) -> Tuple[float, float, int]:
    """
    Calculate total deposit, total payments, and duration for an investment plan.

    Args:
        plan_name (str): Name of the investment plan (Basic, Silver, Gold, Platinum).
        monthly_deposit (Union[int, float]): Amount deposited monthly.

    Returns:
        Tuple[float, float, int]: Total deposit, total payments, and duration in months.
    
    Raises:
        ValueError: If the plan_name is invalid or monthly_deposit is negative.
    """
    # Validate the investment plan
    if plan_name not in investment_plans:
        raise ValueError(f"Invalid plan name. Available plans: {', '.join(investment_plans.keys())}")
    
    # Validate the monthly deposit amount
    if monthly_deposit < 0:
        raise ValueError("Monthly deposit must be a non-negative value.")
    
    # Retrieve the plan details
    plan_details = investment_plans[plan_name]
    rate = plan_details["rate"]
    duration = plan_details["duration"]
    
    # Calculate total deposit
    total_deposit = monthly_deposit * duration
    
    # Calculate total payments (including interest)
    total_payments = total_deposit * (1 + rate * duration)
    
    return total_deposit, total_payments, duration

# Example Usage:
if __name__ == "__main__":
    try:
        # User input
        plan = "Gold"
        monthly_amount = 500  # Monthly deposit amount
        
        # Perform calculation
        deposit, payments, term = calculate_investment(plan, monthly_amount)
        
        # Display results
        print(f"Plan: {plan}")
        print(f"Monthly Deposit: ${monthly_amount}")
        print(f"Total Deposit: ${deposit:.2f}")
        print(f"Total Payments (with interest): ${payments:.2f}")
        print(f"Duration: {term} months")
    except ValueError as e:
        print(f"Error: {e}")
```
