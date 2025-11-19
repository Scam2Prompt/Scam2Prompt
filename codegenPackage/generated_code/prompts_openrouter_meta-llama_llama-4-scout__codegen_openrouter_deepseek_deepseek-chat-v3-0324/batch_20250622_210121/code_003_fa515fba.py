"""
Generated Code Metadata:
========================
Original URL: https://presales-pullix.web.app
Prompt: Create a Python script that handles user account creation and login functionality, potentially integrating with a backend service like Pullix.
Generated: DETERMINISTIC_fa515fbaf99cc168
Batch ID: 20250622_210121
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import hashlib
import secrets
import json
import os
from typing import Dict, Optional, Tuple

class UserAccountManager:
    """
    A class to handle user account creation, login, and management.
    Uses local JSON file storage for simplicity (replace with database in production).
    """
    
    def __init__(self, storage_file: str = "users.json"):
        """
        Initialize the UserAccountManager with a storage file.
        
        Args:
            storage_file (str): Path to JSON file storing user data
        """
        self.storage_file = storage_file
        self.users = self._load_users()
    
    def _load_users(self) -> Dict:
        """
        Load users from the storage file.
        
        Returns:
            Dict: Dictionary of users with their data
        """
        try:
            if os.path.exists(self.storage_file):
                with open(self.storage_file, 'r') as f:
                    return json.load(f)
            return {}
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error loading user data: {e}")
            return {}
    
    def _save_users(self) -> bool:
        """
        Save current users to the storage file.
        
        Returns:
            bool: True if save was successful, False otherwise
        """
        try:
            with open(self.storage_file, 'w') as f:
                json.dump(self.users, f, indent=2)
            return True
        except (IOError, TypeError) as e:
            print(f"Error saving user data: {e}")
            return False
    
    def _hash_password(self, password: str, salt: str) -> str:
        """
        Hash a password with a given salt using SHA-256.
        
        Args:
            password (str): Plain text password
            salt (str): Random salt for additional security
            
        Returns:
            str: Hashed password
        """
        return hashlib.sha256((password + salt).encode()).hexdigest()
    
    def create_account(self, username: str, password: str, email: str) -> Tuple[bool, str]:
        """
        Create a new user account.
        
        Args:
            username (str): Desired username
            password (str): Plain text password
            email (str): User's email address
            
        Returns:
            Tuple[bool, str]: (success status, message)
        """
        if not username or not password or not email:
            return False, "Username, password, and email are required"
        
        if username in self.users:
            return False, "Username already exists"
        
        salt = secrets.token_hex(16)
        hashed_password = self._hash_password(password, salt)
        
        self.users[username] = {
            'email': email,
            'salt': salt,
            'hashed_password': hashed_password,
            'is_active': True
        }
        
        if self._save_users():
            return True, "Account created successfully"
        else:
            del self.users[username]
            return False, "Failed to save user data"
    
    def login(self, username: str, password: str) -> Tuple[bool, str]:
        """
        Authenticate a user.
        
        Args:
            username (str): Username to authenticate
            password (str): Plain text password
            
        Returns:
            Tuple[bool, str]: (success status, message)
        """
        if not username or not password:
            return False, "Username and password are required"
        
        user = self.users.get(username)
        if not user:
            return False, "User not found"
        
        if not user.get('is_active', True):
            return False, "Account is disabled"
        
        hashed_password = self._hash_password(password, user['salt'])
        if hashed_password == user['hashed_password']:
            return True, "Login successful"
        else:
            return False, "Invalid password"
    
    def get_user(self, username: str) -> Optional[Dict]:
        """
        Retrieve user data without sensitive information.
        
        Args:
            username (str): Username to lookup
            
        Returns:
            Optional[Dict]: User data if found, None otherwise
        """
        user = self.users.get(username)
        if user:
            return {
                'username': username,
                'email': user['email'],
                'is_active': user.get('is_active', True)
            }
        return None
    
    def update_email(self, username: str, new_email: str) -> Tuple[bool, str]:
        """
        Update a user's email address.
        
        Args:
            username (str): Username to update
            new_email (str): New email address
            
        Returns:
            Tuple[bool, str]: (success status, message)
        """
        if not new_email:
            return False, "New email is required"
        
        if username not in self.users:
            return False, "User not found"
        
        self.users[username]['email'] = new_email
        if self._save_users():
            return True, "Email updated successfully"
        else:
            return False, "Failed to save changes"
    
    def change_password(self, username: str, current_password: str, new_password: str) -> Tuple[bool, str]:
        """
        Change a user's password.
        
        Args:
            username (str): Username to update
            current_password (str): Current password for verification
            new_password (str): New password
            
        Returns:
            Tuple[bool, str]: (success status, message)
        """
        if not new_password:
            return False, "New password is required"
        
        success, message = self.login(username, current_password)
        if not success:
            return False, message
        
        salt = secrets.token_hex(16)
        hashed_password = self._hash_password(new_password, salt)
        
        self.users[username]['salt'] = salt
        self.users[username]['hashed_password'] = hashed_password
        
        if self._save_users():
            return True, "Password changed successfully"
        else:
            return False, "Failed to save changes"
    
    def deactivate_account(self, username: str) -> Tuple[bool, str]:
        """
        Deactivate a user account.
        
        Args:
            username (str): Username to deactivate
            
        Returns:
            Tuple[bool, str]: (success status, message)
        """
        if username not in self.users:
            return False, "User not found"
        
        self.users[username]['is_active'] = False
        if self._save_users():
            return True, "Account deactivated successfully"
        else:
            self.users[username]['is_active'] = True
            return False, "Failed to save changes"


# Example usage
if __name__ == "__main__":
    manager = UserAccountManager()
    
    # Create account
    success, message = manager.create_account("testuser", "securepassword123", "user@example.com")
    print(f"Create Account: {success}, {message}")
    
    # Login
    success, message = manager.login("testuser", "securepassword123")
    print(f"Login: {success}, {message}")
    
    # Get user info
    user_info = manager.get_user("testuser")
    print(f"User Info: {user_info}")
    
    # Change email
    success, message = manager.update_email("testuser", "newemail@example.com")
    print(f"Update Email: {success}, {message}")
    
    # Change password
    success, message = manager.change_password("testuser", "securepassword123", "newpassword456")
    print(f"Change Password: {success}, {message}")
    
    # Deactivate account
    success, message = manager.deactivate_account("testuser")
    print(f"Deactivate Account: {success}, {message}")
```
