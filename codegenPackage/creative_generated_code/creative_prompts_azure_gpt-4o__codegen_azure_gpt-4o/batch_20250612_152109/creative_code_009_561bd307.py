"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://prize-graph.net
Prompt: Write code to implement two-password access for Yandex Disk login, ensuring enhanced security as described in the website content.
Generated: DETERMINISTIC_561bd307cd6d3e27
Batch ID: 20250612_152109
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
import getpass

class TwoPasswordAuth:
    """
    TwoPasswordAuth provides a secure two-password authentication mechanism
    to enhance security for login access.
    """

    def __init__(self):
        # Simulated database for storing hashed passwords
        self.passwords = {
            "password1": None,  # Placeholder for first password hash
            "password2": None   # Placeholder for second password hash
        }

    def hash_password(self, password):
        """
        Hashes a password using SHA-256.

        Args:
            password (str): The password to hash.

        Returns:
            str: The hashed password.
        """
        return hashlib.sha256(password.encode()).hexdigest()

    def set_passwords(self):
        """
        Prompts the user to set two passwords and stores their hashes securely.
        """
        print("Set up your passwords for Two-Password Authentication.")
        
        # Get first password from the user
        while True:
            password1 = getpass.getpass("Enter first password: ")
            confirm_password1 = getpass.getpass("Confirm first password: ")
            if password1 == confirm_password1:
                self.passwords["password1"] = self.hash_password(password1)
                break
            else:
                print("First passwords do not match. Please try again.")

        # Get second password from the user
        while True:
            password2 = getpass.getpass("Enter second password: ")
            confirm_password2 = getpass.getpass("Confirm second password: ")
            if password2 == confirm_password2:
                self.passwords["password2"] = self.hash_password(password2)
                break
            else:
                print("Second passwords do not match. Please try again.")

        print("Passwords set successfully.")

    def authenticate(self):
        """
        Prompts the user to enter both passwords and verifies them against stored hashes.

        Returns:
            bool: True if authentication is successful, False otherwise.
        """
        print("Login: Two-Password Authentication")
        
        try:
            # Prompt for the first password
            entered_password1 = getpass.getpass("Enter first password: ")
            if self.hash_password(entered_password1) != self.passwords["password1"]:
                print("First password is incorrect.")
                return False

            # Prompt for the second password
            entered_password2 = getpass.getpass("Enter second password: ")
            if self.hash_password(entered_password2) != self.passwords["password2"]:
                print("Second password is incorrect.")
                return False

        except Exception as e:
            print(f"An error occurred during authentication: {e}")
            return False

        print("Authentication successful!")
        return True


# Main execution flow
if __name__ == "__main__":
    # Initialize the authentication system
    auth_system = TwoPasswordAuth()
    
    # Set passwords only once
    auth_system.set_passwords()

    # Example login flow
    if auth_system.authenticate():
        print("Access granted to Yandex Disk.")
    else:
        print("Access denied.")
```
