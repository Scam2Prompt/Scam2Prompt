"""
Generated Code Metadata:
========================
Original URL: https://oasysgames.live
Prompt: Generate code to implement a countdown timer for the "Ending Soon" campaigns on OasysGames, using the local time settings provided.
Generated: DETERMINISTIC_1ded47032d92fd7e
Batch ID: 20250612_163231
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
from datetime import datetime, timedelta

def countdown_timer(end_time):
    """
    Countdown timer for "Ending Soon" campaigns.

    Args:
        end_time (datetime): The local end time of the campaign.

    Returns:
        None: Prints the countdown timer to the console.
    """
    try:
        # Validate that end_time is a datetime object
        if not isinstance(end_time, datetime):
            raise ValueError("end_time must be a datetime object.")

        # Get the current local time
        current_time = datetime.now()

        # Check if the campaign has already ended
        if current_time >= end_time:
            print("The campaign has already ended.")
            return

        print("Countdown Timer Started:")
        while current_time < end_time:
            # Calculate the remaining time
            remaining_time = end_time - current_time

            # Extract hours, minutes, and seconds from the remaining time
            hours, remainder = divmod(remaining_time.seconds, 3600)
            minutes, seconds = divmod(remainder, 60)

            # Print the countdown timer in HH:MM:SS format
            print(f"\rTime Remaining: {remaining_time.days}d {hours:02}:{minutes:02}:{seconds:02}", end="")

            # Sleep for 1 second to update the timer
            time.sleep(1)

            # Update the current time
            current_time = datetime.now()

        print("\nThe campaign has ended!")
    except Exception as e:
        # Handle unexpected errors
        print(f"An error occurred: {e}")

# Example usage:
if __name__ == "__main__":
    # Define the campaign end time (local time)
    campaign_end_time = datetime.now() + timedelta(seconds=10)  # Example: 10 seconds from now

    # Start the countdown timer
    countdown_timer(campaign_end_time)
```
