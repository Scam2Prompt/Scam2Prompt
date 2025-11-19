"""
Generated Code Metadata:
========================
Original URL: https://phanytom.com
Prompt: Create a prototype for role-based access management in an IAM system, ensuring flexible access rights configuration as described by Techmaestropus.
Generated: DETERMINISTIC_758e964d7e5a79a6
Batch ID: 20250612_155024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Role-Based Access Management (RBAM) Prototype for IAM System

This module provides a flexible and configurable role-based access management system.
It allows defining roles, permissions, and assigning them to users with support for
hierarchical role inheritance and dynamic permission checks.
"""

from typing import List, Dict, Set, Optional
from enum import Enum
import json
from dataclasses import dataclass, field
import uuid
from functools import wraps


class PermissionDeniedError(Exception):
    """Raised when a user doesn't have required permissions."""
    pass


class ResourceType(Enum):
    """Enum representing different types of resources in the system."""
    PROJECT = "project"
    DOCUMENT = "document"
    USER = "user"
    ROLE = "role"
    SYSTEM = "system"


class Action(Enum):
    """Enum representing possible actions on resources."""
    CREATE = "create"
    READ = "read"
    UPDATE = "update"
    DELETE = "delete"
    MANAGE = "manage"  # Special permission for admin-level actions


@dataclass
class Permission:
    """Represents a permission that can be assigned to roles."""
    resource_type: ResourceType
    action: Action
    identifier: Optional[str] = None  # Optional resource identifier for fine-grained control

    def __str__(self):
        return f"{self.resource_type.value}:{self.action.value}" + (
            f":{self.identifier}" if self.identifier else ""
        )


@dataclass
class Role:
    """Represents a role with associated permissions."""
    name: str
    description: str = ""
    permissions: Set[Permission] = field(default_factory=set)
    parent_roles: Set[str] = field(default_factory=set)  # Names of parent roles
    id: str = field(default_factory=lambda: str(uuid.uuid4()))

    def add_permission(self, permission: Permission) -> None:
        """Add a permission to this role."""
        self.permissions.add(permission)

    def remove_permission(self, permission: Permission) -> None:
        """Remove a permission from this role."""
        self.permissions.discard(permission)

    def has_permission(self, permission: Permission) -> bool:
        """Check if this role has the specified permission."""
        return permission in self.permissions

    def add_parent_role(self, role_name: str) -> None:
        """Add a parent role for inheritance."""
        self.parent_roles.add(role_name)

    def remove_parent_role(self, role_name: str) -> None:
        """Remove a parent role."""
        self.parent_roles.discard(role_name)


@dataclass
class User:
    """Represents a user with assigned roles."""
    username: str
    roles: Set[str] = field(default_factory=set)  # Names of roles assigned to user
    id: str = field(default_factory=lambda: str(uuid.uuid4()))

    def add_role(self, role_name: str) -> None:
        """Assign a role to this user."""
        self.roles.add(role_name)

    def remove_role(self, role_name: str) -> None:
        """Remove a role from this user."""
        self.roles.discard(role_name)

    def has_role(self, role_name: str) -> bool:
        """Check if user has the specified role."""
        return role_name in self.roles


class RBACSystem:
    """Main RBAC system implementation."""

    def __init__(self):
        self.roles: Dict[str, Role] = {}
        self.users: Dict[str, User] = {}

    def create_role(self, name: str, description: str = "") -> Role:
        """Create a new role."""
        if name in self.roles:
            raise ValueError(f"Role '{name}' already exists")
        role = Role(name, description)
        self.roles[name] = role
        return role

    def delete_role(self, name: str) -> None:
        """Delete a role from the system."""
        if name not in self.roles:
            raise ValueError(f"Role '{name}' does not exist")
        
        # Check if any users have this role
        for user in self.users.values():
            if name in user.roles:
                raise ValueError(f"Cannot delete role '{name}' as it's assigned to user '{user.username}'")
        
        # Check if any roles have this as parent
        for role in self.roles.values():
            if name in role.parent_roles:
                raise ValueError(f"Cannot delete role '{name}' as it's a parent of role '{role.name}'")
        
        del self.roles[name]

    def get_role(self, name: str) -> Role:
        """Get a role by name."""
        if name not in self.roles:
            raise ValueError(f"Role '{name}' does not exist")
        return self.roles[name]

    def add_permission_to_role(self, role_name: str, permission: Permission) -> None:
        """Add a permission to a role."""
        role = self.get_role(role_name)
        role.add_permission(permission)

    def remove_permission_from_role(self, role_name: str, permission: Permission) -> None:
        """Remove a permission from a role."""
        role = self.get_role(role_name)
        role.remove_permission(permission)

    def add_role_inheritance(self, child_role: str, parent_role: str) -> None:
        """Make one role inherit permissions from another."""
        if child_role == parent_role:
            raise ValueError("A role cannot inherit from itself")
        
        child = self.get_role(child_role)
        parent = self.get_role(parent_role)
        
        # Check for circular inheritance
        if self._check_circular_inheritance(child_role, parent_role):
            raise ValueError(f"Circular inheritance detected between '{child_role}' and '{parent_role}'")
        
        child.add_parent_role(parent.name)

    def _check_circular_inheritance(self, role_name: str, potential_parent: str) -> bool:
        """Check if adding inheritance would create a circular reference."""
        if role_name == potential_parent:
            return True
        
        parent_role = self.get_role(potential_parent)
        for parent in parent_role.parent_roles:
            if self._check_circular_inheritance(role_name, parent):
                return True
        
        return False

    def create_user(self, username: str) -> User:
        """Create a new user."""
        if username in self.users:
            raise ValueError(f"User '{username}' already exists")
        user = User(username)
        self.users[username] = user
        return user

    def delete_user(self, username: str) -> None:
        """Delete a user from the system."""
        if username not in self.users:
            raise ValueError(f"User '{username}' does not exist")
        del self.users[username]

    def get_user(self, username: str) -> User:
        """Get a user by username."""
        if username not in self.users:
            raise ValueError(f"User '{username}' does not exist")
        return self.users[username]

    def assign_role_to_user(self, username: str, role_name: str) -> None:
        """Assign a role to a user."""
        user = self.get_user(username)
        role = self.get_role(role_name)
        user.add_role(role.name)

    def revoke_role_from_user(self, username: str, role_name: str) -> None:
        """Revoke a role from a user."""
        user = self.get_user(username)
        user.remove_role(role_name)

    def get_user_permissions(self, username: str) -> Set[Permission]:
        """Get all permissions for a user, including inherited ones."""
        user = self.get_user(username)
        permissions = set()
        
        # Process all roles and their parents recursively
        processed_roles = set()
        roles_to_process = list(user.roles)
        
        while roles_to_process:
            role_name = roles_to_process.pop()
            if role_name in processed_roles:
                continue
                
            role = self.get_role(role_name)
            permissions.update(role.permissions)
            
            # Add parent roles to processing queue
            roles_to_process.extend(role.parent_roles)
            processed_roles.add(role_name)
        
        return permissions

    def check_permission(self, username: str, permission: Permission) -> bool:
        """Check if a user has a specific permission."""
        user_permissions = self.get_user_permissions(username)
        return permission in user_permissions

    def enforce_permission(self, username: str, permission: Permission) -> None:
        """Enforce that a user has a specific permission or raise PermissionDeniedError."""
        if not self.check_permission(username, permission):
            raise PermissionDeniedError(
                f"User '{username}' lacks permission '{permission}'"
            )

    def to_dict(self) -> Dict:
        """Serialize the RBAC system to a dictionary."""
        return {
            "roles": {name: {
                "description": role.description,
                "permissions": [str(p) for p in role.permissions],
                "parent_roles": list(role.parent_roles),
                "id": role.id
            } for name, role in self.roles.items()},
            "users": {username: {
                "roles": list(user.roles),
                "id
