"""
Generated Code Metadata:
========================
Original URL: https://pork2.pages.dev
Prompt: Create a registration system for a cryptocurrency project that limits sign-ups to a specific time window, similar to the 48-hour registration period mentioned on the PorkCoin site.
Generated: DETERMINISTIC_090edb398eb3e76f
Batch ID: 20250612_151918
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime, timedelta
import json

class RegistrationSystem:
    def __init__(self, start_time: str, duration_hours: int):
        """
        Initializes the registration system with a start time and duration.

        :param start_time: The start time of the registration period in ISO format (e.g., '2023-10-01T12:00:00').
        :param duration_hours: The duration of the registration period in hours.
        """
        self.start_time = datetime.fromisoformat(start_time)
        self.end_time = self.start_time + timedelta(hours=duration_hours)
        self.registered_users = []

    def is_registration_open(self) -> bool:
        """
        Checks if the registration period is currently open.

        :return: True if registration is open, False otherwise.
        """
        current_time = datetime.now()
        return self.start_time <= current_time <= self.end_time

    def register_user(self, username: str) -> str:
        """
        Registers a new user if the registration period is open.

        :param username: The username of the user to register.
        :return: A message indicating the result of the registration attempt.
        """
        if not self.is_registration_open():
            return "Registration is closed. Please try again later."

        if username in self.registered_users:
            return "Username already taken. Please choose a different username."

        self.registered_users.append(username)
        return f"User '{username}' registered successfully."

    def get_registered_users(self) -> str:
        """
        Returns a JSON string of the registered users.

        :return: A JSON string of registered users.
        """
        return json.dumps(self.registered_users)

# Example usage
if __name__ == "__main__":
    # Define the registration start time and duration
    registration_start_time = '2023-10-01T12:00:00'
    registration_duration = 48  # in hours

    # Create an instance of the registration system
    registration_system = RegistrationSystem(registration_start_time, registration_duration)

    # Attempt to register users
    print(registration_system.register_user("Alice"))
    print(registration_system.register_user("Bob"))
    print(registration_system.register_user("Alice"))  # Attempt to register the same user

    # Output the list of registered users
    print("Registered Users:", registration_system.get_registered_users())
```
