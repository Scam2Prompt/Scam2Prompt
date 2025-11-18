"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://financeinvestmentslimited.org
Prompt: Create a secure login system with brute-force protection and personalized account management features, modeled after Finance Investment Limited's security protocols.
Generated: DETERMINISTIC_503ae3772ba09bd4
Batch ID: 20250612_154631
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import bcrypt
import sqlite3
import time
from datetime import datetime, timedelta

# Constants
MAX_LOGIN_ATTEMPTS = 5
LOCKOUT_DURATION = timedelta(minutes=15)

# Database setup
DB_FILE = "secure_login.db"

def initialize_database():
    """Initialize database and required tables."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    
    # Create users table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password_hash TEXT NOT NULL,
        login_attempts INTEGER NOT NULL DEFAULT 0,
        lockout_until TEXT DEFAULT NULL,
        created_at TEXT NOT NULL
    )
    """)
    
    conn.commit()
    conn.close()

def hash_password(password):
    """Hash a plaintext password securely."""
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode('utf-8')

def verify_password(password, password_hash):
    """Verify a plaintext password against its hashed version."""
    return bcrypt.checkpw(password.encode(), password_hash.encode())

def register_user(username, password):
    """Register a new user in the system."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    
    try:
        password_hash = hash_password(password)
        created_at = datetime.now().isoformat()
        cursor.execute("INSERT INTO users (username, password_hash, created_at) VALUES (?, ?, ?)", 
                       (username, password_hash, created_at))
        conn.commit()
        print("User registered successfully.")
    except sqlite3.IntegrityError:
        print("Error: Username already exists.")
    finally:
        conn.close()

def check_lockout_status(username):
    """Check if a user is currently locked out."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    
    cursor.execute("SELECT lockout_until FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()
    conn.close()
    
    if result and result[0]:
        lockout_until = datetime.fromisoformat(result[0])
        if datetime.now() < lockout_until:
            return True, lockout_until
    return False, None

def update_lockout_status(username, attempts):
    """Update a user's lockout status based on failed login attempts."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    
    if attempts >= MAX_LOGIN_ATTEMPTS:
        lockout_until = datetime.now() + LOCKOUT_DURATION
        cursor.execute("UPDATE users SET lockout_until = ?, login_attempts = ? WHERE username = ?", 
                       (lockout_until.isoformat(), attempts, username))
    else:
        cursor.execute("UPDATE users SET login_attempts = ? WHERE username = ?", (attempts, username))
    
    conn.commit()
    conn.close()

def login_user(username, password):
    """Login a user with brute-force protection."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    
    # Check if user exists
    cursor.execute("SELECT password_hash, login_attempts FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()
    
    if not result:
        print("Error: User not found.")
        conn.close()
        return False
    
    password_hash, login_attempts = result
    
    # Check lockout status
    locked_out, lockout_until = check_lockout_status(username)
    if locked_out:
        print(f"Account is locked. Try again after {lockout_until}.")
        conn.close()
        return False

    # Verify password
    if verify_password(password, password_hash):
        print("Login successful.")
        cursor.execute("UPDATE users SET login_attempts = 0, lockout_until = NULL WHERE username = ?", (username,))
        conn.commit()
        conn.close()
        return True
    else:
        print("Invalid credentials.")
        login_attempts += 1
        update_lockout_status(username, login_attempts)
        conn.close()
        return False

def user_account_management(username):
    """Display account management options for the user."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    
    cursor.execute("SELECT created_at, login_attempts FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()
    
    conn.close()
    
    if result:
        created_at, login_attempts = result
        print(f"Account for {username}:")
        print(f"  Created at: {created_at}")
        print(f"  Failed login attempts: {login_attempts}")
    else:
        print("Error: User not found.")

# Initialize the database
initialize_database()

# Example usage (replace these calls with actual user input handling in production)
register_user("testuser", "SecurePassword123")
login_user("testuser", "WrongPassword")
login_user("testuser", "SecurePassword123")
user_account_management("testuser")
```
