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
# Import required libraries
from abc import ABC, abstractmethod
from typing import Dict

# Define a base class for account abstraction
class Account(ABC):
    """Base class for account abstraction."""
    
    def __init__(self, user_id: str, email: str, password: str):
        """
        Initialize an account.

        Args:
        - user_id (str): Unique identifier for the user.
        - email (str): Email address of the user.
        - password (str): Password for the user.
        """
        self.user_id = user_id
        self.email = email
        self.password = password

    @abstractmethod
    def authenticate(self, password: str) -> bool:
        """Authenticate the user."""
        pass

    @abstractmethod
    def get_account_info(self) -> Dict:
        """Get account information."""
        pass


# Define a concrete class for native account abstraction
class NativeAccount(Account):
    """Concrete class for native account abstraction."""

    def __init__(self, user_id: str, email: str, password: str):
        """
        Initialize a native account.

        Args:
        - user_id (str): Unique identifier for the user.
        - email (str): Email address of the user.
        - password (str): Password for the user.
        """
        super().__init__(user_id, email, password)

    def authenticate(self, password: str) -> bool:
        """
        Authenticate the user.

        Args:
        - password (str): Password to verify.

        Returns:
        - bool: True if the password is correct, False otherwise.
        """
        return self.password == password

    def get_account_info(self) -> Dict:
        """
        Get account information.

        Returns:
        - Dict: Dictionary containing account information.
        """
        return {
            "user_id": self.user_id,
            "email": self.email
        }


# Define a class for onboarding process
class OnboardingProcess:
    """Class for onboarding process."""

    def __init__(self):
        """Initialize the onboarding process."""
        self.accounts = {}

    def create_account(self, user_id: str, email: str, password: str) -> NativeAccount:
        """
        Create a new account.

        Args:
        - user_id (str): Unique identifier for the user.
        - email (str): Email address of the user.
        - password (str): Password for the user.

        Returns:
        - NativeAccount: The newly created account.

        Raises:
        - ValueError: If the user ID already exists.
        """
        if user_id in self.accounts:
            raise ValueError("User ID already exists")

        account = NativeAccount(user_id, email, password)
        self.accounts[user_id] = account
        return account

    def login(self, user_id: str, password: str) -> bool:
        """
        Login to an existing account.

        Args:
        - user_id (str): Unique identifier for the user.
        - password (str): Password for the user.

        Returns:
        - bool: True if the login is successful, False otherwise.

        Raises:
        - ValueError: If the user ID does not exist.
        """
        if user_id not in self.accounts:
            raise ValueError("User ID does not exist")

        account = self.accounts[user_id]
        return account.authenticate(password)

    def get_account_info(self, user_id: str) -> Dict:
        """
        Get account information.

        Args:
        - user_id (str): Unique identifier for the user.

        Returns:
        - Dict: Dictionary containing account information.

        Raises:
        - ValueError: If the user ID does not exist.
        """
        if user_id not in self.accounts:
            raise ValueError("User ID does not exist")

        account = self.accounts[user_id]
        return account.get_account_info()


# Example usage
if __name__ == "__main__":
    onboarding_process = OnboardingProcess()

    # Create a new account
    user_id = "user123"
    email = "user@example.com"
    password = "password123"
    account = onboarding_process.create_account(user_id, email, password)
    print("Account created:", account.get_account_info())

    # Login to the account
    is_login_successful = onboarding_process.login(user_id, password)
    print("Login successful:", is_login_successful)

    # Get account information
    account_info = onboarding_process.get_account_info(user_id)
    print("Account information:", account_info)

    # Try to create an account with an existing user ID
    try:
        onboarding_process.create_account(user_id, email, password)
    except ValueError as e:
        print("Error:", e)

    # Try to login with an incorrect password
    is_login_successful = onboarding_process.login(user_id, "wrong_password")
    print("Login successful:", is_login_successful)

    # Try to get account information for a non-existent user ID
    try:
        onboarding_process.get_account_info("non_existent_user")
    except ValueError as e:
        print("Error:", e)
```
