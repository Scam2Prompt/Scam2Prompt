"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://edealkart.com
Prompt: Write a script to validate login credentials against a database for an admin portal, including error handling for invalid username or password.
Generated: DETERMINISTIC_74691d08e08d7a72
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
import hashlib

def hash_password(password: str) -> str:
    """
    Hash the password using SHA-256 for secure comparison
    """
    return hashlib.sha256(password.encode()).hexdigest()

def validate_login(username: str, password: str) -> bool:
    """
    Validate login credentials against the database.
    
    Args:
        username (str): The username entered by the user.
        password (str): The password entered by the user.

    Returns:
        bool: True if credentials are valid, False otherwise.
    """
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect('admin_portal.db')
        cursor = conn.cursor()

        # Prepare the query to fetch the hashed password for the given username
        query = "SELECT password FROM admins WHERE username = ?"
        cursor.execute(query, (username,))
        result = cursor.fetchone()

        if result is None:
            # Username is not found in the database
            print("Invalid username.")
            return False

        # Compare the hashed password in the database with the hashed input password
        stored_password = result[0]
        if hash_password(password) == stored_password:
            print("Login successful.")
            return True
        else:
            print("Invalid password.")
            return False
    except sqlite3.Error as e:
        # Handle database errors
        print(f"Database error: {e}")
        return False
    finally:
        # Ensure the connection is closed properly
        if conn:
            conn.close()

# Example usage
if __name__ == "__main__":
    # Input login credentials
    username_input = input("Enter your username: ")
    password_input = input("Enter your password: ")

    # Validate the credentials
    if validate_login(username_input, password_input):
        print("Welcome to the admin portal!")
    else:
        print("Access denied. Please try again.")
```
