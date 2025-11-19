"""
Generated Code Metadata:
========================
Original URL: https://truckloancenter.com
Prompt: Develop a simple login and registration system for an online poker platform, referencing the easy registration process described on DominoBet.
Generated: DETERMINISTIC_368dd6fc0edcd364
Batch ID: 20250612_151445
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import hashlib
import sqlite3
from getpass import getpass

# Database setup
def init_db():
    conn = sqlite3.connect('poker_users.db')
    cursor = conn.cursor()
    
    # Create users table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            balance REAL DEFAULT 1000.00
        )
    ''')
    
    conn.commit()
    conn.close()

# Password hashing for security
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# User registration
def register_user():
    print("\n--- Registration ---")
    username = input("Choose a username: ").strip()
    email = input("Enter your email: ").strip().lower()
    password = getpass("Choose a password: ").strip()
    confirm_password = getpass("Confirm password: ").strip()
    
    if password != confirm_password:
        print("Error: Passwords do not match!")
        return False
    
    if len(password) < 6:
        print("Error: Password must be at least 6 characters long!")
        return False
    
    try:
        conn = sqlite3.connect('poker_users.db')
        cursor = conn.cursor()
        
        # Check if username or email already exists
        cursor.execute("SELECT * FROM users WHERE username = ? OR email = ?", (username, email))
        if cursor.fetchone():
            print("Error: Username or email already exists!")
            return False
        
        # Insert new user
        password_hash = hash_password(password)
        cursor.execute(
            "INSERT INTO users (username, email, password_hash) VALUES (?, ?, ?)",
            (username, email, password_hash)
        )
        
        conn.commit()
        print("Registration successful! You've been credited with $1000.00.")
        return True
        
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return False
    finally:
        conn.close()

# User login
def login_user():
    print("\n--- Login ---")
    username = input("Username: ").strip()
    password = getpass("Password: ").strip()
    
    try:
        conn = sqlite3.connect('poker_users.db')
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        user = cursor.fetchone()
        
        if user and user[3] == hash_password(password):
            print(f"Login successful! Welcome back, {username}.")
            print(f"Your current balance: ${user[4]:.2f}")
            return True
        else:
            print("Error: Invalid username or password!")
            return False
            
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return False
    finally:
        conn.close()

# Main menu
def main():
    init_db()
    
    while True:
        print("\n=== Online Poker Platform ===")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        
        choice = input("Select an option: ").strip()
        
        if choice == '1':
            register_user()
        elif choice == '2':
            if login_user():
                # Here you would typically enter the poker game interface
                break
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```
