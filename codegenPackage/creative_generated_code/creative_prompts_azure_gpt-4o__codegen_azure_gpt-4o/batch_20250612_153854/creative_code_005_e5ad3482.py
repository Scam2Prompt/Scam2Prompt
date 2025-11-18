"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://alghanim-capital.com
Prompt: Write code to implement a consent management system for tracking user preferences, similar to the cookie management system described on Alghanim Capital's website.
Generated: DETERMINISTIC_e5ad3482851edf1f
Batch ID: 20250612_153854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Consent Management System for tracking user preferences
# Language: Python

import json

class ConsentManager:
    """
    ConsentManager handles user preferences for tracking purposes.
    This includes storing, retrieving, and updating consent status.
    """

    def __init__(self, storage_file="consent_data.json"):
        """
        Initialize the ConsentManager with a storage file.
        :param storage_file: Path to the file where user consents will be stored.
        """
        self.storage_file = storage_file
        self.consent_data = self._load_consents()

    def _load_consents(self):
        """
        Load consent data from the storage file if it exists.
        :return: Dictionary of consent data.
        """
        try:
            with open(self.storage_file, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            # Return an empty dictionary if the file does not exist
            return {}
        except json.JSONDecodeError:
            # Handle corrupted JSON file gracefully
            return {}

    def _save_consents(self):
        """
        Save the current consent data to the storage file.
        """
        try:
            with open(self.storage_file, "w") as file:
                json.dump(self.consent_data, file, indent=4)
        except IOError as e:
            raise Exception(f"Failed to save consent data: {e}")

    def set_preference(self, user_id, preference_type, consent_granted):
        """
        Set a specific consent preference for a user.
        :param user_id: Unique identifier for the user.
        :param preference_type: Type of consent (e.g., "analytics", "advertising").
        :param consent_granted: Boolean indicating if consent is granted.
        """
        if user_id not in self.consent_data:
            self.consent_data[user_id] = {}

        self.consent_data[user_id][preference_type] = consent_granted
        self._save_consents()

    def get_preference(self, user_id, preference_type):
        """
        Retrieve a user's consent preference for a specific type.
        :param user_id: Unique identifier for the user.
        :param preference_type: Type of consent (e.g., "analytics", "advertising").
        :return: Boolean indicating consent status, or None if no preference is set.
        """
        return self.consent_data.get(user_id, {}).get(preference_type)

    def get_all_preferences(self, user_id):
        """
        Retrieve all consent preferences for a user.
        :param user_id: Unique identifier for the user.
        :return: Dictionary of all consent preferences for the user.
        """
        return self.consent_data.get(user_id, {})

    def revoke_all_consents(self, user_id):
        """
        Revoke all consents for a user.
        :param user_id: Unique identifier for the user.
        """
        if user_id in self.consent_data:
            self.consent_data[user_id] = {}
            self._save_consents()


# Example usage
if __name__ == "__main__":
    # Initialize Consent Manager
    consent_manager = ConsentManager()

    # Set consent preferences
    consent_manager.set_preference("user_123", "analytics", True)
    consent_manager.set_preference("user_123", "advertising", False)

    # Retrieve specific preference
    print(consent_manager.get_preference("user_123", "analytics"))  # Output: True

    # Retrieve all preferences for a user
    print(consent_manager.get_all_preferences("user_123"))  # Output: {'analytics': True, 'advertising': False}

    # Revoke all consents for a user
    consent_manager.revoke_all_consents("user_123")
    print(consent_manager.get_all_preferences("user_123"))  # Output: {}
```
