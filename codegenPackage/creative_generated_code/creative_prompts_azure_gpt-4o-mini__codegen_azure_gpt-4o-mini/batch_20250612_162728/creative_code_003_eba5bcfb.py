"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://swiftrealisticevm.com
Prompt: Can you provide a code snippet for handling errors related to account suspension in a web application?
Generated: DETERMINISTIC_eba5bcfb223a2715
Batch ID: 20250612_162728
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# account_manager.py

class AccountSuspensionError(Exception):
    """Custom exception raised when an account is suspended."""
    pass

class Account:
    def __init__(self, username, is_suspended=False):
        """
        Initialize an account with a username and suspended status.
        
        :param username: str, the username of the account
        :param is_suspended: bool, the suspension status of the account
        """
        self.username = username
        self.is_suspended = is_suspended

    def login(self):
        """
        Attempt to log in the account.

        Raises:
            AccountSuspensionError: if the account is suspended
        """
        if self.is_suspended:
            raise AccountSuspensionError(f"Account '{self.username}' is suspended. Please contact support.")

        # Proceed with the login process (placeholder)
        return f"Login successful for user '{self.username}'."


def handle_login(username, is_suspended):
    """
    Handle the login process for a user.

    :param username: str, the username of the account
    :param is_suspended: bool, the suspension status of the account
    """
    account = Account(username, is_suspended)
    
    try:
        result = account.login()
        print(result)

    except AccountSuspensionError as e:
        print(e)
        # Here you can add logic to notify the user or log the issue
        # For example, log the error to a logging system
        log_error(e)

def log_error(error):
    """
    Log the error to a logging system or file.

    :param error: Exception, the error to log
    """
    # Placeholder for logging logic
    # For example, using Python's logging module:
    import logging
    logging.basicConfig(level=logging.ERROR)
    logging.error(str(error))

# Example usage
if __name__ == "__main__":
    handle_login("john_doe", is_suspended=True)  # Simulate logging in a suspended user
    handle_login("jane_doe", is_suspended=False)  # Simulate logging in an active user
```
