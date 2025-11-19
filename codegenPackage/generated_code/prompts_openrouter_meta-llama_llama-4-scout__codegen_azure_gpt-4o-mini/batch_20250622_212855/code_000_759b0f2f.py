"""
Generated Code Metadata:
========================
Original URL: https://mommyanew.com
Prompt: "Write a guide for managing screen time for children using iPhone parental controls and IOS 12 features."
Generated: DETERMINISTIC_759b0f2fdaacfa2e
Batch ID: 20250622_212855
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import json

class ScreenTimeManager:
    """
    A class to manage screen time for children using iPhone parental controls and iOS 12 features.
    """

    def __init__(self):
        """
        Initializes the ScreenTimeManager with default settings.
        """
        self.settings = {
            "app_limits": {},
            "downtime": {"start": "22:00", "end": "07:00"},
            "always_allowed": [],
            "content_restrictions": {}
        }

    def set_app_limit(self, app_name, limit_hours):
        """
        Sets a time limit for a specific app.

        :param app_name: Name of the app to limit
        :param limit_hours: Number of hours allowed per day
        """
        if limit_hours < 0:
            raise ValueError("Limit hours must be a non-negative integer.")
        self.settings["app_limits"][app_name] = limit_hours

    def set_downtime(self, start_time, end_time):
        """
        Sets the downtime hours during which the device cannot be used.

        :param start_time: Start time for downtime (HH:MM format)
        :param end_time: End time for downtime (HH:MM format)
        """
        self.settings["downtime"]["start"] = start_time
        self.settings["downtime"]["end"] = end_time

    def add_always_allowed_app(self, app_name):
        """
        Adds an app to the list of always allowed apps.

        :param app_name: Name of the app to always allow
        """
        if app_name not in self.settings["always_allowed"]:
            self.settings["always_allowed"].append(app_name)

    def set_content_restriction(self, category, restriction_level):
        """
        Sets content restrictions based on category.

        :param category: Category of content to restrict (e.g., "movies", "apps")
        :param restriction_level: Level of restriction (e.g., "age_12", "age_17")
        """
        self.settings["content_restrictions"][category] = restriction_level

    def save_settings(self, file_path):
        """
        Saves the current settings to a JSON file.

        :param file_path: Path to the file where settings will be saved
        """
        try:
            with open(file_path, 'w') as json_file:
                json.dump(self.settings, json_file, indent=4)
        except IOError as e:
            print(f"Error saving settings: {e}")

    def load_settings(self, file_path):
        """
        Loads settings from a JSON file.

        :param file_path: Path to the file from which settings will be loaded
        """
        try:
            with open(file_path, 'r') as json_file:
                self.settings = json.load(json_file)
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading settings: {e}")

# Example usage
if __name__ == "__main__":
    manager = ScreenTimeManager()
    manager.set_app_limit("YouTube", 2)
    manager.set_downtime("22:00", "07:00")
    manager.add_always_allowed_app("Phone")
    manager.set_content_restriction("movies", "age_12")
    
    # Save settings to a file
    manager.save_settings("screen_time_settings.json")
    
    # Load settings from a file
    manager.load_settings("screen_time_settings.json")
```
