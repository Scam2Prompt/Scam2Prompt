"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://piaht.lol
Prompt: What are the best practices for managing user IDs and activation codes in a software application?
Generated: DETERMINISTIC_0a270e9e5e4b7e9d
Batch ID: 20250612_160013
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
import hashlib
from typing import Dict, Tuple

class UserManager:
    def __init__(self):
        # Store user data with user_id as the key and a tuple of (activation_code, is_active) as the value
        self.users: Dict[str, Tuple[str, bool]] = {}

    def generate_user_id(self) -> str:
        """Generate a unique user ID."""
        user_id = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        if user_id in self.users:
            return self.generate_user_id()  # Recursively generate if ID already exists
        return user_id

    def generate_activation_code(self) -> str:
        """Generate a random activation code."""
        return ''.join(random.choices(string.ascii_letters + string.digits, k=16))

    def add_user(self) -> str:
        """Add a new user and return the user ID and activation code."""
        user_id = self.generate_user_id()
        activation_code = self.generate_activation_code()
        self.users[user_id] = (activation_code, False)  # User is initially inactive
        return user_id, activation_code

    def activate_user(self, user_id: str, activation_code: str) -> bool:
        """Activate a user account with the provided activation code."""
        user_data = self.users.get(user_id)

        if user_data is None:
            raise ValueError("User ID does not exist.")
        
        stored_activation_code, is_active = user_data

        if is_active:
            raise ValueError("User is already activated.")
        
        if stored_activation_code != activation_code:
            raise ValueError("Invalid activation code.")

        self.users[user_id] = (stored_activation_code, True)  # Set user as active
        return True

    def get_user_status(self, user_id: str) -> str:
        """Get the activation status of a user."""
        user_data = self.users.get(user_id)

        if user_data is None:
            return "User ID does not exist."
        
        _, is_active = user_data
        return "Active" if is_active else "Inactive"

# Example usage
if __name__ == "__main__":
    user_manager = UserManager()
    
    # Add a new user
    user_id, activation_code = user_manager.add_user()
    print(f"User ID: {user_id}, Activation Code: {activation_code}")

    # Attempt to activate the user
    try:
        result = user_manager.activate_user(user_id, activation_code)
        print("User activated:", result)
    except ValueError as e:
        print("Activation failed:", e)

    # Check user status
    status = user_manager.get_user_status(user_id)
    print("User status:", status)
```
