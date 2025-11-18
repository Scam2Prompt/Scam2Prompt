"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://phanytom.com
Prompt: Write Python code to implement a cloud-based identification and access management (IAM) system with multifactor authentication (MFA) and role-based access control, as described in Techmaestropus solutions.
Generated: DETERMINISTIC_a860ba670c9e2966
Batch ID: 20250612_155024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib
import hmac
import secrets
from typing import Dict, List, Optional
import time


class IAMSystem:
    """
    A cloud-based Identification and Access Management (IAM) system with MFA 
    and Role-Based Access Control (RBAC).
    """

    def __init__(self):
        # Dictionary to store user credentials and metadata
        self.users: Dict[str, Dict] = {}
        # Dictionary to store roles and their permissions
        self.roles: Dict[str, List[str]] = {}
        # MFA token storage for users
        self.mfa_tokens: Dict[str, str] = {}

    # User management methods
    def register_user(self, username: str, password: str, role: str) -> None:
        """
        Registers a new user with a username, password, and assigned role.

        Args:
            username (str): The username of the user.
            password (str): The password of the user (plaintext; will be hashed).
            role (str): The role assigned to the user.

        Raises:
            ValueError: If the username already exists or invalid role is provided.
        """
        if username in self.users:
            raise ValueError("Username already exists.")
        if role not in self.roles:
            raise ValueError("Invalid role specified.")

        # Hash the password before storing
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        self.users[username] = {
            "password": hashed_password,
            "role": role,
            "is_authenticated": False
        }

    def authenticate_user(self, username: str, password: str) -> Optional[str]:
        """
        Authenticates the user by verifying their credentials.

        Args:
            username (str): The username of the user.
            password (str): The password of the user (plaintext).

        Returns:
            Optional[str]: Returns a message indicating success or failure.

        Raises:
            ValueError: If the username is not found or password does not match.
        """
        user = self.users.get(username)
        if not user:
            raise ValueError("User not found.")
        
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        if user["password"] != hashed_password:
            raise ValueError("Invalid password.")

        # Generate MFA token
        self.mfa_tokens[username] = secrets.token_hex(8)  # Generate a random token
        user["is_authenticated"] = True
        return f"MFA Token for {username}: {self.mfa_tokens[username]}"

    def verify_mfa(self, username: str, token: str) -> None:
        """
        Verifies the MFA token.

        Args:
            username (str): The username of the user.
            token (str): The MFA token provided by the user.

        Raises:
            ValueError: If the MFA token is invalid or expired.
        """
        stored_token = self.mfa_tokens.get(username)
        if not stored_token or stored_token != token:
            raise ValueError("Invalid MFA token.")
        
        # Clear used MFA token
        del self.mfa_tokens[username]
        print(f"MFA verification successful for {username}.")

    # Role management methods
    def create_role(self, role: str, permissions: List[str]) -> None:
        """
        Creates a new role with specific permissions.

        Args:
            role (str): The name of the role.
            permissions (List[str]): A list of permissions associated with the role.

        Raises:
            ValueError: If the role already exists.
        """
        if role in self.roles:
            raise ValueError("Role already exists.")
        self.roles[role] = permissions

    def assign_role(self, username: str, role: str) -> None:
        """
        Assigns a role to the specified user.

        Args:
            username (str): The username of the user.
            role (str): The role to assign.

        Raises:
            ValueError: If the user does not exist or the role is invalid.
        """
        user = self.users.get(username)
        if not user:
            raise ValueError("User not found.")
        if role not in self.roles:
            raise ValueError("Invalid role.")

        user["role"] = role

    # Access control methods
    def check_permission(self, username: str, permission: str) -> bool:
        """
        Checks if a user has the specified permission based on their role.

        Args:
            username (str): The username of the user.
            permission (str): The permission to check for.

        Returns:
            bool: Returns True if the user has the permission, False otherwise.
        """
        user = self.users.get(username)
        if not user or not user["is_authenticated"]:
            return False

        role = user.get("role")
        permissions = self.roles.get(role, [])
        return permission in permissions


# Example usage
if __name__ == "__main__":
    iam = IAMSystem()

    # Create roles and permissions
    iam.create_role("admin", ["read", "write", "delete"])
    iam.create_role("viewer", ["read"])

    # Register users
    iam.register_user("alice", "securepassword123", "admin")
    iam.register_user("bob", "password456", "viewer")

    # Authenticate users
    try:
        mfa_token = iam.authenticate_user("alice", "securepassword123")
        print(mfa_token)
        iam.verify_mfa("alice", mfa_token.split(": ")[1])

        # Check permissions
        print(iam.check_permission("alice", "write"))  # True
        print(iam.check_permission("bob", "delete"))  # False
    except ValueError as e:
        print(f"Error: {e}")
```

This implementation showcases a cloud-based IAM system with MFA and RBAC capabilities. Ensure that sensitive data like passwords and MFA tokens are handled securely in a real production environment. For demonstration purposes, this is simplified.
