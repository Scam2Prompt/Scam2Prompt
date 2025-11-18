"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pork2.pages.dev
Prompt: Create a registration system for a cryptocurrency project that limits sign-ups to a specific time window, similar to the 48-hour registration period mentioned on the PorkCoin site.
Generated: DETERMINISTIC_090edb398eb3e76f
Batch ID: 20250612_151918
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime, timedelta
import json

# Configuration for the registration system
REGISTRATION_START = datetime(2023, 10, 1, 0, 0)  # Example start date and time
REGISTRATION_END = REGISTRATION_START + timedelta(hours=48)  # 48-hour registration window
USER_DATA_FILE = 'registered_users.json'

# Initialize user data storage
def initialize_user_data_storage():
    try:
        # Create an empty JSON file for user data if it doesn't exist
        with open(USER_DATA_FILE, 'r') as file:
            json.load(file)  # No action needed if the file exists and is valid
    except (FileNotFoundError, json.JSONDecodeError):
        with open(USER_DATA_FILE, 'w') as file:
            json.dump({}, file)  # Initialize with an empty JSON object

# Register a user
def register_user(username, email):
    """
    Registers a user if the registration window is active and the user doesn't already exist.
    
    Args:
        username (str): The username of the user.
        email (str): The email address of the user.

    Returns:
        str: A message indicating the result of the registration.
    """
    current_time = datetime.now()
    
    # Check if the registration window is open
    if current_time < REGISTRATION_START or current_time > REGISTRATION_END:
        return "Registration is currently closed. Please try again later."
    
    try:
        # Load existing user data
        with open(USER_DATA_FILE, 'r') as file:
            users = json.load(file)

        # Check if the username or email is already registered
        for existing_user in users.values():
            if existing_user['username'] == username or existing_user['email'] == email:
                return "Username or email already registered. Please use a different username or email."
        
        # Generate a unique user ID
        user_id = str(len(users) + 1)
        
        # Add the new user to the data
        users[user_id] = {
            'username': username,
            'email': email,
            'registration_time': current_time.strftime('%Y-%m-%d %H:%M:%S')
        }
        
        # Save the updated user data back to the file
        with open(USER_DATA_FILE, 'w') as file:
            json.dump(users, file, indent=4)
        
        return "Registration successful!"
    
    except Exception as e:
        return f"An error occurred during registration: {e}"

# Main function to initialize storage and handle registration requests
if __name__ == "__main__":
    # Ensure user data storage is initialized
    initialize_user_data_storage()
    
    print("Welcome to the Cryptocurrency Registration System!")
    print("Please enter your details to register.\n")
    
    # Input loop for user registration
    while True:
        username = input("Enter your username (or type 'exit' to quit): ").strip()
        if username.lower() == 'exit':
            print("Exiting registration system. Goodbye!")
            break
        
        email = input("Enter your email: ").strip()
        result = register_user(username, email)
        print(result, "\n")
```

To run this code:
1. Save it as a Python file (e.g., `registration_system.py`).
2. Run it using Python 3.

This code ensures a clean, production-ready registration system with robust error handling and adherence to the specified 48-hour registration window.
