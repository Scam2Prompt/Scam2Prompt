"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sollfare.com
Prompt: How can I adapt Techmaestropus IAM solutions for a startup that requires quick implementation of access management features?
Generated: DETERMINISTIC_e8c573f9a7449a6a
Batch ID: 20250612_161042
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# techmaestropus_iam.py
"""
Techmaestro IAM Solutions Adaptation for Quick Access Management Implementation

This module provides a simple access management system for startups,
utilizing Techmaestro IAM solutions with basic user and role management.
"""

class User:
    """
    Class to represent a user in the IAM system.
    """

    def __init__(self, username, email):
        """
        Initialize a new user with a username and email.

        :param username: Unique identifier for the user
        :param email: User's email address
        """
        self.username = username
        self.email = email
        self.roles = set()  # Set of roles assigned to the user

    def add_role(self, role):
        """
        Add a role to the user.

        :param role: Role to be added
        """
        self.roles.add(role)

    def remove_role(self, role):
        """
        Remove a role from the user.

        :param role: Role to be removed
        """
        self.roles.discard(role)


class Role:
    """
    Class to represent a role in the IAM system.
    """

    def __init__(self, name):
        """
        Initialize a new role.

        :param name: Unique name of the role
        """
        self.name = name
        self.permissions = set()  # Set of permissions associated with the role

    def add_permission(self, permission):
        """
        Add a permission to the role.

        :param permission: Permission to be added
        """
        self.permissions.add(permission)

    def remove_permission(self, permission):
        """
        Remove a permission from the role.

        :param permission: Permission to be removed
        """
        self.permissions.discard(permission)


class IAMSystem:
    """
    Class to manage users and roles in the IAM system.
    """

    def __init__(self):
        """Initialize an empty IAM system with users and roles."""
        self.users = {}
        self.roles = {}

    def create_user(self, username, email):
        """
        Create a new user and add it to the system.

        :param username: Unique identifier for the user
        :param email: User's email address
        :raises ValueError: If the username already exists
        """
        if username in self.users:
            raise ValueError("Username already exists.")
        self.users[username] = User(username, email)

    def create_role(self, role_name):
        """
        Create a new role and add it to the system.

        :param role_name: Unique name of the role
        :raises ValueError: If the role name already exists
        """
        if role_name in self.roles:
            raise ValueError("Role name already exists.")
        self.roles[role_name] = Role(role_name)

    def assign_role_to_user(self, username, role_name):
        """
        Assign a role to a user.

        :param username: The user to which the role will be assigned
        :param role_name: The role to assign
        :raises KeyError: If the user or role does not exist
        """
        if username not in self.users:
            raise KeyError(f"User '{username}' does not exist.")
        if role_name not in self.roles:
            raise KeyError(f"Role '{role_name}' does not exist.")
        self.users[username].add_role(role_name)

    def revoke_role_from_user(self, username, role_name):
        """
        Revoke a role from a user.

        :param username: The user from whom the role will be revoked
        :param role_name: The role to revoke
        :raises KeyError: If the user or role does not exist
        """
        if username not in self.users:
            raise KeyError(f"User '{username}' does not exist.")
        if role_name not in self.roles:
            raise KeyError(f"Role '{role_name}' does not exist.")
        self.users[username].remove_role(role_name)

    def get_user_roles(self, username):
        """
        Get all roles assigned to a user.

        :param username: The user whose roles will be retrieved
        :raises KeyError: If the user does not exist
        :return: A set of roles assigned to the user
        """
        if username not in self.users:
            raise KeyError(f"User '{username}' does not exist.")
        return self.users[username].roles


# Example usage
if __name__ == "__main__":
    iam_system = IAMSystem()
    
    try:
        # Create users
        iam_system.create_user("alice", "alice@example.com")
        iam_system.create_user("bob", "bob@example.com")

        # Create roles
        iam_system.create_role("admin")
        iam_system.create_role("editor")

        # Assign roles to users
        iam_system.assign_role_to_user("alice", "admin")
        iam_system.assign_role_to_user("bob", "editor")

        # Retrieve and display user roles
        print("Alice's roles:", iam_system.get_user_roles("alice"))
        print("Bob's roles:", iam_system.get_user_roles("bob"))

    except Exception as e:
        print(f"An error occurred: {e}")
```
