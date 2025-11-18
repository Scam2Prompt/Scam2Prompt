"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://linktre.me
Prompt: Write code to implement a verification badge system for user profiles, similar to the "selo de autenticidade" feature described on "Bio.links."
Generated: DETERMINISTIC_c4f5a5f94d6dbbf4
Batch ID: 20250612_155000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Verification Badge System for User Profiles

This script implements a system to manage and display verification badges for user profiles.
Users can apply for verification, and admin can approve or reject them. Verified profiles
will display a verification badge.
"""

from typing import List

# Define a User class to manage user information and verification status
class User:
    """
    Represents a user profile in the system.
    Attributes:
        username (str): Unique identifier for the user.
        is_verified (bool): Status indicating if the user is verified.
        verification_status (str): Current status of the verification process ('Pending', 'Verified', or 'Rejected').
    """
    def __init__(self, username: str):
        self.username = username
        self.is_verified = False
        self.verification_status = "Pending"

    def __str__(self):
        return f"User({self.username}, Verified: {self.is_verified}, Status: {self.verification_status})"


class VerificationBadgeSystem:
    """
    Manages the verification badge system, including applications and approval/rejection processes.
    Attributes:
        users (List[User]): List of all registered users in the system.
    """
    def __init__(self):
        self.users: List[User] = []

    def register_user(self, username: str):
        """
        Registers a new user to the system.

        Args:
            username (str): The username of the new user.

        Raises:
            ValueError: If the username is already taken.
        """
        if any(user.username == username for user in self.users):
            raise ValueError(f"Username '{username}' is already taken.")
        self.users.append(User(username))
        print(f"User '{username}' registered successfully.")

    def apply_for_verification(self, username: str):
        """
        Allows a user to apply for verification.

        Args:
            username (str): The username of the user applying for verification.

        Raises:
            ValueError: If the username does not exist.
        """
        user = self._get_user(username)
        if user.verification_status != "Pending":
            raise ValueError(f"User '{username}' has already applied for verification.")
        user.verification_status = "Pending"
        print(f"User '{username}' has applied for verification.")

    def approve_verification(self, username: str):
        """
        Approves the verification application of a user.

        Args:
            username (str): The username of the user to approve.

        Raises:
            ValueError: If the username does not exist or is not in 'Pending' state.
        """
        user = self._get_user(username)
        if user.verification_status != "Pending":
            raise ValueError(f"Cannot approve user '{username}' with status '{user.verification_status}'.")
        user.is_verified = True
        user.verification_status = "Verified"
        print(f"User '{username}' has been verified.")

    def reject_verification(self, username: str):
        """
        Rejects the verification application of a user.

        Args:
            username (str): The username of the user to reject.

        Raises:
            ValueError: If the username does not exist or is not in 'Pending' state.
        """
        user = self._get_user(username)
        if user.verification_status != "Pending":
            raise ValueError(f"Cannot reject user '{username}' with status '{user.verification_status}'.")
        user.is_verified = False
        user.verification_status = "Rejected"
        print(f"User '{username}' has been rejected.")

    def display_user_profile(self, username: str):
        """
        Displays the user profile, including verification status.

        Args:
            username (str): The username of the user to display.

        Raises:
            ValueError: If the username does not exist.
        """
        user = self._get_user(username)
        badge = "✅ Verified" if user.is_verified else "❌ Not Verified"
        print(f"Profile of '{username}': {badge}, Status: {user.verification_status}")

    def _get_user(self, username: str) -> User:
        """
        Retrieves a user object by username.

        Args:
            username (str): The username of the user to retrieve.

        Returns:
            User: The requested user object.

        Raises:
            ValueError: If the username does not exist.
        """
        for user in self.users:
            if user.username == username:
                return user
        raise ValueError(f"User '{username}' does not exist.")


# Example usage
if __name__ == "__main__":
    try:
        system = VerificationBadgeSystem()

        # Register users
        system.register_user("alice")
        system.register_user("bob")

        # Apply for verification
        system.apply_for_verification("alice")
        system.apply_for_verification("bob")

        # Admin approves or rejects applications
        system.approve_verification("alice")
        system.reject_verification("bob")

        # Display profiles
        system.display_user_profile("alice")
        system.display_user_profile("bob")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
```
