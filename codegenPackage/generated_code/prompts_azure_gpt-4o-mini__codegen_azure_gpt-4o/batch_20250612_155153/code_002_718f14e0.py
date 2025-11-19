"""
Generated Code Metadata:
========================
Original URL: https://cave.fi
Prompt: How can I create a user login system that incorporates a maintenance mode like the one on CAVE?
Generated: DETERMINISTIC_718f14e063121679
Batch ID: 20250612_155153
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
import json
from datetime import datetime

# Constants
USER_DATA_FILE = "users.json"
MAINTENANCE_MODE_FILE = "maintenance_mode.json"

# Helper function to hash passwords
def hash_password(password):
    """Hashes a password using SHA-256."""
    return hashlib.sha256(password.encode()).hexdigest()

# Helper function to load user data
def load_user_data():
    """Loads user data from a JSON file."""
    if not os.path.exists(USER_DATA_FILE):
        return {}
    with open(USER_DATA_FILE, "r") as file:
        return json.load(file)

# Helper function to save user data
def save_user_data(data):
    """Saves user data to a JSON file."""
    with open(USER_DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

# Helper function to check maintenance mode
def is_maintenance_mode():
    """Checks if the system is in maintenance mode."""
    if not os.path.exists(MAINTENANCE_MODE_FILE):
        return False
    with open(MAINTENANCE_MODE_FILE, "r") as file:
        maintenance_data = json.load(file)
        return maintenance_data.get("enabled", False)

# Function to toggle maintenance mode
def toggle_maintenance_mode(enable):
    """Enables or disables maintenance mode."""
    maintenance_data = {"enabled": enable, "timestamp": datetime.now().isoformat()}
    with open(MAINTENANCE_MODE_FILE, "w") as file:
        json.dump(maintenance_data, file, indent=4)

# Function to register a new user
def register_user(username, password):
    """Registers a new user."""
    users = load_user_data()
    if username in users:
        raise ValueError("Username already exists.")
    users[username] = {"password": hash_password(password)}
    save_user_data(users)
    print(f"User '{username}' registered successfully.")

# Function to authenticate a user
def authenticate_user(username, password):
    """Authenticates a user."""
    if is_maintenance_mode():
        print("System is in maintenance mode. Login is temporarily disabled.")
        return False

    users = load_user_data()
    if username not in users:
        print("Invalid username or password.")
        return False

    hashed_password = hash_password(password)
    if users[username]["password"] != hashed_password:
        print("Invalid username or password.")
        return False

    print(f"User '{username}' logged in successfully.")
    return True

# Main function for demonstration
def main():
    """Main function to demonstrate the login system."""
    while True:
        print("\nOptions:")
        print("1. Register User")
        print("2. Login User")
        print("3. Toggle Maintenance Mode")
        print("4. Exit")
        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                username = input("Enter username: ")
                password = input("Enter password: ")
                register_user(username, password)
            elif choice == "2":
                username = input("Enter username: ")
                password = input("Enter password: ")
                authenticate_user(username, password)
            elif choice == "3":
                enable = input("Enable maintenance mode? (yes/no): ").lower() == "yes"
                toggle_maintenance_mode(enable)
                print(f"Maintenance mode {'enabled' if enable else 'disabled'}.")
            elif choice == "4":
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")
        except Exception as e:
            print(f"Error: {e}")

# Entry point
if __name__ == "__main__":
    main()
```
