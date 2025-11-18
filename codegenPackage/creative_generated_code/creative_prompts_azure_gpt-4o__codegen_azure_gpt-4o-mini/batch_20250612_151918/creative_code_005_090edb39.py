"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pork2.pages.dev
Prompt: Create a registration system for a cryptocurrency project that limits sign-ups to a specific time window, similar to the 48-hour registration period mentioned on the PorkCoin site.
Generated: DETERMINISTIC_090edb398eb3e76f
Batch ID: 20250612_151918
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime, timedelta
import json

class RegistrationSystem:
    def __init__(self, registration_duration_hours=48):
        """Initialize the registration system with a specified duration."""
        self.registration_start_time = datetime.now()
        self.registration_end_time = self.registration_start_time + timedelta(hours=registration_duration_hours)
        self.registered_users = []
    
    def is_registration_open(self):
        """Check if the registration period is currently open."""
        current_time = datetime.now()
        return self.registration_start_time <= current_time <= self.registration_end_time

    def register_user(self, username):
        """Register a new user if the registration is open and username is valid.

        Args:
            username (str): The username of the user to register.

        Raises:
            ValueError: If registration is closed or if username is invalid.
        """
        if not self.is_registration_open():
            raise ValueError("Registration is closed.")
        
        if not self.validate_username(username):
            raise ValueError("Invalid username. Please choose a valid username.")

        self.registered_users.append(username)
        print(f"User '{username}' registered successfully.")

    @staticmethod
    def validate_username(username):
        """Check if the username is valid.

        Args:
            username (str): The username to validate.

        Returns:
            bool: True if valid, False otherwise.
        """
        return isinstance(username, str) and len(username) > 0

    def save_registration_data(self, filename='registrations.json'):
        """Save registered users to a JSON file for persistence.

        Args:
            filename (str): The name of the file to save the data to.
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.registered_users, file)
            print(f"Registered users saved to {filename}.")
        except IOError as e:
            print(f"Error saving to file: {e}")

    def load_registration_data(self, filename='registrations.json'):
        """Load registered users from a JSON file.

        Args:
            filename (str): The name of the file to load data from.
        """
        try:
            with open(filename, 'r') as file:
                self.registered_users = json.load(file)
            print(f"Registered users loaded from {filename}.")
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading from file: {e}")

# Example usage
if __name__ == "__main__":
    registration_system = RegistrationSystem()
    
    try:
        registration_system.register_user("user1")
    except ValueError as e:
        print(e)

    registration_system.save_registration_data()
    registration_system.load_registration_data()
```
