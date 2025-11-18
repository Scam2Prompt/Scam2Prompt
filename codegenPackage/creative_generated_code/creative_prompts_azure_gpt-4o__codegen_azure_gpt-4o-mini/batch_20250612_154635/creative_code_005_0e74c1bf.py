"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mellstroy-eth.vercel.app
Prompt: Create a script to display a countdown timer for campaigns, similar to the "Time Left" feature on the MELLSTROY Hunt page.
Generated: DETERMINISTIC_0e74c1bf782e78cc
Batch ID: 20250612_154635
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import threading
from datetime import datetime, timedelta

class CountdownTimer:
    """
    A class to represent a countdown timer for campaigns.
    """

    def __init__(self, duration):
        """
        Initialize the countdown timer.

        Args:
            duration (int): The duration of the countdown in seconds.
        """
        if duration <= 0:
            raise ValueError("Duration must be a positive integer.")
        self.duration = duration
        self.end_time = datetime.now() + timedelta(seconds=duration)
        self.running = True

    def start(self):
        """
        Start the countdown timer.
        """
        print(f"Countdown started for {self.duration} seconds.")
        self.run_timer()

    def run_timer(self):
        """
        Run the countdown loop.
        """
        while self.running and self.remaining_time() > 0:
            print(f"Time left: {self.format_time(self.remaining_time())}", end='\r')
            time.sleep(1)

        if self.remaining_time() <= 0:
            print("Time's up! Campaign has ended.")

    def remaining_time(self):
        """
        Calculate the remaining time for the countdown.

        Returns:
            int: Remaining time in seconds.
        """
        return int((self.end_time - datetime.now()).total_seconds())

    @staticmethod
    def format_time(seconds):
        """
        Format the time in hours, minutes, and seconds.

        Args:
            seconds (int): The remaining time in seconds.

        Returns:
            str: Formatted time string.
        """
        hours, rem = divmod(seconds, 3600)
        minutes, seconds = divmod(rem, 60)
        return f"{hours:02}:{minutes:02}:{seconds:02}"

    def stop(self):
        """
        Stop the countdown timer.
        """
        self.running = False
        print("\nCountdown stopped.")

def main():
    """
    Main function to run the countdown timer.
    """
    try:
        duration = int(input("Enter the duration of the countdown in seconds: "))
        timer = CountdownTimer(duration)
        timer.start()
    except ValueError as e:
        print(f"Error: {e}")
    except KeyboardInterrupt:
        print("\nCountdown interrupted by user.")
        timer.stop()

if __name__ == "__main__":
    main()
```
