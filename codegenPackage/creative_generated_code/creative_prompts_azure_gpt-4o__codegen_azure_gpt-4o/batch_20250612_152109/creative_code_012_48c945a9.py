"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nhshsvsgdg.pages.dev
Prompt: Create a program to handle locked account issues and restore access, using the guidelines provided by the Dapps Rectifier platform.
Generated: DETERMINISTIC_48c945a966413002
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime


class AccountLockedException(Exception):
    """
    Custom exception raised when an account is locked
    """
    pass


class Account:
    """
    Represents a user account with lock status and unlock functionality.
    """
    def __init__(self, username: str):
        self.username = username
        self.is_locked = False
        self.locked_until = None

    def lock_account(self, duration_minutes: int):
        """
        Locks the account for a specified duration.
        :param duration_minutes: Number of minutes to lock the account.
        """
        self.is_locked = True
        self.locked_until = datetime.datetime.now() + datetime.timedelta(minutes=duration_minutes)
        print(f"Account '{self.username}' has been locked until {self.locked_until}")

    def unlock_account(self):
        """
        Unlocks the account if the lock duration has expired.
        Raises an exception if the lock period is not over.
        """
        if not self.is_locked:
            print(f"Account '{self.username}' is already unlocked.")
            return

        current_time = datetime.datetime.now()
        if current_time < self.locked_until:
            raise AccountLockedException(
                f"Account '{self.username}' is locked until {self.locked_until}. Please try again later."
            )

        self.is_locked = False
        self.locked_until = None
        print(f"Account '{self.username}' has been successfully unlocked.")

    def get_status(self):
        """
        Returns the current lock status of the account.
        """
        if self.is_locked:
            return f"Locked until {self.locked_until}"
        return "Unlocked"


def restore_access(account: Account):
    """
    Handles the process of restoring access to a locked account.
    :param account: Instance of the Account class to restore access for.
    """
    try:
        account.unlock_account()
    except AccountLockedException as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def main():
    """
    Main function to demonstrate account lock and restore access functionality.
    """
    # Create an account instance
    user_account = Account("JohnDoe")

    # Lock the account for 5 minutes
    user_account.lock_account(duration_minutes=5)

    # Display account status
    print(f"Account Status: {user_account.get_status()}")

    # Attempt to restore access (will fail if the lock period is not over)
    restore_access(user_account)

    # Simulating a wait for lock period expiration (for demonstration purposes)
    print("\nWaiting for lock period to expire...")
    import time
    time.sleep(5)  # Reduce sleep duration for demonstration purposes

    # Attempt to restore access again (should succeed now)
    restore_access(user_account)

    # Display updated account status
    print(f"Account Status: {user_account.get_status()}")


if __name__ == "__main__":
    main()
```
