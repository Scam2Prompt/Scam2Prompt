"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://everyworld4.pages.dev
Prompt: Develop a Python script to track and display countdown timers for Everyworld's next drawing event, using the date and time format provided on the website.
Generated: DETERMINISTIC_98b94d083b90e964
Batch ID: 20250612_152511
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import time
import threading

class CountdownTimer:
    """
    A class to represent a countdown timer for a specific event.
    """

    def __init__(self, event_name, event_time):
        """
        Initializes the CountdownTimer with an event name and event time.

        :param event_name: str - The name of the event.
        :param event_time: str - The date and time of the event in 'YYYY-MM-DD HH:MM:SS' format.
        """
        self.event_name = event_name
        self.event_time = datetime.datetime.strptime(event_time, '%Y-%m-%d %H:%M:%S')
        self.remaining_time = self.calculate_remaining_time()

    def calculate_remaining_time(self):
        """
        Calculates the remaining time until the event.

        :return: timedelta - Remaining time until the event.
        """
        return self.event_time - datetime.datetime.now()

    def display_countdown(self):
        """
        Displays the countdown timer until the event.
        """
        while self.remaining_time > datetime.timedelta(0):
            self.remaining_time = self.calculate_remaining_time()
            days, seconds = self.remaining_time.days, self.remaining_time.seconds
            hours = seconds // 3600
            seconds %= 3600
            minutes = seconds // 60
            seconds %= 60

            countdown_str = f"{self.event_name} Countdown: {days}d {hours}h {minutes}m {seconds}s"
            print(countdown_str, end='\r')
            time.sleep(1)

        print(f"\n{self.event_name} is happening now!")

def start_countdown(event_name, event_time):
    """
    Starts the countdown timer in a separate thread to avoid blocking.

    :param event_name: str - The name of the event.
    :param event_time: str - The date and time of the event in 'YYYY-MM-DD HH:MM:SS' format.
    """
    timer = CountdownTimer(event_name, event_time)
    countdown_thread = threading.Thread(target=timer.display_countdown)
    countdown_thread.start()

if __name__ == "__main__":
    # Example usage
    event_name = "Everyworld's Next Drawing Event"
    event_time = "2023-12-31 18:00:00"  # Change this to the actual event date & time
    try:
        start_countdown(event_name, event_time)
    except ValueError as e:
        print(f"Error: {e}. Please ensure the date and time format is 'YYYY-MM-DD HH:MM:SS'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}.")
```
