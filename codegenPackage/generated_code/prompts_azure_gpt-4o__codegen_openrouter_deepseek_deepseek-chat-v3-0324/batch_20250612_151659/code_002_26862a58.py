"""
Generated Code Metadata:
========================
Original URL: https://ahopefulme.com
Prompt: Generate code to create a login and registration system for a platform inspired by HopefulMe, including options for username, email, or phone-based authentication.
Generated: DETERMINISTIC_26862a582f7edb96
Batch ID: 20250612_151659
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
import string
from datetime import datetime, timedelta
from typing import Optional, Union, Dict, Any
import sqlite3
from sqlite3 import Error

# Database setup
def create_connection(db_file: str) -> sqlite3.Connection:
    """Create a database connection to the SQLite database specified by db_file"""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        conn.execute("PRAGMA foreign_keys = ON")
        return conn
    except Error as e:
        print(e)
    return conn

def create_tables(conn: sqlite3.Connection) -> None:
    """Create necessary tables if they don't exist"""
    users_table = """CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT UNIQUE,
                        email TEXT UNIQUE,
                        phone TEXT UNIQUE,
                        password_hash TEXT NOT NULL,
                        salt TEXT NOT NULL,
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        is_active BOOLEAN DEFAULT 1,
                        last_login TIMESTAMP
                    );"""
    
    login_attempts_table = """CREATE TABLE IF NOT EXISTS login_attempts (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                user_id INTEGER,
                                attempt_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                                success BOOLEAN,
                                ip_address TEXT,
                                FOREIGN KEY (user_id) REFERENCES users (id)
                            );"""
    
    password_reset_tokens = """CREATE TABLE IF NOT EXISTS password_reset_tokens (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                user_id INTEGER NOT NULL,
                                token TEXT NOT NULL,
                                expires_at TIMESTAMP NOT NULL,
                                used BOOLEAN DEFAULT 0,
                                FOREIGN KEY (user_id) REFERENCES users (id)
                            );"""
    
    try:
        c = conn.cursor()
        c.execute(users_table)
        c.execute(login_attempts_table)
        c.execute(password_reset_tokens)
        conn.commit()
    except Error as e:
        print(e)

# Password utilities
def generate_salt(length: int = 16) -> str:
    """Generate a random salt for password hashing"""
    alphabet = string.ascii_letters + string.digits
    return ''.join(secrets.choice(alphabet) for _ in range(length))

def hash_password(password: str, salt: str) -> str:
    """Hash the password with the given salt"""
    return hashlib.pbkdf2_hmac(
        'sha256',
        password.encode('utf-8'),
        salt.encode('utf-8'),
        100000
    ).hex()

def verify_password(stored_hash: str, stored_salt: str, provided_password: str) -> bool:
    """Verify a password against stored hash and salt"""
    return hash_password(provided_password, stored_salt) == stored_hash

# Validation utilities
def is_valid_email(email: str) -> bool:
    """Check if email is valid"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def is_valid_phone(phone: str) -> bool:
    """Check if phone number is valid (basic international format)"""
    pattern = r'^\+?[1-9]\d{1,14}$'
    return re.match(pattern, phone) is not None

def is_valid_username(username: str) -> bool:
    """Check if username is valid (alphanumeric with underscores)"""
    pattern = r'^[a-zA-Z0-9_]{3,30}$'
    return re.match(pattern, username) is not None

def is_strong_password(password: str) -> bool:
    """Check if password meets strength requirements"""
    if len(password) < 8:
        return False
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'[a-z]', password):
        return False
    if not re.search(r'[0-9]', password):
        return False
    if not re.search(r'[^A-Za-z0-9]', password):
        return False
    return True

# User management
class UserManager:
    def __init__(self, db_file: str = 'hopefulme.db'):
        self.conn = create_connection(db_file)
        if self.conn is not None:
            create_tables(self.conn)
        else:
            raise Exception("Error: Cannot create database connection")

    def __del__(self):
        if self.conn:
            self.conn.close()

    def register_user(self, username: Optional[str] = None, 
                     email: Optional[str] = None, 
                     phone: Optional[str] = None, 
                     password: str = None) -> Dict[str, Any]:
        """Register a new user with at least one identifier (username, email, or phone)"""
        if not any([username, email, phone]):
            return {"success": False, "message": "At least one identifier (username, email, or phone) is required"}
        
        if password is None or not is_strong_password(password):
            return {"success": False, "message": "Password does not meet strength requirements"}
        
        if username and not is_valid_username(username):
            return {"success": False, "message": "Invalid username format"}
        
        if email and not is_valid_email(email):
            return {"success": False, "message": "Invalid email format"}
        
        if phone and not is_valid_phone(phone):
            return {"success": False, "message": "Invalid phone format"}
        
        salt = generate_salt()
        password_hash = hash_password(password, salt)
        
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                "INSERT INTO users (username, email, phone, password_hash, salt) VALUES (?, ?, ?, ?, ?)",
                (username, email, phone, password_hash, salt)
            )
            self.conn.commit()
            return {"success": True, "message": "User registered successfully", "user_id": cursor.lastrowid}
        except sqlite3.IntegrityError as e:
            error_msg = str(e)
            if "username" in error_msg:
                return {"success": False, "message": "Username already exists"}
            elif "email" in error_msg:
                return {"success": False, "message": "Email already exists"}
            elif "phone" in error_msg:
                return {"success": False, "message": "Phone number already exists"}
            return {"success": False, "message": "Registration failed"}
        except Error as e:
            return {"success": False, "message": f"Database error: {str(e)}"}

    def authenticate_user(self, identifier: str, password: str, ip_address: str = None) -> Dict[str, Any]:
        """Authenticate a user by username, email, or phone"""
        try:
            cursor = self.conn.cursor()
            
            # Check if identifier is email
            if '@' in identifier:
                cursor.execute("SELECT id, password_hash, salt, is_active FROM users WHERE email = ?", (identifier,))
            # Check if identifier is phone (starts with + or has digits)
            elif identifier.startswith('+') or identifier.isdigit():
                cursor.execute("SELECT id, password_hash, salt, is_active FROM users WHERE phone = ?", (identifier,))
            # Otherwise assume username
            else:
                cursor.execute("SELECT id, password_hash, salt, is_active FROM users WHERE username = ?", (identifier,))
            
            user = cursor.fetchone()
            
            if user is None:
                self._record_login_attempt(None, False, ip_address)
                return {"success": False, "message": "User not found"}
            
            user_id, stored_hash, stored_salt, is_active = user
            
            if not is_active:
                self._record_login_attempt(user_id, False, ip_address)
                return {"success": False, "message": "Account is inactive"}
            
            if verify_password(stored_hash, stored_salt, password):
                # Update last login time
                cursor.execute("UPDATE users SET last_login = CURRENT_TIMESTAMP WHERE id = ?", (user_id,))
                self.conn.commit()
                self._record_login_attempt(user_id, True, ip_address)
                return {"success": True, "message": "Authentication successful", "user_id": user_id}
            else:
                self._record_login_attempt(user_id, False, ip_address)
                return {"success": False, "message": "Invalid credentials"}
        except Error as e:
            return {"success": False, "message": f"Authentication error: {str(e)}"}

    def _record_login_attempt(self, user_id: Optional[int], success: bool, ip_address: str = None) -> None:
        """Record a login attempt in the database"""
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                "INSERT INTO login_attempts (user_id, success, ip_address) VALUES (?, ?, ?)",
                (user_id, success, ip_address)
            )
            self.conn.commit()
        except Error:
            pass  # Don't fail authentication if logging fails

    def
