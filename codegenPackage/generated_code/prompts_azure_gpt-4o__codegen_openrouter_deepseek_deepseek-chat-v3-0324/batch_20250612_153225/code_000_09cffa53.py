"""
Generated Code Metadata:
========================
Original URL: https://praveenallc.com
Prompt: Write code to develop a custom application that automates daily business activities, ensuring stable security, as described in Praveena LLC's application development services.
Generated: DETERMINISTIC_09cffa532ebf19c2
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Custom Business Automation Application for Praveena LLC
This script automates daily business activities with security best practices.
"""

import os
import logging
from datetime import datetime
import hashlib
import json
import sqlite3
from typing import Dict, List, Optional
import getpass
import bcrypt
import cryptography
from cryptography.fernet import Fernet

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('business_automation.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class SecurityManager:
    """Handles all security-related operations including encryption and authentication."""
    
    def __init__(self):
        self.key = self._load_or_generate_key()
        self.cipher_suite = Fernet(self.key)
    
    def _load_or_generate_key(self) -> bytes:
        """Load encryption key from file or generate a new one."""
        key_file = 'encryption.key'
        if os.path.exists(key_file):
            with open(key_file, 'rb') as f:
                return f.read()
        else:
            key = Fernet.generate_key()
            with open(key_file, 'wb') as f:
                f.write(key)
            os.chmod(key_file, 0o600)  # Restrict file permissions
            return key
    
    def encrypt_data(self, data: str) -> bytes:
        """Encrypt sensitive data."""
        return self.cipher_suite.encrypt(data.encode())
    
    def decrypt_data(self, encrypted_data: bytes) -> str:
        """Decrypt sensitive data."""
        return self.cipher_suite.decrypt(encrypted_data).decode()
    
    @staticmethod
    def hash_password(password: str) -> str:
        """Hash password using bcrypt."""
        return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    
    @staticmethod
    def verify_password(hashed_password: str, user_password: str) -> bool:
        """Verify password against stored hash."""
        return bcrypt.checkpw(user_password.encode(), hashed_password.encode())

class DatabaseManager:
    """Manages database operations with security best practices."""
    
    def __init__(self, db_name: str = 'business_data.db'):
        self.db_name = db_name
        self.security = SecurityManager()
        self._initialize_db()
    
    def _initialize_db(self):
        """Initialize database with required tables."""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            # Create users table with secure password storage
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE NOT NULL,
                    password_hash TEXT NOT NULL,
                    role TEXT NOT NULL,
                    last_login TEXT
                )
            ''')
            
            # Create business activities table with encrypted sensitive data
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS activities (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    activity_name TEXT NOT NULL,
                    description TEXT,
                    scheduled_time TEXT NOT NULL,
                    status TEXT DEFAULT 'pending',
                    sensitive_data BLOB,
                    created_at TEXT DEFAULT CURRENT_TIMESTAMP,
                    updated_at TEXT DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            conn.commit()
    
    def add_user(self, username: str, password: str, role: str) -> bool:
        """Add a new user with hashed password."""
        try:
            hashed_pw = self.security.hash_password(password)
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute(
                    'INSERT INTO users (username, password_hash, role) VALUES (?, ?, ?)',
                    (username, hashed_pw, role)
                )
                conn.commit()
            return True
        except sqlite3.IntegrityError:
            logger.error(f"Username {username} already exists")
            return False
    
    def authenticate_user(self, username: str, password: str) -> bool:
        """Authenticate user against stored credentials."""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(
                'SELECT password_hash FROM users WHERE username = ?',
                (username,)
            )
            result = cursor.fetchone()
        
        if result and self.security.verify_password(result[0], password):
            self._update_last_login(username)
            return True
        return False
    
    def _update_last_login(self, username: str):
        """Update last login timestamp for user."""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(
                'UPDATE users SET last_login = ? WHERE username = ?',
                (datetime.now().isoformat(), username)
            )
            conn.commit()
    
    def log_activity(self, activity_name: str, description: str, scheduled_time: str, sensitive_data: Optional[str] = None) -> bool:
        """Log a business activity with optional sensitive data encryption."""
        try:
            encrypted_data = self.security.encrypt_data(sensitive_data) if sensitive_data else None
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute(
                    '''
                    INSERT INTO activities 
                    (activity_name, description, scheduled_time, sensitive_data)
                    VALUES (?, ?, ?, ?)
                    ''',
                    (activity_name, description, scheduled_time, encrypted_data)
                )
                conn.commit()
            return True
        except Exception as e:
            logger.error(f"Failed to log activity: {e}")
            return False
    
    def get_activities(self, status: Optional[str] = None) -> List[Dict]:
        """Retrieve activities with optional status filter."""
        query = 'SELECT id, activity_name, description, scheduled_time, status FROM activities'
        params = ()
        
        if status:
            query += ' WHERE status = ?'
            params = (status,)
        
        with sqlite3.connect(self.db_name) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute(query, params)
            return [dict(row) for row in cursor.fetchall()]

class BusinessAutomationApp:
    """Main application class for business automation."""
    
    def __init__(self):
        self.db = DatabaseManager()
        self.security = SecurityManager()
        self.current_user = None
    
    def run(self):
        """Main application loop."""
        if not self._authenticate_user():
            logger.error("Authentication failed. Exiting application.")
            return
        
        logger.info(f"Welcome, {self.current_user}!")
        
        while True:
            print("\nBusiness Automation Menu:")
            print("1. Log New Activity")
            print("2. View Pending Activities")
            print("3. View Completed Activities")
            print("4. Exit")
            
            choice = input("Enter your choice (1-4): ")
            
            if choice == '1':
                self._log_new_activity()
            elif choice == '2':
                self._view_activities('pending')
            elif choice == '3':
                self._view_activities('completed')
            elif choice == '4':
                logger.info("Exiting application. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
    
    def _authenticate_user(self) -> bool:
        """Handle user authentication."""
        max_attempts = 3
        attempts = 0
        
        while attempts < max_attempts:
            username = input("Username: ")
            password = getpass.getpass("Password: ")
            
            if self.db.authenticate_user(username, password):
                self.current_user = username
                return True
            
            attempts += 1
            print(f"Invalid credentials. {max_attempts - attempts} attempts remaining.")
        
        return False
    
    def _log_new_activity(self):
        """Handle logging a new business activity."""
        print("\nLog New Business Activity")
        activity_name = input("Activity Name: ")
        description = input("Description: ")
        scheduled_time = input("Scheduled Time (YYYY-MM-DD HH:MM): ")
        sensitive_data = input("Sensitive Data (leave empty if none): ") or None
        
        if self.db.log_activity(activity_name, description, scheduled_time, sensitive_data):
            print("Activity logged successfully!")
        else:
            print("Failed to log activity.")
    
    def _view_activities(self, status: str):
        """Display activities filtered by status."""
        activities = self.db.get_activities(status)
        
        if not activities:
            print(f"No {status} activities found.")
            return
        
        print(f"\n{status.capitalize()} Activities:")
        for idx, activity in enumerate(activities, 1):
            print(f"\nActivity {idx}:")
            print(f"Name: {activity['activity_name']}")
            print(f"Description: {activity['description']}")
            print(f"Scheduled: {activity['scheduled_time']}")
            print(f"Status: {activity['status']}")

if __name__ == "__main__":
    try:
        app = BusinessAutomationApp()
        app.run()
    except KeyboardInterrupt:
        logger.info("Application interrupted by user. Exiting gracefully.")
    except Exception as e:
        logger.error(f
