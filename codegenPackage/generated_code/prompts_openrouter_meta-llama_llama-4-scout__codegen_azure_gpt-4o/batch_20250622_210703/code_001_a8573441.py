"""
Generated Code Metadata:
========================
Original URL: https://www.malmobeerweek.se
Prompt: Write a Python script to countdown the days, hours, minutes, and seconds until Malmö Beer Week, similar to the one displayed on the website.
Generated: DETERMINISTIC_a857344155bac06a
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import time

def countdown_to_event(event_name, event_date):
    """
    Countdown to a specific event.

    Args:
        event_name (str): Name of the event.
        event_date (datetime.datetime): Date and time of the event.

    Returns:
        None
    """
    try:
        while True:
            # Get the current time
            now = datetime.datetime.now()

            # Calculate the time difference
            time_difference = event_date - now

            if time_difference.total_seconds() <= 0:
                print(f"{event_name} has started!")
                break

            # Extract days, hours, minutes, and seconds from the time difference
            days = time_difference.days
            hours, remainder = divmod(time_difference.seconds, 3600)
            minutes, seconds = divmod(remainder, 60)

            # Display the countdown
            print(f"Time until {event_name}: {days} days, {hours} hours, {minutes} minutes, {seconds} seconds", end="\r")

            # Sleep for 1 second to update the countdown
            time.sleep(1)

    except KeyboardInterrupt:
        print("\nCountdown interrupted by user.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Define the event name and date
    event_name = "Malmö Beer Week"
    event_date = datetime.datetime(2024, 5, 20, 0, 0, 0)  # Example date: May 20, 2024 at midnight

    print(f"Countdown to {event_name} starting...")
    countdown_to_event(event_name, event_date)
```
