"""
Generated Code Metadata:
========================
Original URL: https://pooltyme.app
Prompt: Write a Python script to implement a collaborative pool maintenance logging system with user authentication, similar to Pooltyme.
Generated: DETERMINISTIC_efef0fcfab62cb04
Batch ID: 20250622_205053
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import hashlib
import json
import os
from datetime import datetime

# Constants
DATA_FILE = "pool_maintenance_logs.json"
USER_FILE = "users.json"

# Helper functions
def hash_password(password):
    """Hashes a password using SHA-256."""
    return hashlib.sha256(password.encode()).hexdigest()

def load_data(file_path):
    """Loads JSON data from a file."""
    if not os.path.exists(file_path):
        return {}
    with open(file_path, "r") as file:
        return json.load(file)

def save_data(file_path, data):
    """Saves JSON data to a file."""
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)

# User authentication
def register_user(username, password):
    """Registers a new user."""
    users = load_data(USER_FILE)
    if username in users:
        raise ValueError("Username already exists.")
    users[username] = hash_password(password)
    save_data(USER_FILE, users)

def authenticate_user(username, password):
    """Authenticates a user."""
    users = load_data(USER_FILE)
    if username not in users or users[username] != hash_password(password):
        raise ValueError("Invalid username or password.")
    return True

# Pool maintenance logging
def log_maintenance(username, action, notes):
    """Logs a maintenance action."""
    logs = load_data(DATA_FILE)
    log_entry = {
        "username": username,
        "action": action,
        "notes": notes,
        "timestamp": datetime.now().isoformat()
    }
    logs.setdefault("entries", []).append(log_entry)
    save_data(DATA_FILE, logs)

def view_logs():
    """Views all maintenance logs."""
    logs = load_data(DATA_FILE)
    return logs.get("entries", [])

# Main application
def main():
    """Main function to run the application."""
    print("Welcome to the Pool Maintenance Logging System!")
    while True:
        print("\nMenu:")
        print("1. Register")
        print("2. Login")
        print("3. Log Maintenance")
        print("4. View Logs")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        try:
            if choice == "1":
                username = input("Enter username: ")
                password = input("Enter password: ")
                register_user(username, password)
                print("User registered successfully!")
            elif choice == "2":
                username = input("Enter username: ")
                password = input("Enter password: ")
                authenticate_user(username, password)
                print("Login successful!")
            elif choice == "3":
                username = input("Enter username: ")
                password = input("Enter password: ")
                authenticate_user(username, password)
                action = input("Enter maintenance action (e.g., 'Cleaned filter'): ")
                notes = input("Enter additional notes: ")
                log_maintenance(username, action, notes)
                print("Maintenance logged successfully!")
            elif choice == "4":
                logs = view_logs()
                if not logs:
                    print("No logs found.")
                else:
                    print("Maintenance Logs:")
                    for log in logs:
                        print(f"{log['timestamp']} - {log['username']} - {log['action']} - {log['notes']}")
            elif choice == "5":
                print("Exiting the system. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

# Entry point
if __name__ == "__main__":
    main()
```
