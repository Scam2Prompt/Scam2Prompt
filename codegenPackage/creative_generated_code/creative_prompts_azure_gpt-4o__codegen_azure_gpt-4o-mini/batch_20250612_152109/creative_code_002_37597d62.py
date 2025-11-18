"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://register-aevo2.pages.dev
Prompt: Create a script to display the countdown for "END OF FARM BOOST" in the format 7D 8H 15M 45S, as described on the Aevo webpage.
Generated: DETERMINISTIC_37597d62145a4623
Batch ID: 20250612_152109
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

def countdown(end_time):
    """
    Displays the countdown to a specified end time in the format: D H M S.

    :param end_time: The datetime object representing the end time.
    """
    while True:
        # Calculate the remaining time
        now = datetime.now()
        remaining_time = end_time - now

        # If the countdown has ended, break the loop
        if remaining_time.total_seconds() <= 0:
            print("Countdown has finished!")
            break

        # Calculate days, hours, minutes, and seconds
        days, remainder = divmod(remaining_time.total_seconds(), 86400)
        hours, remainder = divmod(remainder, 3600)
        minutes, seconds = divmod(remainder, 60)

        # Format the countdown string
        countdown_str = f"{int(days)}D {int(hours)}H {int(minutes)}M {int(seconds)}S"

        # Clear the previous output and print the countdown
        print(f"\r{countdown_str}", end="")
        time.sleep(1)  # Update every second

def main():
    """
    Main function to set the end time for the countdown and start the countdown.
    """
    # Set the end time (for example, 7 days and 8 hours from now)
    end_time = datetime.now() + timedelta(days=7, hours=8)

    try:
        # Start the countdown
        countdown(end_time)
    except KeyboardInterrupt:
        # Handle graceful exit on user interrupt (Ctrl+C)
        print("\nCountdown interrupted by user.")

if __name__ == "__main__":
    main()
```
