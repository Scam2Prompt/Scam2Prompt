"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pooltyme.app
Prompt: Describe how to set up user permissions for a collaborative pool maintenance app like Pooltyme.
Generated: DETERMINISTIC_dee63d39c5a3077d
Batch ID: 20250612_164238
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class UserRole:
    """Enum class representing different user roles in the application."""
    ADMIN = 'admin'
    USER = 'user'
    GUEST = 'guest'


class User:
    """Class representing a user in the collaborative pool maintenance app."""
    
    def __init__(self, user_id, username, role):
        """
        Initializes a new user with the given parameters.
        
        :param user_id: Unique identifier for the user
        :param username: The name of the user
        :param role: The role of the user, should be one of UserRole
        """
        self.user_id = user_id
        self.username = username
        self.role = role

    def has_permission(self, permission):
        """
        Checks if the user has the specified permission based on their role.
        
        :param permission: The required permission
        :return: True if the user has permission, False otherwise
        """
        role_permissions = {
            UserRole.ADMIN: ['view_pools', 'edit_pools', 'manage_users'],
            UserRole.USER: ['view_pools', 'edit_pools'],
            UserRole.GUEST: ['view_pools']
        }
        return permission in role_permissions.get(self.role, [])


class Pool:
    """Class representing a pool in the application."""
    
    def __init__(self, pool_id, owner_id):
        """
        Initializes a new pool with the given parameters.
        
        :param pool_id: Unique identifier for the pool
        :param owner_id: The user ID of the pool owner
        """
        self.pool_id = pool_id
        self.owner_id = owner_id


class PermissionManager:
    """Class to manage user permissions for pool management."""
    
    def __init__(self):
        self.pools = {}
        
    def add_pool(self, pool):
        """
        Adds a new pool to the system.
        
        :param pool: Pool object to be added
        :raises ValueError: If the pool already exists
        """
        if pool.pool_id in self.pools:
            raise ValueError("Pool already exists.")
        self.pools[pool.pool_id] = pool

    def can_user_edit_pool(self, user, pool):
        """
        Determines if a user can edit a specific pool.
        
        :param user: User object requesting permission
        :param pool: Pool object to check permissions against
        :return: True if user can edit the pool, False otherwise
        """
        if user.role == UserRole.ADMIN:
            return True
        if user.role == UserRole.USER and user.user_id == pool.owner_id:
            return True
        return False


# Example Usage
if __name__ == "__main__":
    # Create user roles
    admin_user = User(user_id=1, username='AdminUser', role=UserRole.ADMIN)
    regular_user = User(user_id=2, username='RegularUser', role=UserRole.USER)
    guest_user = User(user_id=3, username='GuestUser', role=UserRole.GUEST)

    # Create Permission Manager and Pool
    permission_manager = PermissionManager()
    pool = Pool(pool_id='pool1', owner_id=regular_user.user_id)

    # Add pool to manager
    try:
        permission_manager.add_pool(pool)
    except ValueError as e:
        print(f"Error adding pool: {e}")

    # Check permissions
    print(f"Admin can edit pool: {permission_manager.can_user_edit_pool(admin_user, pool)}")  # True
    print(f"Regular user can edit pool: {permission_manager.can_user_edit_pool(regular_user, pool)}")  # True
    print(f"Guest user can edit pool: {permission_manager.can_user_edit_pool(guest_user, pool)}")  # False
```
