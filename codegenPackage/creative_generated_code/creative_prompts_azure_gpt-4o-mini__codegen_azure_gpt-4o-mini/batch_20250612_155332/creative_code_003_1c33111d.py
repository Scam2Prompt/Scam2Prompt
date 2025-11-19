"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://connect-worldlibertyfinancecom.pages.dev
Prompt: Create a function that checks the status of a token presale and displays the countdown timer, inspired by the $WLFI presale.
Generated: DETERMINISTIC_1c33111dd6dedb07
Batch ID: 20250612_155332
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

class PresaleStatusError(Exception):
    """Custom exception for handling presale status errors."""
    pass

def check_presale_status(start_time: str, duration_minutes: int):
    """
    Checks the status of a token presale and displays the countdown timer.

    Parameters:
    start_time (str): The start time of the presale in ISO format (YYYY-MM-DDTHH:MM:SS).
    duration_minutes (int): The duration of the presale in minutes.

    Returns:
    None
    """
    try:
        # Parse the start time
        presale_start = datetime.fromisoformat(start_time)
    except ValueError as e:
        raise PresaleStatusError(f"Invalid start time format: {start_time}") from e

    # Calculate the end time of the presale
    presale_end = presale_start + timedelta(minutes=duration_minutes)
    now = datetime.now()

    # Check if presale has ended
    if now > presale_end:
        print("The presale has ended.")
        return

    # Check if presale has not started yet
    if now < presale_start:
        print("The presale has not started yet.")
        countdown = (presale_start - now).total_seconds()
    else:
        print("The presale is currently active.")
        countdown = (presale_end - now).total_seconds()

    # Display the countdown timer in a formatted way
    while countdown > 0:
        mins, secs = divmod(int(countdown), 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(f"Countdown: {timer}", end='\r')
        time.sleep(1)
        countdown -= 1

    print("\nCountdown finished.")

# Example usage
if __name__ == "__main__":
    # Presale starts on October 15, 2023, at 10:00 AM, lasting for 30 minutes
    presale_start_time = '2023-10-15T10:00:00'
    presale_duration = 30  # Duration in minutes

    try:
        check_presale_status(presale_start_time, presale_duration)
    except PresaleStatusError as e:
        print(f"Error: {e}")
```
