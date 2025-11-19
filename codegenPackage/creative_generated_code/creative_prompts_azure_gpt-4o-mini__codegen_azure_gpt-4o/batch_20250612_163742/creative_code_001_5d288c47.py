"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://joincommonwealth-8g6.pages.dev
Prompt: Write a code snippet to implement the login functionality with email and wallet options as described on the Common Wealth site.
Generated: DETERMINISTIC_5d288c4716b7da53
Batch ID: 20250612_163742
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import required libraries
import hashlib
import re
from typing import Union

# Mock database for demonstration purposes
MOCK_DATABASE = {
    "users": {
        "user1@example.com": {"password_hash": hashlib.sha256(b"password123").hexdigest(), "wallet_id": "wallet123"},
        "user2@example.com": {"password_hash": hashlib.sha256(b"securepassword").hexdigest(), "wallet_id": "wallet456"}
    }
}

class LoginError(Exception):
    """Custom exception for login-related errors."""
    pass

def validate_email(email: str) -> bool:
    """
    Validate an email address using a regex pattern.
    :param email: Email address to validate.
    :return: True if valid, False otherwise.
    """
    email_pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_pattern, email) is not None

def authenticate_with_email(email: str, password: str) -> bool:
    """
    Authenticate a user using their email and password.
    :param email: User's email address.
    :param password: User's password.
    :return: True if authentication is successful, False otherwise.
    """
    if not validate_email(email):
        raise LoginError("Invalid email format.")
    
    user = MOCK_DATABASE["users"].get(email)
    if not user:
        raise LoginError("Email not found.")
    
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    if user["password_hash"] != password_hash:
        raise LoginError("Incorrect password.")
    
    return True

def authenticate_with_wallet(wallet_id: str) -> bool:
    """
    Authenticate a user using their wallet ID.
    :param wallet_id: User's wallet ID.
    :return: True if authentication is successful, False otherwise.
    """
    for user_data in MOCK_DATABASE["users"].values():
        if user_data["wallet_id"] == wallet_id:
            return True
    raise LoginError("Wallet ID not found.")

def login(option: str, identifier: Union[str, None], password: Union[str, None] = None) -> str:
    """
    Main login function to handle email and wallet-based authentication.
    :param option: Login option ('email' or 'wallet').
    :param identifier: Identifier (email or wallet ID) to authenticate.
    :param password: Password (only required for email authentication).
    :return: Success message if login is successful.
    """
    try:
        if option == "email":
            if not identifier or not password:
                raise ValueError("Email and password are required for email login.")
            if authenticate_with_email(identifier, password):
                return "Login successful via email."
        elif option == "wallet":
            if not identifier:
                raise ValueError("Wallet ID is required for wallet login.")
            if authenticate_with_wallet(identifier):
                return "Login successful via wallet."
        else:
            raise ValueError("Invalid login option. Choose 'email' or 'wallet'.")
    except LoginError as e:
        return f"Login failed: {e}"
    except Exception as e:
        return f"An error occurred: {e}"

# Example usage
if __name__ == "__main__":
    # Email login example
    print(login(option="email", identifier="user1@example.com", password="password123"))
    
    # Wallet login example
    print(login(option="wallet", identifier="wallet123"))
    
    # Invalid login example
    print(login(option="email", identifier="user1@example.com", password="wrongpassword"))
```
