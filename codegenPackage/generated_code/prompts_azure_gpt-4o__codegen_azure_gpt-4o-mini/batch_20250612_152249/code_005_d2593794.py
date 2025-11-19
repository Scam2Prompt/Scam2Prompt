"""
Generated Code Metadata:
========================
Original URL: https://sandbox.co.com
Prompt: Write code to implement a "responsible gaming" feature for an online casino platform, inspired by 8KBet's policies.
Generated: DETERMINISTIC_d2593794825986a3
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime, timedelta

class ResponsibleGaming:
    """
    A class to implement responsible gaming features for an online casino platform.
    """

    def __init__(self, user_id):
        """
        Initializes the ResponsibleGaming instance for a specific user.

        :param user_id: Unique identifier for the user
        """
        self.user_id = user_id
        self.settings = {
            "deposit_limit": 0,
            "loss_limit": 0,
            "session_time_limit": 0,
            "self_exclusion": False,
            "last_updated": datetime.now()
        }

    def set_deposit_limit(self, amount):
        """
        Set a deposit limit for the user.

        :param amount: The maximum amount the user can deposit
        :raises ValueError: If the amount is negative
        """
        if amount < 0:
            raise ValueError("Deposit limit must be a non-negative value.")
        self.settings["deposit_limit"] = amount
        self.settings["last_updated"] = datetime.now()

    def set_loss_limit(self, amount):
        """
        Set a loss limit for the user.

        :param amount: The maximum amount the user can lose
        :raises ValueError: If the amount is negative
        """
        if amount < 0:
            raise ValueError("Loss limit must be a non-negative value.")
        self.settings["loss_limit"] = amount
        self.settings["last_updated"] = datetime.now()

    def set_session_time_limit(self, minutes):
        """
        Set a session time limit for the user.

        :param minutes: The maximum session time in minutes
        :raises ValueError: If the minutes are negative
        """
        if minutes < 0:
            raise ValueError("Session time limit must be a non-negative value.")
        self.settings["session_time_limit"] = minutes
        self.settings["last_updated"] = datetime.now()

    def enable_self_exclusion(self):
        """
        Enable self-exclusion for the user.
        """
        self.settings["self_exclusion"] = True
        self.settings["last_updated"] = datetime.now()

    def disable_self_exclusion(self):
        """
        Disable self-exclusion for the user.
        """
        self.settings["self_exclusion"] = False
        self.settings["last_updated"] = datetime.now()

    def get_settings(self):
        """
        Retrieve the current responsible gaming settings for the user.

        :return: A dictionary containing the user's responsible gaming settings
        """
        return self.settings

    def save_settings(self, file_path):
        """
        Save the current settings to a JSON file.

        :param file_path: The path to the file where settings will be saved
        :raises IOError: If there is an error writing to the file
        """
        try:
            with open(file_path, 'w') as file:
                json.dump(self.settings, file, default=str)
        except IOError as e:
            raise IOError(f"Error saving settings to file: {e}")

    def load_settings(self, file_path):
        """
        Load settings from a JSON file.

        :param file_path: The path to the file from which settings will be loaded
        :raises IOError: If there is an error reading the file
        :raises ValueError: If the file contains invalid JSON
        """
        try:
            with open(file_path, 'r') as file:
                self.settings = json.load(file)
                self.settings["last_updated"] = datetime.now()
        except IOError as e:
            raise IOError(f"Error loading settings from file: {e}")
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON format in settings file: {e}")

# Example usage:
if __name__ == "__main__":
    user_rg = ResponsibleGaming(user_id=12345)
    user_rg.set_deposit_limit(500)
    user_rg.set_loss_limit(200)
    user_rg.set_session_time_limit(60)
    user_rg.enable_self_exclusion()

    print(user_rg.get_settings())

    # Save settings to a file
    user_rg.save_settings("user_12345_rg_settings.json")

    # Load settings from a file
    user_rg.load_settings("user_12345_rg_settings.json")
```
