"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://usdtchecker.agency
Prompt: How can I implement error handling in my application to manage account suspension scenarios effectively?
Generated: DETERMINISTIC_674af799b48b46bd
Batch ID: 20250612_161235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class AccountSuspensionError(Exception):
    """Custom exception for handling account suspension scenarios."""
    pass

class Account:
    def __init__(self, username, is_suspended=False):
        """Initialize an account with a username and suspension status.

        Args:
            username (str): The username of the account.
            is_suspended (bool): The suspension status of the account.
        """
        self.username = username
        self.is_suspended = is_suspended

    def suspend(self):
        """Suspend the account."""
        self.is_suspended = True
        print(f"Account '{self.username}' has been suspended.")

    def activate(self):
        """Activate the account."""
        self.is_suspended = False
        print(f"Account '{self.username}' has been activated.")

    def perform_action(self, action):
        """Perform an action on the account. Raises an error if the account is suspended.

        Args:
            action (str): The action to be performed.

        Raises:
            AccountSuspensionError: If the account is suspended.
        """
        if self.is_suspended:
            raise AccountSuspensionError(f"Action '{action}' cannot be performed. Account '{self.username}' is suspended.")
        else:
            print(f"Action '{action}' performed successfully on account '{self.username}'.")

def main():
    """Main function to demonstrate account management."""
    # Create an account
    account = Account("user123")

    # Attempt to perform an action
    try:
        account.perform_action("login")  # Should work
    except AccountSuspensionError as e:
        print(e)

    # Suspend the account
    account.suspend()

    # Attempt to perform an action after suspension
    try:
        account.perform_action("login")  # Should raise an error
    except AccountSuspensionError as e:
        print(e)

    # Activate the account
    account.activate()

    # Attempt to perform an action after activation
    try:
        account.perform_action("login")  # Should work again
    except AccountSuspensionError as e:
        print(e)

if __name__ == "__main__":
    main()
```
