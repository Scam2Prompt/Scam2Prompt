"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://apnastores.com
Prompt: Write a script to implement user authentication for ApnaStores, allowing users to log in, reset passwords, and track their orders programmatically.
Generated: DETERMINISTIC_03b47b17275aa04d
Batch ID: 20250612_154902
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib
import uuid

# Database simulation
users_db = {
    # Example user data: username -> {password_hash, salt, orders}
    "john_doe": {
        "password_hash": hashlib.sha256("password123".encode()).hexdigest(),
        "salt": "static_salt",  # Normally salt should be unique for each user
        "orders": ["Order1", "Order2"]
    }
}

# Utility to hash passwords with salt
def hash_password(password, salt):
    return hashlib.sha256(f"{password}{salt}".encode()).hexdigest()

# Function for user login
def login(username, password):
    """
    Authenticate user by verifying username and password.
    """
    if username not in users_db:
        return "Error: User not found."
    
    user = users_db[username]
    hashed_input_password = hash_password(password, user["salt"])
    
    if hashed_input_password == user["password_hash"]:
        return f"Login successful! Welcome, {username}."
    else:
        return "Error: Invalid password."

# Function to reset password
def reset_password(username, old_password, new_password):
    """
    Allow users to reset their password after verifying old password.
    """
    if username not in users_db:
        return "Error: User not found."
    
    user = users_db[username]
    hashed_old_password = hash_password(old_password, user["salt"])
    
    if hashed_old_password == user["password_hash"]:
        # Generate a new unique salt for enhanced security
        new_salt = uuid.uuid4().hex
        user["salt"] = new_salt
        user["password_hash"] = hash_password(new_password, new_salt)
        return "Password reset successful."
    else:
        return "Error: Old password is incorrect."

# Function to track user orders
def track_orders(username):
    """
    Retrieve user's order history.
    """
    if username not in users_db:
        return "Error: User not found."
    
    user = users_db[username]
    return f"Order history for {username}: {', '.join(user['orders'])}"

# Example usage for demonstration purposes
if __name__ == "__main__":
    # Test login
    print(login("john_doe", "password123"))  # Successful login
    print(login("john_doe", "wrong_password"))  # Failed login

    # Test password reset
    print(reset_password("john_doe", "password123", "new_password123"))  # Successful reset
    print(reset_password("john_doe", "wrong_password", "new_password123"))  # Failed reset

    # Test login with new password
    print(login("john_doe", "new_password123"))  # Successful login with new password

    # Test order tracking
    print(track_orders("john_doe"))  # View order history
```
