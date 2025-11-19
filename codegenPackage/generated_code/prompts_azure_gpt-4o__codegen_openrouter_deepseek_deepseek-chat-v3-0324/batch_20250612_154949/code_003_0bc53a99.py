"""
Generated Code Metadata:
========================
Original URL: https://ebrasilbrazz.blogspot.com
Prompt: Create a function to handle user login and registration for an e-commerce site, inspired by the "Login | Cadastre-se" feature on ebrasilbrazz.
Generated: DETERMINISTIC_0bc53a99f9e3021f
Batch ID: 20250612_154949
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import hashlib
import re
from datetime import datetime
from typing import Dict, Optional, Tuple

# Database simulation (in a real application, this would be a database connection)
users_db = {}

class User:
    def __init__(self, email: str, password_hash: str, name: str, registration_date: datetime):
        self.email = email
        self.password_hash = password_hash
        self.name = name
        self.registration_date = registration_date

def hash_password(password: str) -> str:
    """Hash a password using SHA-256 with a salt."""
    salt = "ecommerce_salt"  # In production, use a unique salt per user
    return hashlib.sha256((password + salt).encode()).hexdigest()

def validate_email(email: str) -> bool:
    """Validate email format using regex."""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def validate_password(password: str) -> Tuple[bool, Optional[str]]:
    """Validate password meets security requirements."""
    if len(password) < 8:
        return False, "Password must be at least 8 characters long"
    if not re.search(r'[A-Z]', password):
        return False, "Password must contain at least one uppercase letter"
    if not re.search(r'[a-z]', password):
        return False, "Password must contain at least one lowercase letter"
    if not re.search(r'[0-9]', password):
        return False, "Password must contain at least one digit"
    return True, None

def register_user(email: str, password: str, name: str) -> Tuple[bool, Optional[str]]:
    """Register a new user with email, password, and name."""
    # Validate inputs
    if not validate_email(email):
        return False, "Invalid email format"
    
    valid_password, password_msg = validate_password(password)
    if not valid_password:
        return False, password_msg
    
    if not name or len(name.strip()) < 2:
        return False, "Name must be at least 2 characters long"
    
    # Check if user already exists
    if email in users_db:
        return False, "Email already registered"
    
    # Create and store user
    password_hash = hash_password(password)
    users_db[email] = User(
        email=email,
        password_hash=password_hash,
        name=name.strip(),
        registration_date=datetime.now()
    )
    
    return True, "Registration successful"

def login_user(email: str, password: str) -> Tuple[bool, Optional[Dict], Optional[str]]:
    """Authenticate a user with email and password."""
    # Validate inputs
    if not validate_email(email):
        return False, None, "Invalid email format"
    
    if not password:
        return False, None, "Password cannot be empty"
    
    # Check if user exists
    user = users_db.get(email)
    if not user:
        return False, None, "User not found"
    
    # Verify password
    if user.password_hash != hash_password(password):
        return False, None, "Incorrect password"
    
    # Return user data (without sensitive information)
    user_data = {
        'email': user.email,
        'name': user.name,
        'registration_date': user.registration_date.isoformat()
    }
    
    return True, user_data, "Login successful"

# Example usage
if __name__ == "__main__":
    # Test registration
    success, message = register_user(
        email="test@example.com",
        password="SecurePass123",
        name="Test User"
    )
    print(f"Registration: {success}, {message}")
    
    # Test login
    success, user_data, message = login_user(
        email="test@example.com",
        password="SecurePass123"
    )
    print(f"Login: {success}, {user_data}, {message}")
```
