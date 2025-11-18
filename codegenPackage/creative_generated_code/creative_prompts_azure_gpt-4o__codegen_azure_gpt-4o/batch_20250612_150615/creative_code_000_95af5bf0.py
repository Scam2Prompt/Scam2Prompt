"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://flagship.luc.edu
Prompt: Write Python code to simulate a login system that verifies a user's UVID and password, similar to the authentication system described on the Loyola University Chicago Libraries portal.
Generated: DETERMINISTIC_95af5bf02cc5d2c1
Batch ID: 20250612_150615
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib


class LoginSystem:
    def __init__(self):
        # In a real-world scenario, user data should be stored securely in a database.
        # This is a mock data representation for demonstration purposes.
        self.users = {
            "12345678": {
                "password_hash": self._hash_password("securepassword123"),  # Example hashed password
                "name": "John Doe"
            },
            "87654321": {
                "password_hash": self._hash_password("mypassword456"),  # Example hashed password
                "name": "Jane Smith"
            }
        }

    @staticmethod
    def _hash_password(password: str) -> str:
        """
        Hashes a password using SHA-256 algorithm for secure storage.
        :param password: The plain text password to be hashed.
        :return: The hexadecimal string of the hashed password.
        """
        return hashlib.sha256(password.encode()).hexdigest()

    def verify_login(self, uvid: str, password: str) -> str:
        """
        Verifies if the provided UVID and password match the stored data.
        :param uvid: User's unique ID (UVID).
        :param password: User's password.
        :return: Success message if login is valid, or an error message if invalid.
        """
        try:
            # Check if the UVID exists in the user database
            if uvid not in self.users:
                return "Error: UVID not found."

            # Validate the password
            user_data = self.users[uvid]
            hashed_password = self._hash_password(password)
            if hashed_password == user_data["password_hash"]:
                return f"Login successful! Welcome, {user_data['name']}."
            else:
                return "Error: Incorrect password."

        except Exception as e:
            # Catch any unexpected errors
            return f"An unexpected error occurred: {str(e)}"


def main():
    # Simulate the login system
    login_system = LoginSystem()

    print("Welcome to the Loyola University Chicago Libraries Login Portal.")
    uvid = input("Enter your UVID: ").strip()
    password = input("Enter your password: ").strip()

    # Verify login credentials
    result = login_system.verify_login(uvid, password)
    print(result)


if __name__ == "__main__":
    # Entry point for the application
    main()
```
