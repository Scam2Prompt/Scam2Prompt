"""
Generated Code Metadata:
========================
Original URL: https://securespend.io
Prompt: Develop a script that simulates a user registration process for an online togel betting platform, ensuring unique member IDs.
Generated: DETERMINISTIC_78d0a370db14e58d
Batch ID: 20250612_163935
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import string
from typing import Dict, Optional

class UserRegistration:
    """
    A class to simulate user registration for an online togel betting platform.
    Ensures unique member IDs are generated for each user.
    """

    def __init__(self):
        self.registered_users: Dict[str, Dict[str, str]] = {}
        self.member_id_length = 8

    def generate_member_id(self) -> str:
        """
        Generates a unique alphanumeric member ID.
        
        Returns:
            str: A unique member ID.
        """
        while True:
            member_id = ''.join(
                random.choices(
                    string.ascii_uppercase + string.digits,
                    k=self.member_id_length
                )
            )
            if member_id not in self.registered_users:
                return member_id

    def register_user(
        self,
        username: str,
        password: str,
        email: str,
        phone: str
    ) -> Optional[Dict[str, str]]:
        """
        Registers a new user with a unique member ID.
        
        Args:
            username (str): The user's chosen username.
            password (str): The user's chosen password.
            email (str): The user's email address.
            phone (str): The user's phone number.
            
        Returns:
            Optional[Dict[str, str]]: User details including member ID if successful, None otherwise.
        """
        if not all([username, password, email, phone]):
            print("Error: All fields are required.")
            return None

        if username in [user['username'] for user in self.registered_users.values()]:
            print("Error: Username already exists.")
            return None

        if email in [user['email'] for user in self.registered_users.values()]:
            print("Error: Email already registered.")
            return None

        member_id = self.generate_member_id()
        self.registered_users[member_id] = {
            'username': username,
            'password': password,  # Note: In production, hash the password!
            'email': email,
            'phone': phone
        }

        print(f"User {username} registered successfully with Member ID: {member_id}")
        return {
            'member_id': member_id,
            'username': username,
            'email': email,
            'phone': phone
        }

    def get_user_details(self, member_id: str) -> Optional[Dict[str, str]]:
        """
        Retrieves user details by member ID.
        
        Args:
            member_id (str): The member ID to look up.
            
        Returns:
            Optional[Dict[str, str]]: User details if found, None otherwise.
        """
        return self.registered_users.get(member_id)


# Example usage
if __name__ == "__main__":
    registration_system = UserRegistration()

    # Register new users
    user1 = registration_system.register_user(
        username="johndoe",
        password="secure123",
        email="john@example.com",
        phone="1234567890"
    )

    user2 = registration_system.register_user(
        username="janedoe",
        password="safe456",
        email="jane@example.com",
        phone="0987654321"
    )

    # Attempt to register duplicate username
    user3 = registration_system.register_user(
        username="johndoe",
        password="anotherpass",
        email="john2@example.com",
        phone="1112223333"
    )

    # Retrieve user details
    if user1:
        details = registration_system.get_user_details(user1['member_id'])
        print(f"User details: {details}")
```
