"""
Generated Code Metadata:
========================
Original URL: https://miningbase.cloud
Prompt: Create a Python script to simulate free hashing power allocation for new users, similar to the MiningBase free GH/s feature.
Generated: DETERMINISTIC_1fecd0f2434b187c
Batch ID: 20250612_154905
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import json
from typing import Dict, Any

class User:
    """Class representing a user in the mining system."""
    
    def __init__(self, username: str):
        self.username = username
        self.hash_power: float = 0.0  # Initial hashing power in GH/s

    def allocate_hash_power(self, amount: float):
        """Allocate hashing power to the user."""
        if amount < 0:
            raise ValueError("Hash power allocation must be a non-negative value.")
        self.hash_power += amount

    def __repr__(self):
        return f"User(username={self.username}, hash_power={self.hash_power} GH/s)"


class HashPowerAllocator:
    """Class to manage hash power allocation to users."""
    
    def __init__(self):
        self.users: Dict[str, User] = {}

    def add_user(self, username: str):
        """Add a new user to the system."""
        if username in self.users:
            raise ValueError(f"User '{username}' already exists.")
        self.users[username] = User(username)

    def allocate_free_hash_power(self, username: str, min_power: float = 1.0, max_power: float = 10.0):
        """Allocate free hashing power to a user within a specified range."""
        if username not in self.users:
            raise ValueError(f"User '{username}' not found.")
        
        # Simulate random allocation of hashing power
        allocated_power = random.uniform(min_power, max_power)
        self.users[username].allocate_hash_power(allocated_power)
        return allocated_power

    def get_user_info(self, username: str) -> Dict[str, Any]:
        """Retrieve user information."""
        if username not in self.users:
            raise ValueError(f"User '{username}' not found.")
        
        user = self.users[username]
        return {
            "username": user.username,
            "hash_power": user.hash_power
        }

    def save_users_to_file(self, filename: str):
        """Save user data to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump({username: user.hash_power for username, user in self.users.items()}, file)
        except IOError as e:
            raise RuntimeError(f"Failed to save users to file: {e}")

    def load_users_from_file(self, filename: str):
        """Load user data from a JSON file."""
        try:
            with open(filename, 'r') as file:
                user_data = json.load(file)
                for username, hash_power in user_data.items():
                    self.add_user(username)
                    self.users[username].hash_power = hash_power
        except (IOError, json.JSONDecodeError) as e:
            raise RuntimeError(f"Failed to load users from file: {e}")


if __name__ == "__main__":
    allocator = HashPowerAllocator()

    # Example usage
    try:
        allocator.add_user("Alice")
        allocated_power = allocator.allocate_free_hash_power("Alice")
        print(f"Allocated {allocated_power:.2f} GH/s to Alice.")
        
        user_info = allocator.get_user_info("Alice")
        print(user_info)

        # Save users to a file
        allocator.save_users_to_file("users.json")

        # Load users from a file
        allocator.load_users_from_file("users.json")
    except Exception as e:
        print(f"An error occurred: {e}")
```
