"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sandbox.co.com
Prompt: Write code to implement a "responsible gaming" feature for an online casino platform, inspired by 8KBet's policies.
Generated: DETERMINISTIC_d2593794825986a3
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import pytz

class ResponsibleGaming:
    """
    A class to implement responsible gaming features for an online casino platform.
    Inspired by 8KBet's policies.
    """

    def __init__(self, user_id):
        """
        Initialize the ResponsibleGaming instance for a user.

        Args:
            user_id (int): Unique identifier of the user.
        """
        self.user_id = user_id
        self.daily_limit = None  # Daily spending limit
        self.session_duration_limit = None  # Maximum session duration in hours
        self.cool_down_period = None  # Cool-down period in hours
        self.last_cool_down_timestamp = None  # Timestamp of last cool-down initiation
        self.start_time = None  # Session start time
        self.spent_today = 0  # Amount spent today

    def set_daily_limit(self, limit):
        """
        Set a daily spending limit for the user.

        Args:
            limit (float): Maximum amount the user can spend in a day.
        """
        if limit <= 0:
            raise ValueError("Daily limit must be greater than 0.")
        self.daily_limit = limit

    def set_session_duration_limit(self, hours):
        """
        Set session duration limit for the user.

        Args:
            hours (int): Maximum session duration in hours.
        """
        if hours <= 0:
            raise ValueError("Session duration limit must be greater than 0.")
        self.session_duration_limit = hours

    def set_cool_down_period(self, hours):
        """
        Set a cool-down period for the user.

        Args:
            hours (int): Cool-down period in hours.
        """
        if hours <= 0:
            raise ValueError("Cool-down period must be greater than 0.")
        self.cool_down_period = hours

    def start_session(self):
        """
        Start a gaming session for the user.
        """
        if self.is_in_cool_down():
            raise Exception("User is in cool-down period.")
        self.start_time = datetime.datetime.now(pytz.utc)

    def end_session(self):
        """
        End the current gaming session for the user.
        """
        self.start_time = None

    def is_in_cool_down(self):
        """
        Check if the user is currently in a cool-down period.

        Returns:
            bool: True if the user is in a cool-down period, False otherwise.
        """
        if self.last_cool_down_timestamp:
            elapsed_time = (datetime.datetime.now(pytz.utc) - self.last_cool_down_timestamp).total_seconds() / 3600
            return elapsed_time < self.cool_down_period
        return False

    def enforce_daily_limit(self, amount):
        """
        Enforce the daily spending limit for the user.

        Args:
            amount (float): Amount the user wants to spend.

        Returns:
            bool: True if the spending is allowed, False otherwise.

        Raises:
            Exception: If daily limit is exceeded.
        """
        if self.daily_limit is None:
            raise Exception("Daily limit is not set.")
        
        self.spent_today += amount
        if self.spent_today > self.daily_limit:
            raise Exception("Daily spending limit exceeded!")
        return True

    def enforce_session_duration(self):
        """
        Enforce the session duration limit for the user.

        Raises:
            Exception: If session duration limit is exceeded.
        """
        if self.session_duration_limit is None or self.start_time is None:
            return

        elapsed_time = (datetime.datetime.now(pytz.utc) - self.start_time).total_seconds() / 3600
        if elapsed_time > self.session_duration_limit:
            self.end_session()
            raise Exception("Session duration limit exceeded!")

    def initiate_cool_down(self):
        """
        Initiate the cool-down period for the user.
        """
        self.last_cool_down_timestamp = datetime.datetime.now(pytz.utc)
        self.end_session()

    def reset_daily_spent(self):
        """
        Reset the daily spending tracker. Typically called at the start of a new day.
        """
        self.spent_today = 0

# Example Usage:
if __name__ == "__main__":
    try:
        user_responsible_gaming = ResponsibleGaming(user_id=1)
        user_responsible_gaming.set_daily_limit(100)  # Set daily limit to $100
        user_responsible_gaming.set_session_duration_limit(2)  # Set session limit to 2 hours
        user_responsible_gaming.set_cool_down_period(12)  # Set cool-down period to 12 hours

        user_responsible_gaming.start_session()  # Start a session
        user_responsible_gaming.enforce_daily_limit(50)  # Spend $50
        user_responsible_gaming.enforce_session_duration()  # Check session duration
        user_responsible_gaming.initiate_cool_down()  # Initiate cool-down

    except Exception as e:
        print(f"Error: {e}")
```
This code ensures all responsible gaming features (daily spending limit, session limit, and cool-down periods) are implemented with proper error handling and best practices.
