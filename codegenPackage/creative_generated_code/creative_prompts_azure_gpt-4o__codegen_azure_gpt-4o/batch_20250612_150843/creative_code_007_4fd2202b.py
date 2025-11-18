"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thequixbit.com
Prompt: Write code to create a registration system for a cryptocurrency trading app, including account creation and funding steps modeled after QUIXBIT's process.
Generated: DETERMINISTIC_4fd2202be6aeadbc
Batch ID: 20250612_150843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re
import sqlite3

# Constants
MIN_PASSWORD_LENGTH = 8
MIN_INITIAL_FUNDING = 10.0  # Minimum initial funding in USD

# Database Initialization
DB_FILE = 'crypto_app.db'

# Function to initialize the database
def initialize_database():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    
    # Create users table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            email TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            balance REAL NOT NULL DEFAULT 0.0
        )
    ''')
    conn.commit()
    conn.close()

# Helper Functions
def validate_email(email):
    """
    Validates the format of the provided email address.
    Returns True if the email format is valid, otherwise False.
    """
    email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(email_regex, email) is not None

def validate_password(password):
    """
    Validates the strength of the provided password.
    Returns True if the password meets the minimum length requirement.
    """
    return len(password) >= MIN_PASSWORD_LENGTH

# Registration Function
def register_user(username, email, password, initial_funding):
    """
    Registers a new user into the system.
    Returns a success message or raises an exception if the process fails.
    """
    if not validate_email(email):
        raise ValueError("Invalid email format.")
    
    if not validate_password(password):
        raise ValueError(f"Password must be at least {MIN_PASSWORD_LENGTH} characters long.")
    
    if initial_funding < MIN_INITIAL_FUNDING:
        raise ValueError(f"Initial funding must be at least ${MIN_INITIAL_FUNDING}.")
    
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        
        # Insert user record
        cursor.execute('''
            INSERT INTO users (username, email, password, balance)
            VALUES (?, ?, ?, ?)
        ''', (username, email, password, initial_funding))
        
        conn.commit()
        conn.close()
        return f"User '{username}' successfully registered with an initial balance of ${initial_funding}."
    
    except sqlite3.IntegrityError:
        raise ValueError("Username or email already exists.")
    except Exception as e:
        raise RuntimeError(f"An error occurred during registration: {e}")

# Main Execution
if __name__ == "__main__":
    # Initialize the database
    initialize_database()
    
    print("Welcome to the Cryptocurrency Trading App Registration Process!")
    
    try:
        # Collect user information
        username = input("Enter your desired username: ").strip()
        email = input("Enter your email address: ").strip()
        password = input("Enter your password: ").strip()
        initial_funding = float(input(f"Enter initial funding amount (minimum ${MIN_INITIAL_FUNDING}): "))
        
        # Register the user
        message = register_user(username, email, password, initial_funding)
        print(message)
        
    except ValueError as ve:
        print(f"Registration Error: {ve}")
    except Exception as e:
        print(f"Unexpected Error: {e}")
```
