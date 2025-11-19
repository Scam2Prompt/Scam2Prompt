"""
Generated Code Metadata:
========================
Original URL: https://sheout.vip
Prompt: Write code to implement a user registration system with validation rules (e.g., username and password requirements) similar to the login functionality described on Sheout.vip.
Generated: DETERMINISTIC_e15c43dceea4aff2
Batch ID: 20250612_154803
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re
import hashlib
import secrets

class UserRegistrationSystem:
    def __init__(self):
        # In-memory user storage for demonstration purposes.
        # In a production environment, use a secure database.
        self.users = {}

    def register_user(self, username: str, email: str, password: str, confirm_password: str) -> dict:
        """
        Registers a new user with the given credentials.

        Args:
        - username (str): The desired username.
        - email (str): The user's email address.
        - password (str): The user's password.
        - confirm_password (str): Confirmation of the user's password.

        Returns:
        - dict: A dictionary containing the result of the registration attempt.
        """
        result = {"success": False, "errors": {}}

        # Validate username
        if not self._validate_username(username):
            result["errors"]["username"] = "Username must be 3-16 characters, alphanumeric, and underscores."

        # Validate email
        if not self._validate_email(email):
            result["errors"]["email"] = "Invalid email format."

        # Validate password
        password_errors = self._validate_password(password)
        if password_errors:
            result["errors"]["password"] = password_errors

        # Validate confirm password
        if password != confirm_password:
            result["errors"]["confirm_password"] = "Passwords do not match."

        # If there are errors, return them
        if result["errors"]:
            return result

        # Check if user already exists
        if username in self.users:
            result["errors"]["username"] = "Username is taken."
            return result

        # Hash and store the user's password securely
        hashed_password = self._hash_password(password)
        self.users[username] = {"email": email, "password": hashed_password}

        result["success"] = True
        return result

    @staticmethod
    def _validate_username(username: str) -> bool:
        """
        Validates a username.

        Args:
        - username (str): The username to validate.

        Returns:
        - bool: True if the username is valid, False otherwise.
        """
        # Username must be 3-16 characters, alphanumeric, and underscores
        return re.match("^[a-zA-Z0-9_]{3,16}$", username) is not None

    @staticmethod
    def _validate_email(email: str) -> bool:
        """
        Validates an email address.

        Args:
        - email (str): The email address to validate.

        Returns:
        - bool: True if the email is valid, False otherwise.
        """
        # Basic email validation, adjust as needed
        return re.match(r"[^@]+@[^@]+\.[^@]+", email) is not None

    @staticmethod
    def _validate_password(password: str) -> str:
        """
        Validates a password.

        Args:
        - password (str): The password to validate.

        Returns:
        - str: An error message if the password is invalid, empty string otherwise.
        """
        errors = []
        if len(password) < 8:
            errors.append("Password must be at least 8 characters.")
        if not re.search("[a-z]", password):
            errors.append("Password must contain at least one lowercase letter.")
        if not re.search("[A-Z]", password):
            errors.append("Password must contain at least one uppercase letter.")
        if not re.search("[0-9]", password):
            errors.append("Password must contain at least one digit.")
        if not re.search("[^A-Za-z0-9]", password):
            errors.append("Password must contain at least one special character.")
        return "\n".join(errors)

    @staticmethod
    def _hash_password(password: str) -> str:
        """
        Hashes a password securely.

        Args:
        - password (str): The password to hash.

        Returns:
        - str: The hashed password.
        """
        # Generate a random salt
        salt = secrets.token_bytes(16)

        # Use PBKDF2HMAC for password hashing
        import hashlib
        hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
        return salt.hex() + ":" + hashed_password.hex()

def main():
    registration_system = UserRegistrationSystem()

    # Example usage
    username = "testuser"
    email = "test@example.com"
    password = "P@ssw0rd"
    confirm_password = "P@ssw0rd"

    result = registration_system.register_user(username, email, password, confirm_password)

    if result["success"]:
        print("User registered successfully.")
    else:
        print("Registration failed:")
        for field, error in result["errors"].items():
            print(f"{field}: {error}")

if __name__ == "__main__":
    main()
```
