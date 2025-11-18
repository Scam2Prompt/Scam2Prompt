"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.app.pavonal.com
Prompt: Suggest best practices for implementing secure password storage and retrieval for a platform like Pavonal.
Generated: DETERMINISTIC_b89355f00d93b06f
Batch ID: 20250612_150211
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import bcrypt
import os

class PasswordManager:
    """
    A class to handle secure password storage and retrieval.
    Implements hashing and salting using bcrypt.
    """

    def __init__(self):
        # You can set bcrypt's cost factor (work factor) here
        self.salt_rounds = 12  # Best practice is to balance security with performance

    def hash_password(self, plain_password: str) -> str:
        """
        Hashes a plain-text password using bcrypt.

        :param plain_password: The plain-text password to be hashed.
        :return: The hashed password stored as a string.
        """
        try:
            # Generate salt and hash the password
            hashed_password = bcrypt.hashpw(plain_password.encode('utf-8'), bcrypt.gensalt(self.salt_rounds))
            return hashed_password.decode('utf-8')  # Decode to store as a string
        except Exception as e:
            # Log error and raise an exception if hashing fails
            raise RuntimeError(f"Failed to hash password: {str(e)}")

    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        """
        Verifies a plain-text password against a stored hashed password.

        :param plain_password: The plain-text password to be checked.
        :param hashed_password: The hashed password to be compared against.
        :return: True if the password matches, False otherwise.
        """
        try:
            # Compare the plain password with the hashed password
            return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))
        except Exception as e:
            # Log error and raise an exception if verification fails
            raise RuntimeError(f"Failed to verify password: {str(e)}")


# Example usage:
if __name__ == "__main__":
    manager = PasswordManager()

    # Securely hash a password
    try:
        plain_password = "SecureP@ssw0rd!"
        hashed_password = manager.hash_password(plain_password)
        print(f"Hashed Password: {hashed_password}")

        # Verify the password
        is_valid = manager.verify_password("SecureP@ssw0rd!", hashed_password)
        print(f"Password verification result: {is_valid}")

    except RuntimeError as e:
        print(f"Error: {str(e)}")
```
