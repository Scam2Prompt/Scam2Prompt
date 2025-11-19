"""
Generated Code Metadata:
========================
Original URL: https://penfinance.io
Prompt: Generate a Python script to create a waitlist system for a financial platform like Pencil Finance.
Generated: DETERMINISTIC_b9eef7c485f97edc
Batch ID: 20250622_212548
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import uuid
from datetime import datetime


class WaitlistSystem:
    """
    A class to manage a waitlist system for a financial platform.
    """

    def __init__(self):
        """
        Initializes the waitlist system with an empty list.
        """
        self.waitlist = {}

    def add_user(self, name, email):
        """
        Adds a user to the waitlist.

        Args:
            name (str): The name of the user.
            email (str): The email of the user.

        Returns:
            str: A unique ID for the user.
        """
        try:
            if not name or not email:
                raise ValueError("Name and email are required.")

            user_id = str(uuid.uuid4())  # Generate a unique ID for the user
            self.waitlist[user_id] = {
                "name": name,
                "email": email,
                "joined_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            }
            return user_id
        except Exception as e:
            print(f"Error adding user: {e}")
            return None

    def remove_user(self, user_id):
        """
        Removes a user from the waitlist.

        Args:
            user_id (str): The unique ID of the user.

        Returns:
            bool: True if the user was removed, False otherwise.
        """
        try:
            if user_id in self.waitlist:
                del self.waitlist[user_id]
                return True
            else:
                print("User ID not found.")
                return False
        except Exception as e:
            print(f"Error removing user: {e}")
            return False

    def list_users(self):
        """
        Lists all users currently in the waitlist.

        Returns:
            dict: A dictionary of users in the waitlist.
        """
        return self.waitlist

    def get_user(self, user_id):
        """
        Retrieves information about a specific user.

        Args:
            user_id (str): The unique ID of the user.

        Returns:
            dict: The user's information, or None if not found.
        """
        try:
            return self.waitlist.get(user_id, None)
        except Exception as e:
            print(f"Error retrieving user: {e}")
            return None


# Example usage
if __name__ == "__main__":
    # Initialize the waitlist system
    waitlist = WaitlistSystem()

    # Add users to the waitlist
    user1_id = waitlist.add_user("Alice", "alice@example.com")
    user2_id = waitlist.add_user("Bob", "bob@example.com")

    # List all users
    print("Current waitlist:")
    print(waitlist.list_users())

    # Get details of a specific user
    print("\nDetails of user 1:")
    print(waitlist.get_user(user1_id))

    # Remove a user from the waitlist
    print("\nRemoving user 2...")
    waitlist.remove_user(user2_id)

    # List all users after removal
    print("\nUpdated waitlist:")
    print(waitlist.list_users())
```
