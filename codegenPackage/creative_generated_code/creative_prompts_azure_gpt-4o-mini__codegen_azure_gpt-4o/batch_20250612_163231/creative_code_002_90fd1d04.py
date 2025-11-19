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
from datetime import datetime, timezone, timedelta

def calculate_remaining_time(campaign_end_datetime_utc, user_local_timezone_offset):
    """
    Calculate the remaining time for upcoming campaigns on OasysGames.
    
    Args:
        campaign_end_datetime_utc (str): The campaign's end date-time in UTC as an ISO 8601 string.
        user_local_timezone_offset (int): The user's local timezone offset in hours (e.g., +3 or -5).
    
    Returns:
        dict: A dictionary containing the remaining time in days, hours, minutes, and seconds.
    """
    try:
        # Parse the campaign end date-time in UTC
        campaign_end_utc = datetime.fromisoformat(campaign_end_datetime_utc).replace(tzinfo=timezone.utc)
        
        # Get the current UTC time
        current_utc = datetime.now(timezone.utc)
        
        # Calculate the remaining time in UTC
        remaining_time_utc = campaign_end_utc - current_utc
        
        # If the campaign has already ended
        if remaining_time_utc.total_seconds() <= 0:
            return {
                "days": 0,
                "hours": 0,
                "minutes": 0,
                "seconds": 0,
                "message": "The campaign has already ended."
            }
        
        # Convert UTC remaining time to the user's local time
        user_local_offset = timedelta(hours=user_local_timezone_offset)
        campaign_end_local = campaign_end_utc + user_local_offset
        remaining_time_local = campaign_end_local - current_utc
        
        # Extract days, hours, minutes, and seconds from the remaining time
        days = remaining_time_local.days
        hours, remainder = divmod(remaining_time_local.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        
        # Return a dictionary of the remaining time in local timezone
        return {
            "days": days,
            "hours": hours,
            "minutes": minutes,
            "seconds": seconds,
            "message": "Campaign is ongoing."
        }
    except ValueError as e:
        # Handle incorrect date-time format or other value errors
        return {"error": f"Invalid input: {str(e)}"}
    except Exception as e:
        # Handle any unexpected exceptions
        return {"error": f"An unexpected error occurred: {str(e)}"}

# Example usage:
if __name__ == "__main__":
    campaign_end_utc = "2023-12-25T12:00:00"
    local_offset = -5  # User's local timezone offset in hours
    print(calculate_remaining_time(campaign_end_utc, local_offset))
```
