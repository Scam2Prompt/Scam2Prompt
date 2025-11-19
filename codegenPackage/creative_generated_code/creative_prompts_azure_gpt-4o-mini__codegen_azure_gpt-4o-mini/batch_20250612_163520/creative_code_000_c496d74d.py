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
import json
import os

class SettingsManager:
    """
    A class to manage user settings for the application.
    It allows loading, saving, and updating settings in a JSON file.
    """

    SETTINGS_FILE = 'settings.json'

    def __init__(self):
        """
        Initializes the SettingsManager. Loads settings from file if it exists.
        """
        self.settings = self.load_settings()

    def load_settings(self):
        """
        Loads settings from the JSON file.

        Returns:
            dict: A dictionary containing the settings. Defaults to an empty dictionary if file is not found.
        """
        if os.path.exists(self.SETTINGS_FILE):
            with open(self.SETTINGS_FILE, 'r') as file:
                try:
                    return json.load(file)
                except json.JSONDecodeError:
                    print("Error: Settings file is corrupted. Loading defaults.")
        return {}  # Return an empty dict if file does not exist or is corrupted.

    def save_settings(self):
        """
        Saves the current settings to the JSON file.
        """
        with open(self.SETTINGS_FILE, 'w') as file:
            json.dump(self.settings, file, indent=4)
    
    def update_setting(self, key, value):
        """
        Updates a specific setting.
        
        Args:
            key (str): The key of the setting to update.
            value: The new value for the setting.
        """
        self.settings[key] = value
        self.save_settings()  # Save settings after update

    def get_setting(self, key, default=None):
        """
        Retrieves the value of a specific setting.
        
        Args:
            key (str): The key of the setting to retrieve.
            default: The default value to return if the setting does not exist.
        
        Returns:
            The value of the setting or the default if not found.
        """
        return self.settings.get(key, default)


if __name__ == '__main__':
    # Example usage of the SettingsManager
    settings_manager = SettingsManager()

    # Display current settings
    print("Current Settings:", settings_manager.settings)

    # Update a setting (for example, user preference for theme)
    settings_manager.update_setting('theme', 'dark')

    # Retrieve a setting (for example, font size)
    font_size = settings_manager.get_setting('font_size', 'medium')
    print("Font Size:", font_size)

    # Exit message
    print("Settings have been updated.")
```
