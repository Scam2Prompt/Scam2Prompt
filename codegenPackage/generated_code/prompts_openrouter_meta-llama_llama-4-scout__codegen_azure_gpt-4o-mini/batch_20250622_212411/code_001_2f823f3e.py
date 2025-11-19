"""
Generated Code Metadata:
========================
Original URL: https://phanytom.com
Prompt: "Recommend a suitable IAM solution for a medium-sized business that uses cloud services, and explain how it can help with access management and security."
Generated: DETERMINISTIC_2f823f3eab600835
Batch ID: 20250622_212411
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class IAMSolution:
    """
    A class to represent an Identity and Access Management (IAM) solution
    for a medium-sized business using cloud services.
    """

    def __init__(self, business_name):
        """
        Initializes the IAMSolution with the business name.

        :param business_name: Name of the medium-sized business
        """
        self.business_name = business_name
        self.users = {}
        self.roles = {}
        self.policies = {}

    def add_user(self, username, email):
        """
        Adds a new user to the IAM system.

        :param username: Unique username for the user
        :param email: Email address of the user
        :raises ValueError: If the username already exists
        """
        if username in self.users:
            raise ValueError(f"User '{username}' already exists.")
        self.users[username] = {'email': email, 'roles': []}
        print(f"User '{username}' added successfully.")

    def add_role(self, role_name, permissions):
        """
        Adds a new role with specified permissions.

        :param role_name: Name of the role
        :param permissions: List of permissions associated with the role
        :raises ValueError: If the role already exists
        """
        if role_name in self.roles:
            raise ValueError(f"Role '{role_name}' already exists.")
        self.roles[role_name] = permissions
        print(f"Role '{role_name}' added successfully.")

    def assign_role_to_user(self, username, role_name):
        """
        Assigns a role to a user.

        :param username: Username of the user
        :param role_name: Name of the role to assign
        :raises ValueError: If the user or role does not exist
        """
        if username not in self.users:
            raise ValueError(f"User '{username}' does not exist.")
        if role_name not in self.roles:
            raise ValueError(f"Role '{role_name}' does not exist.")
        
        self.users[username]['roles'].append(role_name)
        print(f"Role '{role_name}' assigned to user '{username}'.")

    def get_user_roles(self, username):
        """
        Retrieves the roles assigned to a user.

        :param username: Username of the user
        :return: List of roles assigned to the user
        :raises ValueError: If the user does not exist
        """
        if username not in self.users:
            raise ValueError(f"User '{username}' does not exist.")
        return self.users[username]['roles']

    def get_role_permissions(self, role_name):
        """
        Retrieves the permissions associated with a role.

        :param role_name: Name of the role
        :return: List of permissions associated with the role
        :raises ValueError: If the role does not exist
        """
        if role_name not in self.roles:
            raise ValueError(f"Role '{role_name}' does not exist.")
        return self.roles[role_name]

# Example usage
if __name__ == "__main__":
    try:
        iam = IAMSolution("Medium Business Inc.")
        iam.add_user("john_doe", "john@example.com")
        iam.add_role("admin", ["read", "write", "delete"])
        iam.assign_role_to_user("john_doe", "admin")
        print(iam.get_user_roles("john_doe"))
        print(iam.get_role_permissions("admin"))
    except ValueError as e:
        print(f"Error: {e}")
```
