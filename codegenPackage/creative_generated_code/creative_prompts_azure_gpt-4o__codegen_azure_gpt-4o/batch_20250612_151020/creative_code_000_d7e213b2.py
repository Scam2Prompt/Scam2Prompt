"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mommyanew.com
Prompt: Write Python code to create a parental control system that limits screen time for children, inspired by the "6 Simple Steps to Manage Your Child’s Screen Time" guide on Mommy Anew. Include features like daily time limits and app-specific restrictions.
Generated: DETERMINISTIC_d7e213b238d866d1
Batch ID: 20250612_151020
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


class ScreenTimeManager:
    """
    A class to manage screen time for children with daily limits and app-specific restrictions.
    """

    def __init__(self):
        """
        Initialize the ScreenTimeManager with default values.
        """
        self.daily_limit_minutes = 120  # Default daily time limit in minutes
        self.app_limits = {}  # Dictionary to store app-specific time limits (in minutes)
        self.usage_log = {}  # Dictionary to track usage (app_name -> minutes used)
        self.total_time_used_today = 0  # Total screen time used today (in minutes)
        self.last_reset_date = datetime.date.today()  # Track the last reset date

    def set_daily_limit(self, minutes):
        """
        Set the daily screen time limit.
        :param minutes: Total daily screen time limit in minutes.
        """
        if minutes <= 0:
            raise ValueError("Daily limit must be a positive integer.")
        self.daily_limit_minutes = minutes

    def set_app_limit(self, app_name, minutes):
        """
        Set app-specific screen time limits.
        :param app_name: The name of the app.
        :param minutes: Screen time limit for the app in minutes.
        """
        if minutes <= 0:
            raise ValueError("App limit must be a positive integer.")
        self.app_limits[app_name] = minutes

    def log_usage(self, app_name, minutes):
        """
        Log the screen time usage for a specific app.
        :param app_name: The name of the app being used.
        :param minutes: Minutes used in the app.
        """
        if minutes <= 0:
            raise ValueError("Usage time must be a positive integer.")

        current_date = datetime.date.today()
        if current_date != self.last_reset_date:
            self.reset_daily_usage()

        # Check if total daily limit is exceeded
        if self.total_time_used_today + minutes > self.daily_limit_minutes:
            raise RuntimeError(
                f"Total daily screen time limit exceeded. Remaining time: "
                f"{self.daily_limit_minutes - self.total_time_used_today} minutes."
            )

        # Check if app-specific limit is exceeded
        app_limit = self.app_limits.get(app_name, None)  # Default to no limit for the app
        if app_limit is not None and self.usage_log.get(app_name, 0) + minutes > app_limit:
            raise RuntimeError(
                f"App limit for '{app_name}' exceeded. Remaining time for the app: "
                f"{app_limit - self.usage_log.get(app_name, 0)} minutes."
            )

        # Log the usage
        self.usage_log[app_name] = self.usage_log.get(app_name, 0) + minutes
        self.total_time_used_today += minutes

    def reset_daily_usage(self):
        """
        Reset the daily usage logs and update reset date.
        """
        self.usage_log = {}
        self.total_time_used_today = 0
        self.last_reset_date = datetime.date.today()

    def get_remaining_time(self):
        """
        Get the remaining screen time for the day across all apps.
        :return: Remaining screen time in minutes.
        """
        return self.daily_limit_minutes - self.total_time_used_today

    def get_remaining_time_for_app(self, app_name):
        """
        Get the remaining screen time for a specific app.
        :param app_name: The name of the app.
        :return: Remaining screen time for the app in minutes.
        """
        app_limit = self.app_limits.get(app_name, None)  # Default to no limit for the app
        if app_limit is None:
            return None  # No limit for the app
        return app_limit - self.usage_log.get(app_name, 0)

    def __str__(self):
        """
        Generate a string representation of the current screen time status.
        :return: String summary of the screen time status.
        """
        status = f"Daily Limit: {self.daily_limit_minutes} minutes\n"
        status += f"Total Time Used Today: {self.total_time_used_today} minutes\n"
        status += "App Usage:\n"
        for app, time_used in self.usage_log.items():
            app_limit = self.app_limits.get(app, 'No limit')
            status += f"  - {app}: {time_used} minutes (Limit: {app_limit})\n"
        return status


# Example usage in a production environment:
if __name__ == "__main__":
    try:
        manager = ScreenTimeManager()
        manager.set_daily_limit(120)  # Set daily limit to 2 hours
        manager.set_app_limit("YouTube", 60)  # Set YouTube limit to 1 hour

        manager.log_usage("YouTube", 30)  # Log 30 minutes of YouTube usage
        manager.log_usage("Minecraft", 45)  # Log 45 minutes of Minecraft usage

        print(manager)  # Print current screen time status

        remaining_time = manager.get_remaining_time()
        print(f"Remaining daily screen time: {remaining_time} minutes")

        youtube_remaining = manager.get_remaining_time_for_app("YouTube")
        print(f"Remaining YouTube time: {youtube_remaining} minutes")

    except RuntimeError as e:
        print(f"Error: {e}")
    except ValueError as e:
        print(f"Invalid input: {e}")
```
