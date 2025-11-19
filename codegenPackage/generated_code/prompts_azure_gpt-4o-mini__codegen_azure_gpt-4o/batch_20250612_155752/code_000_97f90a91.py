"""
Generated Code Metadata:
========================
Original URL: https://bonanzavc.com
Prompt: How can I implement a user registration system for a membership platform similar to BonanzaVC that includes different membership levels and referral codes?
Generated: DETERMINISTIC_97f90a914e479c18
Batch ID: 20250612_155752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import re
import uuid
from datetime import datetime

# Define a class for the user registration system
class UserRegistrationSystem:
    def __init__(self):
        # Initialize storage for users
        self.users = {}
        # Define membership levels
        self.membership_levels = ["Basic", "Silver", "Gold", "Platinum"]

    def validate_email(self, email):
        """
        Validate the email format using regex.
        """
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(email_regex, email) is not None

    def generate_referral_code(self):
        """
        Generate a unique referral code for the user.
        """
        return str(uuid.uuid4())[:8]

    def register_user(self, name, email, membership_level, referral_code=None):
        """
        Register a new user with the given details.
        """
        # Validate input
        if not name or not email or not membership_level:
            return {"success": False, "message": "Name, email, and membership level are required."}

        if not self.validate_email(email):
            return {"success": False, "message": "Invalid email format."}

        if membership_level not in self.membership_levels:
            return {"success": False, "message": f"Invalid membership level. Choose from {self.membership_levels}."}

        if email in self.users:
            return {"success": False, "message": "Email is already registered."}

        # Create user data
        user_data = {
            "name": name,
            "email": email,
            "membership_level": membership_level,
            "referral_code": referral_code if referral_code else self.generate_referral_code(),
            "registration_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        # Store user data
        self.users[email] = user_data

        return {"success": True, "message": "User registered successfully.", "user_data": user_data}

    def get_user(self, email):
        """
        Retrieve user details by email.
        """
        if email in self.users:
            return {"success": True, "user_data": self.users[email]}
        return {"success": False, "message": "User not found."}

    def list_users(self):
        """
        List all registered users.
        """
        return {"success": True, "users": list(self.users.values())}


# Example usage
if __name__ == "__main__":
    # Initialize the registration system
    system = UserRegistrationSystem()

    # Register a user
    response = system.register_user(name="John Doe", email="john.doe@example.com", membership_level="Gold")
    print(response)

    # Register another user with a referral code
    response = system.register_user(name="Jane Smith", email="jane.smith@example.com", membership_level="Silver", referral_code="REF12345")
    print(response)

    # Attempt to register with an invalid email
    response = system.register_user(name="Invalid User", email="invalid-email", membership_level="Basic")
    print(response)

    # Retrieve user details
    response = system.get_user(email="john.doe@example.com")
    print(response)

    # List all users
    response = system.list_users()
    print(response)
```
