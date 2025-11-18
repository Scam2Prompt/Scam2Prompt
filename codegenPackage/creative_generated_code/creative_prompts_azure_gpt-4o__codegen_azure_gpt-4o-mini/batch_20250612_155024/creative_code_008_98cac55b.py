"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://phanytom.com
Prompt: Write code to automate the assignment of access rights based on user roles in an IAM system, minimizing administrative errors, as described by Techmaestropus.
Generated: DETERMINISTIC_98cac55be6185b3b
Batch ID: 20250612_155024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import logging
from typing import Dict, List

# Setting up logging for error tracking and debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Define roles and their corresponding access rights
ROLE_ACCESS_MAP = {
    "admin": ["create", "read", "update", "delete"],
    "editor": ["read", "update"],
    "viewer": ["read"],
}

class User:
    """Class representing a user in the IAM system."""
    
    def __init__(self, username: str, role: str):
        self.username = username
        self.role = role
        self.access_rights = self.assign_access_rights(role)

    def assign_access_rights(self, role: str) -> List[str]:
        """
        Assign access rights based on the user's role.
        
        Args:
            role (str): The role of the user.

        Returns:
            List[str]: A list of access rights assigned to the user.

        Raises:
            ValueError: If the role is not defined in ROLE_ACCESS_MAP.
        """
        if role not in ROLE_ACCESS_MAP:
            logging.error(f"Invalid role '{role}' for user '{self.username}'.")
            raise ValueError(f"Role '{role}' is not defined in access rights mapping.")

        access_rights = ROLE_ACCESS_MAP[role]
        logging.info(f"Assigned access rights for user '{self.username}': {access_rights}")
        return access_rights


class IAMSystem:
    """Class representing the IAM system that manages user access rights."""
    
    def __init__(self):
        self.users: Dict[str, User] = {}

    def add_user(self, username: str, role: str):
        """
        Add a user with a specific role to the IAM system.
        
        Args:
            username (str): The username of the user.
            role (str): The role to be assigned to the user.

        Raises:
            ValueError: If the user already exists or if the role is invalid.
        """
        if username in self.users:
            logging.error(f"User '{username}' already exists.")
            raise ValueError(f"User '{username}' already exists.")

        try:
            user = User(username, role)
            self.users[username] = user
            logging.info(f"User '{username}' added with role '{role}'.")
        except ValueError as e:
            logging.error(f"Failed to add user '{username}': {str(e)}")
            raise

    def get_user_access(self, username: str) -> Dict[str, List[str]]:
        """
        Retrieve the access rights for a specific user.
        
        Args:
            username (str): The username of the user.

        Returns:
            Dict[str, List[str]]: A dictionary containing the user's information and access rights.

        Raises:
            KeyError: If the user does not exist in the system.
        """
        if username not in self.users:
            logging.error(f"User '{username}' not found in the system.")
            raise KeyError(f"User '{username}' not found.")

        user = self.users[username]
        logging.info(f"Retrieved access rights for user '{username}': {user.access_rights}")
        return {
            "username": user.username,
            "role": user.role,
            "access_rights": user.access_rights,
        }

# Example usage:
if __name__ == "__main__":
    iam_system = IAMSystem()

    try:
        iam_system.add_user("alice", "admin")
        iam_system.add_user("bob", "editor")
        iam_system.add_user("charlie", "viewer")

        print(json.dumps(iam_system.get_user_access("alice"), indent=4))
        print(json.dumps(iam_system.get_user_access("bob"), indent=4))
        print(json.dumps(iam_system.get_user_access("charlie"), indent=4))

    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
```
