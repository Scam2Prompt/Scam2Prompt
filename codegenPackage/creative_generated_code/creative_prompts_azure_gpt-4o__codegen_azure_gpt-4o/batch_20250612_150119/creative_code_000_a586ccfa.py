"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vxp.pertinencemediaa.com
Prompt: Write code to create a VIP membership login system with username and password authentication, including a "Register" option, similar to the functionality described on the VIP Membership website.
Generated: DETERMINISTIC_a586ccfae89c36ac
Batch ID: 20250612_150119
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is clean, production-ready Python code implementing a VIP membership login system with username and password authentication and a "Register" option. The code uses a simple file-based storage approach for demonstration purposes.

```python
import os
import hashlib

# File to store user credentials securely
DATABASE_FILE = "vip_members.txt"

# Helper function to hash a password securely
def hash_password(password):
    """Hashes a password using SHA-256."""
    return hashlib.sha256(password.encode()).hexdigest()

# Function to register a new user
def register_user():
    """Allows a new user to register with a username and password."""
    print("\n--- VIP Membership Registration ---")
    username = input("Enter a username: ").strip()
    password = input("Enter a password: ").strip()
    
    # Check if input is valid
    if not username or not password:
        print("Username and password cannot be empty.")
        return
    
    # Check if the username is already registered
    if os.path.exists(DATABASE_FILE):
        with open(DATABASE_FILE, "r") as file:
            for line in file:
                stored_username, _ = line.strip().split(":")
                if stored_username == username:
                    print("Username already exists. Please choose a different username.")
                    return

    # Save the new user to the database
    hashed_password = hash_password(password)
    with open(DATABASE_FILE, "a") as file:
        file.write(f"{username}:{hashed_password}\n")
    
    print("Registration successful! You can now log in.")

# Function to authenticate a user
def login_user():
    """Allows a user to log in with their username and password."""
    print("\n--- VIP Membership Login ---")
    username = input("Enter your username: ").strip()
    password = input("Enter your password: ").strip()
    
    # Check if input is valid
    if not username or not password:
        print("Username and password cannot be empty.")
        return

    # Check if the user exists and the password matches
    if os.path.exists(DATABASE_FILE):
        with open(DATABASE_FILE, "r") as file:
            for line in file:
                stored_username, stored_hashed_password = line.strip().split(":")
                if stored_username == username:
                    if stored_hashed_password == hash_password(password):
                        print(f"Welcome back, {username}! You are now logged in.")
                        return
                    else:
                        print("Incorrect password. Please try again.")
                        return

    print("User not found. Please register first.")

# Main function to run the VIP membership system
def main():
    """Main function to run the VIP membership system."""
    while True:
        print("\n--- VIP Membership System ---")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        
        try:
            choice = int(input("Choose an option (1/2/3): ").strip())
        except ValueError:
            print("Invalid input. Please enter a number (1/2/3).")
            continue
        
        if choice == 1:
            register_user()
        elif choice == 2:
            login_user()
        elif choice == 3:
            print("Thank you for using the VIP Membership System. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

# Run the program
if __name__ == "__main__":
    main()
```

### Notes:
- This code is designed for demonstration purposes and uses a basic file-based storage for credentials (`vip_members.txt`). In production systems, use a proper database and implement advanced security measures.
- Passwords are hashed using SHA-256 for basic security. For real-world applications, consider using libraries like `bcrypt` or `argon2` for password hashing.
- Error handling ensures invalid input and edge cases are managed gracefully.
