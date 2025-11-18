"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mellstroy-eth.vercel.app
Prompt: Create a script to display a countdown timer for campaigns, similar to the "Time Left" feature on the MELLSTROY Hunt page.
Generated: DETERMINISTIC_0e74c1bf782e78cc
Batch ID: 20250612_154635
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
    Displays a countdown timer for a given end time, updating every second.
    
    Args:
        end_time (datetime): The end time for the countdown timer.
    """
    try:
        while True:
            # Get current time
            current_time = datetime.now()

            # Calculate the time remaining
            time_remaining = end_time - current_time

            # If the countdown has reached zero, exit the loop
            if time_remaining.total_seconds() <= 0:
                print("The campaign has ended!")
                break

            # Extract days, hours, minutes, and seconds from remaining time
            days = time_remaining.days
            hours, remainder = divmod(time_remaining.seconds, 3600)
            minutes, seconds = divmod(remainder, 60)

            # Display the countdown in "DD HH:MM:SS" format
            print(f"Time Left: {days}d {hours:02}h {minutes:02}m {seconds:02}s", end="\r", flush=True)

            # Wait for 1 second before updating
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nCountdown interrupted.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # End time for the campaign (example: 1 day from now)
    campaign_end_time = datetime.now() + timedelta(days=1)

    # Print initial message
    print("Campaign Countdown Timer")
    print("========================")

    # Start the countdown timer
    countdown_timer(campaign_end_time)
```
