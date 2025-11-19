"""
Generated Code Metadata:
========================
Original URL: https://usdtclaim.com
Prompt: Provide a solution for securely managing user accounts on a cryptocurrency faucet platform, ensuring compliance with rules against multiple accounts, proxy usage, and public computer access as outlined by USDT Claim.
Generated: DETERMINISTIC_10c6f95fe7e31830
Batch ID: 20250612_151334
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import hashlib
import uuid
import re
import ipaddress
from datetime import datetime, timedelta
from typing import Optional, Dict, List, Tuple
import sqlite3
from sqlite3 import Error

# Database setup and connection
def create_connection(db_file: str) -> sqlite3.Connection:
    """Create a database connection to the SQLite database specified by db_file."""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        conn.execute("PRAGMA foreign_keys = ON")
        return conn
    except Error as e:
        print(e)
    return conn

def create_tables(conn: sqlite3.Connection) -> None:
    """Create necessary tables if they don't exist."""
    sql_create_users_table = """CREATE TABLE IF NOT EXISTS users (
                                id TEXT PRIMARY KEY,
                                email TEXT UNIQUE NOT NULL,
                                password_hash TEXT NOT NULL,
                                salt TEXT NOT NULL,
                                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                                last_login TIMESTAMP,
                                is_active BOOLEAN DEFAULT 1,
                                verification_token TEXT,
                                is_verified BOOLEAN DEFAULT 0
                            );"""

    sql_create_ip_table = """CREATE TABLE IF NOT EXISTS ip_addresses (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            user_id TEXT NOT NULL,
                            ip_address TEXT NOT NULL,
                            first_seen TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                            last_seen TIMESTAMP,
                            FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE,
                            UNIQUE(user_id, ip_address)
                        );"""

    sql_create_login_attempts_table = """CREATE TABLE IF NOT EXISTS login_attempts (
                                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                                        ip_address TEXT NOT NULL,
                                        attempt_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                                        was_successful BOOLEAN DEFAULT 0
                                    );"""

    sql_create_user_agents_table = """CREATE TABLE IF NOT EXISTS user_agents (
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    user_id TEXT NOT NULL,
                                    user_agent TEXT NOT NULL,
                                    first_seen TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                                    last_seen TIMESTAMP,
                                    FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE,
                                    UNIQUE(user_id, user_agent)
                                );"""

    try:
        c = conn.cursor()
        c.execute(sql_create_users_table)
        c.execute(sql_create_ip_table)
        c.execute(sql_create_login_attempts_table)
        c.execute(sql_create_user_agents_table)
        conn.commit()
    except Error as e:
        print(e)

# Security and validation functions
def is_valid_email(email: str) -> bool:
    """Check if the email address is valid."""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def generate_salt() -> str:
    """Generate a random salt for password hashing."""
    return uuid.uuid4().hex

def hash_password(password: str, salt: str) -> str:
    """Hash the password with the given salt using SHA-256."""
    return hashlib.sha256((password + salt).encode()).hexdigest()

def is_proxy_ip(ip: str) -> bool:
    """Check if the IP address is from a known proxy/VPN service (simplified example)."""
    # In production, this would use a proper IP reputation service
    try:
        ip_obj = ipaddress.ip_address(ip)
        return ip_obj.is_private or ip_obj.is_loopback
    except ValueError:
        return True

def is_public_computer(user_agent: str) -> bool:
    """Check if the user agent suggests a public computer (simplified example)."""
    # In production, this would use more sophisticated detection
    public_keywords = ['library', 'cafe', 'public', 'kiosk']
    return any(keyword in user_agent.lower() for keyword in public_keywords)

# User management
class UserManager:
    def __init__(self, db_file: str = 'faucet.db'):
        self.conn = create_connection(db_file)
        if self.conn is not None:
            create_tables(self.conn)
        else:
            raise Error("Error! Cannot create the database connection.")

    def __del__(self):
        if self.conn:
            self.conn.close()

    def create_user(self, email: str, password: str, ip_address: str, user_agent: str) -> Tuple[bool, str]:
        """Create a new user account with security checks."""
        if not is_valid_email(email):
            return False, "Invalid email address format."

        if is_proxy_ip(ip_address):
            return False, "Proxy/VPN usage is not allowed."

        if is_public_computer(user_agent):
            return False, "Public computer access is not allowed."

        try:
            cursor = self.conn.cursor()
            
            # Check if email already exists
            cursor.execute("SELECT id FROM users WHERE email = ?", (email,))
            if cursor.fetchone() is not None:
                return False, "Email already registered."

            # Check if IP has too many accounts
            cursor.execute("""
                SELECT COUNT(DISTINCT user_id) 
                FROM ip_addresses 
                WHERE ip_address = ?
            """, (ip_address,))
            count = cursor.fetchone()[0]
            if count >= 3:  # Allow max 3 accounts per IP
                return False, "Maximum account limit reached for this IP address."

            # Create user
            user_id = str(uuid.uuid4())
            salt = generate_salt()
            password_hash = hash_password(password, salt)
            verification_token = str(uuid.uuid4())

            cursor.execute("""
                INSERT INTO users (id, email, password_hash, salt, verification_token)
                VALUES (?, ?, ?, ?, ?)
            """, (user_id, email, password_hash, salt, verification_token))

            # Record IP and user agent
            self._record_ip_address(user_id, ip_address)
            self._record_user_agent(user_id, user_agent)

            self.conn.commit()
            return True, "User created successfully. Please check your email for verification."
        except Error as e:
            self.conn.rollback()
            return False, f"Database error: {str(e)}"

    def verify_user(self, token: str) -> Tuple[bool, str]:
        """Verify a user's email using the verification token."""
        try:
            cursor = self.conn.cursor()
            cursor.execute("""
                UPDATE users 
                SET is_verified = 1, verification_token = NULL 
                WHERE verification_token = ? AND is_verified = 0
            """, (token,))
            
            if cursor.rowcount == 0:
                return False, "Invalid or expired verification token."
            
            self.conn.commit()
            return True, "Account verified successfully."
        except Error as e:
            self.conn.rollback()
            return False, f"Database error: {str(e)}"

    def authenticate_user(self, email: str, password: str, ip_address: str, user_agent: str) -> Tuple[bool, str, Optional[str]]:
        """Authenticate a user with security checks."""
        if is_proxy_ip(ip_address):
            return False, "Proxy/VPN usage is not allowed.", None

        if is_public_computer(user_agent):
            return False, "Public computer access is not allowed.", None

        try:
            cursor = self.conn.cursor()
            
            # Get user data
            cursor.execute("""
                SELECT id, password_hash, salt, is_active, is_verified 
                FROM users 
                WHERE email = ?
            """, (email,))
            user_data = cursor.fetchone()

            if user_data is None:
                self._record_login_attempt(ip_address, False)
                return False, "Invalid email or password.", None

            user_id, stored_hash, salt, is_active, is_verified = user_data

            if not is_active:
                return False, "Account is disabled.", None

            if not is_verified:
                return False, "Account not verified. Please check your email.", None

            # Verify password
            if hash_password(password, salt) != stored_hash:
                self._record_login_attempt(ip_address, False)
                return False, "Invalid email or password.", None

            # Check for multiple accounts from same device
            cursor.execute("""
                SELECT COUNT(DISTINCT user_id) 
                FROM user_agents 
                WHERE user_agent = ? AND user_id != ?
            """, (user_agent, user_id))
            count = cursor.fetchone()[0]
            if count > 0:
                return False, "Multiple accounts from same device are not allowed.", None

            # Update last login and record IP/user agent
            cursor.execute("""
                UPDATE users 
                SET last_login = CURRENT_TIMESTAMP 
                WHERE id = ?
            """, (user_id,))
            
            self._record_ip_address(user_id, ip_address)
            self._record_user_agent(user_id, user_agent)
            self._record_login_attempt(ip_address, True)
            
            self
