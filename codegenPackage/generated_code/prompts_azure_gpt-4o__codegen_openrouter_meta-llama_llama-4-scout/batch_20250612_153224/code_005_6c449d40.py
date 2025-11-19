"""
Generated Code Metadata:
========================
Original URL: https://vigilanciadomotica.es
Prompt: Create a program to manage cookie consent preferences for a smart home system, inspired by the privacy and cookie management features described on vigilanciadomotica.es.
Generated: DETERMINISTIC_6c449d40eff2b6ed
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# cookie_consent_manager.py

import json
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class CookieConsentManager:
    """
    Manages cookie consent preferences for a smart home system.
    """

    def __init__(self, cookie_file='cookie_consent.json'):
        """
        Initializes the CookieConsentManager.

        Args:
            cookie_file (str): The file path to store cookie consent preferences.
        """
        self.cookie_file = cookie_file
        self.consent_preferences = self.load_consent_preferences()

    def load_consent_preferences(self):
        """
        Loads cookie consent preferences from the specified file.

        Returns:
            dict: A dictionary containing cookie consent preferences.
        """
        try:
            with open(self.cookie_file, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            logging.info("Cookie consent file not found. Creating a new one.")
            return {}

    def save_consent_preferences(self):
        """
        Saves cookie consent preferences to the specified file.
        """
        try:
            with open(self.cookie_file, 'w') as file:
                json.dump(self.consent_preferences, file, indent=4)
        except Exception as e:
            logging.error(f"Error saving cookie consent preferences: {str(e)}")

    def get_consent_preferences(self):
        """
        Retrieves the current cookie consent preferences.

        Returns:
            dict: A dictionary containing cookie consent preferences.
        """
        return self.consent_preferences

    def update_consent_preferences(self, preferences):
        """
        Updates the cookie consent preferences.

        Args:
            preferences (dict): A dictionary containing updated cookie consent preferences.
        """
        self.consent_preferences = preferences
        self.save_consent_preferences()

    def opt_out_all(self):
        """
        Opts out of all cookie tracking.
        """
        self.consent_preferences = {}
        self.save_consent_preferences()

def main():
    # Example usage:
    cookie_manager = CookieConsentManager()

    # Get current consent preferences
    print("Current Consent Preferences:")
    print(cookie_manager.get_consent_preferences())

    # Update consent preferences
    new_preferences = {
        "analytics": True,
        "advertising": False,
        "functional": True
    }
    cookie_manager.update_consent_preferences(new_preferences)

    # Get updated consent preferences
    print("\nUpdated Consent Preferences:")
    print(cookie_manager.get_consent_preferences())

    # Opt out of all cookie tracking
    cookie_manager.opt_out_all()

    # Get consent preferences after opting out
    print("\nConsent Preferences after Opting Out:")
    print(cookie_manager.get_consent_preferences())

if __name__ == "__main__":
    main()
```
