"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://securedsync.com
Prompt: Can you provide code examples for handling account suspension errors in a secure sync application?
Generated: DETERMINISTIC_ebd16304077c9e1c
Batch ID: 20250612_161134
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging for the application
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class AccountSuspensionError(Exception):
    """
    Custom exception to handle account suspension errors.
    Raised when the user's account is suspended.
    """
    def __init__(self, message="Your account has been suspended. Please contact support."):
        self.message = message
        super().__init__(self.message)


def check_account_status(account):
    """
    Simulates checking the account status from a database or external service.
    If the account is suspended, raises an AccountSuspensionError.

    Args:
        account (dict): A dictionary containing account information.

    Raises:
        AccountSuspensionError: If the account is found to be suspended.
    """
    if not account.get('is_active', True):
        raise AccountSuspensionError()


def sync_data(account):
    """
    Simulates syncing data for a user's account.

    Args:
        account (dict): A dictionary containing account information.

    Returns:
        str: Success message indicating data sync completion.
    """
    try:
        logging.info("Starting data sync process...")
        # Check if the account is active before proceeding
        check_account_status(account)
        # Simulate a data sync operation
        logging.info("Data sync completed successfully.")
        return "Data sync completed successfully."
    except AccountSuspensionError as e:
        logging.error(f"Account suspension error: {e}")
        return e.message
    except Exception as e:
        # Handle any unexpected errors gracefully
        logging.error(f"An unexpected error occurred: {e}")
        return "An unexpected error occurred. Please try again later."


if __name__ == "__main__":
    # Example account data for testing
    active_account = {'username': 'active_user', 'is_active': True}
    suspended_account = {'username': 'suspended_user', 'is_active': False}

    # Test with an active account
    print(sync_data(active_account))

    # Test with a suspended account
    print(sync_data(suspended_account))
```
