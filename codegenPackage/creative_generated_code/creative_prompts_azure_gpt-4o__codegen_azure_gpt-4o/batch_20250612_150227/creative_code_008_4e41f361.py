"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polymarketscanner.com
Prompt: Write a function to calculate and display the next fetch time based on Polymarket Scanner's fetch interval settings.
Generated: DETERMINISTIC_4e41f3610cb95571
Batch ID: 20250612_150227
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime, timedelta

def calculate_next_fetch_time(current_time: datetime, fetch_interval_seconds: int) -> str:
    """
    Calculate and display the next fetch time based on the given fetch interval.

    Parameters:
    - current_time (datetime): The current datetime.
    - fetch_interval_seconds (int): The fetch interval in seconds.

    Returns:
    - str: The next fetch time as a formatted string.
    """
    try:
        # Validate that fetch_interval_seconds is non-negative
        if fetch_interval_seconds < 0:
            raise ValueError("Fetch interval must be a non-negative integer.")

        # Calculate the next fetch time
        next_fetch_time = current_time + timedelta(seconds=fetch_interval_seconds)

        # Return the next fetch time as a formatted string
        return next_fetch_time.strftime("%Y-%m-%d %H:%M:%S")
    except Exception as e:
        # Handle unexpected errors and log them
        return f"Error calculating next fetch time: {str(e)}"

# Example Usage:
if __name__ == "__main__":
    # Current timestamp
    current_time = datetime.now()

    # Example fetch interval (e.g., 300 seconds = 5 minutes)
    fetch_interval_seconds = 300  # Replace with dynamic input if necessary, e.g., from a config file

    # Calculate and print the next fetch time
    print("Current Time:", current_time.strftime("%Y-%m-%d %H:%M:%S"))
    next_time = calculate_next_fetch_time(current_time, fetch_interval_seconds)
    print("Next Fetch Time:", next_time)
```
