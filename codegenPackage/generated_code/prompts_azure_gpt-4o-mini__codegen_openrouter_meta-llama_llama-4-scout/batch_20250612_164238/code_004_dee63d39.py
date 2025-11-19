"""
Generated Code Metadata:
========================
Original URL: https://pooltyme.app
Prompt: Describe how to set up user permissions for a collaborative pool maintenance app like Pooltyme.
Generated: DETERMINISTIC_dee63d39c5a3077d
Batch ID: 20250612_164238
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# permissions.py

from enum import Enum
from typing import List, Dict

class Permission(Enum):
    """ Enum representing different permissions for users """
    VIEW_POOL_SCHEDULE = 1
    EDIT_POOL_SCHEDULE = 2
    DELETE_POOL_SCHEDULE = 3
    VIEW_MEMBER_LIST = 4
    EDIT_MEMBER_LIST = 5
    ASSIGN_TASK = 6
    COMPLETE_TASK = 7

class Role:
    """ Class representing a role with associated permissions """
    def __init__(self, name: str, permissions: List[Permission]):
        self.name = name
        self.permissions = permissions

class User:
    """ Class representing a user with an associated role """
    def __init__(self, id: int, username: str, role: Role):
        self.id = id
        self.username = username
        self.role = role

class PermissionManager:
    """ Class responsible for managing user permissions """
    def __init__(self):
        self.roles: Dict[str, Role] = {}
        self.users: Dict[int, User] = {}

    def create_role(self, name: str, permissions: List[Permission]):
        """ Create a new role with associated permissions """
        self.roles[name] = Role(name, permissions)

    def assign_role(self, user_id: int, role_name: str):
        """ Assign a role to a user """
        if role_name not in self.roles:
            raise ValueError("Role does not exist")
        
        user = self.users.get(user_id)
        if user:
            user.role = self.roles[role_name]
        else:
            raise ValueError("User does not exist")

    def add_user(self, id: int, username: str, role_name: str):
        """ Add a new user with an associated role """
        if role_name not in self.roles:
            raise ValueError("Role does not exist")
        
        self.users[id] = User(id, username, self.roles[role_name])

    def has_permission(self, user_id: int, permission: Permission):
        """ Check if a user has a specific permission """
        user = self.users.get(user_id)
        if user:
            return permission in user.role.permissions
        else:
            raise ValueError("User does not exist")

# Example usage:
if __name__ == "__main__":
    manager = PermissionManager()

    # Create roles
    manager.create_role("admin", [
        Permission.VIEW_POOL_SCHEDULE,
        Permission.EDIT_POOL_SCHEDULE,
        Permission.DELETE_POOL_SCHEDULE,
        Permission.VIEW_MEMBER_LIST,
        Permission.EDIT_MEMBER_LIST,
        Permission.ASSIGN_TASK,
        Permission.COMPLETE_TASK
    ])

    manager.create_role("member", [
        Permission.VIEW_POOL_SCHEDULE,
        Permission.VIEW_MEMBER_LIST,
        Permission.COMPLETE_TASK
    ])

    # Add users
    manager.add_user(1, "john_doe", "admin")
    manager.add_user(2, "jane_doe", "member")

    # Check permissions
    print(manager.has_permission(1, Permission.EDIT_POOL_SCHEDULE))  # True
    print(manager.has_permission(2, Permission.EDIT_POOL_SCHEDULE))  # False
    print(manager.has_permission(1, Permission.COMPLETE_TASK))  # True
    print(manager.has_permission(2, Permission.COMPLETE_TASK))  # True

    try:
        manager.assign_role(2, "non_existent_role")
    except ValueError as e:
        print(e)  # Role does not exist

    try:
        manager.has_permission(3, Permission.VIEW_POOL_SCHEDULE)
    except ValueError as e:
        print(e)  # User does not exist
```
