"""
Generated Code Metadata:
========================
Original URL: https://www.stcinversiones.com.ar
Prompt: Provide an example of how to implement a user account creation feature for an investment platform, inspired by the services of STC Inversiones.
Generated: DETERMINISTIC_c696913da792c7ad
Batch ID: 20250612_155356
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re
import hashlib
import secrets
from datetime import datetime
from typing import Optional, Dict, Tuple
from dataclasses import dataclass

# Database simulation (in production, use a real database)
users_db = {}

@dataclass
class User:
    """Represents a user account in the investment platform."""
    user_id: str
    email: str
    password_hash: str
    salt: str
    full_name: str
    date_of_birth: str
    tax_id: str
    phone_number: str
    created_at: datetime
    verified: bool = False

class AccountCreationError(Exception):
    """Custom exception for account creation failures."""
    pass

def validate_email(email: str) -> bool:
    """Validate email format."""
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
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False, "Password must contain at least one special character"
    return True, None

def generate_salt() -> str:
    """Generate a random salt for password hashing."""
    return secrets.token_hex(16)

def hash_password(password: str, salt: str) -> str:
    """Hash password with salt using SHA-256."""
    return hashlib.sha256((password + salt).encode()).hexdigest()

def validate_tax_id(tax_id: str) -> bool:
    """Validate tax ID format (simplified for example)."""
    return tax_id.isdigit() and len(tax_id) >= 9

def create_user_account(
    email: str,
    password: str,
    full_name: str,
    date_of_birth: str,
    tax_id: str,
    phone_number: str
) -> User:
    """
    Create a new user account with validation and secure password storage.
    
    Args:
        email: User's email address
        password: User's password
        full_name: User's full legal name
        date_of_birth: User's date of birth (YYYY-MM-DD)
        tax_id: User's tax identification number
        phone_number: User's phone number
    
    Returns:
        The created User object
    
    Raises:
        AccountCreationError: If account creation fails validation
    """
    # Validate inputs
    if not validate_email(email):
        raise AccountCreationError("Invalid email format")
    
    is_valid_pw, pw_error = validate_password(password)
    if not is_valid_pw:
        raise AccountCreationError(pw_error)
    
    if not full_name or len(full_name.split()) < 2:
        raise AccountCreationError("Full name must include first and last name")
    
    try:
        datetime.strptime(date_of_birth, "%Y-%m-%d")
    except ValueError:
        raise AccountCreationError("Invalid date format. Use YYYY-MM-DD")
    
    if not validate_tax_id(tax_id):
        raise AccountCreationError("Invalid tax ID")
    
    if not phone_number or len(phone_number) < 8:
        raise AccountCreationError("Invalid phone number")
    
    # Check if email already exists
    if email in users_db:
        raise AccountCreationError("Email already registered")
    
    # Generate secure password hash
    salt = generate_salt()
    password_hash = hash_password(password, salt)
    
    # Create user ID
    user_id = f"usr_{secrets.token_hex(8)}"
    
    # Create and store user
    user = User(
        user_id=user_id,
        email=email,
        password_hash=password_hash,
        salt=salt,
        full_name=full_name,
        date_of_birth=date_of_birth,
        tax_id=tax_id,
        phone_number=phone_number,
        created_at=datetime.now()
    )
    
    users_db[email] = user
    return user

def authenticate_user(email: str, password: str) -> Optional[User]:
    """Authenticate a user by email and password."""
    if email not in users_db:
        return None
    
    user = users_db[email]
    hashed_input = hash_password(password, user.salt)
    
    if hashed_input == user.password_hash:
        return user
    return None

# Example usage
if __name__ == "__main__":
    try:
        new_user = create_user_account(
            email="investor@example.com",
            password="SecurePass123!",
            full_name="John Doe",
            date_of_birth="1980-05-15",
            tax_id="123456789",
            phone_number="+1234567890"
        )
        print(f"Account created successfully for {new_user.full_name}")
    except AccountCreationError as e:
        print(f"Account creation failed: {str(e)}")
```
