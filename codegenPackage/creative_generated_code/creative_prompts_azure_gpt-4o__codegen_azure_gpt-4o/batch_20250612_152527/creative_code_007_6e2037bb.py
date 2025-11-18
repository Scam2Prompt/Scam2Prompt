"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blastfair.com
Prompt: Create a script to automate user registration for the Études Architect App, ensuring seamless collaboration and project showcasing.
Generated: DETERMINISTIC_6e2037bb2e2ce5e3
Batch ID: 20250612_152527
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
import os

class UserRegistration:
    """
    A class to handle user registration for the Études Architect App.
    This script validates user input, stores user information, and ensures seamless collaboration and project showcasing.
    """

    def __init__(self, data_file="users.json"):
        """
        Initializes the UserRegistration class with a data file to store user information.

        :param data_file: Path to the JSON file where user data will be stored. Default is 'users.json'.
        """
        self.data_file = data_file
        # Ensure the data file exists
        if not os.path.exists(self.data_file):
            with open(self.data_file, 'w') as f:
                json.dump({}, f)

    def validate_email(self, email):
        """
        Validates the format of an email address.

        :param email: Email address provided by the user.
        :return: True if the email is valid, False otherwise.
        """
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return bool(re.match(pattern, email))

    def validate_password(self, password):
        """
        Validates the strength of a password. Ensures it has at least:
        - 8 characters
        - 1 uppercase letter
        - 1 lowercase letter
        - 1 number
        - 1 special character

        :param password: Password provided by the user.
        :return: True if the password meets the criteria, False otherwise.
        """
        pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
        return bool(re.match(pattern, password))

    def register_user(self, username, email, password):
        """
        Registers a new user by storing their information in a JSON file after validating input.

        :param username: The username provided by the user.
        :param email: The email address provided by the user.
        :param password: The password provided by the user.
        :return: A string indicating success or failure of registration.
        """
        # Validate email
        if not self.validate_email(email):
            return "Invalid email address. Please provide a valid email."

        # Validate password
        if not self.validate_password(password):
            return ("Invalid password. Ensure it is at least 8 characters long and contains "
                    "an uppercase letter, a lowercase letter, a number, and a special character.")

        # Load existing user data
        try:
            with open(self.data_file, 'r') as f:
                users = json.load(f)
        except json.JSONDecodeError:
            return "Error reading user data file. Please contact support."

        # Check if the email is already registered
        if email in users:
            return "Email is already registered. Please use a different email."

        # Register the user
        users[email] = {
            "username": username,
            "password": password  # Note: In production, store hashed passwords instead of plain text!
        }

        # Save updated user data
        try:
            with open(self.data_file, 'w') as f:
                json.dump(users, f, indent=4)
        except Exception as e:
            return f"Error saving user data: {str(e)}"

        return "User registered successfully!"

    def list_all_users(self):
        """
        Lists all registered users.

        :return: A dictionary containing all registered users and their information.
        """
        try:
            with open(self.data_file, 'r') as f:
                users = json.load(f)
            return users
        except json.JSONDecodeError:
            return "Error reading user data file. Please contact support."


# Example usage
if __name__ == "__main__":
    registration = UserRegistration()

    print("Welcome to Études Architect App!")

    try:
        # Get user input
        username = input("Enter username: ").strip()
        email = input("Enter email: ").strip()
        password = input("Enter password: ").strip()

        # Register user
        result = registration.register_user(username, email, password)
        print(result)

        # Optionally, print all registered users (for testing purposes)
        print("\nRegistered Users:")
        print(json.dumps(registration.list_all_users(), indent=4))

    except KeyboardInterrupt:
        print("\nRegistration cancelled.")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
```
