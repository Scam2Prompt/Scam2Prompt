"""
Generated Code Metadata:
========================
Original URL: https://boxes-lives.web.app
Prompt: Generate code to create a simple whitelist application that requires user authentication and authorization.
Generated: DETERMINISTIC_c1f5501a26c117b5
Batch ID: 20250622_205751
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

# In-memory storage for users and whitelist
users = {}
whitelist = set()

# Function to hash passwords securely
def hash_password(password):
    salt = os.urandom(16)
    hashed = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    return salt, hashed

# Function to verify hashed passwords
def verify_password(stored_salt, stored_hash, password):
    hashed = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), stored_salt, 100000)
    return hashed == stored_hash

# Function to register a new user
def register_user(username, password):
    if username in users:
        raise ValueError("Username already exists.")
    salt, hashed_password = hash_password(password)
    users[username] = {'salt': salt, 'password': hashed_password}
    print(f"User '{username}' registered successfully.")

# Function to authenticate a user
def authenticate_user(username, password):
    if username not in users:
        raise ValueError("Invalid username or password.")
    stored_salt = users[username]['salt']
    stored_hash = users[username]['password']
    if verify_password(stored_salt, stored_hash, password):
        print(f"User '{username}' authenticated successfully.")
        return True
    else:
        raise ValueError("Invalid username or password.")

# Function to add an item to the whitelist
def add_to_whitelist(username, item):
    if username not in users:
        raise ValueError("User not found.")
    whitelist.add(item)
    print(f"Item '{item}' added to whitelist by user '{username}'.")

# Function to check if an item is in the whitelist
def is_whitelisted(item):
    return item in whitelist

# Main application loop
def main():
    print("Welcome to the Whitelist Application!")
    while True:
        try:
            print("\nOptions:")
            print("1. Register User")
            print("2. Authenticate User")
            print("3. Add to Whitelist")
            print("4. Check Whitelist")
            print("5. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                username = input("Enter username: ")
                password = input("Enter password: ")
                register_user(username, password)

            elif choice == '2':
                username = input("Enter username: ")
                password = input("Enter password: ")
                authenticate_user(username, password)

            elif choice == '3':
                username = input("Enter username: ")
                password = input("Enter password: ")
                if authenticate_user(username, password):
                    item = input("Enter item to whitelist: ")
                    add_to_whitelist(username, item)

            elif choice == '4':
                item = input("Enter item to check: ")
                if is_whitelisted(item):
                    print(f"Item '{item}' is whitelisted.")
                else:
                    print(f"Item '{item}' is not whitelisted.")

            elif choice == '5':
                print("Exiting application. Goodbye!")
                break

            else:
                print("Invalid choice. Please try again.")

        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

# Run the application
if __name__ == "__main__":
    main()
```
