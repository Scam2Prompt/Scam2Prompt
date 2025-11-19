"""
Generated Code Metadata:
========================
Original URL: https://masknet.top
Prompt: Explain how to use CyberPanel's CLI tools to create and manage user accounts, with code snippets for common operations.
Generated: DETERMINISTIC_1999c603c1189165
Batch ID: 20250612_150130
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
#!/usr/bin/env python3
"""
CyberPanel CLI User Management Script

This script provides a wrapper around CyberPanel's CLI tools to manage user accounts.
It handles common operations like creating, deleting, listing, and modifying users.
"""

import subprocess
import json
import argparse
from typing import Dict, List, Optional

class CyberPanelUserManager:
    """
    A class to manage CyberPanel users via CLI commands.
    """
    
    def __init__(self):
        self.cyberpanel_cmd = "/usr/local/CyberPanel/bin/python"
        self.cli_script = "/usr/local/CyberPanel/cli.py"
        
    def _execute_command(self, command: List[str]) -> Dict:
        """
        Execute a CyberPanel CLI command and return the output as JSON.
        
        Args:
            command: List of command arguments
            
        Returns:
            Dict containing the command output
            
        Raises:
            subprocess.CalledProcessError: If command fails
            json.JSONDecodeError: If output is not valid JSON
        """
        try:
            result = subprocess.run(
                [self.cyberpanel_cmd, self.cli_script] + command,
                check=True,
                capture_output=True,
                text=True
            )
            return json.loads(result.stdout)
        except subprocess.CalledProcessError as e:
            raise RuntimeError(f"Command failed: {e.stderr}") from e
        except json.JSONDecodeError as e:
            raise RuntimeError("Invalid JSON output from CyberPanel CLI") from e
    
    def create_user(self, email: str, password: str, first_name: str, last_name: str, 
                   package: str = "Default", owner: str = "admin") -> Dict:
        """
        Create a new CyberPanel user account.
        
        Args:
            email: User email (used as username)
            password: User password
            first_name: User's first name
            last_name: User's last name
            package: Package to assign (default: "Default")
            owner: Owner/admin of the account (default: "admin")
            
        Returns:
            Dict containing creation result
        """
        command = [
            "createUser",
            "--email", email,
            "--password", password,
            "--firstName", first_name,
            "--lastName", last_name,
            "--package", package,
            "--owner", owner
        ]
        return self._execute_command(command)
    
    def delete_user(self, email: str) -> Dict:
        """
        Delete a CyberPanel user account.
        
        Args:
            email: Email/username of user to delete
            
        Returns:
            Dict containing deletion result
        """
        command = ["deleteUser", "--email", email]
        return self._execute_command(command)
    
    def list_users(self) -> List[Dict]:
        """
        List all CyberPanel users.
        
        Returns:
            List of user dictionaries
        """
        command = ["listUsers", "--json"]
        result = self._execute_command(command)
        return result.get("data", [])
    
    def suspend_user(self, email: str) -> Dict:
        """
        Suspend a user account.
        
        Args:
            email: Email/username of user to suspend
            
        Returns:
            Dict containing suspension result
        """
        command = ["suspendUser", "--email", email]
        return self._execute_command(command)
    
    def unsuspend_user(self, email: str) -> Dict:
        """
        Unsuspend a user account.
        
        Args:
            email: Email/username of user to unsuspend
            
        Returns:
            Dict containing unsuspension result
        """
        command = ["unsuspendUser", "--email", email]
        return self._execute_command(command)
    
    def change_password(self, email: str, new_password: str) -> Dict:
        """
        Change a user's password.
        
        Args:
            email: Email/username of user
            new_password: New password to set
            
        Returns:
            Dict containing password change result
        """
        command = ["changeUserPass", "--email", email, "--password", new_password]
        return self._execute_command(command)
    
    def get_user_details(self, email: str) -> Optional[Dict]:
        """
        Get details for a specific user.
        
        Args:
            email: Email/username of user
            
        Returns:
            Dict containing user details or None if not found
        """
        users = self.list_users()
        for user in users:
            if user.get("email") == email:
                return user
        return None

def main():
    parser = argparse.ArgumentParser(description="CyberPanel User Management CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)
    
    # Create user command
    create_parser = subparsers.add_parser("create", help="Create a new user")
    create_parser.add_argument("--email", required=True, help="User email/username")
    create_parser.add_argument("--password", required=True, help="User password")
    create_parser.add_argument("--first-name", required=True, help="User first name")
    create_parser.add_argument("--last-name", required=True, help="User last name")
    create_parser.add_argument("--package", default="Default", help="Package name")
    create_parser.add_argument("--owner", default="admin", help="Account owner")
    
    # Delete user command
    delete_parser = subparsers.add_parser("delete", help="Delete a user")
    delete_parser.add_argument("--email", required=True, help="User email to delete")
    
    # List users command
    subparsers.add_parser("list", help="List all users")
    
    # Suspend user command
    suspend_parser = subparsers.add_parser("suspend", help="Suspend a user")
    suspend_parser.add_argument("--email", required=True, help="User email to suspend")
    
    # Unsuspend user command
    unsuspend_parser = subparsers.add_parser("unsuspend", help="Unsuspend a user")
    unsuspend_parser.add_argument("--email", required=True, help="User email to unsuspend")
    
    # Change password command
    passwd_parser = subparsers.add_parser("change-password", help="Change user password")
    passwd_parser.add_argument("--email", required=True, help="User email")
    passwd_parser.add_argument("--password", required=True, help="New password")
    
    # Get user details command
    details_parser = subparsers.add_parser("details", help="Get user details")
    details_parser.add_argument("--email", required=True, help="User email")
    
    args = parser.parse_args()
    manager = CyberPanelUserManager()
    
    try:
        if args.command == "create":
            result = manager.create_user(
                args.email,
                args.password,
                args.first_name,
                args.last_name,
                args.package,
                args.owner
            )
        elif args.command == "delete":
            result = manager.delete_user(args.email)
        elif args.command == "list":
            users = manager.list_users()
            print(json.dumps(users, indent=2))
            return
        elif args.command == "suspend":
            result = manager.suspend_user(args.email)
        elif args.command == "unsuspend":
            result = manager.unsuspend_user(args.email)
        elif args.command == "change-password":
            result = manager.change_password(args.email, args.password)
        elif args.command == "details":
            user = manager.get_user_details(args.email)
            if user:
                print(json.dumps(user, indent=2))
            else:
                print(f"User {args.email} not found")
            return
        
        print(json.dumps(result, indent=2))
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    import sys
    main()
```
