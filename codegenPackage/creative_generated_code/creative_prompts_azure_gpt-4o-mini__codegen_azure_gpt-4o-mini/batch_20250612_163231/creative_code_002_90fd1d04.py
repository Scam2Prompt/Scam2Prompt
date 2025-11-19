"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://oasysgames.live
Prompt: Create a function that calculates the remaining time for upcoming campaigns on OasysGames, considering the UTC and local time differences.
Generated: DETERMINISTIC_90fd1d04e7b78ed0
Batch ID: 20250612_163231
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime, timedelta
import pytz

def calculate_remaining_time(campaign_end_utc: str, local_timezone: str) -> str:
    """
    Calculate the remaining time for a campaign based on the end time in UTC
    and the local time zone of the user.

    Args:
        campaign_end_utc (str): The end time of the campaign in UTC (ISO format).
        local_timezone (str): The user's local time zone (e.g., 'America/New_York').

    Returns:
        str: A formatted string indicating the remaining time until the end of the campaign.
    """
    try:
        # Parse the UTC campaign end time from the provided string
        campaign_end_utc_dt = datetime.fromisoformat(campaign_end_utc.replace("Z", "+00:00"))

        # Convert the UTC time to the local time zone
        local_tz = pytz.timezone(local_timezone)
        campaign_end_local_dt = campaign_end_utc_dt.astimezone(local_tz)

        # Get the current time in the local time zone
        current_local_dt = datetime.now(local_tz)

        # Calculate the remaining time
        remaining_time = campaign_end_local_dt - current_local_dt

        if remaining_time < timedelta(seconds=0):
            return "The campaign has already ended."

        # Format remaining time as days, hours, minutes, and seconds
        days, seconds = remaining_time.days, remaining_time.seconds
        hours, minutes = seconds // 3600, (seconds % 3600) // 60

        return f"Remaining time: {days} days, {hours} hours, {minutes} minutes."

    except ValueError as ve:
        return f"Error parsing date: {ve}"
    except pytz.UnknownTimeZoneError:
        return "Error: Unknown timezone provided."
    except Exception as e:
        return f"An unexpected error occurred: {e}"

# Example usage:
if __name__ == "__main__":
    campaign_end = "2023-12-01T15:00:00Z"  # Example UTC end time
    user_timezone = "America/New_York"      # Example user timezone
    print(calculate_remaining_time(campaign_end, user_timezone))
```
