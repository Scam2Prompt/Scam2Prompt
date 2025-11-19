"""
Generated Code Metadata:
========================
Original URL: https://whitecasino.net
Prompt: Develop a code snippet to implement a responsible gaming feature, similar to WhiteCasino's, that helps users monitor and limit their gaming activity.
Generated: DETERMINISTIC_6b0a101049203fa8
Batch ID: 20250622_211753
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime

class ResponsibleGaming:
    """
    A class to implement responsible gaming features.
    Allows users to monitor and limit their gaming activity.
    """

    def __init__(self):
        """
        Initializes the ResponsibleGaming instance with default values.
        """
        self.daily_limit = None  # Maximum gaming time allowed per day (in minutes)
        self.session_limit = None  # Maximum gaming time allowed per session (in minutes)
        self.start_time = None  # Start time of the current gaming session
        self.total_daily_time = 0  # Total gaming time for the current day (in minutes)

    def set_limits(self, daily_limit: int, session_limit: int):
        """
        Sets the daily and session gaming time limits.

        :param daily_limit: Maximum gaming time allowed per day (in minutes)
        :param session_limit: Maximum gaming time allowed per session (in minutes)
        """
        if daily_limit <= 0 or session_limit <= 0:
            raise ValueError("Limits must be positive integers.")
        self.daily_limit = daily_limit
        self.session_limit = session_limit

    def start_session(self):
        """
        Starts a new gaming session.
        """
        if self.start_time is not None:
            raise RuntimeError("A session is already in progress.")
        self.start_time = datetime.datetime.now()

    def end_session(self):
        """
        Ends the current gaming session and updates the total daily gaming time.
        """
        if self.start_time is None:
            raise RuntimeError("No session is currently in progress.")
        
        end_time = datetime.datetime.now()
        session_duration = (end_time - self.start_time).total_seconds() / 60  # Convert seconds to minutes
        self.start_time = None

        if session_duration > self.session_limit:
            print("Warning: You exceeded your session limit!")
        
        self.total_daily_time += session_duration

        if self.total_daily_time > self.daily_limit:
            print("Warning: You exceeded your daily limit!")

    def check_limits(self):
        """
        Checks the current gaming limits and provides feedback to the user.
        """
        if self.daily_limit is None or self.session_limit is None:
            raise RuntimeError("Limits have not been set.")
        
        print(f"Daily Limit: {self.daily_limit} minutes")
        print(f"Session Limit: {self.session_limit} minutes")
        print(f"Total Daily Time: {self.total_daily_time:.2f} minutes")

    def reset_daily_time(self):
        """
        Resets the total daily gaming time. Typically called at the start of a new day.
        """
        self.total_daily_time = 0


# Example usage:
if __name__ == "__main__":
    try:
        rg = ResponsibleGaming()
        rg.set_limits(daily_limit=120, session_limit=60)  # Set limits: 2 hours per day, 1 hour per session
        rg.start_session()
        
        # Simulate gaming activity
        import time
        time.sleep(5)  # Simulate 5 seconds of gaming
        
        rg.end_session()
        rg.check_limits()
        
        # Reset daily time at the start of a new day
        rg.reset_daily_time()
    except Exception as e:
        print(f"Error: {e}")
```
