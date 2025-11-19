"""
Generated Code Metadata:
========================
Original URL: https://oasysgames.live
Prompt: Create a function that calculates the remaining time for upcoming campaigns on OasysGames, considering the UTC and local time differences.
Generated: DETERMINISTIC_90fd1d04e7b78ed0
Batch ID: 20250612_163231
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime
import pytz

def calculate_campaign_time(campaign_start_time: str, campaign_end_time: str) -> dict:
    """
    Calculate the remaining time for upcoming campaigns on OasysGames.

    Args:
    - campaign_start_time (str): The start time of the campaign in UTC, format: 'YYYY-MM-DD HH:MM:SS'.
    - campaign_end_time (str): The end time of the campaign in UTC, format: 'YYYY-MM-DD HH:MM:SS'.

    Returns:
    - dict: A dictionary containing the remaining time in days, hours, minutes, and seconds.
    """

    # Define the UTC timezone
    utc_timezone = pytz.UTC

    # Parse the campaign start and end times from strings to datetime objects in UTC
    try:
        campaign_start_time_utc = utc_timezone.localize(datetime.strptime(campaign_start_time, '%Y-%m-%d %H:%M:%S'))
        campaign_end_time_utc = utc_timezone.localize(datetime.strptime(campaign_end_time, '%Y-%m-%d %H:%M:%S'))
    except ValueError:
        raise ValueError("Invalid date format. Please use 'YYYY-MM-DD HH:MM:SS'.")

    # Get the current time in UTC
    current_time_utc = datetime.now(utc_timezone)

    # Check if the campaign has started and not ended
    if current_time_utc < campaign_start_time_utc:
        # Calculate the remaining time until the campaign starts
        remaining_time = campaign_start_time_utc - current_time_utc
    elif current_time_utc < campaign_end_time_utc:
        # Calculate the remaining time until the campaign ends
        remaining_time = campaign_end_time_utc - current_time_utc
    else:
        # The campaign has ended
        return {"days": 0, "hours": 0, "minutes": 0, "seconds": 0}

    # Calculate the remaining time in days, hours, minutes, and seconds
    days = remaining_time.days
    hours, remainder = divmod(remaining_time.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    return {"days": days, "hours": hours, "minutes": minutes, "seconds": seconds}


def main():
    campaign_start_time = '2024-09-20 10:00:00'
    campaign_end_time = '2024-09-25 10:00:00'

    try:
        remaining_time = calculate_campaign_time(campaign_start_time, campaign_end_time)
        print(f"Remaining time: {remaining_time['days']} days, {remaining_time['hours']} hours, {remaining_time['minutes']} minutes, {remaining_time['seconds']} seconds")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
