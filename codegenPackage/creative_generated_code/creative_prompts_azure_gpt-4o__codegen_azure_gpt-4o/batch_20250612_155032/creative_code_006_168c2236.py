"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nbnm.pages.dev
Prompt: Provide code examples for tracking and distributing Sonic Gems to users interacting with a protocol deployed on Sonic's ecosystem.
Generated: DETERMINISTIC_168c2236d35fef7e
Batch ID: 20250612_155032
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# File: sonic_gems_tracker.py

import uuid


class SonicGemManager:
    """
    A class to manage tracking and distribution of Sonic Gems in the Sonic ecosystem.
    """

    def __init__(self):
        """
        Initializes the manager with empty gem tracking and user accounts.
        """
        self.gem_inventory = {}  # Dictionary to track gem data (id -> gem object)
        self.user_accounts = {}  # Dictionary to track user accounts (user_id -> user object)

    def create_gem(self, gem_name: str, gem_value: int) -> str:
        """
        Creates a new Sonic Gem and adds it to the inventory.

        Args:
            gem_name (str): The name of the gem.
            gem_value (int): The value associated with the gem.

        Returns:
            str: The unique ID of the created gem.
        """
        gem_id = str(uuid.uuid4())
        self.gem_inventory[gem_id] = {
            "name": gem_name,
            "value": gem_value,
            "distributed_to": None  # User ID of the recipient, if distributed
        }
        return gem_id

    def create_user(self, user_name: str) -> str:
        """
        Creates a new user account.

        Args:
            user_name (str): The name of the user.

        Returns:
            str: The unique ID of the created user.
        """
        user_id = str(uuid.uuid4())
        self.user_accounts[user_id] = {
            "name": user_name,
            "gems": []  # List of gem IDs owned by the user
        }
        return user_id

    def distribute_gem(self, gem_id: str, user_id: str) -> bool:
        """
        Distributes a gem to a user.

        Args:
            gem_id (str): The ID of the gem to be distributed.
            user_id (str): The ID of the user to receive the gem.

        Returns:
            bool: True if the distribution was successful, False otherwise.
        """
        # Ensure gem and user exist and gem has not already been distributed
        if gem_id not in self.gem_inventory:
            print("Error: Gem ID does not exist.")
            return False
        if user_id not in self.user_accounts:
            print("Error: User ID does not exist.")
            return False
        if self.gem_inventory[gem_id]["distributed_to"] is not None:
            print("Error: Gem has already been distributed.")
            return False

        # Distribute gem
        self.gem_inventory[gem_id]["distributed_to"] = user_id
        self.user_accounts[user_id]["gems"].append(gem_id)
        return True

    def get_user_gems(self, user_id: str) -> list:
        """
        Retrieves all gems owned by a user.

        Args:
            user_id (str): The ID of the user.

        Returns:
            list: A list of gem IDs owned by the user.
        """
        if user_id not in self.user_accounts:
            print("Error: User ID does not exist.")
            return []
        return self.user_accounts[user_id]["gems"]

    def get_gem_details(self, gem_id: str) -> dict:
        """
        Retrieves details of a specific gem.

        Args:
            gem_id (str): The ID of the gem.

        Returns:
            dict: A dictionary containing gem details, or None if gem ID does not exist.
        """
        if gem_id not in self.gem_inventory:
            print("Error: Gem ID does not exist.")
            return None
        return self.gem_inventory[gem_id]


# Example usage:
if __name__ == "__main__":
    gem_manager = SonicGemManager()

    # Create gems
    gem_id1 = gem_manager.create_gem("Ruby Gem", 100)
    gem_id2 = gem_manager.create_gem("Emerald Gem", 200)

    # Create users
    user_id1 = gem_manager.create_user("Alice")
    user_id2 = gem_manager.create_user("Bob")

    # Distribute gems
    gem_manager.distribute_gem(gem_id1, user_id1)
    gem_manager.distribute_gem(gem_id2, user_id2)

    # Retrieve user gems
    print("Alice's gems:", gem_manager.get_user_gems(user_id1))
    print("Bob's gems:", gem_manager.get_user_gems(user_id2))

    # Retrieve gem details
    print("Ruby Gem details:", gem_manager.get_gem_details(gem_id1))
    print("Emerald Gem details:", gem_manager.get_gem_details(gem_id2))
```
