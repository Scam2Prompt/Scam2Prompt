"""
Generated Code Metadata:
========================
Original URL: https://sophon.xyz
Prompt: Write a code snippet that demonstrates how to create a user-friendly onboarding process with Sophon's native account abstraction.
Generated: DETERMINISTIC_dfdb51a630fdbb4b
Batch ID: 20250612_135046
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sophon_sdk  # Importing the Sophon SDK for account abstraction
from sophon_sdk.exceptions import AccountCreationError, AccountRetrievalError

class UserOnboarding:
    def __init__(self):
        """Initialize the UserOnboarding class."""
        self.account_service = sophon_sdk.AccountService()

    def create_account(self, username: str, password: str) -> str:
        """
        Create a new user account.

        Args:
            username (str): The desired username for the account.
            password (str): The desired password for the account.

        Returns:
            str: A success message or an error message.
        """
        try:
            # Attempt to create a new account
            account = self.account_service.create_account(username, password)
            return f"Account created successfully for {account.username}."
        except AccountCreationError as e:
            # Handle account creation errors
            return f"Error creating account: {str(e)}"

    def retrieve_account(self, username: str) -> dict:
        """
        Retrieve account details for a given username.

        Args:
            username (str): The username of the account to retrieve.

        Returns:
            dict: Account details or an error message.
        """
        try:
            # Attempt to retrieve the account
            account = self.account_service.get_account(username)
            return {
                "username": account.username,
                "created_at": account.created_at,
                "status": account.status
            }
        except AccountRetrievalError as e:
            # Handle account retrieval errors
            return {"error": f"Error retrieving account: {str(e)}"}

    def onboarding_process(self, username: str, password: str):
        """
        Execute the onboarding process for a new user.

        Args:
            username (str): The desired username for the account.
            password (str): The desired password for the account.
        """
        # Step 1: Create the account
        creation_message = self.create_account(username, password)
        print(creation_message)

        # Step 2: Retrieve and display account details
        account_details = self.retrieve_account(username)
        print(account_details)

# Example usage
if __name__ == "__main__":
    onboarding = UserOnboarding()
    onboarding.onboarding_process("new_user", "secure_password123")
```
