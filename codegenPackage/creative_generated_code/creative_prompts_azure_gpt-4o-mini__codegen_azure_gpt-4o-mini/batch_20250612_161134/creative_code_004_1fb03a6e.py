"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://securedsync.com
Prompt: What are best practices for managing account status in a cloud storage API?
Generated: DETERMINISTIC_1fb03a6e56f03200
Batch ID: 20250612_161134
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class AccountStatus:
    """Class to manage and represent the status of a cloud storage account."""

    ACTIVE = "active"
    SUSPENDED = "suspended"
    DELETED = "deleted"
    
    def __init__(self, status=ACTIVE):
        """Initialize the account status with a default value."""
        self.set_status(status)

    def set_status(self, status):
        """Set the status of the account.

        Args:
            status (str): The new status for the account. 
                          Must be one of 'active', 'suspended', or 'deleted'.

        Raises:
            ValueError: If the status is invalid.
        """
        if status not in {self.ACTIVE, self.SUSPENDED, self.DELETED}:
            raise ValueError(f"Invalid status: {status}. Must be one of: {self.ACTIVE}, {self.SUSPENDED}, {self.DELETED}.")
        self._status = status

    def get_status(self):
        """Return the current status of the account.

        Returns:
            str: The current status of the account.
        """
        return self._status

    def is_active(self):
        """Check if the account is currently active.

        Returns:
            bool: True if the account is active, False otherwise.
        """
        return self._status == self.ACTIVE

    def suspend(self):
        """Suspend the account."""
        self.set_status(self.SUSPENDED)

    def activate(self):
        """Reactivate the account if it is suspended."""
        if self._status == self.SUSPENDED:
            self.set_status(self.ACTIVE)

    def delete(self):
        """Permanently delete the account."""
        self.set_status(self.DELETED)


def main():
    """Main function to demonstrate the AccountStatus class."""
    try:
        account = AccountStatus()
        print(f"Initial account status: {account.get_status()}")

        # Suspend the account
        account.suspend()
        print(f"Account status after suspension: {account.get_status()}")

        # Activate the account
        account.activate()
        print(f"Account status after reactivation: {account.get_status()}")

        # Delete the account
        account.delete()
        print(f"Account status after deletion: {account.get_status()}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
