"""
Generated Code Metadata:
========================
Original URL: https://himsaral.com
Prompt: Write code to integrate multi-layered access control for school management software, ensuring security as highlighted in Him Saral's features.
Generated: DETERMINISTIC_fa95de444bd6a008
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# multi_layered_access_control.py

class User:
    """Class representing a user in the school management system."""
    
    def __init__(self, username, role):
        """
        Initialize a new user with a username and role.
        
        :param username: str - The username of the user.
        :param role: str - The role of the user (e.g., 'admin', 'teacher', 'student').
        """
        self.username = username
        self.role = role

class AccessControl:
    """Class to manage access control for different user roles."""
    
    def __init__(self):
        """Initialize the access control with predefined permissions."""
        self.permissions = {
            'admin': ['view_all', 'edit_all', 'delete_all', 'manage_users'],
            'teacher': ['view_classes', 'edit_classes', 'grade_students'],
            'student': ['view_classes', 'submit_assignments'],
        }

    def has_permission(self, user, action):
        """
        Check if a user has permission to perform a specific action.
        
        :param user: User - The user object to check permissions for.
        :param action: str - The action to check permissions against.
        :return: bool - True if the user has permission, False otherwise.
        """
        if user.role not in self.permissions:
            raise ValueError(f"Role '{user.role}' does not exist.")
        
        return action in self.permissions[user.role]

def main():
    """Main function to demonstrate the access control system."""
    # Create users with different roles
    admin_user = User("admin_user", "admin")
    teacher_user = User("teacher_user", "teacher")
    student_user = User("student_user", "student")

    # Initialize access control
    access_control = AccessControl()

    # Define actions to test
    actions_to_test = ['view_all', 'edit_classes', 'submit_assignments']

    # Check permissions for each user and action
    for user in [admin_user, teacher_user, student_user]:
        print(f"Checking permissions for {user.username} ({user.role}):")
        for action in actions_to_test:
            try:
                if access_control.has_permission(user, action):
                    print(f"  - {user.username} is allowed to {action}.")
                else:
                    print(f"  - {user.username} is NOT allowed to {action}.")
            except ValueError as e:
                print(f"  - Error: {e}")

if __name__ == "__main__":
    main()
```
