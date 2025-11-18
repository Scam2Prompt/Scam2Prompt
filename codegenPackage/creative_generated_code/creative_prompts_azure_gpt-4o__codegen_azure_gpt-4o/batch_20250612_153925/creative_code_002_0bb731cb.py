"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://avabase.vercel.app
Prompt: Generate code to create a countdown timer for a crypto campaign, showing days, hours, minutes, and seconds remaining, similar to the AVAAI Hunt timer.
Generated: DETERMINISTIC_0bb731cbe640e1c6
Batch ID: 20250612_153925
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
    Function to display a countdown timer that shows days, hours, 
    minutes, and seconds remaining until a specified end time.

    Args:
        end_time (datetime): The target datetime for the countdown to end.
    """
    try:
        while True:
            # Calculate the remaining time
            now = datetime.now()
            remaining_time = end_time - now

            # Break the loop if the countdown has ended
            if remaining_time.total_seconds() <= 0:
                print("Campaign has ended!")
                break

            # Extract days, hours, minutes, and seconds from the remaining time
            days = remaining_time.days
            hours, remainder = divmod(remaining_time.seconds, 3600)
            minutes, seconds = divmod(remainder, 60)

            # Display the countdown in a readable format
            print(f"Time Remaining: {days}d {hours}h {minutes}m {seconds}s", end="\r")

            # Wait for 1 second before updating the timer
            time.sleep(1)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Define the end time for the campaign (example: 3 days from now)
    campaign_duration = timedelta(days=3)
    campaign_end_time = datetime.now() + campaign_duration

    print("Crypto Campaign Countdown Timer")
    print("================================")
    countdown_timer(campaign_end_time)
```
