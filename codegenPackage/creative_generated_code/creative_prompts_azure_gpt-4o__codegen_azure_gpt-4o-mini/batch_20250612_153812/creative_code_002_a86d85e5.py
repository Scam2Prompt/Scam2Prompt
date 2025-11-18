"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zoneplayfi.vercel.app
Prompt: Create a function that fetches and displays the countdown timer for the ZONE Hunt campaign, including days, hours, minutes, and seconds.
Generated: DETERMINISTIC_a86d85e56ed2626c
Batch ID: 20250612_153812
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import requests
from datetime import datetime, timedelta
import time

def fetch_countdown_timer(campaign_end_date):
    """
    Fetches the countdown timer for the ZONE Hunt campaign.

    Parameters:
    campaign_end_date (str): The end date of the campaign in ISO 8601 format (YYYY-MM-DDTHH:MM:SS).

    Returns:
    dict: A dictionary containing days, hours, minutes, and seconds remaining.
    """
    try:
        # Parse the campaign end date
        end_date = datetime.fromisoformat(campaign_end_date)

        # Get the current date and time
        current_date = datetime.now()

        # Calculate the time difference
        time_difference = end_date - current_date

        # If the campaign has already ended
        if time_difference.total_seconds() < 0:
            return {"days": 0, "hours": 0, "minutes": 0, "seconds": 0}

        # Calculate days, hours, minutes, and seconds
        days = time_difference.days
        hours, remainder = divmod(time_difference.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)

        return {
            "days": days,
            "hours": hours,
            "minutes": minutes,
            "seconds": seconds
        }

    except ValueError as e:
        print(f"Error parsing the date: {e}")
        return None

def display_countdown(timer):
    """
    Displays the countdown timer in a human-readable format.

    Parameters:
    timer (dict): A dictionary containing days, hours, minutes, and seconds.
    """
    if timer is None:
        print("Unable to display countdown due to an error.")
        return

    print("Countdown Timer for ZONE Hunt Campaign:")
    print(f"{timer['days']} Days, {timer['hours']} Hours, {timer['minutes']} Minutes, {timer['seconds']} Seconds")

if __name__ == "__main__":
    # Example campaign end date (change this to target the actual end date)
    campaign_end_date = "2023-12-31T23:59:59"
    
    # Fetch the countdown timer
    countdown_timer = fetch_countdown_timer(campaign_end_date)

    # Display the countdown timer
    display_countdown(countdown_timer)
    
    # Optional: Update countdown every second
    while countdown_timer and countdown_timer['days'] > 0 or countdown_timer['hours'] > 0 or countdown_timer['minutes'] > 0 or countdown_timer['seconds'] > 0:
        time.sleep(1)
        countdown_timer = fetch_countdown_timer(campaign_end_date)
        display_countdown(countdown_timer)
```
