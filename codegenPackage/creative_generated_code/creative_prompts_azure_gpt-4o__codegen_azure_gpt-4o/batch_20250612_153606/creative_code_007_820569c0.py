"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://centraldata-enterpristore.com
Prompt: Create a function to manage customer accounts and passwords for first-time login on an ecommerce site, similar to the process described for Central Data's platform.
Generated: DETERMINISTIC_820569c0131471b1
Batch ID: 20250612_153606
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib
import os
import re

class AccountManager:
    """
    A class to manage customer accounts and passwords for an e-commerce site.
    Handles account creation, password validation, and password storage.
    """

    def __init__(self):
        # Dictionary to store user accounts securely (for demonstration purposes)
        # In production, use a secure database instead of in-memory storage.
        self.accounts = {}

    def create_account(self, username, password):
        """
        Create a new customer account with a username and first-time password.
        Validates password strength and ensures the username is unique.

        Args:
            username (str): The customer's username.
            password (str): The customer's initial password.

        Returns:
            str: Success or error message.
        """
        try:
            # Validate username
            if username in self.accounts:
                return "Error: Username already exists. Please choose a different username."

            if not self._is_valid_username(username):
                return "Error: Invalid username. Must contain only alphanumeric characters."

            # Validate password
            password_validation = self._validate_password(password)
            if not password_validation["valid"]:
                return f"Error: Password validation failed. {password_validation['message']}"

            # Hash the password and store the account
            hashed_password = self._hash_password(password)
            self.accounts[username] = hashed_password

            return "Account successfully created!"
        except Exception as e:
            return f"Error: An unexpected issue occurred while creating the account. Details: {str(e)}"

    def _validate_password(self, password):
        """
        Validates the strength of the password based on defined criteria.

        Args:
            password (str): The customer's password.

        Returns:
            dict: A dictionary containing validation result and error message (if applicable).
        """
        if len(password) < 8:
            return {"valid": False, "message": "Password must be at least 8 characters long."}
        if not re.search("[A-Z]", password):
            return {"valid": False, "message": "Password must contain at least one uppercase letter."}
        if not re.search("[a-z]", password):
            return {"valid": False, "message": "Password must contain at least one lowercase letter."}
        if not re.search("[0-9]", password):
            return {"valid": False, "message": "Password must contain at least one numeric digit."}
        if not re.search("[@#$%^&+=]", password):
            return {"valid": False, "message": "Password must contain at least one special character (@#$%^&+=)."}

        return {"valid": True, "message": "Password is valid."}

    def _hash_password(self, password):
        """
        Hashes the password using a secure hashing algorithm (SHA-256).

        Args:
            password (str): The customer's password.

        Returns:
            str: The securely hashed password.
        """
        salt = os.urandom(16)  # Generate a random salt
        salted_password = salt + password.encode("utf-8")  # Combine salt and password
        hashed_password = hashlib.sha256(salted_password).hexdigest()  # Generate SHA-256 hash
        return f"{salt.hex()}:{hashed_password}"  # Return salt and hashed password in a single string

    def _is_valid_username(self, username):
        """
        Validates the username to ensure it contains only alphanumeric characters.

        Args:
            username (str): The customer's username.

        Returns:
            bool: True if valid, False otherwise.
        """
        return bool(re.match("^[a-zA-Z0-9]+$", username))

    def authenticate(self, username, password):
        """
        Authenticates a user based on their username and password.

        Args:
            username (str): The customer's username.
            password (str): The customer's password.

        Returns:
            str: Authentication success or error message.
        """
        try:
            if username not in self.accounts:
                return "Error: Username does not exist."

            # Retrieve stored credentials
            stored_credentials = self.accounts[username]
            stored_salt, stored_hash = stored_credentials.split(":")

            # Hash the input password with the stored salt
            salted_password = bytes.fromhex(stored_salt) + password.encode("utf-8")
            hashed_password = hashlib.sha256(salted_password).hexdigest()

            # Compare the hashes
            if hashed_password == stored_hash:
                return "Authentication successful!"
            else:
                return "Error: Incorrect password."
        except Exception as e:
            return f"Error: An unexpected issue occurred during authentication. Details: {str(e)}"
```

This code provides a complete solution for managing customer accounts and passwords for first-time login with proper validation, password hashing, and secure storage.
