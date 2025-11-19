"""
Generated Code Metadata:
========================
Original URL: https://itmastar.pages.dev
Prompt: Generate a code snippet for a project that showcases real skills in IT development.
Generated: DETERMINISTIC_6bfe7d5f9424742a
Batch ID: 20250612_163224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# user_service.py

"""
User Service Module
====================
Provides functionality for user management.
"""

import logging
from typing import Dict, Optional

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class User:
    """Represents a user entity."""

    def __init__(self, id: int, name: str, email: str):
        """
        Initializes a User instance.

        Args:
        id (int): Unique identifier for the user.
        name (str): User's name.
        email (str): User's email address.
        """
        self.id = id
        self.name = name
        self.email = email

class UserService:
    """Provides methods for managing users."""

    def __init__(self):
        # In-memory user storage for demonstration purposes.
        # In a real application, use a database.
        self.users: Dict[int, User] = {}

    def create_user(self, id: int, name: str, email: str) -> User:
        """
        Creates a new user.

        Args:
        id (int): Unique identifier for the user.
        name (str): User's name.
        email (str): User's email address.

        Returns:
        User: The created user instance.

        Raises:
        ValueError: If a user with the given ID already exists.
        """
        if id in self.users:
            raise ValueError(f"User with ID {id} already exists")

        user = User(id, name, email)
        self.users[id] = user
        logger.info(f"User {id} created")
        return user

    def get_user(self, id: int) -> Optional[User]:
        """
        Retrieves a user by ID.

        Args:
        id (int): Unique identifier for the user.

        Returns:
        User: The user instance if found, otherwise None.
        """
        return self.users.get(id)

    def update_user(self, id: int, name: Optional[str] = None, email: Optional[str] = None) -> User:
        """
        Updates an existing user's information.

        Args:
        id (int): Unique identifier for the user.
        name (str): User's new name (optional).
        email (str): User's new email address (optional).

        Returns:
        User: The updated user instance.

        Raises:
        ValueError: If the user with the given ID does not exist.
        """
        user = self.get_user(id)
        if user is None:
            raise ValueError(f"User with ID {id} does not exist")

        if name:
            user.name = name
        if email:
            user.email = email

        logger.info(f"User {id} updated")
        return user

    def delete_user(self, id: int) -> None:
        """
        Deletes a user by ID.

        Args:
        id (int): Unique identifier for the user.

        Raises:
        ValueError: If the user with the given ID does not exist.
        """
        if id not in self.users:
            raise ValueError(f"User with ID {id} does not exist")

        del self.users[id]
        logger.info(f"User {id} deleted")

def main():
    # Example usage
    user_service = UserService()

    try:
        user1 = user_service.create_user(1, "John Doe", "john@example.com")
        print(f"Created user: {user1.name} ({user1.email})")

        user_service.update_user(1, name="Jane Doe")
        updated_user = user_service.get_user(1)
        print(f"Updated user: {updated_user.name} ({updated_user.email})")

        user_service.delete_user(1)
        print("User deleted")

    except ValueError as e:
        logger.error(f"Error: {e}")

if __name__ == "__main__":
    main()
```
