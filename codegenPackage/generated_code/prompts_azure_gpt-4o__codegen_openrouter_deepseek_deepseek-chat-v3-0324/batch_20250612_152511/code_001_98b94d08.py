"""
Generated Code Metadata:
========================
Original URL: https://everyworld4.pages.dev
Prompt: Develop a Python script to track and display countdown timers for Everyworld's next drawing event, using the date and time format provided on the website.
Generated: DETERMINISTIC_98b94d083b90e964
Batch ID: 20250612_152511
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import pytz
import time
from typing import Optional

class CountdownTimer:
    """
    A class to track and display countdown timers for Everyworld's next drawing event.
    """
    
    def __init__(self, event_time_str: str, timezone_str: str = "UTC"):
        """
        Initialize the CountdownTimer with the event time and timezone.
        
        Args:
            event_time_str: The event time in the format "%Y-%m-%d %H:%M:%S"
            timezone_str: The timezone string (e.g., "America/New_York")
        """
        self.event_time_str = event_time_str
        self.timezone_str = timezone_str
        self.event_time = self._parse_event_time()
        
    def _parse_event_time(self) -> datetime.datetime:
        """
        Parse the event time string into a timezone-aware datetime object.
        
        Returns:
            A timezone-aware datetime object representing the event time.
            
        Raises:
            ValueError: If the time string or timezone is invalid.
        """
        try:
            naive_time = datetime.datetime.strptime(self.event_time_str, "%Y-%m-%d %H:%M:%S")
            timezone = pytz.timezone(self.timezone_str)
            return timezone.localize(naive_time)
        except ValueError as e:
            raise ValueError(f"Invalid time format or timezone: {e}")
            
    def get_remaining_time(self) -> Optional[datetime.timedelta]:
        """
        Calculate the remaining time until the event.
        
        Returns:
            A timedelta representing the remaining time, or None if the event has passed.
        """
        now = datetime.datetime.now(pytz.timezone(self.timezone_str))
        if now >= self.event_time:
            return None
        return self.event_time - now
        
    def display_countdown(self, refresh_interval: int = 1) -> None:
        """
        Continuously display the countdown until the event time is reached.
        
        Args:
            refresh_interval: The interval in seconds to refresh the display.
        """
        try:
            while True:
                remaining = self.get_remaining_time()
                if remaining is None:
                    print("The event has started or already passed!")
                    break
                    
                days = remaining.days
                hours, remainder = divmod(remaining.seconds, 3600)
                minutes, seconds = divmod(remainder, 60)
                
                print(f"Countdown: {days}d {hours}h {minutes}m {seconds}s", end="\r")
                time.sleep(refresh_interval)
        except KeyboardInterrupt:
            print("\nCountdown stopped by user.")
            
    @staticmethod
    def format_countdown(remaining: datetime.timedelta) -> str:
        """
        Format the remaining time into a human-readable string.
        
        Args:
            remaining: The remaining time as a timedelta.
            
        Returns:
            A formatted string representing the remaining time.
        """
        days = remaining.days
        hours, remainder = divmod(remaining.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        return f"{days}d {hours}h {minutes}m {seconds}s"


if __name__ == "__main__":
    # Example usage
    try:
        # Replace with the actual event time and timezone from Everyworld's website
        event_time = "2023-12-31 23:59:59"  # Example format: YYYY-MM-DD HH:MM:SS
        timezone = "America/New_York"  # Example timezone
        
        timer = CountdownTimer(event_time, timezone)
        print(f"Counting down to event at {event_time} ({timezone})")
        timer.display_countdown()
    except ValueError as e:
        print(f"Error: {e}")
```
