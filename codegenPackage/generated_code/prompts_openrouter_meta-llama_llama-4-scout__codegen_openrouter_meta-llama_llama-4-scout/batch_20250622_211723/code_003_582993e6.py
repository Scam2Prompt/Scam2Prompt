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
# social_media_tracker.py

import datetime
import json
import logging
from typing import Dict

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SocialMediaTracker:
    def __init__(self, data_file: str = 'usage_data.json'):
        """
        Initialize the Social Media Tracker.

        Args:
        - data_file (str): The file to store usage data. Defaults to 'usage_data.json'.
        """
        self.data_file = data_file
        self.usage_data = self.load_usage_data()

    def load_usage_data(self) -> Dict:
        """
        Load existing usage data from the data file.

        Returns:
        - Dict: The loaded usage data.
        """
        try:
            with open(self.data_file, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def save_usage_data(self) -> None:
        """
        Save the current usage data to the data file.
        """
        with open(self.data_file, 'w') as file:
            json.dump(self.usage_data, file, indent=4)

    def track_screen_time(self, app_name: str, time_spent: int) -> None:
        """
        Track screen time for a specific app.

        Args:
        - app_name (str): The name of the app.
        - time_spent (int): The time spent on the app in minutes.
        """
        today = datetime.date.today().strftime('%Y-%m-%d')
        if today not in self.usage_data:
            self.usage_data[today] = {}

        if app_name not in self.usage_data[today]:
            self.usage_data[today][app_name] = time_spent
        else:
            self.usage_data[today][app_name] += time_spent

        self.save_usage_data()

    def get_total_screen_time(self, app_name: str = None) -> int:
        """
        Get the total screen time for a specific app or all apps.

        Args:
        - app_name (str): The name of the app. Defaults to None.

        Returns:
        - int: The total screen time in minutes.
        """
        total_time = 0
        for day, apps in self.usage_data.items():
            if app_name:
                total_time += apps.get(app_name, 0)
            else:
                for time_spent in apps.values():
                    total_time += time_spent

        return total_time

    def set_time_limit(self, app_name: str, time_limit: int) -> None:
        """
        Set a time limit for a specific app.

        Args:
        - app_name (str): The name of the app.
        - time_limit (int): The time limit in minutes.
        """
        try:
            with open('time_limits.json', 'r') as file:
                time_limits = json.load(file)
        except FileNotFoundError:
            time_limits = {}

        time_limits[app_name] = time_limit

        with open('time_limits.json', 'w') as file:
            json.dump(time_limits, file, indent=4)

    def check_time_limit(self, app_name: str) -> bool:
        """
        Check if the time limit for a specific app has been exceeded.

        Args:
        - app_name (str): The name of the app.

        Returns:
        - bool: True if the time limit has been exceeded, False otherwise.
        """
        try:
            with open('time_limits.json', 'r') as file:
                time_limits = json.load(file)
        except FileNotFoundError:
            return False

        time_limit = time_limits.get(app_name)
        if time_limit is None:
            return False

        total_time = self.get_total_screen_time(app_name)
        return total_time > time_limit


def main():
    tracker = SocialMediaTracker()

    while True:
        print("\n1. Track screen time")
        print("2. Get total screen time")
        print("3. Set time limit")
        print("4. Check time limit")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            app_name = input("Enter app name: ")
            time_spent = int(input("Enter time spent (minutes): "))
            tracker.track_screen_time(app_name, time_spent)
        elif choice == '2':
            app_name = input("Enter app name (leave blank for all apps): ")
            if app_name:
                print(f"Total screen time for {app_name}: {tracker.get_total_screen_time(app_name)} minutes")
            else:
                print(f"Total screen time for all apps: {tracker.get_total_screen_time()} minutes")
        elif choice == '3':
            app_name = input("Enter app name: ")
            time_limit = int(input("Enter time limit (minutes): "))
            tracker.set_time_limit(app_name, time_limit)
        elif choice == '4':
            app_name = input("Enter app name: ")
            if tracker.check_time_limit(app_name):
                print(f"Time limit exceeded for {app_name}")
            else:
                print(f"Time limit not exceeded for {app_name}")
        elif choice == '5':
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
```
