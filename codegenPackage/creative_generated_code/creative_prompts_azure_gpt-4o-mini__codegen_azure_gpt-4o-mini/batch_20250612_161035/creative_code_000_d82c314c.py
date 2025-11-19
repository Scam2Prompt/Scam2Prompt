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
import datetime

class CountdownTimer:
    def __init__(self, event_time):
        """
        Initialize the countdown timer.
        
        :param event_time: The target datetime for the countdown
        """
        if not isinstance(event_time, datetime.datetime):
            raise ValueError("event_time must be a datetime object")
        
        self.event_time = event_time

    def get_time_remaining(self):
        """
        Calculate the time remaining until the event.
        
        :return: A timedelta object representing the time remaining
        """
        now = datetime.datetime.now()
        return self.event_time - now

    def start(self):
        """
        Start the countdown timer and display the remaining time.
        """
        try:
            while True:
                remaining = self.get_time_remaining()
                
                if remaining.total_seconds() <= 0:
                    print("Event has started!")
                    break
                
                # Format the remaining time as days, hours, minutes, and seconds
                days, seconds = remaining.days, remaining.seconds
                hours = seconds // 3600
                minutes = (seconds % 3600) // 60
                seconds = seconds % 60

                # Clear the output and print the countdown
                print(f"\rTime remaining: {days}d {hours}h {minutes}m {seconds}s", end="")
                time.sleep(1)  # Update every second

        except KeyboardInterrupt:
            print("\nCountdown stopped by user.")

if __name__ == "__main__":
    # Define the target event time (YYYY, MM, DD, HH, MM, SS)
    target_event_time = datetime.datetime(2023, 12, 31, 23, 59, 59)

    # Initialize and start the countdown timer
    countdown_timer = CountdownTimer(target_event_time)
    countdown_timer.start()
```
