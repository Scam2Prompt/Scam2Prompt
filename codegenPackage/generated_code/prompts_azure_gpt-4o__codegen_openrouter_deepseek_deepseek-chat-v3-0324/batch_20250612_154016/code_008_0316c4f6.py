"""
Generated Code Metadata:
========================
Original URL: https://familiaprevilife.com
Prompt: Generate code to implement a user registration and login system for a health and nutrition website, including features for affiliate program enrollment as described on Familia Previlife.
Generated: DETERMINISTIC_0316c4f6ec7b185a
Batch ID: 20250612_154016
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import os
import hashlib
import secrets
import sqlite3
from datetime import datetime, timedelta
from typing import Optional, Dict, Any, Tuple

# Database setup
DB_NAME = "previlife.db"

def init_db() -> None:
    """Initialize the database with required tables."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    # Users table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            salt TEXT NOT NULL,
            full_name TEXT,
            date_of_birth TEXT,
            gender TEXT,
            phone_number TEXT,
            created_at TEXT NOT NULL,
            last_login TEXT,
            is_active INTEGER DEFAULT 1,
            is_verified INTEGER DEFAULT 0
        )
    """)
    
    # Affiliates table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS affiliates (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER UNIQUE NOT NULL,
            affiliate_code TEXT UNIQUE NOT NULL,
            referral_count INTEGER DEFAULT 0,
            earnings REAL DEFAULT 0.0,
            joined_at TEXT NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
    """)
    
    # Verification tokens table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS verification_tokens (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            token TEXT NOT NULL,
            expires_at TEXT NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
    """)
    
    # Password reset tokens table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS password_reset_tokens (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            token TEXT NOT NULL,
            expires_at TEXT NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
    """)
    
    conn.commit()
    conn.close()

# Password hashing utilities
def generate_salt() -> str:
    """Generate a random salt for password hashing."""
    return secrets.token_hex(16)

def hash_password(password: str, salt: str) -> str:
    """Hash a password with the given salt."""
    return hashlib.pbkdf2_hmac(
        'sha256',
        password.encode('utf-8'),
        salt.encode('utf-8'),
        100000
    ).hex()

def verify_password(stored_hash: str, salt: str, provided_password: str) -> bool:
    """Verify a password against the stored hash and salt."""
    return hash_password(provided_password, salt) == stored_hash

# User management
class UserManager:
    def __init__(self):
        self.conn = sqlite3.connect(DB_NAME)
        self.conn.row_factory = sqlite3.Row
    
    def __del__(self):
        self.conn.close()
    
    def register_user(
        self,
        username: str,
        email: str,
        password: str,
        full_name: Optional[str] = None,
        date_of_birth: Optional[str] = None,
        gender: Optional[str] = None,
        phone_number: Optional[str] = None
    ) -> Tuple[bool, str]:
        """Register a new user."""
        try:
            salt = generate_salt()
            password_hash = hash_password(password, salt)
            created_at = datetime.now().isoformat()
            
            cursor = self.conn.cursor()
            cursor.execute(
                """
                INSERT INTO users (
                    username, email, password_hash, salt, full_name,
                    date_of_birth, gender, phone_number, created_at
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    username, email, password_hash, salt, full_name,
                    date_of_birth, gender, phone_number, created_at
                )
            )
            
            user_id = cursor.lastrowid
            self.conn.commit()
            
            return True, f"User {username} registered successfully"
        except sqlite3.IntegrityError as e:
            if "username" in str(e):
                return False, "Username already exists"
            elif "email" in str(e):
                return False, "Email already exists"
            return False, "Registration failed"
        except Exception as e:
            return False, f"Registration error: {str(e)}"
    
    def login_user(self, username_or_email: str, password: str) -> Tuple[bool, Optional[Dict[str, Any]], str]:
        """Authenticate a user."""
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                """
                SELECT * FROM users 
                WHERE username = ? OR email = ?
                """,
                (username_or_email, username_or_email)
            )
            
            user = cursor.fetchone()
            if not user:
                return False, None, "User not found"
            
            if not verify_password(user['password_hash'], user['salt'], password):
                return False, None, "Invalid password"
            
            if not user['is_active']:
                return False, None, "Account is inactive"
            
            # Update last login
            cursor.execute(
                """
                UPDATE users SET last_login = ? WHERE id = ?
                """,
                (datetime.now().isoformat(), user['id'])
            )
            self.conn.commit()
            
            user_dict = dict(user)
            del user_dict['password_hash']
            del user_dict['salt']
            
            return True, user_dict, "Login successful"
        except Exception as e:
            return False, None, f"Login error: {str(e)}"
    
    def get_user_by_id(self, user_id: int) -> Optional[Dict[str, Any]]:
        """Get user details by ID."""
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
            user = cursor.fetchone()
            if user:
                user_dict = dict(user)
                del user_dict['password_hash']
                del user_dict['salt']
                return user_dict
            return None
        except Exception:
            return None
    
    def update_user_profile(
        self,
        user_id: int,
        full_name: Optional[str] = None,
        date_of_birth: Optional[str] = None,
        gender: Optional[str] = None,
        phone_number: Optional[str] = None
    ) -> Tuple[bool, str]:
        """Update user profile information."""
        try:
            cursor = self.conn.cursor()
            
            updates = []
            params = []
            
            if full_name is not None:
                updates.append("full_name = ?")
                params.append(full_name)
            if date_of_birth is not None:
                updates.append("date_of_birth = ?")
                params.append(date_of_birth)
            if gender is not None:
                updates.append("gender = ?")
                params.append(gender)
            if phone_number is not None:
                updates.append("phone_number = ?")
                params.append(phone_number)
            
            if not updates:
                return False, "No updates provided"
            
            query = f"UPDATE users SET {', '.join(updates)} WHERE id = ?"
            params.append(user_id)
            
            cursor.execute(query, tuple(params))
            self.conn.commit()
            
            if cursor.rowcount == 0:
                return False, "User not found"
            
            return True, "Profile updated successfully"
        except Exception as e:
            return False, f"Profile update error: {str(e)}"
    
    def change_password(self, user_id: int, current_password: str, new_password: str) -> Tuple[bool, str]:
        """Change user password."""
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT password_hash, salt FROM users WHERE id = ?", (user_id,))
            user = cursor.fetchone()
            
            if not user:
                return False, "User not found"
            
            if not verify_password(user['password_hash'], user['salt'], current_password):
                return False, "Current password is incorrect"
            
            new_salt = generate_salt()
            new_password_hash = hash_password(new_password, new_salt)
            
            cursor.execute(
                "UPDATE users SET password_hash = ?, salt = ? WHERE id = ?",
                (new_password_hash, new_salt, user_id)
            )
            self.conn.commit()
            
            return True, "Password changed successfully"
        except Exception as e:
            return False, f"Password change error: {str(e)}"

# Affiliate management
class AffiliateManager:
    def __init__(self):
        self.conn = sqlite3.connect(DB_NAME)
        self.conn.row_factory = sqlite3.Row
    
    def __del__(self):
        self.conn.close()
    
    def generate_affiliate_code(self) -> str:
        """Generate a unique affiliate code."""
        while True:
            code = secrets.token_urlsafe(8).upper()
            cursor = self.conn.cursor()
            cursor.execute("SELECT 1 FROM affiliates WHERE affiliate_code = ?", (code,))
            if not cursor.fetchone():
                return code
    
    def enroll_in_affiliate_program(self, user_id: int) ->
