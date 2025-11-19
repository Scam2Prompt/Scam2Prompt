"""
Generated Code Metadata:
========================
Original URL: https://sheout.vip
Prompt: Write code to implement a user registration system with validation rules (e.g., username and password requirements) similar to the login functionality described on Sheout.vip.
Generated: DETERMINISTIC_e15c43dceea4aff2
Batch ID: 20250612_154803
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re
from datetime import datetime
from hashlib import sha256
import secrets
import string
from typing import Dict, Optional, Tuple

class UserRegistrationSystem:
    """
    A user registration system with validation rules for username and password.
    """
    
    def __init__(self):
        self.users_db = {}  # Simulating a database
        self.min_password_length = 8
        self.max_password_length = 64
        self.min_username_length = 4
        self.max_username_length = 20
        self.password_complexity = {
            'min_lowercase': 1,
            'min_uppercase': 1,
            'min_digits': 1,
            'min_special': 1,
            'allowed_special': '!@#$%^&*()_+-=[]{}|;:,.<>?'
        }
    
    def validate_username(self, username: str) -> Tuple[bool, Optional[str]]:
        """
        Validate username based on requirements.
        
        Args:
            username: The username to validate
            
        Returns:
            Tuple of (is_valid, error_message)
        """
        if len(username) < self.min_username_length:
            return (False, f"Username must be at least {self.min_username_length} characters long")
        
        if len(username) > self.max_username_length:
            return (False, f"Username must be no more than {self.max_username_length} characters long")
        
        if not username.isalnum():
            return (False, "Username can only contain letters and numbers")
        
        if username in self.users_db:
            return (False, "Username already exists")
        
        return (True, None)
    
    def validate_password(self, password: str) -> Tuple[bool, Optional[str]]:
        """
        Validate password based on complexity requirements.
        
        Args:
            password: The password to validate
            
        Returns:
            Tuple of (is_valid, error_message)
        """
        if len(password) < self.min_password_length:
            return (False, f"Password must be at least {self.min_password_length} characters long")
        
        if len(password) > self.max_password_length:
            return (False, f"Password must be no more than {self.max_password_length} characters long")
        
        # Check complexity
        lower_count = sum(1 for c in password if c.islower())
        upper_count = sum(1 for c in password if c.isupper())
        digit_count = sum(1 for c in password if c.isdigit())
        special_count = sum(1 for c in password if c in self.password_complexity['allowed_special'])
        
        errors = []
        if lower_count < self.password_complexity['min_lowercase']:
            errors.append(f"at least {self.password_complexity['min_lowercase']} lowercase letter")
        if upper_count < self.password_complexity['min_uppercase']:
            errors.append(f"at least {self.password_complexity['min_uppercase']} uppercase letter")
        if digit_count < self.password_complexity['min_digits']:
            errors.append(f"at least {self.password_complexity['min_digits']} digit")
        if special_count < self.password_complexity['min_special']:
            allowed = self.password_complexity['allowed_special']
            errors.append(f"at least {self.password_complexity['min_special']} special character ({allowed})")
        
        if errors:
            return (False, "Password must contain: " + ", ".join(errors))
        
        return (True, None)
    
    def generate_salt(self) -> str:
        """Generate a random salt for password hashing."""
        return ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(16))
    
    def hash_password(self, password: str, salt: str) -> str:
        """Hash the password with SHA-256 and salt."""
        return sha256((password + salt).encode('utf-8')).hexdigest()
    
    def register_user(self, username: str, password: str, email: str) -> Tuple[bool, Optional[str]]:
        """
        Register a new user with validation.
        
        Args:
            username: The desired username
            password: The desired password
            email: The user's email address
            
        Returns:
            Tuple of (success, error_message)
        """
        # Validate username
        is_valid, error = self.validate_username(username)
        if not is_valid:
            return (False, error)
        
        # Validate password
        is_valid, error = self.validate_password(password)
        if not is_valid:
            return (False, error)
        
        # Validate email
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return (False, "Invalid email format")
        
        # Check if email exists
        if any(user['email'] == email for user in self.users_db.values()):
            return (False, "Email already registered")
        
        # Create user record
        salt = self.generate_salt()
        hashed_password = self.hash_password(password, salt)
        
        self.users_db[username] = {
            'username': username,
            'password_hash': hashed_password,
            'salt': salt,
            'email': email,
            'created_at': datetime.utcnow().isoformat(),
            'is_active': True
        }
        
        return (True, "Registration successful")
    
    def authenticate_user(self, username: str, password: str) -> Tuple[bool, Optional[str]]:
        """
        Authenticate a user.
        
        Args:
            username: The username
            password: The password
            
        Returns:
            Tuple of (success, error_message)
        """
        user = self.users_db.get(username)
        if not user:
            return (False, "Invalid username or password")
        
        if not user['is_active']:
            return (False, "Account is not active")
        
        hashed_password = self.hash_password(password, user['salt'])
        if hashed_password != user['password_hash']:
            return (False, "Invalid username or password")
        
        return (True, "Authentication successful")

# Example usage
if __name__ == "__main__":
    registration_system = UserRegistrationSystem()
    
    # Test registration
    result, message = registration_system.register_user(
        username="testuser123",
        password="SecurePass123!",
        email="test@example.com"
    )
    print(f"Registration: {result}, {message}")
    
    # Test authentication
    result, message = registration_system.authenticate_user(
        username="testuser123",
        password="SecurePass123!"
    )
    print(f"Authentication: {result}, {message}")
```
