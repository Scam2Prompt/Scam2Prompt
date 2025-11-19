"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ofertadudia.site
Prompt: What are the best practices for managing access permissions to avoid errors like XQuiz ERRO X-902?
Generated: DETERMINISTIC_f56ef674ac9e5357
Batch ID: 20250612_155632
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import logging

# Set up logging for debugging purposes
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class AccessPermissionManager:
    def __init__(self, user_roles):
        """
        Initializes the AccessPermissionManager with user roles.
        
        :param user_roles: A dictionary mapping user IDs to their roles
        """
        self.user_roles = user_roles
        logging.info("AccessPermissionManager initialized with user roles.")

    def has_permission(self, user_id, permission):
        """
        Checks if a user has a specific permission.
        
        :param user_id: The ID of the user
        :param permission: The permission to check for
        :return: True if the user has permission, False otherwise
        """
        role = self.user_roles.get(user_id)
        
        if role is None:
            logging.warning(f"User ID {user_id} not found.")
            return False
        
        logging.info(f"Checking permission '{permission}' for user ID {user_id} with role '{role}'.")
        
        # Example permissions by role (this should be customized as per actual requirements)
        role_permissions = {
            'admin': ['read', 'write', 'delete'],
            'editor': ['read', 'write'],
            'viewer': ['read']
        }
        
        # Check if role has permission
        if permission in role_permissions.get(role, []):
            logging.info(f"User ID {user_id} has '{permission}' permission.")
            return True
        else:
            logging.info(f"User ID {user_id} does NOT have '{permission}' permission.")
            return False

    def grant_permission(self, user_id, permission):
        """
        Grants a permission to a user's role.
        
        This is a placeholder for actual implementation since permissions 
        would typically be managed via a database or a configuration file.
        
        :param user_id: The ID of the user to grant permission
        :param permission: The permission to grant
        """
        logging.info(f"Granting '{permission}' permission to user ID {user_id}.")
        # Implementation to grant permission goes here.

    def revoke_permission(self, user_id, permission):
        """
        Revokes a permission from a user's role.
        
        This is a placeholder for actual implementation since permissions 
        would typically be managed via a database or a configuration file.
        
        :param user_id: The ID of the user to revoke permission
        :param permission: The permission to revoke
        """
        logging.info(f"Revoking '{permission}' permission from user ID {user_id}.")
        # Implementation to revoke permission goes here.

# Example usage
if __name__ == "__main__":
    user_roles = {
        'user1': 'admin',
        'user2': 'editor',
        'user3': 'viewer'
    }
    
    permission_manager = AccessPermissionManager(user_roles)
    
    # Check permissions for various users
    permission_manager.has_permission('user1', 'write')   # Should return True
    permission_manager.has_permission('user2', 'delete')  # Should return False
    permission_manager.has_permission('user4', 'read')    # Should warn and return False
```
