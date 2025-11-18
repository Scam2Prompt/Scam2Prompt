"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://midoin.com
Prompt: Generate a script to enforce user-defined privacy settings when sharing Midoin transaction data with friends or the community.
Generated: DETERMINISTIC_8c44c8909a122e27
Batch ID: 20250612_154609
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

class PrivacySettingsError(Exception):
    """Custom exception for privacy settings errors."""
    pass

class UserPrivacySettings:
    """Class to handle user-defined privacy settings for sharing transactions."""

    def __init__(self, user_id):
        """Initialize with user ID and default privacy settings."""
        self.user_id = user_id
        self.settings_file = f"{user_id}_privacy_settings.json"
        self.privacy_settings = self.load_privacy_settings()

    def load_privacy_settings(self):
        """Load privacy settings from a JSON file or create default settings."""
        if os.path.exists(self.settings_file):
            with open(self.settings_file, 'r') as file:
                return json.load(file)
        return self.set_default_privacy_settings()

    def set_default_privacy_settings(self):
        """Set default privacy settings if no settings exist."""
        default_settings = {
            "share_with_friends": True,
            "share_with_community": False,
            "transaction_details": False
        }
        self.save_privacy_settings(default_settings)
        return default_settings

    def save_privacy_settings(self, settings):
        """Save privacy settings to a JSON file."""
        with open(self.settings_file, 'w') as file:
            json.dump(settings, file, indent=4)
        self.privacy_settings = settings

    def update_privacy_setting(self, key, value):
        """Update a specific privacy setting."""
        if key not in self.privacy_settings:
            raise PrivacySettingsError(f"Invalid privacy setting: {key}")
        if not isinstance(value, bool):
            raise PrivacySettingsError(f"Value for {key} must be a boolean.")
        
        self.privacy_settings[key] = value
        self.save_privacy_settings(self.privacy_settings)

    def can_share_transaction(self, transaction):
        """Determine if transaction data can be shared based on privacy settings."""
        if self.privacy_settings['share_with_friends']:
            return True if transaction['shared_with'] == 'friends' else False
        if self.privacy_settings['share_with_community']:
            return True if transaction['shared_with'] == 'community' else False
        return False

def main():
    """Main function to demonstrate privacy settings functionality."""
    user_id = "user123"
    user_privacy = UserPrivacySettings(user_id)

    # Example of updating privacy settings
    try:
        user_privacy.update_privacy_setting('share_with_community', True)
    except PrivacySettingsError as e:
        print(f"Error updating privacy setting: {e}")

    # Example transaction data
    transaction = {
        "amount": 100,
        "currency": "USD",
        "description": "Dinner with friends",
        "shared_with": "friends"
    }

    # Check if transaction can be shared
    if user_privacy.can_share_transaction(transaction):
        print("Transaction data can be shared.")
    else:
        print("Transaction data cannot be shared based on privacy settings.")

if __name__ == "__main__":
    main()
```
