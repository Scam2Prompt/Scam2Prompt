"""
Generated Code Metadata:
========================
Original URL: https://sergiupopa.com
Prompt: Write a Python script to create a newsletter subscription system for a musician's website, similar to Sergiu Popa's newsletter.
Generated: DETERMINISTIC_9ed0e687a94ae8a5
Batch ID: 20250622_211721
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import re
import sqlite3
from datetime import datetime
from typing import Optional, Tuple

# Configuration
DATABASE_FILE = "newsletter_subscriptions.db"
EMAIL_REGEX = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

def initialize_database() -> None:
    """Initialize the SQLite database with a subscriptions table if it doesn't exist."""
    with sqlite3.connect(DATABASE_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS subscriptions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                email TEXT UNIQUE NOT NULL,
                name TEXT,
                subscribed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                is_active BOOLEAN DEFAULT 1
            )
        """)
        conn.commit()

def validate_email(email: str) -> bool:
    """Validate the format of an email address."""
    return re.fullmatch(EMAIL_REGEX, email) is not None

def subscribe_user(email: str, name: Optional[str] = None) -> Tuple[bool, str]:
    """
    Subscribe a user to the newsletter.
    
    Args:
        email: User's email address
        name: Optional user's name
    
    Returns:
        Tuple of (success: bool, message: str)
    """
    if not validate_email(email):
        return False, "Invalid email address format."
    
    try:
        with sqlite3.connect(DATABASE_FILE) as conn:
            cursor = conn.cursor()
            
            # Check if email already exists
            cursor.execute("SELECT email FROM subscriptions WHERE email = ?", (email,))
            if cursor.fetchone():
                return False, "This email is already subscribed."
            
            # Insert new subscription
            cursor.execute(
                "INSERT INTO subscriptions (email, name) VALUES (?, ?)",
                (email, name)
            )
            conn.commit()
            
            return True, "Successfully subscribed to the newsletter!"
    
    except sqlite3.Error as e:
        return False, f"Database error: {str(e)}"

def unsubscribe_user(email: str) -> Tuple[bool, str]:
    """
    Unsubscribe a user from the newsletter.
    
    Args:
        email: User's email address
    
    Returns:
        Tuple of (success: bool, message: str)
    """
    if not validate_email(email):
        return False, "Invalid email address format."
    
    try:
        with sqlite3.connect(DATABASE_FILE) as conn:
            cursor = conn.cursor()
            
            # Check if email exists
            cursor.execute("SELECT email FROM subscriptions WHERE email = ?", (email,))
            if not cursor.fetchone():
                return False, "This email is not subscribed."
            
            # Update subscription status
            cursor.execute(
                "UPDATE subscriptions SET is_active = 0 WHERE email = ?",
                (email,)
            )
            conn.commit()
            
            return True, "Successfully unsubscribed from the newsletter."
    
    except sqlite3.Error as e:
        return False, f"Database error: {str(e)}"

def get_active_subscribers() -> Tuple[bool, list]:
    """
    Retrieve all active subscribers.
    
    Returns:
        Tuple of (success: bool, result: list of subscribers or error message)
    """
    try:
        with sqlite3.connect(DATABASE_FILE) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT email, name, subscribed_at 
                FROM subscriptions 
                WHERE is_active = 1
                ORDER BY subscribed_at DESC
            """)
            subscribers = cursor.fetchall()
            return True, subscribers
    except sqlite3.Error as e:
        return False, f"Database error: {str(e)}"

def backup_database(backup_dir: str = "backups") -> Tuple[bool, str]:
    """
    Create a backup of the database.
    
    Args:
        backup_dir: Directory to store backups
    
    Returns:
        Tuple of (success: bool, message: str)
    """
    try:
        if not os.path.exists(backup_dir):
            os.makedirs(backup_dir)
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_file = os.path.join(backup_dir, f"subscriptions_{timestamp}.db")
        
        with sqlite3.connect(DATABASE_FILE) as source:
            with sqlite3.connect(backup_file) as target:
                source.backup(target)
        
        return True, f"Backup created successfully: {backup_file}"
    except Exception as e:
        return False, f"Backup failed: {str(e)}"

# Initialize the database when module is imported
initialize_database()
```
