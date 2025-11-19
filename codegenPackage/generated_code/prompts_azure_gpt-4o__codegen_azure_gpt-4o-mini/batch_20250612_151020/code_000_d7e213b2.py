"""
Generated Code Metadata:
========================
Original URL: https://mommyanew.com
Prompt: Write Python code to create a parental control system that limits screen time for children, inspired by the "6 Simple Steps to Manage Your Child’s Screen Time" guide on Mommy Anew. Include features like daily time limits and app-specific restrictions.
Generated: DETERMINISTIC_d7e213b238d866d1
Batch ID: 20250612_151020
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
import json
from datetime import datetime, timedelta

class ScreenTimeManager:
    """
    A class to manage screen time for children, allowing for daily limits
    and app-specific restrictions.
    """

    def __init__(self, config_file='screen_time_config.json'):
        """
        Initializes the ScreenTimeManager with a configuration file.

        :param config_file: Path to the JSON configuration file.
        """
        self.config_file = config_file
        self.load_config()

    def load_config(self):
        """
        Loads the configuration from a JSON file.
        """
        try:
            with open(self.config_file, 'r') as file:
                self.config = json.load(file)
        except FileNotFoundError:
            self.config = {
                "daily_limit": 120,  # in minutes
                "app_limits": {
                    "YouTube": 30,  # in minutes
                    "Games": 60,    # in minutes
                }
            }
            self.save_config()

    def save_config(self):
        """
        Saves the current configuration to a JSON file.
        """
        with open(self.config_file, 'w') as file:
            json.dump(self.config, file, indent=4)

    def set_daily_limit(self, minutes):
        """
        Sets the daily screen time limit.

        :param minutes: Daily limit in minutes.
        """
        self.config['daily_limit'] = minutes
        self.save_config()

    def set_app_limit(self, app_name, minutes):
        """
        Sets the screen time limit for a specific app.

        :param app_name: Name of the app.
        :param minutes: Limit in minutes.
        """
        self.config['app_limits'][app_name] = minutes
        self.save_config()

    def check_time(self, app_name, usage_time):
        """
        Checks if the usage time for an app exceeds the limit.

        :param app_name: Name of the app being checked.
        :param usage_time: Time used in minutes.
        :return: Boolean indicating if the limit is exceeded.
        """
        app_limit = self.config['app_limits'].get(app_name, float('inf'))
        return usage_time > app_limit

    def track_usage(self, app_name, usage_time):
        """
        Tracks the usage time for an app and checks against limits.

        :param app_name: Name of the app being tracked.
        :param usage_time: Time used in minutes.
        """
        if self.check_time(app_name, usage_time):
            print(f"Usage limit exceeded for {app_name}. Limit is {self.config['app_limits'][app_name]} minutes.")
        else:
            print(f"{app_name} usage is within limits.")

    def daily_usage_report(self, total_usage):
        """
        Generates a daily usage report.

        :param total_usage: Total screen time used in minutes.
        """
        if total_usage > self.config['daily_limit']:
            print(f"Daily limit exceeded! Limit: {self.config['daily_limit']} minutes, Used: {total_usage} minutes.")
        else:
            print(f"Daily usage is within limits. Limit: {self.config['daily_limit']} minutes, Used: {total_usage} minutes.")

def main():
    """
    Main function to demonstrate the ScreenTimeManager functionality.
    """
    manager = ScreenTimeManager()

    # Example usage
    manager.set_daily_limit(120)  # Set daily limit to 120 minutes
    manager.set_app_limit("YouTube", 30)  # Set YouTube limit to 30 minutes
    manager.set_app_limit("Games", 60)  # Set Games limit to 60 minutes

    # Simulate app usage
    app_usage = {
        "YouTube": 25,
        "Games": 70
    }

    for app, usage in app_usage.items():
        manager.track_usage(app, usage)

    # Simulate total daily usage
    total_daily_usage = sum(app_usage.values())
    manager.daily_usage_report(total_daily_usage)

if __name__ == "__main__":
    main()
```
