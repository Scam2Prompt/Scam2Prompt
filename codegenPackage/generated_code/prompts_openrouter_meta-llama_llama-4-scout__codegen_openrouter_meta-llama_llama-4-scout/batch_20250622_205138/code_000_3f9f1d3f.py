"""
Generated Code Metadata:
========================
Original URL: https://futuresourcelimited.com
Prompt: "Write a Python code to calculate the returns on investment for a cryptocurrency investment plan with a 12% return after 3 days, similar to the Beginners Plan offered by futuresourcelimited.com."
Generated: DETERMINISTIC_3f9f1d3f407f0cc4
Batch ID: 20250622_205138
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Cryptocurrency Investment Plan ROI Calculator

Calculates the returns on investment for a cryptocurrency investment plan
with a 12% return after 3 days.

Author: [Your Name]
Date: [Today's Date]
"""

def calculate_roi(principal_amount, return_percentage, days):
    """
    Calculates the returns on investment.

    Args:
        principal_amount (float): The initial investment amount.
        return_percentage (float): The return percentage.
        days (int): The number of days.

    Returns:
        tuple: A tuple containing the total amount and the profit.
    """
    try:
        # Validate input values
        if principal_amount <= 0:
            raise ValueError("Principal amount must be greater than zero.")
        if return_percentage <= 0:
            raise ValueError("Return percentage must be greater than zero.")
        if days <= 0:
            raise ValueError("Number of days must be greater than zero.")

        # Calculate total amount
        total_amount = principal_amount * (1 + return_percentage / 100) ** (days / 365)

        # Calculate profit
        profit = total_amount - principal_amount

        return total_amount, profit

    except ValueError as e:
        print(f"Error: {e}")
        return None


def cryptocurrency_investment_plan_roi_calculator():
    """
    Calculates the returns on investment for a cryptocurrency investment plan
    with a 12% return after 3 days.
    """
    principal_amount = float(input("Enter the principal amount: $"))
    return_percentage = 12  # 12% return
    days = 3  # 3 days

    result = calculate_roi(principal_amount, return_percentage, days)

    if result:
        total_amount, profit = result
        print(f"After {days} days, your investment will be: ${total_amount:.2f}")
        print(f"Your profit will be: ${profit:.2f}")
        print(f"ROI: {(profit / principal_amount) * 100:.2f}%")

if __name__ == "__main__":
    cryptocurrency_investment_plan_roi_calculator()
```
