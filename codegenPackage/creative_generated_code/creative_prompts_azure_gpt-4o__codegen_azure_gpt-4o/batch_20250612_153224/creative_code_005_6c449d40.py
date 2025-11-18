"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vigilanciadomotica.es
Prompt: Create a program to manage cookie consent preferences for a smart home system, inspired by the privacy and cookie management features described on vigilanciadomotica.es.
Generated: DETERMINISTIC_6c449d40eff2b6ed
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Cookie Consent Management System for Smart Home Devices

This script allows smart home systems to manage and store cookie consent
preferences for users in a privacy-compliant manner.

Key Features:
- Users can provide consent for functional, performance, and marketing cookies.
- Preferences are stored securely in a local JSON file.
- Includes error handling to ensure robust operation.
"""

import json
import os

# Constants
PREFERENCES_FILE = "cookie_preferences.json"
COOKIE_TYPES = ["functional", "performance", "marketing"]

class CookieConsentManager:
    """
    Manages cookie consent preferences for users in a smart home system.
    """
    def __init__(self, preferences_file):
        """
        Initializes the manager with the given preferences file.
        """
        self.preferences_file = preferences_file
        self.preferences = {}

        # Load existing preferences or initialize new ones
        self.load_preferences()

    def load_preferences(self):
        """
        Loads cookie preferences from the JSON file. If not found, initializes empty preferences.
        """
        if os.path.exists(self.preferences_file):
            try:
                with open(self.preferences_file, 'r') as file:
                    self.preferences = json.load(file)
            except json.JSONDecodeError:
                print("Error: Preferences file is corrupted. Initializing new preferences.")
                self.preferences = {}
            except Exception as e:
                print(f"Error: Unable to load preferences file. {e}")
                self.preferences = {}
        else:
            self.preferences = {}

    def save_preferences(self):
        """
        Saves cookie preferences to the JSON file securely.
        """
        try:
            with open(self.preferences_file, 'w') as file:
                json.dump(self.preferences, file, indent=4)
        except Exception as e:
            print(f"Error: Unable to save preferences. {e}")

    def set_preference(self, user_id, cookie_type, consent):
        """
        Sets the cookie consent preference for a specific user and cookie type.

        :param user_id: Unique identifier for the user
        :param cookie_type: Type of cookie (e.g., functional, performance, marketing)
        :param consent: Boolean indicating consent (True for consent, False for no consent)
        """
        if cookie_type not in COOKIE_TYPES:
            print(f"Error: Invalid cookie type '{cookie_type}'. Valid types are: {COOKIE_TYPES}")
            return

        if user_id not in self.preferences:
            self.preferences[user_id] = {cookie: False for cookie in COOKIE_TYPES}

        self.preferences[user_id][cookie_type] = consent
        self.save_preferences()
        print(f"Preference updated: User {user_id}, {cookie_type} cookies = {consent}")

    def get_preferences(self, user_id):
        """
        Retrieves the cookie preferences for a specific user.

        :param user_id: Unique identifier for the user
        :return: Dictionary containing cookie types and their consent statuses
        """
        return self.preferences.get(user_id, {cookie: False for cookie in COOKIE_TYPES})

    def display_preferences(self, user_id):
        """
        Displays the cookie preferences for a specific user.

        :param user_id: Unique identifier for the user
        """
        user_preferences = self.get_preferences(user_id)
        print(f"Cookie preferences for user {user_id}:")
        for cookie_type, consent in user_preferences.items():
            print(f"  {cookie_type.capitalize()}: {'Consented' if consent else 'Not Consented'}")


# Example Usage
if __name__ == "__main__":
    manager = CookieConsentManager(PREFERENCES_FILE)

    # Set preferences for a user
    manager.set_preference("user123", "functional", True)
    manager.set_preference("user123", "performance", False)
    manager.set_preference("user123", "marketing", True)

    # Display preferences for a user
    manager.display_preferences("user123")

    # Get preferences programmatically
    preferences = manager.get_preferences("user123")
    print("Programmatic access to preferences:", preferences)
```
