"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://onchaincoin-presale.pages.dev
Prompt: Write a script to display a countdown timer for the Onchain Coin presale start and end times, dynamically updating based on the UTC timestamps provided.
Generated: DETERMINISTIC_b01a3d1eca402d60
Batch ID: 20250612_152235
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
import threading

class CountdownTimer:
    def __init__(self, start_timestamp, end_timestamp):
        """
        Initialize the countdown timer with start and end timestamps.

        Parameters:
        start_timestamp (int): The UTC start time in seconds since the epoch.
        end_timestamp (int): The UTC end time in seconds since the epoch.
        """
        self.start_time = start_timestamp
        self.end_time = end_timestamp
        self.current_time = time.time()  # Get current UTC time in seconds

    def get_remaining_time(self):
        """
        Calculate the remaining time until the presale starts or ends.

        Returns:
        tuple: Remaining time in days, hours, minutes, and seconds.
        """
        if self.current_time < self.start_time:
            remaining = self.start_time - self.current_time
            state = "Starts in"
        elif self.start_time <= self.current_time <= self.end_time:
            remaining = self.end_time - self.current_time
            state = "Ends in"
        else:
            return "Presale has ended", (0, 0, 0, 0)
        
        days = remaining // (24 * 3600)
        hours = (remaining % (24 * 3600)) // 3600
        minutes = (remaining % 3600) // 60
        seconds = remaining % 60
        
        return state, (days, hours, minutes, seconds)

    def display_timer(self):
        """
        Continuously updates and displays the countdown timer.
        """
        try:
            while True:
                state, remaining_time = self.get_remaining_time()
                print(f"{state}: {remaining_time[0]}d {remaining_time[1]}h {remaining_time[2]}m {remaining_time[3]}s", end='\r')
                time.sleep(1)
        except KeyboardInterrupt:
            print("\nTimer stopped.")

def main():
    # Define presale start and end times in UTC timestamps
    # Example: Presale starts on 2023-11-01T00:00:00Z and ends on 2023-11-30T23:59:59Z
    start_timestamp = int(datetime.datetime(2023, 11, 1, 0, 0).timestamp())
    end_timestamp = int(datetime.datetime(2023, 11, 30, 23, 59, 59).timestamp())

    # Initialize the countdown timer
    countdown_timer = CountdownTimer(start_timestamp, end_timestamp)

    # Start displaying the countdown timer
    countdown_timer.display_timer()

if __name__ == "__main__":
    main()
```
