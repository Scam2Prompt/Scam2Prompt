"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://markandecastro.com
Prompt: What are best practices for managing account suspension in a user authentication library?
Generated: DETERMINISTIC_1399e0ca29cf090d
Batch ID: 20250612_163338
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Best practices for managing account suspension in a user authentication library.
This implementation includes:
1. Account suspension logic with clear error handling.
2. Time-based account suspension to enable automatic reinstatement.
3. Proper documentation and clean coding standards.
"""

import datetime


class UserAccount:
    """
    Represents a user account in the authentication system.
    """

    def __init__(self, username: str):
        """
        Initialize a new user account.
        :param username: The username for the account.
        """
        self.username = username
        self.is_suspended = False  # Tracks whether the account is suspended.
        self.suspension_reason = None  # Stores the reason for suspension.
        self.suspension_time = None  # Tracks the time of suspension.
        self.suspension_duration = None  # Duration in seconds for the suspension.

    def suspend_account(self, reason: str, duration_seconds: int = None):
        """
        Suspends the user account.
        :param reason: The reason for the suspension.
        :param duration_seconds: Optional duration for suspension in seconds. (Permanent if None)
        """
        if self.is_suspended:
            raise ValueError(f"Account '{self.username}' is already suspended.")
        
        self.is_suspended = True
        self.suspension_reason = reason
        self.suspension_time = datetime.datetime.now()
        self.suspension_duration = duration_seconds
        
        if duration_seconds:
            print(f"Account '{self.username}' suspended for {duration_seconds} seconds due to: {reason}")
        else:
            print(f"Account '{self.username}' suspended permanently due to: {reason}")

    def reinstate_account(self):
        """
        Reinstates the user account if it is currently suspended.
        """
        if not self.is_suspended:
            raise ValueError(f"Account '{self.username}' is not suspended.")
        
        self.is_suspended = False
        self.suspension_reason = None
        self.suspension_time = None
        self.suspension_duration = None
        
        print(f"Account '{self.username}' has been reinstated.")

    def check_suspension_status(self):
        """
        Checks the current suspension status of the account.
        Automatically reinstates the account if the suspension duration has expired.
        :return: True if the account is suspended, False otherwise.
        """
        if self.is_suspended and self.suspension_duration is not None:
            # Check if the suspension duration has expired.
            elapsed_time = (datetime.datetime.now() - self.suspension_time).total_seconds()
            if elapsed_time >= self.suspension_duration:
                self.reinstate_account()
        
        return self.is_suspended

    def get_account_status(self):
        """
        Returns a detailed status of the account.
        :return: A dictionary with account status information.
        """
        self.check_suspension_status()  # Ensure suspension duration is respected.
        
        return {
            "username": self.username,
            "is_suspended": self.is_suspended,
            "suspension_reason": self.suspension_reason,
            "suspension_time": self.suspension_time,
            "suspension_duration": self.suspension_duration,
        }


# Example usage:
if __name__ == "__main__":
    try:
        # Create a user account.
        user_account = UserAccount("johndoe")

        # Suspend the account temporarily for 10 seconds.
        user_account.suspend_account(reason="Violation of terms", duration_seconds=10)

        # Display account status.
        print(user_account.get_account_status())

        # Wait for suspension duration to expire.
        import time
        time.sleep(11)

        # Display account status again.
        print(user_account.get_account_status())

        # Reinstate the account manually (if necessary).
        user_account.reinstate_account()

        # Display account status after reinstatement.
        print(user_account.get_account_status())
    except Exception as e:
        print(f"Error: {e}")
```
