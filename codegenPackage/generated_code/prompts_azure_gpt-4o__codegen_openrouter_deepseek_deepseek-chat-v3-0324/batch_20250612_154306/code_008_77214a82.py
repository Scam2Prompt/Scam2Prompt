"""
Generated Code Metadata:
========================
Original URL: https://easydocgestao.com.br
Prompt: Write code to implement a secure document retrieval system for enterprises, incorporating features like categorization and digitalization as highlighted by EasyDoc Gestão.
Generated: DETERMINISTIC_77214a8255533783
Batch ID: 20250612_154306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import uuid
import hashlib
import logging
from typing import List, Dict, Optional
from datetime import datetime
from pathlib import Path
from abc import ABC, abstractmethod
import mimetypes
import shutil
import json
import re
from functools import wraps

# Database and security imports
import sqlite3
from sqlite3 import Error
import bcrypt
from cryptography.fernet import Fernet

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Constants
DATABASE_NAME = "document_management.db"
DOCUMENT_STORAGE = "documents"
KEY_FILE = "encryption.key"
DEFAULT_CATEGORIES = ["Finance", "Legal", "HR", "Operations", "Miscellaneous"]

class DatabaseManager:
    """Handles all database operations."""
    
    def __init__(self, db_name: str = DATABASE_NAME):
        self.db_name = db_name
        self.connection = None
        self._initialize_db()
    
    def _initialize_db(self) -> None:
        """Initialize database tables if they don't exist."""
        try:
            self.connection = sqlite3.connect(self.db_name)
            cursor = self.connection.cursor()
            
            # Users table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE NOT NULL,
                    password_hash TEXT NOT NULL,
                    email TEXT UNIQUE NOT NULL,
                    role TEXT NOT NULL,
                    created_at TEXT NOT NULL,
                    last_login TEXT
                )
            ''')
            
            # Categories table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS categories (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT UNIQUE NOT NULL,
                    description TEXT,
                    created_at TEXT NOT NULL
                )
            ''')
            
            # Documents table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS documents (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    description TEXT,
                    file_name TEXT NOT NULL,
                    file_path TEXT NOT NULL,
                    file_size INTEGER NOT NULL,
                    file_type TEXT NOT NULL,
                    category_id INTEGER,
                    uploaded_by INTEGER NOT NULL,
                    uploaded_at TEXT NOT NULL,
                    last_modified TEXT NOT NULL,
                    FOREIGN KEY (category_id) REFERENCES categories(id),
                    FOREIGN KEY (uploaded_by) REFERENCES users(id)
                )
                ''')
            
            # Document metadata table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS document_metadata (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    document_id INTEGER NOT NULL,
                    key TEXT NOT NULL,
                    value TEXT NOT NULL,
                    FOREIGN KEY (document_id) REFERENCES documents(id)
                )
            ''')
            
            # Document access logs
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS access_logs (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    document_id INTEGER NOT NULL,
                    user_id INTEGER NOT NULL,
                    action TEXT NOT NULL,
                    timestamp TEXT NOT NULL,
                    FOREIGN KEY (document_id) REFERENCES documents(id),
                    FOREIGN KEY (user_id) REFERENCES users(id)
                )
            ''')
            
            self.connection.commit()
            
            # Insert default categories if they don't exist
            for category in DEFAULT_CATEGORIES:
                try:
                    cursor.execute(
                        "INSERT INTO categories (name, created_at) VALUES (?, ?)",
                        (category, datetime.now().isoformat())
                    )
                except sqlite3.IntegrityError:
                    pass
            
            self.connection.commit()
            
        except Error as e:
            logger.error(f"Database initialization error: {e}")
            raise
        finally:
            if cursor:
                cursor.close()
    
    def execute_query(self, query: str, params: tuple = (), commit: bool = False) -> Optional[sqlite3.Cursor]:
        """Execute a SQL query."""
        cursor = None
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, params)
            if commit:
                self.connection.commit()
            return cursor
        except Error as e:
            logger.error(f"Query execution error: {e}")
            if commit:
                self.connection.rollback()
            raise
    
    def close(self) -> None:
        """Close the database connection."""
        if self.connection:
            self.connection.close()

class EncryptionManager:
    """Handles encryption and decryption of sensitive data."""
    
    def __init__(self, key_file: str = KEY_FILE):
        self.key_file = key_file
        self.key = self._load_or_generate_key()
        self.cipher_suite = Fernet(self.key)
    
    def _load_or_generate_key(self) -> bytes:
        """Load encryption key from file or generate a new one."""
        try:
            if os.path.exists(self.key_file):
                with open(self.key_file, 'rb') as f:
                    return f.read()
            else:
                key = Fernet.generate_key()
                with open(self.key_file, 'wb') as f:
                    f.write(key)
                os.chmod(self.key_file, 0o600)  # Restrict permissions
                return key
        except Exception as e:
            logger.error(f"Key management error: {e}")
            raise
    
    def encrypt(self, data: str) -> str:
        """Encrypt data."""
        try:
            return self.cipher_suite.encrypt(data.encode()).decode()
        except Exception as e:
            logger.error(f"Encryption error: {e}")
            raise
    
    def decrypt(self, encrypted_data: str) -> str:
        """Decrypt data."""
        try:
            return self.cipher_suite.decrypt(encrypted_data.encode()).decode()
        except Exception as e:
            logger.error(f"Decryption error: {e}")
            raise

class UserManager:
    """Handles user authentication and management."""
    
    def __init__(self, db_manager: DatabaseManager, encryption_manager: EncryptionManager):
        self.db = db_manager
        self.encryption = encryption_manager
    
    def create_user(self, username: str, password: str, email: str, role: str = "user") -> bool:
        """Create a new user account."""
        try:
            if not self._validate_password(password):
                return False
            
            password_hash = self._hash_password(password)
            encrypted_email = self.encryption.encrypt(email)
            
            query = '''
                INSERT INTO users (username, password_hash, email, role, created_at)
                VALUES (?, ?, ?, ?, ?)
            '''
            params = (
                username,
                password_hash,
                encrypted_email,
                role,
                datetime.now().isoformat()
            )
            
            self.db.execute_query(query, params, commit=True)
            return True
        except Exception as e:
            logger.error(f"User creation error: {e}")
            return False
    
    def authenticate_user(self, username: str, password: str) -> bool:
        """Authenticate a user."""
        try:
            query = "SELECT password_hash FROM users WHERE username = ?"
            cursor = self.db.execute_query(query, (username,))
            result = cursor.fetchone()
            cursor.close()
            
            if result and bcrypt.checkpw(password.encode(), result[0].encode()):
                # Update last login time
                update_query = "UPDATE users SET last_login = ? WHERE username = ?"
                self.db.execute_query(update_query, (datetime.now().isoformat(), username), commit=True)
                return True
            return False
        except Exception as e:
            logger.error(f"Authentication error: {e}")
            return False
    
    def _hash_password(self, password: str) -> str:
        """Hash a password for storage."""
        return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    
    def _validate_password(self, password: str) -> bool:
        """Validate password meets complexity requirements."""
        if len(password) < 8:
            return False
        if not re.search(r"[A-Z]", password):
            return False
        if not re.search(r"[a-z]", password):
            return False
        if not re.search(r"[0-9]", password):
            return False
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
            return False
        return True

class DocumentStorage:
    """Handles document storage and retrieval."""
    
    def __init__(self, storage_path: str = DOCUMENT_STORAGE):
        self.storage_path = Path(storage_path)
        self._initialize_storage()
    
    def _initialize_storage(self) -> None:
        """Create storage directory if it doesn't exist."""
        try:
            self.storage_path.mkdir(exist_ok=True, parents=True)
        except Exception as e:
            logger.error(f"Storage initialization error: {e}")
            raise
    
    def store_document(self, file_data: bytes, file_name: str) -> str:
        """Store a document file and return its path."""
        try:
            # Generate unique filename to prevent collisions
            file_ext = Path(file_name).suffix
            unique_name = f"{uuid.uuid4().hex}{file_ext}"
            file_path = self.storage_path / unique_name
            
            with open(file_path
