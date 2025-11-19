"""
Generated Code Metadata:
========================
Original URL: https://prom-app.vercel.app
Prompt: Generate a code snippet for a countdown timer that displays the time remaining until an event, similar to the countdown on Gabe and Adnan's Prom webpage.
Generated: DETERMINISTIC_d82c314cccdfbb85
Batch ID: 20250612_161035
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

def countdown_timer(event_name, event_datetime):
    """
    Displays a countdown timer for the given event.

    Args:
        event_name (str): Name of the event.
        event_datetime (datetime): Datetime of the event.
    """
    try:
        # Validate that the event_datetime is in the future
        if event_datetime <= datetime.now():
            raise ValueError("Event datetime must be in the future.")

        print(f"Countdown to {event_name}:\n")
        
        while True:
            # Calculate the time remaining
            now = datetime.now()
            time_remaining = event_datetime - now

            # If the event has started, exit the loop
            if time_remaining.total_seconds() <= 0:
                print(f"{event_name} has started!")
                break

            # Extract days, hours, minutes, and seconds from the time remaining
            days = time_remaining.days
            hours, remainder = divmod(time_remaining.seconds, 3600)
            minutes, seconds = divmod(remainder, 60)

            # Display the countdown timer
            print(f"{days} days, {hours:02} hours, {minutes:02} minutes, {seconds:02} seconds remaining", end="\r")

            # Sleep for 1 second to update the timer
            time.sleep(1)

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
if __name__ == "__main__":
    # Define the event name and datetime
    event_name = "Gabe and Adnan's Prom"
    event_datetime = datetime.now() + timedelta(days=1, hours=5, minutes=30)  # Example: 1 day, 5 hours, 30 minutes from now

    # Start the countdown timer
    countdown_timer(event_name, event_datetime)
```
