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
import getpass

# Constants for database configuration
DATABASE_NAME = 'pos_system.db'

def create_connection(db_file):
    """Create a database connection to the SQLite database specified by the db_file."""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
    return conn

def validate_user(username, password):
    """Validate user credentials against the database.
    
    Args:
        username (str): The username of the user.
        password (str): The password of the user.
    
    Returns:
        bool: True if credentials are valid, False otherwise.
    """
    conn = create_connection(DATABASE_NAME)
    if conn is None:
        return False
    
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT password FROM users WHERE username = ?", (username,))
        row = cursor.fetchone()
        
        if row is not None and row[0] == password:
            return True
        else:
            return False
    except sqlite3.Error as e:
        print(f"Database query error: {e}")
        return False
    finally:
        if conn:
            conn.close()

def main():
    """Main function to simulate user login attempts."""
    max_attempts = 3
    attempts = 0

    while attempts < max_attempts:
        username = input("Enter username: ")
        password = getpass.getpass("Enter password: ")
        
        if validate_user(username, password):
            print("Login successful!")
            break
        else:
            attempts += 1
            print("Invalid credentials. Please try again.")
    
    if attempts == max_attempts:
        print("Too many failed login attempts. Access denied.")

if __name__ == "__main__":
    main()
```
