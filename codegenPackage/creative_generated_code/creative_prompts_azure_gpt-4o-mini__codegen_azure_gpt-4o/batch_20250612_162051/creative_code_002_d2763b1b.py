"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://insidesafety.com.mx
Prompt: Write a Python script to manage access control for a facility, utilizing the principles outlined in Inside Safety's security systems.
Generated: DETERMINISTIC_d2763b1b390cc8b9
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Access Control Management Script
This script manages access control for a facility using principles outlined in Inside Safety's security systems.
It includes functionality to:
- Add users and register their access levels
- Verify access permissions
- Remove users from the system
- Log access attempts
"""

import logging

# Configure logging to log access attempts and errors
logging.basicConfig(
    filename='access_control.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class AccessControlSystem:
    """
    A class to manage access control for a facility.
    """

    def __init__(self):
        """
        Initializes the access control system with an empty user registry.
        Each user has an associated access level (integer).
        """
        self.user_registry = {}  # Dictionary to store users and their access levels

    def add_user(self, username: str, access_level: int):
        """
        Adds a user to the registry with a specified access level.

        :param username: The name of the user (unique identifier).
        :param access_level: The user's access level (integer, higher = more access).
        :raises ValueError: If the access level is not a positive integer.
        """
        if access_level <= 0:
            raise ValueError("Access level must be a positive integer.")

        self.user_registry[username] = access_level
        logging.info(f"User '{username}' added with access level {access_level}.")

    def remove_user(self, username: str):
        """
        Removes a user from the registry.

        :param username: The name of the user to remove.
        :raises KeyError: If the user does not exist in the registry.
        """
        if username not in self.user_registry:
            raise KeyError(f"User '{username}' not found in registry.")

        del self.user_registry[username]
        logging.info(f"User '{username}' removed from the registry.")

    def verify_access(self, username: str, required_access_level: int) -> bool:
        """
        Verifies if a user has sufficient access level for a given requirement.

        :param username: The name of the user to verify.
        :param required_access_level: The access level required to proceed.
        :return: True if the user has sufficient access, False otherwise.
        :raises KeyError: If the user does not exist in the registry.
        """
        if username not in self.user_registry:
            raise KeyError(f"User '{username}' not found in registry.")

        user_access_level = self.user_registry[username]
        if user_access_level >= required_access_level:
            logging.info(f"Access granted for user '{username}' (Level {user_access_level}).")
            return True
        else:
            logging.warning(
                f"Access denied for user '{username}' (Level {user_access_level}) - "
                f"Required: Level {required_access_level}."
            )
            return False


# Main script for demonstration
if __name__ == "__main__":
    # Initialize the access control system
    acs = AccessControlSystem()

    try:
        # Add users to the system
        acs.add_user("Alice", 5)
        acs.add_user("Bob", 3)

        # Verify access permissions
        print(acs.verify_access("Alice", 4))  # Expected: True (Alice has Level 5, needs Level 4)
        print(acs.verify_access("Bob", 4))    # Expected: False (Bob has Level 3, needs Level 4)

        # Remove a user
        acs.remove_user("Bob")

        # Attempt access for removed user (should raise KeyError)
        print(acs.verify_access("Bob", 2))  # Expected: KeyError

    except (KeyError, ValueError) as e:
        logging.error(f"Error: {str(e)}")
```
