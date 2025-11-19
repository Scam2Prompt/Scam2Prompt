"""
Generated Code Metadata:
========================
Original URL: https://bazaar.lol
Prompt: Design a system that helps users "take back control" from social media, incorporating features discussed on the webpage, such as tracking and limiting screen time.
Generated: DETERMINISTIC_582993e621e43a5a
Batch ID: 20250622_211723
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
import os
from datetime import datetime, timedelta

class ScreenTimeTracker:
    """
    A class to track and limit screen time for social media applications.
    """

    def __init__(self, data_file='screen_time_data.json'):
        """
        Initializes the ScreenTimeTracker with a data file to store usage data.

        :param data_file: The file where screen time data will be stored.
        """
        self.data_file = data_file
        self.usage_data = self.load_usage_data()

    def load_usage_data(self):
        """
        Loads usage data from the JSON file.

        :return: A dictionary containing usage data.
        """
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as file:
                return json.load(file)
        return {}

    def save_usage_data(self):
        """
        Saves the current usage data to the JSON file.
        """
        with open(self.data_file, 'w') as file:
            json.dump(self.usage_data, file)

    def track_usage(self, app_name):
        """
        Tracks the usage time for a specific application.

        :param app_name: The name of the application being tracked.
        """
        start_time = datetime.now()
        print(f"Tracking usage for {app_name}. Press Ctrl+C to stop.")

        try:
            while True:
                time.sleep(1)  # Simulate tracking every second
        except KeyboardInterrupt:
            end_time = datetime.now()
            usage_duration = end_time - start_time
            self.record_usage(app_name, usage_duration)

    def record_usage(self, app_name, duration):
        """
        Records the usage duration for a specific application.

        :param app_name: The name of the application being tracked.
        :param duration: The duration of usage as a timedelta object.
        """
        duration_in_minutes = duration.total_seconds() / 60
        if app_name in self.usage_data:
            self.usage_data[app_name] += duration_in_minutes
        else:
            self.usage_data[app_name] = duration_in_minutes

        self.save_usage_data()
        print(f"Recorded {duration_in_minutes:.2f} minutes for {app_name}.")

    def get_usage_report(self):
        """
        Generates a report of the usage data.

        :return: A string report of usage data.
        """
        report = "Screen Time Usage Report:\n"
        for app, minutes in self.usage_data.items():
            report += f"{app}: {minutes:.2f} minutes\n"
        return report

    def limit_usage(self, app_name, limit_minutes):
        """
        Checks if the usage for a specific application exceeds the limit.

        :param app_name: The name of the application to check.
        :param limit_minutes: The limit in minutes.
        :return: A boolean indicating if the limit has been exceeded.
        """
        current_usage = self.usage_data.get(app_name, 0)
        if current_usage >= limit_minutes:
            print(f"Usage limit exceeded for {app_name}. Limit: {limit_minutes} minutes.")
            return True
        return False


if __name__ == "__main__":
    tracker = ScreenTimeTracker()

    # Example usage
    app_name = input("Enter the name of the social media app to track: ")
    tracker.track_usage(app_name)

    # After tracking, generate a report
    print(tracker.get_usage_report())

    # Check if usage exceeds a limit
    limit = int(input("Enter the usage limit in minutes for the app: "))
    if tracker.limit_usage(app_name, limit):
        print("Consider taking a break from this app.")
```
