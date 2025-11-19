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
import json
import os

class CookieConsentManager:
    """
    A class to manage cookie consent preferences for a smart home system.
    """

    def __init__(self, consent_file='cookie_consent.json'):
        """
        Initializes the CookieConsentManager with a specified consent file.

        :param consent_file: The path to the JSON file that stores consent preferences.
        """
        self.consent_file = consent_file
        self.consent_data = self.load_consent_data()

    def load_consent_data(self):
        """
        Loads consent data from the JSON file.

        :return: A dictionary containing consent preferences.
        """
        if os.path.exists(self.consent_file):
            with open(self.consent_file, 'r') as file:
                try:
                    return json.load(file)
                except json.JSONDecodeError:
                    print("Error: Consent file is corrupted. Loading default preferences.")
                    return self.default_consent_data()
        else:
            return self.default_consent_data()

    def default_consent_data(self):
        """
        Provides default consent preferences.

        :return: A dictionary with default consent preferences.
        """
        return {
            "analytics": False,
            "personalization": False,
            "advertising": False
        }

    def save_consent_data(self):
        """
        Saves the current consent preferences to the JSON file.
        """
        with open(self.consent_file, 'w') as file:
            json.dump(self.consent_data, file, indent=4)

    def update_consent(self, category, consent):
        """
        Updates the consent preference for a specific category.

        :param category: The category of consent to update (e.g., 'analytics', 'personalization', 'advertising').
        :param consent: A boolean indicating whether consent is given (True) or not (False).
        """
        if category in self.consent_data:
            self.consent_data[category] = consent
            self.save_consent_data()
        else:
            print(f"Error: Invalid consent category '{category}'.")

    def get_consent(self, category):
        """
        Retrieves the consent preference for a specific category.

        :param category: The category of consent to retrieve.
        :return: A boolean indicating whether consent is given or not.
        """
        return self.consent_data.get(category, None)

    def display_consent_preferences(self):
        """
        Displays the current consent preferences in a user-friendly format.
        """
        print("Current Cookie Consent Preferences:")
        for category, consent in self.consent_data.items():
            status = "Granted" if consent else "Denied"
            print(f"{category.capitalize()}: {status}")

if __name__ == "__main__":
    # Example usage of the CookieConsentManager
    manager = CookieConsentManager()

    # Display current preferences
    manager.display_consent_preferences()

    # Update consent preferences
    manager.update_consent('analytics', True)
    manager.update_consent('advertising', False)

    # Display updated preferences
    manager.display_consent_preferences()
```
