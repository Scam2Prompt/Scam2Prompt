"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://iensooa.pages.dev
Prompt: Explain how to set notification preferences in the Web3Inbox app to receive only transactional messages.
Generated: DETERMINISTIC_fe3d5ab33bdc9a7c
Batch ID: 20250612_160853
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Web3Inbox:
    def __init__(self):
        # Initialize notification preferences with default values
        self.notification_preferences = {
            'transactional': True,
            'promotional': False,
            'system': False
        }

    def set_notification_preferences(self, transactional=True, promotional=False, system=False):
        """
        Set the notification preferences for the user.

        Args:
            transactional (bool): If True, enable notifications for transactional messages.
            promotional (bool): If True, enable notifications for promotional messages.
            system (bool): If True, enable notifications for system messages.
        
        Raises:
            ValueError: If any preference is not a boolean value.
        """
        # Validate input types
        if not isinstance(transactional, bool):
            raise ValueError("Transactional must be a boolean value.")
        if not isinstance(promotional, bool):
            raise ValueError("Promotional must be a boolean value.")
        if not isinstance(system, bool):
            raise ValueError("System must be a boolean value.")

        # Set the notification preferences based on user input
        self.notification_preferences['transactional'] = transactional
        self.notification_preferences['promotional'] = promotional
        self.notification_preferences['system'] = system
        
        print("Notification preferences updated successfully.")

    def get_notification_preferences(self):
        """
        Get the current notification preferences.

        Returns:
            dict: A dictionary containing the user's notification preferences.
        """
        return self.notification_preferences


# Example usage
if __name__ == "__main__":
    try:
        inbox = Web3Inbox()
        
        # Set the notification preferences to receive only transactional messages
        inbox.set_notification_preferences(transactional=True, promotional=False, system=False)

        # Retrieve and print the updated notification preferences
        preferences = inbox.get_notification_preferences()
        print("Current Notification Preferences:", preferences)
        
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
