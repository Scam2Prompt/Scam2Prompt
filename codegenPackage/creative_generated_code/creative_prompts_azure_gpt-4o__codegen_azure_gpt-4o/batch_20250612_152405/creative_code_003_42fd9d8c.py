"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pos.graphixals.top
Prompt: Create a script to simulate login attempts to a Point of Sale system and validate user credentials against a database.
Generated: DETERMINISTIC_42fd9d8c8d8d4757
Batch ID: 20250612_152405
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
from hashlib import sha256
import sys

# Set up a database connection
DB_FILE = "pos_system.db"

# Create the database schema if it doesn't exist
def setup_database():
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        
        # Create users table if it doesn't exist
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL
        )
        """)
        
        # Add sample user for demonstration (if not already added)
        cursor.execute("""
        INSERT OR IGNORE INTO users (username, password_hash)
        VALUES (?, ?)""", ("admin", sha256("admin123".encode()).hexdigest()))
        
        conn.commit()
        conn.close()
    except Exception as e:
        print(f"Error setting up database: {e}")
        sys.exit(1)

# Function to validate user credentials
def validate_credentials(username, password):
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        
        # Hash the provided password using SHA-256
        password_hash = sha256(password.encode()).hexdigest()
        
        # Query to check if the user exists with the matching password hash
        cursor.execute("""
        SELECT id FROM users WHERE username = ? AND password_hash = ?
        """, (username, password_hash))
        
        user = cursor.fetchone()
        conn.close()
        
        # Return True if user exists, otherwise False
        return user is not None
    except Exception as e:
        print(f"Error validating credentials: {e}")
        return False

# Main function to handle login attempts
def simulate_login():
    print("Welcome to the Point of Sale System")
    for attempt in range(3):  # Allow 3 login attempts
        username = input("Enter username: ").strip()
        password = input("Enter password: ").strip()
        
        if validate_credentials(username, password):
            print(f"Login successful! Welcome, {username}.")
            return
        
        print("Invalid credentials. Please try again.")
    
    print("Too many failed attempts. Access denied.")
    sys.exit(1)

# Entry point for the script
if __name__ == "__main__":
    setup_database()  # Ensure the database is set up
    simulate_login()  # Start login simulation
```
