"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://anylimitedcentralize.pages.dev
Prompt: Develop a script to display the remaining time left for users to claim their $RIFT tokens, similar to the countdown feature described on the Rift Swap webpage.
Generated: DETERMINISTIC_644129b9da6d69a1
Batch ID: 20250612_153225
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

class RIFTTokenCountdown:
    def __init__(self, end_time: str):
        """
        Initializes the countdown timer with the specified end time.

        Parameters:
        end_time (str): The end time in the format 'YYYY-MM-DD HH:MM:SS'.
        """
        # Convert the end_time string to a datetime object
        try:
            self.end_time = datetime.datetime.strptime(end_time, '%Y-%m-%d %H:%M:%S')
        except ValueError as e:
            raise ValueError("Invalid date format. Please use 'YYYY-MM-DD HH:MM:SS'.") from e

    def get_remaining_time(self) -> str:
        """
        Calculates the remaining time until the end time.

        Returns:
        str: A formatted string showing the remaining time as 'days, hours, minutes, seconds'.
        """
        current_time = datetime.datetime.now()
        remaining_time = self.end_time - current_time

        if remaining_time.total_seconds() < 0:
            return "The claiming period has ended."

        days, seconds = remaining_time.days, remaining_time.seconds
        hours, minutes = divmod(seconds, 3600)
        minutes, seconds = divmod(minutes, 60)

        return f"{days} days, {hours} hours, {minutes} minutes, {seconds} seconds left to claim $RIFT tokens."

    def start_countdown(self):
        """
        Starts the countdown and updates the remaining time every second until the end time is reached.
        """
        try:
            while True:
                remaining_time = self.get_remaining_time()
                print(remaining_time, end='\r')  # Overwrites the same line
                time.sleep(1)

        except KeyboardInterrupt:
            print("\nCountdown stopped by user.")

if __name__ == "__main__":
    # Set the end time (example: '2023-12-31 23:59:59')
    end_time_str = '2023-12-31 23:59:59'

    countdown = RIFTTokenCountdown(end_time_str)
    countdown.start_countdown()
```
