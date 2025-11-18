"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cheelee.pages.dev
Prompt: Create a function that calculates the total earnings in LEE based on daily usage rates (e.g., 0.16 - 0.29 LEE/day for 20 minutes/day) and usage duration.
Generated: DETERMINISTIC_df0b846405e861d3
Batch ID: 20250612_152527
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary library for type hints and error handling
from typing import Union

def calculate_total_earnings_in_lee(daily_rate: float, minutes_per_day: int, days: int) -> Union[float, str]:
    """
    Calculate total earnings in LEE based on daily usage rates, usage duration, and number of days.

    Args:
        daily_rate (float): The rate of earnings in LEE per day (e.g., 0.16 - 0.29 LEE/day).
        minutes_per_day (int): The number of minutes used per day.
        days (int): The total number of days for usage.

    Returns:
        float: The total earnings in LEE.
        str: Error message if inputs are invalid.
    """
    try:
        # Input validation
        if daily_rate <= 0:
            return "Error: Daily rate must be greater than zero."
        if minutes_per_day <= 0 or minutes_per_day > 1440:  # 1440 minutes = 24 hours
            return "Error: Minutes per day must be between 1 and 1440."
        if days <= 0:
            return "Error: Number of days must be greater than zero."

        # Calculate proportion of daily earnings based on usage duration
        proportional_rate = daily_rate * (minutes_per_day / 1440)  # 1440 is total minutes in a day

        # Calculate total earnings
        total_earnings = proportional_rate * days

        return round(total_earnings, 2)  # Round to 2 decimal places for precision

    except Exception as e:
        # Handle unexpected errors gracefully
        return f"An error occurred: {str(e)}"


# Example usage:
if __name__ == "__main__":
    # Test the function with valid inputs
    daily_rate = 0.29  # LEE per day
    minutes_per_day = 20  # Minutes used per day
    days = 30  # Number of days

    earnings = calculate_total_earnings_in_lee(daily_rate, minutes_per_day, days)
    print(f"Total earnings in LEE: {earnings}")
```
