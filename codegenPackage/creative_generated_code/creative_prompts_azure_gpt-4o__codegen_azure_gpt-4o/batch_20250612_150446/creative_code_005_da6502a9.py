"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tradingtrustltd.com
Prompt: Write a program that validates user account creation based on Trading-Trust Ltd's rules, such as preventing multiple accounts under the same IP or payment account.
Generated: DETERMINISTIC_da6502a91d6722c2
Batch ID: 20250612_150446
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re
from typing import List, Dict

# Database simulation for storing user accounts
class UserDatabase:
    def __init__(self):
        self.users = []  # List to store user data (IP, payment account, username)

    def is_ip_used(self, ip_address: str) -> bool:
        """
        Check if the given IP address is already associated with a user account.
        """
        return any(user['ip_address'] == ip_address for user in self.users)

    def is_payment_account_used(self, payment_account: str) -> bool:
        """
        Check if the payment account is already associated with a user account.
        """
        return any(user['payment_account'] == payment_account for user in self.users)

    def add_user(self, user: Dict[str, str]):
        """
        Add a new user to the database.
        """
        self.users.append(user)

# Validator class for account creation
class AccountValidator:
    def __init__(self, database: UserDatabase):
        self.database = database

    def validate_username(self, username: str) -> bool:
        """
        Validate the username format.
        Rules:
        - Username must be 3-20 characters long.
        - Only alphanumeric characters and underscores are allowed.
        """
        return bool(re.match(r'^\w{3,20}$', username))

    def validate_ip(self, ip_address: str) -> bool:
        """
        Validate the IP address format.
        - Must follow IPv4 format: XXX.XXX.XXX.XXX (0-255 range per segment).
        """
        try:
            segments = ip_address.split('.')
            if len(segments) != 4:
                return False
            return all(0 <= int(segment) <= 255 for segment in segments)
        except ValueError:
            return False

    def validate_payment_account(self, payment_account: str) -> bool:
        """
        Validate the payment account format.
        Rules:
        - Must be a valid email address.
        """
        return bool(re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', payment_account))

    def validate_user_creation(self, username: str, ip_address: str, payment_account: str) -> str:
        """
        Validate the account creation request with all the rules.
        """
        if not self.validate_username(username):
            return "Invalid username. Must be 3-20 characters long and contain only alphanumeric characters or underscores."

        if not self.validate_ip(ip_address):
            return "Invalid IP address format."

        if not self.validate_payment_account(payment_account):
            return "Invalid payment account format. Must be a valid email address."

        if self.database.is_ip_used(ip_address):
            return "Account creation denied. An account already exists with this IP address."

        if self.database.is_payment_account_used(payment_account):
            return "Account creation denied. An account already exists with this payment account."

        # If all validations pass, return success message
        return "User validated successfully."

# Main program to simulate user account creation
def main():
    # Instantiate the database and validator
    user_database = UserDatabase()
    account_validator = AccountValidator(user_database)

    # Example user inputs for testing
    users_to_create = [
        {"username": "TraderJohn", "ip_address": "192.168.1.1", "payment_account": "john@example.com"},
        {"username": "TraderJane", "ip_address": "192.168.1.2", "payment_account": "jane@example.com"},
        {"username": "TraderJohn", "ip_address": "192.168.1.1", "payment_account": "duplicate@example.com"},  # Duplicate IP
        {"username": "Invalid_User@", "ip_address": "300.1.1.1", "payment_account": "invalid-email"}
    ]

    for user in users_to_create:
        print(f"Creating account for: {user}")
        validation_message = account_validator.validate_user_creation(
            user["username"], user["ip_address"], user["payment_account"]
        )

        if validation_message == "User validated successfully.":
            user_database.add_user(user)  # Add user to the database only if valid
            print("Account created successfully!\n")
        else:
            print(f"Account creation failed: {validation_message}\n")

# Entry point to the program
if __name__ == "__main__":
    main()
```
