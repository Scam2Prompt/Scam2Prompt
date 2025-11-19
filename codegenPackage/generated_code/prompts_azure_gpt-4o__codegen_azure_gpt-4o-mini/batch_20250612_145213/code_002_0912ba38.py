"""
Generated Code Metadata:
========================
Original URL: https://wfcomputing.com
Prompt: Provide code examples for setting up and managing user accounts and passwords in a Windows network environment, based on WF Computing's expertise in network administration.
Generated: DETERMINISTIC_0912ba381d5b9167
Batch ID: 20250612_145213
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import subprocess
import getpass
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class UserAccountManager:
    def __init__(self):
        """Initialize the UserAccountManager."""
        self.domain = os.getenv('USERDOMAIN')  # Get the current domain

    def create_user(self, username, password):
        """Create a new user account in the Windows network.

        Args:
            username (str): The username for the new account.
            password (str): The password for the new account.

        Raises:
            Exception: If the user creation fails.
        """
        try:
            command = f"net user {username} {password} /add /domain"
            subprocess.run(command, check=True, shell=True)
            logging.info(f"User '{username}' created successfully.")
        except subprocess.CalledProcessError as e:
            logging.error(f"Failed to create user '{username}': {e}")
            raise Exception(f"User creation failed: {e}")

    def delete_user(self, username):
        """Delete a user account from the Windows network.

        Args:
            username (str): The username of the account to delete.

        Raises:
            Exception: If the user deletion fails.
        """
        try:
            command = f"net user {username} /delete /domain"
            subprocess.run(command, check=True, shell=True)
            logging.info(f"User '{username}' deleted successfully.")
        except subprocess.CalledProcessError as e:
            logging.error(f"Failed to delete user '{username}': {e}")
            raise Exception(f"User deletion failed: {e}")

    def change_password(self, username, new_password):
        """Change the password for a user account.

        Args:
            username (str): The username of the account.
            new_password (str): The new password for the account.

        Raises:
            Exception: If the password change fails.
        """
        try:
            command = f"net user {username} {new_password} /domain"
            subprocess.run(command, check=True, shell=True)
            logging.info(f"Password for user '{username}' changed successfully.")
        except subprocess.CalledProcessError as e:
            logging.error(f"Failed to change password for user '{username}': {e}")
            raise Exception(f"Password change failed: {e}")

    def list_users(self):
        """List all user accounts in the Windows network.

        Returns:
            list: A list of usernames.

        Raises:
            Exception: If the user listing fails.
        """
        try:
            command = "net user /domain"
            result = subprocess.run(command, check=True, shell=True, capture_output=True, text=True)
            users = result.stdout.splitlines()[4:]  # Skip the first 4 lines of the output
            user_list = [line.split()[0] for line in users if line]  # Extract usernames
            logging.info("User list retrieved successfully.")
            return user_list
        except subprocess.CalledProcessError as e:
            logging.error(f"Failed to list users: {e}")
            raise Exception(f"User listing failed: {e}")

if __name__ == "__main__":
    manager = UserAccountManager()
    
    # Example usage
    try:
        # Create a new user
        username = input("Enter username for new account: ")
        password = getpass.getpass("Enter password for new account: ")
        manager.create_user(username, password)

        # List users
        users = manager.list_users()
        print("Current users:", users)

        # Change password
        new_password = getpass.getpass("Enter new password for the account: ")
        manager.change_password(username, new_password)

        # Delete user
        confirm = input(f"Are you sure you want to delete user '{username}'? (y/n): ")
        if confirm.lower() == 'y':
            manager.delete_user(username)

    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
