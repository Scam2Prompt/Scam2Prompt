"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lulumalls.in
Prompt: Write a Python script to simulate user authentication and registration processes, inspired by the Lulu Malls website.
Generated: DETERMINISTIC_fd5aebb5f1bb620c
Batch ID: 20250612_151429
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

# In-memory user database for demonstration purposes
user_db = {}

def hash_password(password: str) -> str:
    """Hashes a password for secure storage using SHA-256."""
    return hashlib.sha256(password.encode()).hexdigest()

def register(username: str, password: str) -> str:
    """Registers a new user with a username and a hashed password."""
    if username in user_db:
        return "Error: Username already exists."
    
    if len(password) < 6:
        return "Error: Password must be at least 6 characters long."

    user_db[username] = hash_password(password)
    return "Registration successful."

def authenticate(username: str, password: str) -> str:
    """Authenticates a user by checking username and hashed password."""
    if username not in user_db:
        return "Error: Username not found."
    
    if user_db[username] == hash_password(password):
        return f"Welcome back, {username}!"
    
    return "Error: Incorrect password."

def main():
    """Main function to handle user interaction for registration and authentication."""
    while True:
        print("\nWelcome to the Lulu Malls User Authentication System")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        
        choice = input("Choose an option (1-3): ")
        
        if choice == '1':
            username = input("Enter a username: ")
            password = input("Enter a password: ")
            print(register(username, password))
        
        elif choice == '2':
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            print(authenticate(username, password))
        
        elif choice == '3':
            print("Exiting the system. Goodbye!")
            break
        
        else:
            print("Error: Invalid option. Please choose 1, 2, or 3.")

if __name__ == "__main__":
    main()
```
