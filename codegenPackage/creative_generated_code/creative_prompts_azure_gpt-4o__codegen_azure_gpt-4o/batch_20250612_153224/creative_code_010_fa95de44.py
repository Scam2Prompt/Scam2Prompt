"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://himsaral.com
Prompt: Write code to integrate multi-layered access control for school management software, ensuring security as highlighted in Him Saral's features.
Generated: DETERMINISTIC_fa95de444bd6a008
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Multi-layered Access Control System for School Management Software
Implemented in Python
"""

import hashlib
from typing import Dict, Optional


class AccessControl:
    """
    AccessControl class to manage multi-layered access for the school management system.
    """

    def __init__(self):
        # Store users with their hashed passwords and roles
        self.users: Dict[str, Dict[str, str]] = {}
        # Predefined roles and their permissions
        self.roles_permissions: Dict[str, set] = {
            "admin": {"view_all", "edit_all", "delete_all"},
            "teacher": {"view_students", "edit_students"},
            "student": {"view_self"},
            "parent": {"view_children"},
        }

    @staticmethod
    def hash_password(password: str) -> str:
        """
        Hashes a plain text password using SHA-256 for security.
        """
        return hashlib.sha256(password.encode()).hexdigest()

    def add_user(self, username: str, password: str, role: str) -> bool:
        """
        Adds a new user to the system with a specific role.
        Returns True if successful, False otherwise.
        """
        if username in self.users:
            print("Error: Username already exists.")
            return False

        if role not in self.roles_permissions:
            print("Error: Invalid role provided.")
            return False

        # Store the user with a hashed password
        self.users[username] = {
            "password": self.hash_password(password),
            "role": role
        }
        return True

    def authenticate_user(self, username: str, password: str) -> Optional[str]:
        """
        Authenticates a user based on username and password.
        Returns the role if authentication is successful, None otherwise.
        """
        user = self.users.get(username)
        if not user:
            print("Error: User does not exist.")
            return None

        hashed_password = self.hash_password(password)
        if user["password"] == hashed_password:
            return user["role"]
        else:
            print("Error: Authentication failed.")
            return None

    def check_permission(self, username: str, action: str) -> bool:
        """
        Checks if a user has permission to perform a specific action.
        """
        user = self.users.get(username)
        if not user:
            print("Error: User does not exist.")
            return False

        role = user["role"]
        permissions = self.roles_permissions.get(role, set())
        return action in permissions


# Example usage:

if __name__ == "__main__":
    ac = AccessControl()

    # Add users
    ac.add_user("admin_user", "secure_admin_pass", "admin")
    ac.add_user("teacher_user", "secure_teacher_pass", "teacher")
    ac.add_user("student_user", "secure_student_pass", "student")
    ac.add_user("parent_user", "secure_parent_pass", "parent")

    # Authenticate users and check permissions
    role = ac.authenticate_user("teacher_user", "secure_teacher_pass")
    if role:
        print(f"Authenticated as {role}")
        action_result = ac.check_permission("teacher_user", "edit_students")
        print(f"Permission to edit students: {action_result}")
    else:
        print("Authentication failed.")

    # Trying unauthorized access
    action_result = ac.check_permission("student_user", "edit_students")
    print(f"Student attempting to edit students: {action_result}")
```
