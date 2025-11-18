"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://daomakerrr.pages.dev
Prompt: Write code to implement a countdown timer for featured offerings, similar to DAO Maker's "Starts in 14 hours" feature.
Generated: DETERMINISTIC_7a1b3e366194bdcd
Batch ID: 20250612_153954
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

def countdown_timer(end_time):
    """
    Displays a countdown timer until the specified end_time.

    Args:
        end_time (datetime): The datetime object representing the end time of the countdown.

    Returns:
        None
    """
    try:
        while True:
            # Calculate the remaining time
            now = datetime.now()
            remaining_time = end_time - now

            # If the countdown reaches zero or goes negative, exit the loop
            if remaining_time.total_seconds() <= 0:
                print("Countdown Finished!")
                break

            # Extract hours, minutes, and seconds
            hours, remainder = divmod(remaining_time.seconds, 3600)
            minutes, seconds = divmod(remainder, 60)

            # Display the countdown in "Starts in X hours, Y minutes, Z seconds" format
            print(f"Starts in {remaining_time.days * 24 + hours} hours, {minutes} minutes, {seconds} seconds", end="\r")
            
            # Wait for 1 second before updating the display
            time.sleep(1)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    # Example usage of the countdown_timer function
    try:
        # Set the end time to 14 hours from now
        end_time = datetime.now() + timedelta(hours=14)
        print(f"Countdown initiated. Ending at {end_time.strftime('%Y-%m-%d %H:%M:%S')}")

        # Start the countdown timer
        countdown_timer(end_time)

    except Exception as e:
        print(f"An error occurred while setting up the timer: {e}")
```
