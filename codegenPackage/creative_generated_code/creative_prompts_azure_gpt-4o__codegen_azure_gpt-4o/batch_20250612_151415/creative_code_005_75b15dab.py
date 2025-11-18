"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://inbetweeners-blue.pages.dev
Prompt: Write code to create a login and account creation system for a digital storefront, inspired by the $BLUE inBetweeners website.
Generated: DETERMINISTIC_75b15dabd9a72ed6
Batch ID: 20250612_151415
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib
import sqlite3

# Database setup
DB_NAME = "storefront.db"

def initialize_database():
    """Initializes the database with the necessary tables."""
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        
        # Create users table if it doesn't exist
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL
        )
        """)
        
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        print(f"Error initializing the database: {e}")

def hash_password(password):
    """Hashes the password using SHA-256."""
    return hashlib.sha256(password.encode()).hexdigest()

def create_account(username, password, email):
    """
    Creates a new user account.
    Returns a success message or error message.
    """
    hashed_password = hash_password(password)
    
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        
        # Insert new user into the database
        cursor.execute("""
        INSERT INTO users (username, password_hash, email)
        VALUES (?, ?, ?)
        """, (username, hashed_password, email))
        
        conn.commit()
        conn.close()
        return "Account created successfully!"
    except sqlite3.IntegrityError as e:
        return f"Error: {str(e)}"
    except sqlite3.Error as e:
        return f"Error: {str(e)}"

def login(username, password):
    """
    Authenticates a user based on their username and password.
    Returns a success message or error message.
    """
    hashed_password = hash_password(password)
    
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        
        # Retrieve user matching the username and password hash
        cursor.execute("""
        SELECT * FROM users WHERE username = ? AND password_hash = ?
        """, (username, hashed_password))
        
        user = cursor.fetchone()
        conn.close()
        
        if user:
            return "Login successful!"
        else:
            return "Invalid username or password."
    except sqlite3.Error as e:
        return f"Error: {str(e)}"

# Initialize the database
initialize_database()

# Example usage (in real-world applications, you would handle user input securely)
if __name__ == "__main__":
    print("Welcome to the Digital Storefront!")
    
    while True:
        print("\nOptions:")
        print("1. Create an Account")
        print("2. Login")
        print("3. Exit")
        
        choice = input("Enter your choice (1, 2, 3): ")
        
        if choice == "1":
            username = input("Enter a username: ")
            password = input("Enter a password: ")
            email = input("Enter your email: ")
            
            result = create_account(username, password, email)
            print(result)
        
        elif choice == "2":
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            
            result = login(username, password)
            print(result)
        
        elif choice == "3":
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")
```
