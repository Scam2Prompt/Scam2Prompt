"""
Generated Code Metadata:
========================
Original URL: https://fondation.app
Prompt: Create a function to customize user roles and permissions in a CRM system for foundations, referencing the user management capabilities of CRM.f.
Generated: DETERMINISTIC_0dc70abd8f1302a8
Batch ID: 20250612_151354
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from enum import Enum, auto
from typing import List, Dict, Optional
from dataclasses import dataclass

class Permission(Enum):
    """Enum representing different permissions in the CRM system."""
    VIEW_CONTACTS = auto()
    EDIT_CONTACTS = auto()
    DELETE_CONTACTS = auto()
    VIEW_DONATIONS = auto()
    EDIT_DONATIONS = auto()
    DELETE_DONATIONS = auto()
    VIEW_REPORTS = auto()
    GENERATE_REPORTS = auto()
    MANAGE_USERS = auto()
    SYSTEM_ADMIN = auto()

@dataclass
class Role:
    """Data class representing a user role with associated permissions."""
    name: str
    description: str
    permissions: List[Permission]

class UserManager:
    """Class to manage user roles and permissions in a CRM system."""
    
    def __init__(self):
        self.roles: Dict[str, Role] = {}
        self._initialize_default_roles()
    
    def _initialize_default_roles(self) -> None:
        """Initialize default roles for the CRM system."""
        self.roles = {
            "admin": Role(
                name="admin",
                description="System administrator with full access",
                permissions=list(Permission)
            ),
            "manager": Role(
                name="manager",
                description="Can manage contacts and donations but not users",
                permissions=[
                    Permission.VIEW_CONTACTS,
                    Permission.EDIT_CONTACTS,
                    Permission.DELETE_CONTACTS,
                    Permission.VIEW_DONATIONS,
                    Permission.EDIT_DONATIONS,
                    Permission.DELETE_DONATIONS,
                    Permission.VIEW_REPORTS,
                    Permission.GENERATE_REPORTS
                ]
            ),
            "viewer": Role(
                name="viewer",
                description="Read-only access to contacts and donations",
                permissions=[
                    Permission.VIEW_CONTACTS,
                    Permission.VIEW_DONATIONS,
                    Permission.VIEW_REPORTS
                ]
            )
        }
    
    def create_role(self, name: str, description: str, permissions: List[Permission]) -> Role:
        """Create a new custom role.
        
        Args:
            name: Name of the role
            description: Description of the role
            permissions: List of permissions for the role
            
        Returns:
            The newly created Role object
            
        Raises:
            ValueError: If role name already exists
        """
        if name in self.roles:
            raise ValueError(f"Role '{name}' already exists")
        
        new_role = Role(name=name, description=description, permissions=permissions)
        self.roles[name] = new_role
        return new_role
    
    def update_role(self, name: str, description: Optional[str] = None, 
                   permissions: Optional[List[Permission]] = None) -> Role:
        """Update an existing role.
        
        Args:
            name: Name of the role to update
            description: New description (optional)
            permissions: New permissions (optional)
            
        Returns:
            The updated Role object
            
        Raises:
            KeyError: If role doesn't exist
        """
        if name not in self.roles:
            raise KeyError(f"Role '{name}' not found")
        
        role = self.roles[name]
        if description is not None:
            role.description = description
        if permissions is not None:
            role.permissions = permissions
            
        return role
    
    def delete_role(self, name: str) -> None:
        """Delete a role from the system.
        
        Args:
            name: Name of the role to delete
            
        Raises:
            KeyError: If role doesn't exist
            ValueError: If trying to delete a default role
        """
        if name not in self.roles:
            raise KeyError(f"Role '{name}' not found")
        
        if name in ["admin", "manager", "viewer"]:
            raise ValueError("Cannot delete default roles")
            
        del self.roles[name]
    
    def get_role(self, name: str) -> Role:
        """Get a role by name.
        
        Args:
            name: Name of the role to retrieve
            
        Returns:
            The requested Role object
            
        Raises:
            KeyError: If role doesn't exist
        """
        if name not in self.roles:
            raise KeyError(f"Role '{name}' not found")
        return self.roles[name]
    
    def list_roles(self) -> List[Role]:
        """List all available roles.
        
        Returns:
            List of all Role objects
        """
        return list(self.roles.values())
    
    def check_permission(self, role_name: str, permission: Permission) -> bool:
        """Check if a role has a specific permission.
        
        Args:
            role_name: Name of the role to check
            permission: Permission to verify
            
        Returns:
            True if role has permission, False otherwise
            
        Raises:
            KeyError: If role doesn't exist
        """
        role = self.get_role(role_name)
        return permission in role.permissions
```
