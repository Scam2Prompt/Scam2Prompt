"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://case-review-coinbase.com
Prompt: What are best practices for managing user accounts to prevent suspensions in a web service?
Generated: DETERMINISTIC_918c42389ed4ea8b
Batch ID: 20250612_155805
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here’s production-ready Python code implementing best practices for managing user accounts to prevent suspensions in a web service. These principles include monitoring account activity, enforcing password policies, detecting suspicious behavior, and providing users with proactive notifications.

```python
import re
from datetime import datetime, timedelta

# Constants
PASSWORD_MIN_LENGTH = 8
PASSWORD_COMPLEXITY_REGEX = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
MAX_FAILED_LOGIN_ATTEMPTS = 5
ACCOUNT_LOCK_DURATION = timedelta(minutes=30)
INACTIVITY_THRESHOLD_DAYS = 90

# In-memory storage (replace with actual database in production)
users = {}
login_attempts = {}
locked_accounts = {}

# Error classes
class AccountLockedError(Exception):
    """Raised when an account is locked."""
    pass

class InvalidPasswordError(Exception):
    """Raised when a password does not meet complexity requirements."""
    pass

# Helper Functions
def enforce_password_policy(password: str) -> bool:
    """
    Enforces password complexity rules.
    """
    if len(password) < PASSWORD_MIN_LENGTH:
        raise InvalidPasswordError("Password is too short.")
    if not re.match(PASSWORD_COMPLEXITY_REGEX, password):
        raise InvalidPasswordError("Password does not meet complexity requirements.")
    return True

def is_account_locked(username: str) -> bool:
    """
    Checks if an account is locked due to repeated failed login attempts.
    """
    if username in locked_accounts:
        lock_time = locked_accounts[username]
        if datetime.now() < lock_time + ACCOUNT_LOCK_DURATION:
            return True
        else:
            # Unlock account after lock duration expires
            del locked_accounts[username]
    return False

def track_failed_login(username: str):
    """
    Tracks failed login attempts and locks account if necessary.
    """
    if username not in login_attempts:
        login_attempts[username] = 0
    login_attempts[username] += 1

    if login_attempts[username] >= MAX_FAILED_LOGIN_ATTEMPTS:
        locked_accounts[username] = datetime.now()
        raise AccountLockedError(f"Account for user '{username}' is locked due to repeated failed login attempts.")

def reset_failed_logins(username: str):
    """
    Resets failed login attempt counter after a successful login.
    """
    if username in login_attempts:
        del login_attempts[username]

def monitor_account_inactivity():
    """
    Identifies inactive accounts and sends notifications.
    """
    now = datetime.now()
    for username, user_data in users.items():
        last_active_date = user_data.get('last_active')
        if last_active_date and (now - last_active_date).days > INACTIVITY_THRESHOLD_DAYS:
            notify_user_of_inactivity(username)

def notify_user_of_inactivity(username: str):
    """
    Sends a proactive notification to the user about inactivity.
    """
    print(f"Notification: User '{username}', your account has been inactive for over {INACTIVITY_THRESHOLD_DAYS} days.")

# User Account Management
def create_user(username: str, password: str):
    """
    Creates a new user account with proper password validation.
    """
    if username in users:
        raise ValueError("Username already exists.")
    enforce_password_policy(password)
    users[username] = {
        'password': password,
        'last_active': datetime.now(),  # Record initial activity
        'created_at': datetime.now()
    }

def login(username: str, password: str):
    """
    Handles user login and manages failed login attempts.
    """
    if username not in users:
        raise ValueError("Invalid username or password.")
    
    if is_account_locked(username):
        raise AccountLockedError("Your account is temporarily locked. Please try again later.")
    
    user_data = users[username]
    if user_data['password'] == password:
        reset_failed_logins(username)
        user_data['last_active'] = datetime.now()  # Update last active timestamp
        print(f"Welcome back, {username}!")
    else:
        track_failed_login(username)
        raise ValueError("Invalid username or password.")

def change_password(username: str, old_password: str, new_password: str):
    """
    Allows a user to change their password securely.
    """
    if username not in users:
        raise ValueError("Invalid username.")
    
    user_data = users[username]
    if user_data['password'] != old_password:
        raise ValueError("Old password is incorrect.")
    
    enforce_password_policy(new_password)
    user_data['password'] = new_password
    print("Password changed successfully.")

# Example usage
if __name__ == '__main__':
    try:
        # Creating user accounts
        create_user('john_doe', 'StrongPassword1@')
        create_user('jane_doe', 'AnotherStrongPassword2$')

        # Logging in
        login('john_doe', 'StrongPassword1@')

        # Simulating failed logins
        try:
            login('john_doe', 'WrongPassword')
        except ValueError as e:
            print(e)

        # Changing password
        change_password('john_doe', 'StrongPassword1@', 'NewStrongPassword3@')

        # Detect inactive accounts
        monitor_account_inactivity()

    except Exception as e:
        print(f"Error: {e}")
```

This code includes robust error handling, adheres to best practices, and is well-documented with comments. Replace in-memory structures with appropriate database queries for a production environment.
