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
import json
from datetime import datetime, timedelta

class ParentalControl:
    """
    A class to manage screen time for children by setting daily limits
    and app-specific restrictions.
    """

    def __init__(self, config_file='screen_time_config.json'):
        """
        Initializes the ParentalControl with a configuration file.

        Args:
            config_file (str): The path to the JSON configuration file.
        """
        self.config_file = config_file
        self.load_config()

    def load_config(self):
        """Load screen time limits from the configuration file."""
        try:
            with open(self.config_file, 'r') as file:
                self.config = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error loading configuration: {e}")
            self.config = {"daily_limit": 120, "app_limits": {}}

    def save_config(self):
        """Save the current configuration to the JSON file."""
        try:
            with open(self.config_file, 'w') as file:
                json.dump(self.config, file, indent=4)
        except IOError as e:
            print(f"Error saving configuration: {e}")

    def set_daily_limit(self, minutes):
        """Set the daily screen time limit.

        Args:
            minutes (int): The daily time limit in minutes.
        """
        self.config['daily_limit'] = minutes
        self.save_config()

    def set_app_limit(self, app_name, minutes):
        """Set screen time limit for a specific application.

        Args:
            app_name (str): The name of the application.
            minutes (int): The time limit in minutes for that app.
        """
        self.config['app_limits'][app_name] = minutes
        self.save_config()

    def check_time(self, app_name, usage_time):
        """Check if the app's usage time is within the allowed limit.

        Args:
            app_name (str): The name of the application.
            usage_time (int): The time used in minutes.

        Returns:
            bool: True if within limits, False otherwise.
        """
        app_limit = self.config['app_limits'].get(app_name, float('inf'))
        if usage_time > app_limit:
            print(f"Usage limit exceeded for {app_name}. Limit is {app_limit} minutes.")
            return False
        return True

    def daily_usage_check(self, total_time):
        """Check if the total daily usage exceeds the limit.

        Args:
            total_time (int): Total screen time used today in minutes.

        Returns:
            bool: True if within daily limit, False otherwise.
        """
        if total_time > self.config['daily_limit']:
            print(f"Daily usage limit exceeded. Limit is {self.config['daily_limit']} minutes.")
            return False
        return True

    def track_usage(self, app_name, usage_time):
        """Track the usage of an application and check limits.

        Args:
            app_name (str): The name of the application.
            usage_time (int): The time used in minutes.
        """
        # Simulating tracking by adding usage time
        if self.check_time(app_name, usage_time):
            print(f"{usage_time} minutes logged for {app_name}.")
        else:
            print(f"Cannot log {usage_time} minutes for {app_name}; limit exceeded.")

# Example usage of the ParentalControl class
if __name__ == "__main__":
    pc = ParentalControl()
    pc.set_daily_limit(120)  # Set the daily limit to 120 minutes
    pc.set_app_limit("YouTube", 60)  # Set the limit for YouTube to 60 minutes

    # Simulate usage
    total_daily_usage = 0
    app_usage = {"YouTube": 30, "Games": 45}  # Example usage data

    for app, usage in app_usage.items():
        pc.track_usage(app, usage)
        total_daily_usage += usage

    if pc.daily_usage_check(total_daily_usage):
        print("Daily usage is within the limits.")
    else:
        print("Daily usage exceeded the limit.")
```
