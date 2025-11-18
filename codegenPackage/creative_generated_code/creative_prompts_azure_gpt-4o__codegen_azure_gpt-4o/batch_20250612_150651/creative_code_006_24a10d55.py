"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://globallinknext.com
Prompt: Create a script to analyze user preferences and manage consent for cookies, similar to the consent management system described on the GlobalLink NEXT website.
Generated: DETERMINISTIC_24a10d55ea84f145
Batch ID: 20250612_150651
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import Dict, List

class CookieConsentManager:
    """
    A class to manage user cookie preferences and consent.
    """

    def __init__(self, default_preferences: Dict[str, bool] = None):
        """
        Initialize the CookieConsentManager with default preferences.

        :param default_preferences: A dictionary defining default cookie preferences.
                                    Example: {"analytics": False, "functional": True, "ads": False}
        """
        if default_preferences is None:
            default_preferences = {
                "analytics": False,
                "functional": True,
                "ads": False
            }
        self.preferences = default_preferences
        self.consent_given = False  # Tracks if the user has given consent

    def set_preferences(self, preferences: Dict[str, bool]) -> None:
        """
        Update cookie preferences based on user input.

        :param preferences: A dictionary specifying updated cookie preferences.
                            Example: {"analytics": True, "functional": True, "ads": True}
        :raises ValueError: If preferences contain invalid cookie categories.
        """
        for key in preferences.keys():
            if key not in self.preferences:
                raise ValueError(f"Invalid cookie category: {key}")
        self.preferences.update(preferences)

    def give_consent(self) -> None:
        """
        Sets consent to True, indicating the user has actively given consent to cookie usage.
        """
        self.consent_given = True

    def withdraw_consent(self) -> None:
        """
        Withdraw consent and reset preferences to default settings.
        """
        self.consent_given = False
        self.preferences = {key: False for key in self.preferences}

    def get_preferences(self) -> Dict[str, bool]:
        """
        Retrieve the current cookie preferences.

        :return: A dictionary containing current cookie preferences.
        """
        return self.preferences

    def save_preferences_to_file(self, file_path: str) -> None:
        """
        Save current preferences to a JSON file.

        :param file_path: The file path where preferences should be saved.
        :raises IOError: If an error occurs while writing to the file.
        """
        try:
            with open(file_path, 'w') as f:
                json.dump({"preferences": self.preferences, "consent_given": self.consent_given}, f, indent=4)
        except IOError as e:
            raise IOError(f"Error saving preferences to file: {e}")

    def load_preferences_from_file(self, file_path: str) -> None:
        """
        Load preferences from a JSON file.

        :param file_path: The file path from which preferences should be loaded.
        :raises IOError: If an error occurs while reading from the file.
        :raises ValueError: If the file contains invalid data.
        """
        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
                if "preferences" not in data or "consent_given" not in data:
                    raise ValueError("Invalid preferences file format.")
                self.preferences = data["preferences"]
                self.consent_given = data["consent_given"]
        except IOError as e:
            raise IOError(f"Error loading preferences from file: {e}")
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON format in preferences file.")

if __name__ == "__main__":
    # Example usage of CookieConsentManager
    consent_manager = CookieConsentManager()

    # Show default preferences
    print("Default preferences:", consent_manager.get_preferences())

    # User updates preferences
    updated_preferences = {"analytics": True, "functional": True, "ads": False}
    consent_manager.set_preferences(updated_preferences)
    print("Updated preferences:", consent_manager.get_preferences())

    # User gives consent
    consent_manager.give_consent()
    print("Consent given:", consent_manager.consent_given)

    # Save to file
    consent_manager.save_preferences_to_file("preferences.json")
    print("Preferences saved to file.")

    # Load preferences from file
    consent_manager.load_preferences_from_file("preferences.json")
    print("Preferences loaded from file:", consent_manager.get_preferences())
    print("Consent status from file:", consent_manager.consent_given)

    # Withdraw consent
    consent_manager.withdraw_consent()
    print("Consent withdrawn. Preferences reset:", consent_manager.get_preferences())
```
