"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cashb90.net
Prompt: Write a Python script to automate user registration for a betting site that offers live dealer games, inspired by BaxBet's features.
Generated: DETERMINISTIC_e410295d9a010a2d
Batch ID: 20250612_155855
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re
import json


class BettingSiteRegistration:
    """Class to handle user registration for a betting site."""

    def __init__(self, database_file="users.json"):
        """
        Initialize the registration system.

        Args:
            database_file (str): Path to the JSON file that stores user data.
        """
        self.database_file = database_file
        self.users = self._load_users()

    def _load_users(self):
        """
        Load users from the JSON file.

        Returns:
            list: List of users loaded from the file.
        """
        try:
            with open(self.database_file, "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            # Initialize with an empty list if file doesn't exist or is invalid
            return []

    def _save_users(self):
        """Save users to the JSON file."""
        try:
            with open(self.database_file, "w") as file:
                json.dump(self.users, file, indent=4)
        except Exception as e:
            print(f"Error saving users: {e}")

    def validate_email(self, email):
        """
        Validate email format.

        Args:
            email (str): Email address to validate.

        Returns:
            bool: True if email is valid, False otherwise.
        """
        email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        return bool(re.match(email_regex, email))

    def validate_password(self, password):
        """
        Validate password strength.

        Args:
            password (str): Password to validate.

        Returns:
            bool: True if password is strong, False otherwise.
        """
        # Password must be at least 8 characters, include a number, a capital letter, and a special character
        password_regex = r"^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
        return bool(re.match(password_regex, password))

    def register_user(self, username, email, password):
        """
        Register a new user.

        Args:
            username (str): Username of the user.
            email (str): Email address of the user.
            password (str): Password for the user.

        Returns:
            str: Registration status message.
        """
        # Check if username already exists
        if any(user["username"] == username for user in self.users):
            return "Error: Username already exists."

        # Validate email
        if not self.validate_email(email):
            return "Error: Invalid email format."

        # Check if email already exists
        if any(user["email"] == email for user in self.users):
            return "Error: Email already exists."

        # Validate password
        if not self.validate_password(password):
            return (
                "Error: Password must be at least 8 characters long, include a "
                "number, a capital letter, and a special character."
            )

        # Add the new user to the database
        new_user = {"username": username, "email": email, "password": password}
        self.users.append(new_user)
        self._save_users()

        return "Success: User registered successfully!"

    def display_users(self):
        """Display all registered users."""
        return self.users


if __name__ == "__main__":
    # Instance of the registration system
    registration_system = BettingSiteRegistration()

    # Example user inputs (replace with actual user inputs in production)
    username = input("Enter username: ").strip()
    email = input("Enter email: ").strip()
    password = input("Enter password: ").strip()

    # Register the user
    result = registration_system.register_user(username, email, password)
    print(result)

    # Display all users (for admin purposes)
    print("Registered Users:")
    print(json.dumps(registration_system.display_users(), indent=4))
```
