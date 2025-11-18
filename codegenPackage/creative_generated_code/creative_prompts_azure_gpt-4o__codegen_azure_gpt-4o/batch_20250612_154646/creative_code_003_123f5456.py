"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stowawaypay.com
Prompt: Create a function that calculates savings milestones for users based on the "Simple savings for non-bank customers" model described on StowAwayPay.com.
Generated: DETERMINISTIC_123f5456b0c1977d
Batch ID: 20250612_154646
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Filename: savings_milestones.py

def calculate_savings_milestones(goal_amount, monthly_savings, interest_rate, duration_months):
    """
    Calculate savings milestones based on the "Simple savings for non-bank customers" model.

    Parameters:
    - goal_amount (float): The total savings goal in dollars.
    - monthly_savings (float): The monthly contribution in dollars.
    - interest_rate (float): Annual interest rate (e.g., 0.05 for 5% interest).
    - duration_months (int): The duration in months during which savings will be accumulated.

    Returns:
    - milestones (list of dict): A list of milestone dictionaries with 'month' and 'balance'.
    """
    if monthly_savings <= 0:
        raise ValueError("Monthly savings must be greater than 0.")
    if interest_rate < 0 or interest_rate > 1:
        raise ValueError("Interest rate must be between 0 and 1.")
    if duration_months <= 0:
        raise ValueError("Duration must be greater than 0.")
    if goal_amount <= 0:
        raise ValueError("Goal amount must be greater than 0.")

    milestones = []
    current_balance = 0.0
    monthly_interest_rate = interest_rate / 12

    for month in range(1, duration_months + 1):
        current_balance += monthly_savings  # Add monthly savings
        current_balance += current_balance * monthly_interest_rate  # Apply interest

        # Record the milestone
        milestones.append({
            "month": month,
            "balance": round(current_balance, 2)  # Rounded for better readability
        })

        # Stop if the goal is reached or exceeded
        if current_balance >= goal_amount:
            break

    return milestones


# Example usage:
if __name__ == "__main__":
    try:
        goal = 10000  # Goal amount: $10,000
        monthly_save = 500  # Monthly savings: $500
        interest = 0.05  # Annual interest rate: 5%
        months_duration = 24  # Savings period: 24 months

        milestones = calculate_savings_milestones(goal, monthly_save, interest, months_duration)
        for milestone in milestones:
            print(f"Month {milestone['month']}: ${milestone['balance']}")
    except ValueError as e:
        print(f"Error: {e}")
```
