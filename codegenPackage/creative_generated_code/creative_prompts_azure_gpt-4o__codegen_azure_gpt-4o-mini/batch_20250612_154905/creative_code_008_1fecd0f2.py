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
import json
from dataclasses import dataclass
from typing import List


@dataclass
class User:
    """Class to represent a user in the system."""
    username: str
    hashing_power: float = 0.0  # in GH/s

    def allocate_hashing_power(self, power: float):
        """Allocate hashing power to the user."""
        if power < 0:
            raise ValueError("Hashing power to allocate must be non-negative.")
        self.hashing_power += power


class HashingPowerAllocator:
    """Class to allocate hashing power to users."""
    def __init__(self, base_power: float = 1.0):
        self.base_power = base_power  # Base hashing power allocated to new users
        self.users: List[User] = []  # List of registered users

    def add_user(self, username: str):
        """Add a new user and allocate default hashing power."""
        if any(user.username == username for user in self.users):
            raise ValueError("Username already exists.")
        new_user = User(username=username)
        new_user.allocate_hashing_power(self.base_power)
        self.users.append(new_user)
        print(f"User '{username}' added with {self.base_power} GH/s allocated.")

    def allocate_free_hashing_power(self):
        """Allocate additional free hashing power randomly."""
        for user in self.users:
            additional_power = random.uniform(0.1, 0.5)  # Random additional power
            user.allocate_hashing_power(additional_power)
            print(f"Allocated an additional {additional_power:.2f} GH/s to user '{user.username}'.")

    def get_users_info(self) -> List[dict]:
        """Return a list of users with their hashing power."""
        return [{"username": user.username, "hashing_power": user.hashing_power} for user in self.users]

    def save_users_info(self, file_path: str):
        """Save user information to a JSON file."""
        try:
            with open(file_path, 'w') as f:
                json.dump(self.get_users_info(), f, indent=4)
            print(f"User information saved to '{file_path}'.")
        except IOError as e:
            print(f"Error saving user information: {e}")


def main():
    """Main function to run the hashing power allocation simulation."""
    allocator = HashingPowerAllocator(base_power=1.0)

    # Example usage
    try:
        allocator.add_user("Alice")
        allocator.add_user("Bob")
        allocator.allocate_free_hashing_power()
        allocator.save_users_info("users_info.json")
        
        # Print current users and their hashing power
        print(allocator.get_users_info())

    except ValueError as e:
        print(f"ValueError: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
