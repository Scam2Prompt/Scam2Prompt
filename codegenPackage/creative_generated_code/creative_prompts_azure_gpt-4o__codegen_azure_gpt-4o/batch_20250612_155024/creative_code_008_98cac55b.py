"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://phanytom.com
Prompt: Write code to automate the assignment of access rights based on user roles in an IAM system, minimizing administrative errors, as described by Techmaestropus.
Generated: DETERMINISTIC_98cac55be6185b3b
Batch ID: 20250612_155024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

# Constants for roles and their associated access rights
ROLE_ACCESS_RIGHTS = {
    "admin": ["read", "write", "delete", "manage_users"],
    "editor": ["read", "write"],
    "viewer": ["read"],
}

# Mock database of users and roles
USER_DATABASE = {
    "user_001": "admin",
    "user_002": "editor",
    "user_003": "viewer",
    "user_004": None,  # Unassigned role
}

def assign_access_rights(users, roles_rights_mapping):
    """
    Assign access rights to users based on their roles.

    Args:
        users (dict): Dictionary of user IDs and their roles.
        roles_rights_mapping (dict): Mapping of roles to access rights.

    Returns:
        dict: Dictionary of user IDs and their assigned access rights.
    """
    user_access = {}

    for user_id, role in users.items():
        try:
            # If role is None or invalid, assign no access rights
            if not role or role not in roles_rights_mapping:
                user_access[user_id] = {"access_rights": [], "status": "Role not assigned or invalid"}
            else:
                # Assign access rights based on role
                user_access[user_id] = {"access_rights": roles_rights_mapping[role], "status": "Success"}
        except Exception as e:
            # Catch unexpected errors and log them
            user_access[user_id] = {"access_rights": [], "status": f"Error: {str(e)}"}

    return user_access


def main():
    """
    Main function to handle the automation of access rights assignment.
    """
    try:
        print("Automating access rights assignment...")
        
        # Assign access rights
        assigned_access = assign_access_rights(USER_DATABASE, ROLE_ACCESS_RIGHTS)

        # Output the results in a readable format
        print(json.dumps(assigned_access, indent=4))

        print("Access rights assignment completed.")
    except Exception as e:
        # Handle unexpected errors in the main function
        print(f"An unexpected error occurred: {str(e)}")


if __name__ == "__main__":
    main()
```
