"""
Generated Code Metadata:
========================
Original URL: https://frame.money
Prompt: "Write a Python script to handle user privacy preferences for a website with a privacy policy similar to frame.money's."
Generated: DETERMINISTIC_4b0b02051511efe7
Batch ID: 20250622_204623
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# user_privacy_preferences.py

import json
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class UserPrivacyPreferences:
    """
    Handles user privacy preferences for a website.

    Attributes:
        preferences (dict): User's privacy preferences.
    """

    def __init__(self):
        self.preferences = {
            'analytics': False,
            'functional': False,
            'advertising': False,
            'strictly_necessary': True  # Always true for strictly necessary cookies
        }

    def get_preferences(self):
        """
        Retrieves the user's current privacy preferences.

        Returns:
            dict: User's privacy preferences.
        """
        return self.preferences

    def update_preferences(self, preferences):
        """
        Updates the user's privacy preferences.

        Args:
            preferences (dict): New privacy preferences.

        Raises:
            ValueError: If the provided preferences are invalid.
        """
        if not isinstance(preferences, dict):
            raise ValueError("Preferences must be a dictionary")

        for key, value in preferences.items():
            if key in self.preferences:
                if isinstance(value, bool):
                    self.preferences[key] = value
                else:
                    raise ValueError("Preference values must be boolean")
            else:
                logger.warning(f"Unknown preference: {key}")

    def to_json(self):
        """
        Converts the user's privacy preferences to a JSON string.

        Returns:
            str: JSON representation of the user's privacy preferences.
        """
        return json.dumps(self.preferences)

    @classmethod
    def from_json(cls, json_string):
        """
        Creates a UserPrivacyPreferences instance from a JSON string.

        Args:
            json_string (str): JSON representation of the user's privacy preferences.

        Returns:
            UserPrivacyPreferences: Instance with the user's privacy preferences.

        Raises:
            json.JSONDecodeError: If the JSON string is invalid.
        """
        try:
            preferences = json.loads(json_string)
            instance = cls()
            instance.update_preferences(preferences)
            return instance
        except json.JSONDecodeError as e:
            logger.error(f"Invalid JSON: {e}")
            raise

def main():
    # Example usage
    user_preferences = UserPrivacyPreferences()

    # Update preferences
    new_preferences = {
        'analytics': True,
        'functional': True,
        'advertising': False
    }
    user_preferences.update_preferences(new_preferences)

    # Get current preferences
    current_preferences = user_preferences.get_preferences()
    logger.info(f"Current preferences: {current_preferences}")

    # Convert to JSON
    json_string = user_preferences.to_json()
    logger.info(f"Preferences as JSON: {json_string}")

    # Create instance from JSON
    loaded_preferences = UserPrivacyPreferences.from_json(json_string)
    logger.info(f"Loaded preferences: {loaded_preferences.get_preferences()}")

if __name__ == "__main__":
    main()
```
