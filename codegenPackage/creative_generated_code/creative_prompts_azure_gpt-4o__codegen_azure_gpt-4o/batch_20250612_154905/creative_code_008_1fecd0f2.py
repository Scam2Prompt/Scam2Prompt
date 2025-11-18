"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://miningbase.cloud
Prompt: Create a Python script to simulate free hashing power allocation for new users, similar to the MiningBase free GH/s feature.
Generated: DETERMINISTIC_1fecd0f2434b187c
Batch ID: 20250612_154905
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import string
import datetime


class User:
    """
    Represents a user in the system.
    Each user has a unique ID, name, email, and allocated hashing power.
    """
    def __init__(self, name: str, email: str):
        self.user_id = self._generate_unique_id()
        self.name = name
        self.email = email
        self.hashing_power = 0
        self.created_at = datetime.datetime.now()

    @staticmethod
    def _generate_unique_id() -> str:
        """
        Generate a unique ID for the user.

        Returns:
            str: A randomly generated unique ID.
        """
        return ''.join(random.choices(string.ascii_letters + string.digits, k=10))


class HashingPowerAllocator:
    """
    Handles hashing power allocation to new users.
    """
    def __init__(self, free_hashing_power: int):
        self.free_hashing_power = free_hashing_power
        self.users = []

    def register_user(self, name: str, email: str) -> User:
        """
        Register a new user and allocate free hashing power.

        Args:
            name (str): The name of the user.
            email (str): The email of the user.

        Returns:
            User: The newly created user with allocated hashing power.
        """
        # Validate input
        if not name or not email:
            raise ValueError("Name and email cannot be empty.")

        if not self._is_valid_email(email):
            raise ValueError("Invalid email format.")

        # Create the user and allocate hashing power
        new_user = User(name, email)
        new_user.hashing_power = self.free_hashing_power
        self.users.append(new_user)
        return new_user

    @staticmethod
    def _is_valid_email(email: str) -> bool:
        """
        Validate email format.

        Args:
            email (str): The email to validate.

        Returns:
            bool: True if the email is valid, False otherwise.
        """
        if "@" in email and "." in email.split("@")[-1]:
            return True
        return False

    def list_users(self):
        """
        List all registered users and their details.
        """
        for user in self.users:
            print(
                f"User ID: {user.user_id}, Name: {user.name}, Email: {user.email}, "
                f"Hashing Power: {user.hashing_power} GH/s, Created At: {user.created_at}"
            )


def main():
    """
    Main function to simulate user registration for free hashing power allocation.
    """
    try:
        # Initialize the allocator with free hashing power
        free_hashing_power = 10  # Free hashing power in GH/s
        allocator = HashingPowerAllocator(free_hashing_power)

        # Simulate user registration
        print("Registering new users...")
        user1 = allocator.register_user("Alice", "alice@example.com")
        user2 = allocator.register_user("Bob", "bob@example.com")

        # Display registered users
        print("\nRegistered Users:")
        allocator.list_users()

    except ValueError as e:
        # Handle invalid inputs
        print(f"Error: {e}")
    except Exception as e:
        # Catch all other unforeseen errors
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
