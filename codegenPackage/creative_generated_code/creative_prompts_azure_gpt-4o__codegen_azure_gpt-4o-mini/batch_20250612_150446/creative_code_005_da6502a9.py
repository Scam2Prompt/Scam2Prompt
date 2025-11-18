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
from typing import List, Optional

class AccountCreationError(Exception):
    """Custom exception for account creation errors."""
    pass

class Account:
    def __init__(self, username: str, email: str, ip_address: str, payment_account: str):
        self.username = username
        self.email = email
        self.ip_address = ip_address
        self.payment_account = payment_account

class AccountValidator:
    def __init__(self):
        self.existing_accounts: List[Account] = []

    def validate_username(self, username: str) -> None:
        """Validate the username for restrictions."""
        if not username or len(username) < 5:
            raise AccountCreationError("Username must be at least 5 characters long.")

    def validate_email(self, email: str) -> None:
        """Validate the email format."""
        email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        if not re.match(email_regex, email):
            raise AccountCreationError("Invalid email format.")

    def check_duplicate_ip(self, ip_address: str) -> None:
        """Check for existing accounts under the same IP address."""
        if any(account.ip_address == ip_address for account in self.existing_accounts):
            raise AccountCreationError("An account already exists under this IP address.")

    def check_duplicate_payment_account(self, payment_account: str) -> None:
        """Check for existing accounts with the same payment account."""
        if any(account.payment_account == payment_account for account in self.existing_accounts):
            raise AccountCreationError("An account already exists with this payment account.")

    def create_account(self, username: str, email: str, ip_address: str, payment_account: str) -> Account:
        """Create a new account after validation."""
        self.validate_username(username)
        self.validate_email(email)
        self.check_duplicate_ip(ip_address)
        self.check_duplicate_payment_account(payment_account)

        # If all validations pass, create and store the new account
        new_account = Account(username, email, ip_address, payment_account)
        self.existing_accounts.append(new_account)
        
        return new_account

def main():
    """Main function to demonstrate account creation."""
    validator = AccountValidator()
    
    # Example account creation
    try:
        account = validator.create_account("user123", "user@example.com", "192.168.1.1", "payment_001")
        print(f"Account created successfully: {account.username}")
    except AccountCreationError as e:
        print(f"Account creation failed: {e}")

if __name__ == "__main__":
    main()
```
