"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mint-playpixiz.vercel.app
Prompt: Create a program to track the countdown for the Pixiz whitelist and public minting start times, as displayed on the website.
Generated: DETERMINISTIC_996efe40595cb974
Batch ID: 20250612_153606
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

class CountdownTracker:
    """
    A class to track the countdown for whitelist and public minting start times.
    """
    def __init__(self, whitelist_start: str, public_mint_start: str):
        """
        Initializes the CountdownTracker with the start times for whitelist and public minting.

        :param whitelist_start: Start time for the whitelist minting in 'YYYY-MM-DD HH:MM:SS' format.
        :param public_mint_start: Start time for the public minting in 'YYYY-MM-DD HH:MM:SS' format.
        """
        self.whitelist_start = self._parse_datetime(whitelist_start)
        self.public_mint_start = self._parse_datetime(public_mint_start)
        self.validate_dates()

    @staticmethod
    def _parse_datetime(date_str: str) -> datetime:
        """
        Parses a date string into a datetime object.

        :param date_str: Date string in 'YYYY-MM-DD HH:MM:SS' format.
        :return: Parsed datetime object.
        """
        try:
            return datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
        except ValueError:
            raise ValueError("Invalid date format. Please use 'YYYY-MM-DD HH:MM:SS'.")

    def validate_dates(self):
        """
        Validates that the whitelist start is before the public mint start.
        """
        if self.whitelist_start >= self.public_mint_start:
            raise ValueError("Whitelist start time must be before public mint start time.")

    def get_time_remaining(self, target_time: datetime) -> str:
        """
        Calculates the time remaining until a target datetime.

        :param target_time: Target datetime for the countdown.
        :return: Time remaining as a readable string.
        """
        now = datetime.now()
        if now > target_time:
            return "Event has already started."
        delta = target_time - now
        days, seconds = delta.days, delta.seconds
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        seconds = seconds % 60
        return f"{days} days, {hours} hours, {minutes} minutes, {seconds} seconds"

    def track_countdowns(self):
        """
        Tracks and displays the countdown for whitelist and public mint times.
        """
        while True:
            now = datetime.now()
            print("\nCurrent time:", now.strftime('%Y-%m-%d %H:%M:%S'))
            print("Whitelist starts in:", self.get_time_remaining(self.whitelist_start))
            print("Public mint starts in:", self.get_time_remaining(self.public_mint_start))
            time.sleep(60)  # Update every minute


if __name__ == "__main__":
    """
    Script entry point. Prompts the user for whitelist and public mint start times and begins tracking countdowns.
    """
    try:
        # Example start times (replace with actual values or prompt the user for input)
        whitelist_start = input("Enter whitelist start time (YYYY-MM-DD HH:MM:SS): ")
        public_mint_start = input("Enter public mint start time (YYYY-MM-DD HH:MM:SS): ")

        # Initialize CountdownTracker and start tracking countdowns
        tracker = CountdownTracker(whitelist_start, public_mint_start)
        tracker.track_countdowns()
    except ValueError as e:
        print("Error:", e)
    except KeyboardInterrupt:
        print("\nCountdown tracking stopped.")
```
