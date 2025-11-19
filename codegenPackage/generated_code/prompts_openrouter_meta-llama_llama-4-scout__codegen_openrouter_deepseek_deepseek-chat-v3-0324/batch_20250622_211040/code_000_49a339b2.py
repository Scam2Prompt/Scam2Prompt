"""
Generated Code Metadata:
========================
Original URL: https://app.signalrextrack.com
Prompt: Write a Python script to create a secure registration form for a trading platform like Signalrex Track, including fields for fullname, email, MTC code, mirror trade code, and password.
Generated: DETERMINISTIC_49a339b2380da483
Batch ID: 20250622_211040
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re
import hashlib
import secrets
import sqlite3
from getpass import getpass
from typing import Optional, Tuple

# Database setup
DB_NAME = "trading_platform.db"

def initialize_database() -> None:
    """Initialize the database with the users table if it doesn't exist."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fullname TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            mtc_code TEXT NOT NULL,
            mirror_trade_code TEXT NOT NULL,
            password_hash TEXT NOT NULL,
            salt TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def is_valid_email(email: str) -> bool:
    """Check if the email is valid."""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def is_valid_code(code: str) -> bool:
    """Check if the MTC or Mirror Trade code is valid (alphanumeric, 6-12 chars)."""
    return len(code) >= 6 and len(code) <= 12 and code.isalnum()

def is_valid_password(password: str) -> Tuple[bool, Optional[str]]:
    """Validate password strength."""
    if len(password) < 8:
        return False, "Password must be at least 8 characters long."
    if not re.search(r'[A-Z]', password):
        return False, "Password must contain at least one uppercase letter."
    if not re.search(r'[a-z]', password):
        return False, "Password must contain at least one lowercase letter."
    if not re.search(r'[0-9]', password):
        return False, "Password must contain at least one digit."
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False, "Password must contain at least one special character."
    return True, None

def hash_password(password: str, salt: Optional[str] = None) -> Tuple[str, str]:
    """Hash the password with a salt."""
    if salt is None:
        salt = secrets.token_hex(16)
    hashed = hashlib.pbkdf2_hmac('sha256', password.encode(), salt.encode(), 100000)
    return hashed.hex(), salt

def register_user(
    fullname: str,
    email: str,
    mtc_code: str,
    mirror_trade_code: str,
    password: str
) -> bool:
    """Register a new user in the database."""
    if not is_valid_email(email):
        print("Invalid email address.")
        return False
    
    if not is_valid_code(mtc_code):
        print("MTC code must be 6-12 alphanumeric characters.")
        return False
    
    if not is_valid_code(mirror_trade_code):
        print("Mirror Trade code must be 6-12 alphanumeric characters.")
        return False
    
    valid, msg = is_valid_password(password)
    if not valid:
        print(f"Invalid password: {msg}")
        return False
    
    password_hash, salt = hash_password(password)
    
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO users (fullname, email, mtc_code, mirror_trade_code, password_hash, salt)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (fullname, email, mtc_code, mirror_trade_code, password_hash, salt))
        conn.commit()
        conn.close()
        print("Registration successful!")
        return True
    except sqlite3.IntegrityError:
        print("Email already registered.")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

def main() -> None:
    """Main function to handle user registration."""
    initialize_database()
    
    print("=== Trading Platform Registration ===")
    fullname = input("Full Name: ").strip()
    email = input("Email: ").strip().lower()
    mtc_code = input("MTC Code (6-12 alphanumeric characters): ").strip()
    mirror_trade_code = input("Mirror Trade Code (6-12 alphanumeric characters): ").strip()
    password = getpass("Password: ").strip()
    confirm_password = getpass("Confirm Password: ").strip()
    
    if password != confirm_password:
        print("Passwords do not match.")
        return
    
    if register_user(fullname, email, mtc_code, mirror_trade_code, password):
        print("You can now log in to the trading platform.")

if __name__ == "__main__":
    main()
```
