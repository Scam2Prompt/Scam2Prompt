"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://oasysgames.live
Prompt: Generate code to implement a countdown timer for the "Ending Soon" campaigns on OasysGames, using the local time settings provided.
Generated: DETERMINISTIC_1ded47032d92fd7e
Batch ID: 20250612_163231
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

def start_countdown_timer(end_time):
    """
    Starts a countdown timer for an "Ending Soon" campaign.

    Args:
        end_time (datetime): The local time when the campaign ends.
    """
    try:
        # Validate that end_time is a datetime object
        if not isinstance(end_time, datetime):
            raise ValueError("end_time must be a valid datetime object.")

        current_time = datetime.now()
        if end_time <= current_time:
            print("The campaign has already ended.")
            return

        print("Countdown timer started!")
        while current_time < end_time:
            # Calculate remaining time
            remaining_time = end_time - current_time

            # Extract hours, minutes, and seconds
            hours, remainder = divmod(remaining_time.seconds, 3600)
            minutes, seconds = divmod(remainder, 60)

            print(f"Time Remaining: {remaining_time.days} days, {hours:02}:{minutes:02}:{seconds:02}", end="\r")
            time.sleep(1)  # Wait for 1 second
            current_time = datetime.now()

        print("\nCampaign has ended!")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    try:
        # Example: End time is set to 1 minute from now, using local time settings
        local_time = datetime.now()
        campaign_end_time = local_time + timedelta(minutes=1)

        # Start the countdown timer
        start_countdown_timer(campaign_end_time)
    except Exception as e:
        print(f"Failed to start countdown timer: {e}")
```
