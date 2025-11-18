"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://theprofit-rex-ervaring.com
Prompt: Write code to personalize a cryptocurrency trading interface based on user preferences, similar to the customization options provided by the Profit Rex Ervaring app.
Generated: DETERMINISTIC_7c0a7a4ac6c9c66f
Batch ID: 20250612_150843
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

class UserPreferences:
    """
    Class to manage user preferences for the cryptocurrency trading interface.
    Preferences are stored in a JSON file for persistence.
    """

    def __init__(self, preferences_file="user_preferences.json"):
        """
        Initialize UserPreferences with a preferences file.
        """
        self.preferences_file = preferences_file
        self.preferences = {}
        self._load_preferences()

    def _load_preferences(self):
        """
        Load user preferences from the JSON file.
        If the file doesn't exist, initialize with default preferences.
        """
        if os.path.exists(self.preferences_file):
            try:
                with open(self.preferences_file, 'r') as file:
                    self.preferences = json.load(file)
            except json.JSONDecodeError:
                # Handle cases where the file content is not valid JSON
                print("Error: Preferences file contains invalid JSON. Initializing with default preferences.")
                self.preferences = self._default_preferences()
        else:
            self.preferences = self._default_preferences()

    def _default_preferences(self):
        """
        Return default preferences.
        """
        return {
            "theme": "light",  # Options: "light", "dark"
            "default_currency": "BTC",  # Default cryptocurrency for trades
            "notification_settings": {
                "price_alerts": True,  # Enable or disable price alerts
                "trade_updates": True  # Enable or disable trade update notifications
            },
            "preferred_trading_strategy": "day_trading"  # Options: "day_trading", "long_term"
        }

    def save_preferences(self):
        """
        Save user preferences to the JSON file.
        """
        try:
            with open(self.preferences_file, 'w') as file:
                json.dump(self.preferences, file, indent=4)
        except IOError:
            print("Error: Unable to save preferences. Please check file permissions.")

    def update_preference(self, key, value):
        """
        Update a specific preference and save the changes.
        """
        if key in self.preferences:
            self.preferences[key] = value
            self.save_preferences()
        elif key in self.preferences.get("notification_settings", {}):
            self.preferences["notification_settings"][key] = value
            self.save_preferences()
        else:
            print(f"Error: Invalid preference key '{key}'. No changes made.")

    def get_preferences(self):
        """
        Get current user preferences.
        """
        return self.preferences


# Example usage:
if __name__ == "__main__":
    preferences_manager = UserPreferences()

    # Display current preferences
    print("Current Preferences:", preferences_manager.get_preferences())

    # Update theme to 'dark'
    preferences_manager.update_preference("theme", "dark")

    # Update price alerts setting
    preferences_manager.update_preference("price_alerts", False)

    # Display updated preferences
    print("Updated Preferences:", preferences_manager.get_preferences())
```
