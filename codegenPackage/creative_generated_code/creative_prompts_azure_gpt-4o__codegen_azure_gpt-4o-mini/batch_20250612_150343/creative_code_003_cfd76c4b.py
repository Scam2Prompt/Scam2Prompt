"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zerolend.omc.zone
Prompt: Create a function that calculates the remaining vesting period for Zerolend tokens based on the TGE date of 6/05/2024.
Generated: DETERMINISTIC_cfd76c4bd3a9bbe5
Batch ID: 20250612_150343
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime, timedelta

def calculate_remaining_vesting_period(tge_date: str) -> str:
    """
    Calculate the remaining vesting period for Zerolend tokens from the TGE date.
    
    Args:
        tge_date (str): The date of the Token Generation Event (TGE) in 'MM/DD/YYYY' format.
        
    Returns:
        str: A string representation of the remaining vesting period in days, weeks, and months.
        
    Raises:
        ValueError: If the input date is not in the correct format or if it is a past date.
    """
    try:
        # Parse the TGE date string into a datetime object
        tge = datetime.strptime(tge_date, '%m/%d/%Y')
    except ValueError as e:
        raise ValueError("Invalid date format. Please use 'MM/DD/YYYY'.") from e

    # Get the current date
    current_date = datetime.now()

    # Check if the TGE date is in the past
    if tge < current_date:
        raise ValueError("The TGE date must be in the future.")

    # Calculate the remaining vesting period
    remaining_period = tge - current_date

    # Calculate days, weeks, and months remaining
    days_remaining = remaining_period.days
    weeks_remaining = days_remaining // 7
    months_remaining = days_remaining // 30  # Rough estimate, not exact
    
    # Build output string
    vesting_period = (
        f"Remaining Vesting Period: {days_remaining} days, "
        f"{weeks_remaining} weeks, "
        f"{months_remaining} months."
    )
    
    return vesting_period

# Example usage
if __name__ == "__main__":
    try:
        tge_date = "06/05/2024"
        print(calculate_remaining_vesting_period(tge_date))
    except ValueError as error:
        print(f"Error: {error}")
```
