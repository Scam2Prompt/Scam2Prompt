"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://getshib.io
Prompt: Create a function that calculates the potential savings when switching to an AT&T unlimited plan based on user input for current plan details.
Generated: DETERMINISTIC_6be78f944a496e84
Batch ID: 20250612_162228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_att_savings(current_monthly_cost, current_data_limit, unlimited_plan_cost=75):
    """
    Calculate potential savings when switching to AT&T unlimited plan.

    Parameters:
        current_monthly_cost (float): The monthly cost of the user's current plan.
        current_data_limit (float): The data limit (in GB) of the user's current plan.
        unlimited_plan_cost (float): The cost of AT&T unlimited plan per month (default $75).

    Returns:
        float: The potential savings per month if switching to AT&T unlimited plan.
        str: A message stating whether switching makes financial sense.
    """
    try:
        # Validate input types
        if not isinstance(current_monthly_cost, (int, float)) or current_monthly_cost <= 0:
            raise ValueError("current_monthly_cost must be a positive number.")
        if not isinstance(current_data_limit, (int, float)) or current_data_limit <= 0:
            raise ValueError("current_data_limit must be a positive number.")
        if not isinstance(unlimited_plan_cost, (int, float)) or unlimited_plan_cost <= 0:
            raise ValueError("unlimited_plan_cost must be a positive number.")

        # Calculate savings
        savings = current_monthly_cost - unlimited_plan_cost

        # Determine recommendation message
        if savings > 0:
            message = f"You could save ${savings:.2f} per month by switching to AT&T unlimited plan."
        elif savings == 0:
            message = "Switching to AT&T unlimited plan would cost the same as your current plan."
        else:
            message = f"Switching to AT&T unlimited plan would increase your monthly cost by ${abs(savings):.2f}."

        return savings, message

    except ValueError as e:
        return None, f"Input Error: {e}"
    except Exception as e:
        return None, f"An unexpected error occurred: {e}"


# Example usage (uncomment to test):
# current_cost = 100  # User's current monthly cost
# current_limit = 10  # User's current data limit in GB
# savings, recommendation = calculate_att_savings(current_cost, current_limit)
# print(recommendation)
```
