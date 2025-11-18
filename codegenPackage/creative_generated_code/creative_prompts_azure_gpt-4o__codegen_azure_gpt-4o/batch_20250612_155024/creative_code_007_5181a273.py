"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://phanbtom.com
Prompt: Create a Python program to manage user access rights dynamically based on roles and conditions, integrating multifactor authentication (MFA) and access monitoring features similar to Techmaestropus's IAM system.
Generated: DETERMINISTIC_5181a2735843a1c8
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
import random
import string
import time
from functools import wraps

# Constants for MFA
MFA_TIMEOUT_SECONDS = 300  # MFA token expires after 5 minutes
ACCESS_LOG_FILE = "access_log.txt"

# Example roles and permissions
ROLES = {
    "admin": {"read", "write", "delete"},
    "editor": {"read", "write"},
    "viewer": {"read"},
}

# Example user data (simulated database)
USERS = {
    "alice": {"password": "securepassword", "role": "admin"},
    "bob": {"password": "strongpassword", "role": "editor"},
    "charlie": {"password": "viewerpassword", "role": "viewer"},
}

# MFA token storage
MFA_TOKENS = {}

# Utility: Hash password
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Utility: Generate MFA token
def generate_mfa_token():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

# Utility: Log access attempts
def log_access(user, action, status):
    with open(ACCESS_LOG_FILE, "a") as log_file:
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        log_file.write(f"{timestamp} | User: {user} | Action: {action} | Status: {status}\n")

# Decorator for access control
def access_control(required_permission):
    def decorator(func):
        @wraps(func)
        def wrapper(user, *args, **kwargs):
            if user not in USERS:
                log_access(user, func.__name__, "FAILED: User not found")
                raise PermissionError("User not found.")
            
            role = USERS[user]["role"]
            permissions = ROLES.get(role, set())
            if required_permission not in permissions:
                log_access(user, func.__name__, "FAILED: Permission denied")
                raise PermissionError("Permission denied.")
            
            return func(user, *args, **kwargs)
        return wrapper
    return decorator

# Function: Authenticate user with password and initiate MFA
def authenticate_user(username, password):
    if username not in USERS or hash_password(password) != hash_password(USERS[username]["password"]):
        log_access(username, "authenticate_user", "FAILED: Authentication failed")
        raise ValueError("Invalid username or password.")
    
    # Generate and store MFA token
    token = generate_mfa_token()
    MFA_TOKENS[username] = {
        "token": token,
        "expires_at": time.time() + MFA_TIMEOUT_SECONDS
    }
    log_access(username, "authenticate_user", "SUCCESS")
    print(f"MFA Token for {username}: {token}")
    return token

# Function: Verify MFA token
def verify_mfa(username, token):
    if username not in MFA_TOKENS:
        log_access(username, "verify_mfa", "FAILED: MFA token not found")
        raise ValueError("MFA token not found.")
    
    mfa_data = MFA_TOKENS[username]
    if time.time() > mfa_data["expires_at"]:
        del MFA_TOKENS[username]  # Remove expired token
        log_access(username, "verify_mfa", "FAILED: MFA token expired")
        raise ValueError("MFA token expired.")
    
    if token != mfa_data["token"]:
        log_access(username, "verify_mfa", "FAILED: Invalid MFA token")
        raise ValueError("Invalid MFA token.")
    
    del MFA_TOKENS[username]  # Token used successfully, delete it
    log_access(username, "verify_mfa", "SUCCESS")
    print(f"MFA Verified for {username}")
    return True

# Example: Restricted functions
@access_control("read")
def view_data(user):
    log_access(user, "view_data", "SUCCESS")
    return f"Data viewed by {user}."

@access_control("write")
def modify_data(user):
    log_access(user, "modify_data", "SUCCESS")
    return f"Data modified by {user}."

@access_control("delete")
def delete_data(user):
    log_access(user, "delete_data", "SUCCESS")
    return f"Data deleted by {user}."

# Example usage
if __name__ == "__main__":
    try:
        # Step 1: Authenticate user and get MFA token
        username = input("Enter username: ").strip()
        password = input("Enter password: ").strip()
        mfa_token = authenticate_user(username, password)
        
        # Step 2: Verify MFA token
        entered_token = input("Enter MFA token: ").strip()
        verify_mfa(username, entered_token)
        
        # Step 3: Perform actions based on access rights
        action = input("Enter action (view/modify/delete): ").strip().lower()
        if action == "view":
            print(view_data(username))
        elif action == "modify":
            print(modify_data(username))
        elif action == "delete":
            print(delete_data(username))
        else:
            print("Invalid action.")
    except Exception as e:
        print(f"Error: {e}")
```
