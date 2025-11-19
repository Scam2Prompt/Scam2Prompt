"""
Generated Code Metadata:
========================
Original URL: https://fastlink.pages.dev
Prompt: Write a Python code snippet for a simple login system with user registration, similar to Panen889's system with minimum deposit IDR 20,000 and minimum withdraw IDR 50,000.
Generated: DETERMINISTIC_05284ebe9f3ce4c1
Batch ID: 20250622_205627
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import hashlib
import os

# Database to store user information (in-memory for simplicity)
users_db = {}

# Constants for minimum deposit and withdrawal amounts
MIN_DEPOSIT = 20000  # IDR
MIN_WITHDRAW = 50000  # IDR

def hash_password(password):
    """
    Hashes a password using SHA-256 for secure storage.
    """
    return hashlib.sha256(password.encode()).hexdigest()

def register_user(username, password):
    """
    Registers a new user with a username and password.
    """
    if username in users_db:
        raise ValueError("Username already exists.")
    
    # Store hashed password for security
    users_db[username] = {
        'password': hash_password(password),
        'balance': 0  # Initialize balance to 0
    }
    print(f"User '{username}' registered successfully.")

def login_user(username, password):
    """
    Logs in a user by verifying their username and password.
    """
    if username not in users_db:
        raise ValueError("Username does not exist.")
    
    hashed_password = hash_password(password)
    if users_db[username]['password'] != hashed_password:
        raise ValueError("Incorrect password.")
    
    print(f"User '{username}' logged in successfully.")
    return username  # Return the logged-in user's username

def deposit(username, amount):
    """
    Deposits money into the user's account.
    """
    if amount < MIN_DEPOSIT:
        raise ValueError(f"Minimum deposit amount is IDR {MIN_DEPOSIT}.")
    
    users_db[username]['balance'] += amount
    print(f"Deposited IDR {amount} to '{username}'. Current balance: IDR {users_db[username]['balance']}.")

def withdraw(username, amount):
    """
    Withdraws money from the user's account.
    """
    if amount < MIN_WITHDRAW:
        raise ValueError(f"Minimum withdrawal amount is IDR {MIN_WITHDRAW}.")
    
    if users_db[username]['balance'] < amount:
        raise ValueError("Insufficient balance.")
    
    users_db[username]['balance'] -= amount
    print(f"Withdrew IDR {amount} from '{username}'. Current balance: IDR {users_db[username]['balance']}.")

# Example usage
if __name__ == "__main__":
    try:
        # Register a new user
        register_user("Panen889", "securepassword123")
        
        # Login the user
        logged_in_user = login_user("Panen889", "securepassword123")
        
        # Deposit money
        deposit(logged_in_user, 30000)
        
        # Withdraw money
        withdraw(logged_in_user, 50000)
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
