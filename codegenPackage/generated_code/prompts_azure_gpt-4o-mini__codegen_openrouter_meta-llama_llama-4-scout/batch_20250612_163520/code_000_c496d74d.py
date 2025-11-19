"""
Generated Code Metadata:
========================
Original URL: https://www.cc-community.net
Prompt: Generate a code snippet for customizing software settings discussed in the CC-Community Board, focusing on user-friendly adjustments for beginners.
Generated: DETERMINISTIC_c496d74d997a9cef
Batch ID: 20250612_163520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# settings_manager.py

class SettingsManager:
    """
    A class to manage and customize software settings.

    Attributes:
    ----------
    settings : dict
        A dictionary to store software settings.

    Methods:
    -------
    load_settings()
        Loads default settings.
    save_settings()
        Saves current settings.
    reset_settings()
        Resets settings to default.
    update_setting(key, value)
        Updates a specific setting.
    get_setting(key)
        Retrieves a specific setting.
    """

    def __init__(self):
        # Initialize default settings
        self.settings = {
            "theme": "light",
            "language": "English",
            "notifications": True,
            "font_size": 12
        }

    def load_settings(self):
        """
        Loads default settings.
        """
        try:
            # Attempt to load settings from file
            with open("settings.json", "r") as file:
                import json
                self.settings = json.load(file)
        except FileNotFoundError:
            # If file does not exist, use default settings
            pass

    def save_settings(self):
        """
        Saves current settings to file.
        """
        try:
            with open("settings.json", "w") as file:
                import json
                json.dump(self.settings, file)
        except Exception as e:
            print(f"Error saving settings: {e}")

    def reset_settings(self):
        """
        Resets settings to default.
        """
        self.settings = {
            "theme": "light",
            "language": "English",
            "notifications": True,
            "font_size": 12
        }
        self.save_settings()

    def update_setting(self, key, value):
        """
        Updates a specific setting.

        Args:
        ----
        key (str): The setting key.
        value: The new value for the setting.
        """
        if key in self.settings:
            self.settings[key] = value
            self.save_settings()
        else:
            print("Invalid setting key.")

    def get_setting(self, key):
        """
        Retrieves a specific setting.

        Args:
        ----
        key (str): The setting key.

        Returns:
        -------
        The value of the setting if it exists, otherwise None.
        """
        return self.settings.get(key)


def main():
    # Example usage
    manager = SettingsManager()
    manager.load_settings()

    print("Current settings:")
    for key, value in manager.settings.items():
        print(f"{key}: {value}")

    manager.update_setting("theme", "dark")
    print("Updated theme to dark.")

    print("Current theme:")
    print(manager.get_setting("theme"))

    manager.reset_settings()
    print("Settings reset to default.")


if __name__ == "__main__":
    main()
```
