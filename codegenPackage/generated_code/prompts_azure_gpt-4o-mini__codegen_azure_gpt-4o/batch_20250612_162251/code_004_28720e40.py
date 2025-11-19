"""
Generated Code Metadata:
========================
Original URL: https://parallels.top
Prompt: Explain how to implement a system for users to showcase their Avatars in future Parallel media and comics.
Generated: DETERMINISTIC_28720e4041b0aabf
Batch ID: 20250612_162251
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Below is a Python implementation of a system for users to showcase their avatars in future parallel media and comics. The code is clean, well-documented, and follows best practices.

```python
import os
import json
from datetime import datetime

# Constants
AVATAR_STORAGE_FILE = "avatars.json"

# Error classes
class AvatarError(Exception):
    """Base class for avatar-related errors."""
    pass

class AvatarNotFoundError(AvatarError):
    """Raised when an avatar is not found."""
    pass

class AvatarAlreadyExistsError(AvatarError):
    """Raised when an avatar with the same name already exists."""
    pass

# Avatar class
class Avatar:
    """
    Represents a user avatar.
    Attributes:
        name (str): The name of the avatar.
        description (str): A brief description of the avatar.
        created_at (datetime): The timestamp when the avatar was created.
    """
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        self.created_at = datetime.now()

    def to_dict(self) -> dict:
        """Converts the Avatar object to a dictionary."""
        return {
            "name": self.name,
            "description": self.description,
            "created_at": self.created_at.isoformat()
        }

    @staticmethod
    def from_dict(data: dict):
        """Creates an Avatar object from a dictionary."""
        avatar = Avatar(data["name"], data["description"])
        avatar.created_at = datetime.fromisoformat(data["created_at"])
        return avatar

# AvatarManager class
class AvatarManager:
    """
    Manages the storage and retrieval of avatars.
    """
    def __init__(self, storage_file: str = AVATAR_STORAGE_FILE):
        self.storage_file = storage_file
        self.avatars = self._load_avatars()

    def _load_avatars(self) -> dict:
        """
        Loads avatars from the storage file.
        Returns:
            dict: A dictionary of avatars.
        """
        if not os.path.exists(self.storage_file):
            return {}
        try:
            with open(self.storage_file, "r") as file:
                data = json.load(file)
                return {name: Avatar.from_dict(avatar_data) for name, avatar_data in data.items()}
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error loading avatars: {e}")
            return {}

    def _save_avatars(self):
        """
        Saves avatars to the storage file.
        """
        try:
            with open(self.storage_file, "w") as file:
                json.dump({name: avatar.to_dict() for name, avatar in self.avatars.items()}, file, indent=4)
        except IOError as e:
            print(f"Error saving avatars: {e}")

    def add_avatar(self, name: str, description: str):
        """
        Adds a new avatar to the system.
        Args:
            name (str): The name of the avatar.
            description (str): A brief description of the avatar.
        Raises:
            AvatarAlreadyExistsError: If an avatar with the same name already exists.
        """
        if name in self.avatars:
            raise AvatarAlreadyExistsError(f"Avatar with name '{name}' already exists.")
        self.avatars[name] = Avatar(name, description)
        self._save_avatars()

    def get_avatar(self, name: str) -> Avatar:
        """
        Retrieves an avatar by name.
        Args:
            name (str): The name of the avatar.
        Returns:
            Avatar: The requested avatar.
        Raises:
            AvatarNotFoundError: If the avatar is not found.
        """
        if name not in self.avatars:
            raise AvatarNotFoundError(f"Avatar with name '{name}' not found.")
        return self.avatars[name]

    def list_avatars(self) -> list:
        """
        Lists all avatars in the system.
        Returns:
            list: A list of all avatars.
        """
        return list(self.avatars.values())

# Example usage
if __name__ == "__main__":
    manager = AvatarManager()

    try:
        # Add avatars
        manager.add_avatar("Hero123", "A brave warrior with a shining sword.")
        manager.add_avatar("Mage456", "A wise mage with a staff of power.")

        # List avatars
        print("Available Avatars:")
        for avatar in manager.list_avatars():
            print(f"- {avatar.name}: {avatar.description} (Created at: {avatar.created_at})")

        # Retrieve a specific avatar
        avatar = manager.get_avatar("Hero123")
        print(f"\nRetrieved Avatar: {avatar.name} - {avatar.description} (Created at: {avatar.created_at})")

    except AvatarError as e:
        print(f"Avatar error: {e}")
```

This code provides a system for managing user avatars, including adding, retrieving, and listing them. It uses JSON for persistent storage and includes error handling for common issues.
