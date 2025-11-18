"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://flareportalnet.com
Prompt: Write code for a login system that validates both email/password and recovery phrase inputs, inspired by Cointexcrypto's login functionality.
Generated: DETERMINISTIC_b5bbd4f98a5381cb
Batch ID: 20250612_154631
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re
from typing import Tuple, Optional


class LoginSystem:
    def __init__(self):
        # Simulated database of users
        self.users = {
            "user@example.com": {
                "password": "securepassword",  # In practice, this should be hashed
                "recovery_phrase": "my recovery phrase"
            }
        }

    def validate_email(self, email: str) -> bool:
        """Validate the email format using a regular expression."""
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(email_regex, email) is not None

    def validate_password(self, password: str) -> bool:
        """Validate the password against certain criteria."""
        return len(password) >= 8  # Simple password length check

    def login(self, email: str, password: str) -> Optional[str]:
        """Attempt to log in the user with email and password."""
        if not self.validate_email(email):
            raise ValueError("Invalid email format.")

        if not self.validate_password(password):
            raise ValueError("Password must be at least 8 characters long.")

        user = self.users.get(email)

        if user and user['password'] == password:
            return "Login successful!"
        else:
            raise ValueError("Invalid email or password.")

    def recover_account(self, email: str, recovery_phrase: str) -> str:
        """Recover account using email and recovery phrase."""
        if not self.validate_email(email):
            raise ValueError("Invalid email format.")

        user = self.users.get(email)

        if user and user['recovery_phrase'] == recovery_phrase:
            return "Account recovery successful!"
        else:
            raise ValueError("Invalid email or recovery phrase.")


# Example usage
if __name__ == "__main__":
    login_system = LoginSystem()

    try:
        print(login_system.login("user@example.com", "securepassword"))
    except ValueError as e:
        print(f"Login failed: {e}")

    try:
        print(login_system.recover_account("user@example.com", "my recovery phrase"))
    except ValueError as e:
        print(f"Recovery failed: {e}")
```
