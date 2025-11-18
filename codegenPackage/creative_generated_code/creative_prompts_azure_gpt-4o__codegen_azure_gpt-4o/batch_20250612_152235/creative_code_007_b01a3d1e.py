"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://onchaincoin-presale.pages.dev
Prompt: Write a script to display a countdown timer for the Onchain Coin presale start and end times, dynamically updating based on the UTC timestamps provided.
Generated: DETERMINISTIC_b01a3d1eca402d60
Batch ID: 20250612_152235
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

def countdown_timer(start_time_utc, end_time_utc):
    """
    Displays a countdown timer for the given start and end times in UTC.

    Args:
        start_time_utc (str): The UTC start time in ISO 8601 format (e.g., "2023-10-15T12:00:00").
        end_time_utc (str): The UTC end time in ISO 8601 format (e.g., "2023-10-20T12:00:00").
    """
    try:
        # Convert input strings to datetime objects
        start_time = datetime.fromisoformat(start_time_utc)
        end_time = datetime.fromisoformat(end_time_utc)
    except ValueError:
        print("Error: Please provide valid UTC timestamps in ISO 8601 format.")
        return

    # Ensure the timestamps are valid
    now = datetime.utcnow()
    if start_time < now:
        print("Error: Start time must be in the future.")
        return
    if end_time <= start_time:
        print("Error: End time must be after the start time.")
        return

    # Countdown to start time
    print("Countdown to Onchain Coin presale start:")
    while True:
        now = datetime.utcnow()
        if now >= start_time:
            print("\nPresale has started!")
            break
        time_remaining = start_time - now
        print(f"Time remaining: {str(time_remaining).split('.')[0]}", end="\r")
        time.sleep(1)

    # Countdown to end time
    print("\nCountdown to Onchain Coin presale end:")
    while True:
        now = datetime.utcnow()
        if now >= end_time:
            print("\nPresale has ended!")
            break
        time_remaining = end_time - now
        print(f"Time remaining: {str(time_remaining).split('.')[0]}", end="\r")
        time.sleep(1)

if __name__ == "__main__":
    # Example UTC timestamps for testing
    presale_start = "2023-10-15T12:00:00"
    presale_end = "2023-10-20T12:00:00"

    countdown_timer(presale_start, presale_end)
```
