"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zerolend.omc.zone
Prompt: Generate a function that calculates the vesting amount for a user based on a 12-month linear vesting period after a 1-month cliff.
Generated: DETERMINISTIC_5a7ec8b1b8b4ed73
Batch ID: 20250612_135324
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime, timedelta

def calculate_vesting_amount(total_amount, start_date, current_date):
    """
    Calculates the vested amount of a user's grant based on a 12-month linear vesting schedule
    after a 1-month cliff.

    Parameters:
    - total_amount (float): The total grant amount.
    - start_date (datetime): The grant start date.
    - current_date (datetime): The date for which the vested amount is calculated.

    Returns:
    - float: The vested amount as of the current_date.
    """
    # Validate input
    if total_amount <= 0:
        raise ValueError("Total amount must be greater than 0")
    if not isinstance(start_date, datetime) or not isinstance(current_date, datetime):
        raise TypeError("start_date and current_date must be datetime objects")
    if current_date < start_date:
        raise ValueError("current_date cannot be earlier than start_date")

    # Define the cliff period (1 month) and vesting period (12 months)
    cliff_period = timedelta(days=30)  # 1-month cliff
    vesting_period = timedelta(days=365)  # 12-month linear vesting

    # Calculate the cliff end date
    cliff_end_date = start_date + cliff_period

    # If the current date is before the cliff end date, no vesting occurs
    if current_date < cliff_end_date:
        return 0.0

    # If the current date is beyond the vesting period, the entire amount is vested
    if current_date >= start_date + vesting_period:
        return total_amount

    # Calculate the vested amount linearly
    days_since_cliff = (current_date - cliff_end_date).days
    total_vesting_days = 365 - cliff_period.days  # Remaining days after cliff
    vested_amount = (days_since_cliff / total_vesting_days) * total_amount

    return round(vested_amount, 2)  # Return the vested amount rounded to 2 decimal places


# Example usage:
if __name__ == "__main__":
    try:
        # Grant details
        total_grant = 12000.0  # Total amount
        grant_start_date = datetime(2023, 1, 1)  # Start date
        query_date = datetime(2023, 8, 15)  # Current date to query

        vested = calculate_vesting_amount(total_grant, grant_start_date, query_date)
        print(f"Vested amount as of {query_date.date()}: ${vested}")
    except Exception as e:
        print(f"Error: {e}")
```
