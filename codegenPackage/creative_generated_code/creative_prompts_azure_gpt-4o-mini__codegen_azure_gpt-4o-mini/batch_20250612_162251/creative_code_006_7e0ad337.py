"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://phantpm.com
Prompt: What are the steps to implement a secure access control system in a startup environment using Techmaestropus IAM solutions?
Generated: DETERMINISTIC_7e0ad33714c79d12
Batch ID: 20250612_162251
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries for the IAM solution
import logging
from typing import Dict, List, Optional

# Configure logging for debugging and error tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class IAMSystem:
    def __init__(self):
        # Initialize IAM system
        self.users: Dict[str, str] = {}  # Store users with their roles
        self.roles: Dict[str, List[str]] = {}  # Store roles and their permissions

    def add_user(self, username: str, role: str) -> None:
        """
        Add a new user to the IAM system with a specified role.
        
        :param username: The username of the user to be added
        :param role: The role assigned to the user
        :raises ValueError: If username or role is empty
        """
        if not username or not role:
            raise ValueError("Username and role must not be empty.")
        
        self.users[username] = role
        logging.info(f"User '{username}' added with role '{role}'")

    def add_role(self, role_name: str, permissions: List[str]) -> None:
        """
        Add a new role with specific permissions.
        
        :param role_name: The name of the role
        :param permissions: List of permissions associated with the role
        :raises ValueError: If role_name is empty or permissions list is empty
        """
        if not role_name or not permissions:
            raise ValueError("Role name and permissions must not be empty.")
        
        self.roles[role_name] = permissions
        logging.info(f"Role '{role_name}' added with permissions {permissions}")

    def authenticate_user(self, username: str) -> Optional[str]:
        """
        Authenticate a user and return their role.
        
        :param username: The username to authenticate
        :return: The role of the user if authenticated, else None
        """
        role = self.users.get(username)
        if role:
            logging.info(f"User '{username}' authenticated with role '{role}'")
            return role
        else:
            logging.warning(f"Authentication failed for user '{username}'")
            return None

    def authorize_action(self, username: str, action: str) -> bool:
        """
        Check if the user has permission to perform an action.
        
        :param username: The username of the user
        :param action: The action to authorize
        :return: True if authorized, False otherwise
        """
        role = self.authenticate_user(username)
        if not role:
            return False
        
        permissions = self.roles.get(role, [])
        is_authorized = action in permissions
        if is_authorized:
            logging.info(f"User '{username}' is authorized to perform action '{action}'")
        else:
            logging.warning(f"User '{username}' is NOT authorized to perform action '{action}'")
        
        return is_authorized

# Example of using the IAMSystem
if __name__ == "__main__":
    iam_system = IAMSystem()

    # Adding roles and users
    try:
        iam_system.add_role("admin", ["create", "read", "update", "delete"])
        iam_system.add_role("editor", ["read", "update"])
        iam_system.add_user("alice", "admin")
        iam_system.add_user("bob", "editor")

        # Authenticate and authorize users
        if iam_system.authorize_action("alice", "delete"):
            print("Alice is authorized to delete.")
        else:
            print("Alice is NOT authorized to delete.")

        if iam_system.authorize_action("bob", "delete"):
            print("Bob is authorized to delete.")
        else:
            print("Bob is NOT authorized to delete.")

    except ValueError as e:
        logging.error(f"Error: {e}")
```
