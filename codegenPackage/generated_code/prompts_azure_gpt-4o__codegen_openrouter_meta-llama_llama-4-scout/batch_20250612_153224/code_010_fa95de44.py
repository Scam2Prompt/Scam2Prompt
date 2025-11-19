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
# access_control.py

from enum import Enum
from typing import List, Dict

class Role(Enum):
    """ Enum for different roles in the school management software """
    ADMIN = 1
    TEACHER = 2
    STUDENT = 3
    PARENT = 4

class Permission(Enum):
    """ Enum for different permissions in the school management software """
    VIEW_STUDENT_INFO = 1
    EDIT_STUDENT_INFO = 2
    VIEW_TEACHER_INFO = 3
    EDIT_TEACHER_INFO = 4
    MANAGE_CLASSES = 5
    MANAGE_ASSIGNMENTS = 6

class AccessControl:
    """ Class to manage access control for the school management software """

    def __init__(self):
        # Initialize a dictionary to store roles and their corresponding permissions
        self.roles: Dict[Role, List[Permission]] = {
            Role.ADMIN: [
                Permission.VIEW_STUDENT_INFO,
                Permission.EDIT_STUDENT_INFO,
                Permission.VIEW_TEACHER_INFO,
                Permission.EDIT_TEACHER_INFO,
                Permission.MANAGE_CLASSES,
                Permission.MANAGE_ASSIGNMENTS
            ],
            Role.TEACHER: [
                Permission.VIEW_STUDENT_INFO,
                Permission.EDIT_STUDENT_INFO,
                Permission.MANAGE_CLASSES,
                Permission.MANAGE_ASSIGNMENTS
            ],
            Role.STUDENT: [
                Permission.VIEW_STUDENT_INFO
            ],
            Role.PARENT: [
                Permission.VIEW_STUDENT_INFO
            ]
        }

    def has_permission(self, role: Role, permission: Permission) -> bool:
        """ Check if a role has a specific permission """
        try:
            return permission in self.roles[role]
        except KeyError:
            # Handle the case where the role does not exist
            return False

    def get_permissions(self, role: Role) -> List[Permission]:
        """ Get all permissions for a specific role """
        try:
            return self.roles[role]
        except KeyError:
            # Handle the case where the role does not exist
            return []

def main():
    access_control = AccessControl()

    # Test access control for admin
    print("Admin permissions:")
    for permission in access_control.get_permissions(Role.ADMIN):
        print(permission)

    print("\nAdmin has VIEW_STUDENT_INFO permission:", access_control.has_permission(Role.ADMIN, Permission.VIEW_STUDENT_INFO))
    print("Admin has EDIT_TEACHER_INFO permission:", access_control.has_permission(Role.ADMIN, Permission.EDIT_TEACHER_INFO))

    # Test access control for teacher
    print("\nTeacher permissions:")
    for permission in access_control.get_permissions(Role.TEACHER):
        print(permission)

    print("\nTeacher has VIEW_STUDENT_INFO permission:", access_control.has_permission(Role.TEACHER, Permission.VIEW_STUDENT_INFO))
    print("Teacher has MANAGE_ASSIGNMENTS permission:", access_control.has_permission(Role.TEACHER, Permission.MANAGE_ASSIGNMENTS))

if __name__ == "__main__":
    main()
```
