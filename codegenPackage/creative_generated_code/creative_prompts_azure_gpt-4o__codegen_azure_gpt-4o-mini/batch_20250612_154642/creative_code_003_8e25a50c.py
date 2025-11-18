"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://safemoonmeme.com
Prompt: Write a script to calculate the time left until the SafeMoon token swap ends, using the countdown values (30 days, 18 hrs, 8 min, 52 sec) provided on the website.
Generated: DETERMINISTIC_8e25a50c7821c61a
Batch ID: 20250612_154642
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

def calculate_time_left(swap_duration):
    """
    Calculate the time left until the SafeMoon token swap ends.

    Parameters:
    swap_duration (dict): A dictionary containing the countdown values for days, hours, minutes, and seconds.

    Returns:
    str: A string representation of the time left in the format "DD days, HH hours, MM minutes, SS seconds".
    """
    try:
        # Extract countdown values from the dictionary
        days = swap_duration.get('days', 0)
        hours = swap_duration.get('hours', 0)
        minutes = swap_duration.get('minutes', 0)
        seconds = swap_duration.get('seconds', 0)

        # Validate input types
        if not all(isinstance(i, int) for i in [days, hours, minutes, seconds]):
            raise ValueError("All values must be integers.")

        # Calculate total remaining time in seconds
        total_seconds = (days * 86400) + (hours * 3600) + (minutes * 60) + seconds

        # Ensure total seconds is not negative
        if total_seconds < 0:
            raise ValueError("Time left cannot be negative.")

        # Calculate the time left
        time_left = datetime.timedelta(seconds=total_seconds)

        # Format the time left into days, hours, minutes, and seconds
        days_left = time_left.days
        hours_left, remainder = divmod(time_left.seconds, 3600)
        minutes_left, seconds_left = divmod(remainder, 60)

        return f"{days_left} days, {hours_left} hours, {minutes_left} minutes, {seconds_left} seconds"

    except Exception as e:
        return f"Error calculating time left: {e}"

if __name__ == "__main__":
    # Define the countdown values for the swap
    countdown_values = {
        'days': 30,
        'hours': 18,
        'minutes': 8,
        'seconds': 52
    }

    # Calculate and print the time left until the swap ends
    time_left = calculate_time_left(countdown_values)
    print(time_left)
```
