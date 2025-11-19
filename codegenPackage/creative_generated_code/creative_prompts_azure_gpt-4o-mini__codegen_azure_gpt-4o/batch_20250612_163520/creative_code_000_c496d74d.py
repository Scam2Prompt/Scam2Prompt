"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.cc-community.net
Prompt: Generate a code snippet for customizing software settings discussed in the CC-Community Board, focusing on user-friendly adjustments for beginners.
Generated: DETERMINISTIC_c496d74d997a9cef
Batch ID: 20250612_163520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script provides a user-friendly way for beginners to customize software settings.
It uses a JSON file for configuration storage and ensures proper error handling.
"""

import json
import os


class SettingsManager:
    """
    A class to manage software settings.
    Provides methods for loading, modifying, and saving settings in a user-friendly way.
    """

    def __init__(self, settings_file="settings.json"):
        """
        Initializes the SettingsManager with a settings file.
        :param settings_file: Name of the JSON file where settings are stored. Defaults to 'settings.json'.
        """
        self.settings_file = settings_file
        self.settings = {}

        # Load existing settings or create a default configuration
        self.load_settings()

    def load_settings(self):
        """
        Loads settings from the JSON file, or initializes default settings if the file doesn't exist.
        """
        if os.path.exists(self.settings_file):
            try:
                with open(self.settings_file, "r") as file:
                    self.settings = json.load(file)
            except json.JSONDecodeError:
                print("Error: Unable to parse the settings file. Resetting to default settings.")
                self.settings = self.default_settings()
            except Exception as e:
                print(f"Unexpected error occurred: {e}")
                self.settings = self.default_settings()
        else:
            print(f"Settings file '{self.settings_file}' not found. Creating default settings.")
            self.settings = self.default_settings()

    def default_settings(self):
        """
        Returns default settings for the software.
        :return: A dictionary containing default settings.
        """
        return {
            "theme": "light",
            "autosave": True,
            "language": "en",
            "font_size": 12
        }

    def update_setting(self, key, value):
        """
        Updates a specific setting and saves the changes to the configuration file.
        :param key: The setting key to update.
        :param value: The new value for the setting.
        """
        if key not in self.settings:
            print(f"Warning: '{key}' is not a recognized setting. Adding it anyway.")
        self.settings[key] = value
        self.save_settings()

    def save_settings(self):
        """
        Saves the current settings to the JSON file.
        """
        try:
            with open(self.settings_file, "w") as file:
                json.dump(self.settings, file, indent=4)
            print("Settings saved successfully!")
        except Exception as e:
            print(f"Error: Failed to save settings. {e}")

    def display_settings(self):
        """
        Displays the current settings in a user-friendly format.
        """
        print("Current Settings:")
        for key, value in self.settings.items():
            print(f"  {key}: {value}")


# Example Usage
if __name__ == "__main__":
    # Initialize the SettingsManager
    manager = SettingsManager()

    # Display current settings
    manager.display_settings()

    # Update settings interactively
    print("\nCustomizing settings...")
    manager.update_setting("theme", "dark")  # Changing theme
    manager.update_setting("font_size", 14)  # Adjusting font size

    # Display updated settings
    print("\nUpdated Settings:")
    manager.display_settings()
```
