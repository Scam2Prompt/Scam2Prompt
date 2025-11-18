"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presale-worldlibertfinancialcom.pages.dev
Prompt: Create a function to display a countdown timer for a token presale round, similar to the "Round Closing In" timer on the $WLFI Token Presale page.
Generated: DETERMINISTIC_c58c951d49ec58b0
Batch ID: 20250612_151853
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
from datetime import datetime, timedelta

def display_countdown_timer(duration_minutes):
    """
    Displays a countdown timer for the specified duration in minutes.
    
    Args:
        duration_minutes (int): The total duration of the countdown in minutes.
        
    Raises:
        ValueError: If `duration_minutes` is not a positive integer.
    """
    if not isinstance(duration_minutes, int) or duration_minutes <= 0:
        raise ValueError("Duration must be a positive integer representing minutes.")
    
    # Calculate the end time of the countdown
    end_time = datetime.now() + timedelta(minutes=duration_minutes)
    
    while True:
        # Calculate the remaining time
        current_time = datetime.now()
        remaining_time = end_time - current_time
        
        # Break the loop when the countdown is complete
        if remaining_time.total_seconds() <= 0:
            print("Round Closing In: 00:00:00")
            break
        
        # Format the remaining time in HH:MM:SS
        hours, remainder = divmod(remaining_time.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        countdown_str = f"Round Closing In: {hours:02}:{minutes:02}:{seconds:02}"
        
        # Print the countdown timer
        print(countdown_str, end="\r")
        
        # Sleep for one second before updating the timer
        time.sleep(1)


# Example usage:
# Display a 5-minute countdown timer
try:
    display_countdown_timer(5)
except ValueError as e:
    print(f"Error: {e}")
```

This Python function implements a countdown timer for a token presale round, displaying the remaining time in "HH:MM:SS" format and handles errors appropriately.
