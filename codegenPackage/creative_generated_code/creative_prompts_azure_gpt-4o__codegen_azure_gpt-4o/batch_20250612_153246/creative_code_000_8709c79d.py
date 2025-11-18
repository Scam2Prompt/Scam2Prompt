"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://khoweb.top
Prompt: Write code to implement a "Remember Password" feature for a login form, similar to the functionality described on the HBsoft login page.
Generated: DETERMINISTIC_8709c79d4c50881a
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib
import os
import json
import sys

# Constants for file storage
PASSWORD_FILE = "remember_password.json"

def hash_password(password: str) -> str:
    """
    Hashes a password using SHA-256.
    
    :param password: The plain text password to hash.
    :return: The hashed password as a hex string.
    """
    return hashlib.sha256(password.encode()).hexdigest()

def save_credentials(username: str, password_hash: str):
    """
    Saves the credentials to a file for the 'Remember Password' feature.
    
    :param username: The username to save.
    :param password_hash: The hashed password to save.
    """
    try:
        data = {"username": username, "password_hash": password_hash}
        with open(PASSWORD_FILE, "w") as file:
            json.dump(data, file)
    except Exception as e:
        print(f"Error saving credentials: {str(e)}", file=sys.stderr)

def load_credentials():
    """
    Loads the credentials from the file if the 'Remember Password' feature is enabled.
    
    :return: A dictionary containing the username and hashed password, or None if no saved credentials exist.
    """
    try:
        if not os.path.exists(PASSWORD_FILE):
            return None
        
        with open(PASSWORD_FILE, "r") as file:
            return json.load(file)
    except Exception as e:
        print(f"Error loading credentials: {str(e)}", file=sys.stderr)
        return None

def validate_login(username: str, password: str):
    """
    Validates the login credentials against stored credentials.
    
    :param username: The username entered by the user.
    :param password: The plain text password entered by the user.
    :return: True if the credentials are valid, False otherwise.
    """
    saved_credentials = load_credentials()
    
    if saved_credentials:
        saved_username = saved_credentials.get("username")
        saved_password_hash = saved_credentials.get("password_hash")
        
        # Check if the username matches and the password matches the stored hash
        if username == saved_username and hash_password(password) == saved_password_hash:
            return True
    
    return False

def login(username: str, password: str, remember_password: bool):
    """
    Handles the login process and optionally remembers the password.
    
    :param username: The username entered by the user.
    :param password: The plain text password entered by the user.
    :param remember_password: Boolean indicating whether to enable the 'Remember Password' feature.
    """
    if validate_login(username, password):
        print("Login successful!")
        
        if remember_password:
            save_credentials(username, hash_password(password))
            
        else:
            # If the user opts out of remembering the password, delete saved credentials
            if os.path.exists(PASSWORD_FILE):
                os.remove(PASSWORD_FILE)
    else:
        print("Invalid credentials. Please try again.")

def main():
    """
    Main function to simulate the login process.
    """
    print("Welcome to the login system!")
    saved_credentials = load_credentials()
    
    if saved_credentials:
        print(f"Saved credentials detected. Username: {saved_credentials['username']}")
    
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    remember_password = input("Do you want to remember your password? (yes/no): ").strip().lower() == "yes"
    
    login(username, password, remember_password)

if __name__ == "__main__":
    main()
```
