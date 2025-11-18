"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wynn-seven.vercel.app
Prompt: Create a program to display a countdown timer for campaigns, like the time left for the $WYNN Hunt, using JavaScript or Python.
Generated: DETERMINISTIC_d6e7e5177c789f4b
Batch ID: 20250612_154029
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is the code written in Python:

```python
import time
from datetime import datetime, timedelta


def start_countdown_timer(end_time):
    """
    Starts a countdown timer until the specified end time.
    
    Parameters:
    end_time (datetime): The datetime object representing the campaign end time.

    Returns:
    None
    """
    try:
        # Validate input
        if not isinstance(end_time, datetime):
            raise ValueError("end_time must be a datetime object.")
        
        # Get the current time
        current_time = datetime.now()

        # Check if the end time is in the past
        if end_time <= current_time:
            print("The campaign has already ended.")
            return

        # Calculate the remaining time
        remaining_time = end_time - current_time

        print(f"Countdown for campaign ends at: {end_time}")
        print("Time remaining:")

        while remaining_time.total_seconds() > 0:
            # Recalculate remaining time
            current_time = datetime.now()
            remaining_time = end_time - current_time

            # Extract hours, minutes, and seconds from remaining time
            hours, remainder = divmod(remaining_time.seconds, 3600)
            minutes, seconds = divmod(remainder, 60)

            # Display the countdown
            print(f"\r{remaining_time.days} days, {hours:02d}:{minutes:02d}:{seconds:02d}", end="")

            # Sleep for 1 second before updating
            time.sleep(1)

        # Clear the countdown display
        print("\rThe campaign has ended.                          ")

    except ValueError as ve:
        print(f"ValueError: {ve}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    # Example usage:
    # Set the campaign end time (e.g., 1 day from now for demonstration purposes)
    campaign_end_time = datetime.now() + timedelta(days=1)

    # Start the countdown timer
    start_countdown_timer(campaign_end_time)
```

This Python program starts a countdown timer until a given campaign end time. You can modify the `campaign_end_time` variable in the `if __name__ == "__main__"` section to your desired datetime. The program handles errors gracefully, ensuring production-ready quality.
