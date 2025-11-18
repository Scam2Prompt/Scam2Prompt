"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://spectre-group.limited
Prompt: Develop a program to enhance account security by implementing advanced access control as described in Spectre Group Limited's security features.
Generated: DETERMINISTIC_cf7bd86558d9a979
Batch ID: 20250612_153755
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Program to implement advanced access control for account security.
Features include role-based access control (RBAC), multi-factor authentication (MFA),
and account lockout after multiple failed login attempts.
"""

import hashlib
import time
import random
import string

# Constants
MAX_FAILED_ATTEMPTS = 5  # Lock account after 5 failed attempts
LOCKOUT_DURATION = 300  # Lock account for 300 seconds (5 minutes)
MFA_CODE_VALID_DURATION = 120  # MFA code valid for 120 seconds (2 minutes)

# Dummy user database
user_db = {
    "admin": {
        "password_hash": hashlib.sha256("secure_admin_password".encode()).hexdigest(),
        "role": "admin",
        "failed_attempts": 0,
        "lockout_until": 0,
        "mfa_code": None,
        "mfa_code_expiry": 0,
    },
    "user": {
        "password_hash": hashlib.sha256("secure_user_password".encode()).hexdigest(),
        "role": "user",
        "failed_attempts": 0,
        "lockout_until": 0,
        "mfa_code": None,
        "mfa_code_expiry": 0,
    },
}

# Role-based permissions
permissions = {
    "admin": ["read", "write", "delete"],
    "user": ["read"],
}

def generate_mfa_code():
    """Generate a random MFA code."""
    return ''.join(random.choices(string.digits, k=6))

def is_account_locked(username):
    """Check if an account is currently locked."""
    current_time = time.time()
    user = user_db.get(username)
    return user and current_time < user["lockout_until"]

def lock_account(username):
    """Lock the account for a specified duration."""
    user_db[username]["lockout_until"] = time.time() + LOCKOUT_DURATION

def authenticate(username, password):
    """
    Authenticate the user by verifying the username and password.
    Returns True if successful, otherwise False.
    """
    user = user_db.get(username)
    if not user:
        print("Invalid username.")
        return False

    if is_account_locked(username):
        print("Account is locked. Please try again later.")
        return False

    password_hash = hashlib.sha256(password.encode()).hexdigest()
    if password_hash == user["password_hash"]:
        user["failed_attempts"] = 0  # Reset failed attempts on successful login
        print("Password authentication successful.")
        return True
    else:
        user["failed_attempts"] += 1
        print("Invalid password.")
        if user["failed_attempts"] >= MAX_FAILED_ATTEMPTS:
            print("Account locked due to too many failed attempts.")
            lock_account(username)
        return False

def verify_mfa_code(username, mfa_code):
    """
    Verify the MFA code provided by the user.
    Returns True if successful, otherwise False.
    """
    user = user_db.get(username)
    if not user or not user["mfa_code"]:
        print("MFA not configured or invalid user.")
        return False

    current_time = time.time()
    if current_time > user["mfa_code_expiry"]:
        print("MFA code expired.")
        return False

    if mfa_code == user["mfa_code"]:
        print("MFA verification successful.")
        return True
    else:
        print("Invalid MFA code.")
        return False

def authorize(username, action):
    """
    Verify if the user is authorized to perform a specific action.
    Returns True if authorized, otherwise False.
    """
    user = user_db.get(username)
    if not user:
        print("Invalid username.")
        return False

    role = user["role"]
    if action in permissions.get(role, []):
        print(f"Authorization successful. {username} can perform '{action}'.")
        return True
    else:
        print(f"Authorization failed. {username} cannot perform '{action}'.")
        return False

def login(username, password):
    """
    Login process with password authentication and MFA.
    """
    if not authenticate(username, password):
        return False

    # Generate and send MFA code (for demo purposes, we display it)
    user_db[username]["mfa_code"] = generate_mfa_code()
    user_db[username]["mfa_code_expiry"] = time.time() + MFA_CODE_VALID_DURATION
    print(f"MFA Code for {username}: {user_db[username]['mfa_code']} (valid for 2 minutes)")

    mfa_code = input("Enter MFA Code: ")
    if not verify_mfa_code(username, mfa_code):
        return False

    print(f"{username} logged in successfully.")
    return True

# Example usage
if __name__ == "__main__":
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    if login(username, password):
        action = input("Enter action (read/write/delete): ").strip().lower()
        authorize(username, action)
```
