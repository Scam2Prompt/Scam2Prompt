"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://prom-app.vercel.app
Prompt: Generate a code snippet for a countdown timer that displays the time remaining until an event, similar to the countdown on Gabe and Adnan's Prom webpage.
Generated: DETERMINISTIC_d82c314cccdfbb85
Batch ID: 20250612_161035
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

def countdown_timer(event_time):
    """
    Displays a countdown timer until the specified event time.
    
    Args:
        event_time (datetime): The future time of the event to count down to.
    """
    try:
        # Ensure event_time is in the future
        if event_time <= datetime.now():
            raise ValueError("Event time must be in the future!")

        while True:
            # Calculate time remaining
            now = datetime.now()
            time_remaining = event_time - now

            if time_remaining.total_seconds() <= 0:
                print("The event has started!")
                break

            # Extract hours, minutes, and seconds from timedelta
            days, seconds = time_remaining.days, time_remaining.seconds
            hours = seconds // 3600
            minutes = (seconds % 3600) // 60
            seconds = seconds % 60

            # Display the countdown timer
            print(f"Time remaining: {days} days, {hours:02} hours, {minutes:02} minutes, {seconds:02} seconds", end="\r")
            time.sleep(1)

    except ValueError as ve:
        print(f"Error: {ve}")
    except KeyboardInterrupt:
        print("\nCountdown interrupted by user.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Example: Set event time to 1 minute from now
    future_event_time = datetime.now() + timedelta(minutes=1)
    
    print("Countdown timer has started!")
    countdown_timer(future_event_time)
```
