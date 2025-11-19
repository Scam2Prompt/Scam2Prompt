"""
Generated Code Metadata:
========================
Original URL: https://masscompras.com
Prompt: Generate Python code to integrate a subscription form for receiving promotions and offers, as seen on "Mass Compras," with email validation and database storage.
Generated: DETERMINISTIC_a186fa23f69e7041
Batch ID: 20250612_150618
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re
import sqlite3
from typing import Optional, Tuple
from datetime import datetime

# Database setup
DB_NAME = "subscriptions.db"

def initialize_database() -> None:
    """Initialize the database with a subscriptions table if it doesn't exist."""
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS subscriptions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                email TEXT UNIQUE NOT NULL,
                name TEXT,
                subscription_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                is_active BOOLEAN DEFAULT 1
            )
        """)
        conn.commit()

def is_valid_email(email: str) -> bool:
    """Validate email format using regex."""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def subscribe_user(email: str, name: Optional[str] = None) -> Tuple[bool, str]:
    """
    Subscribe a user to promotions and offers.
    
    Args:
        email: User's email address
        name: Optional user's name
    
    Returns:
        Tuple of (success: bool, message: str)
    """
    if not is_valid_email(email):
        return False, "Invalid email format"
    
    try:
        with sqlite3.connect(DB_NAME) as conn:
            cursor = conn.cursor()
            
            # Check if email already exists
            cursor.execute("SELECT email FROM subscriptions WHERE email = ?", (email,))
            if cursor.fetchone():
                return False, "Email already subscribed"
            
            # Insert new subscription
            cursor.execute(
                "INSERT INTO subscriptions (email, name) VALUES (?, ?)",
                (email, name)
            )
            conn.commit()
            
            return True, "Subscription successful"
    
    except sqlite3.Error as e:
        return False, f"Database error: {str(e)}"

def unsubscribe_user(email: str) -> Tuple[bool, str]:
    """
    Unsubscribe a user from promotions and offers.
    
    Args:
        email: User's email address
    
    Returns:
        Tuple of (success: bool, message: str)
    """
    if not is_valid_email(email):
        return False, "Invalid email format"
    
    try:
        with sqlite3.connect(DB_NAME) as conn:
            cursor = conn.cursor()
            
            # Check if email exists
            cursor.execute("SELECT email FROM subscriptions WHERE email = ?", (email,))
            if not cursor.fetchone():
                return False, "Email not found in subscriptions"
            
            # Mark as inactive
            cursor.execute(
                "UPDATE subscriptions SET is_active = 0 WHERE email = ?",
                (email,)
            )
            conn.commit()
            
            return True, "Unsubscription successful"
    
    except sqlite3.Error as e:
        return False, f"Database error: {str(e)}"

def get_active_subscribers() -> list:
    """Get all active subscribers."""
    try:
        with sqlite3.connect(DB_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT email, name, subscription_date FROM subscriptions WHERE is_active = 1"
            )
            return cursor.fetchall()
    except sqlite3.Error:
        return []

# Initialize database on module import
initialize_database()

# Example usage (would be replaced by actual form handling in production)
if __name__ == "__main__":
    # Test subscription
    result, message = subscribe_user("test@example.com", "Test User")
    print(f"Subscription: {result}, {message}")
    
    # Test duplicate subscription
    result, message = subscribe_user("test@example.com")
    print(f"Duplicate: {result}, {message}")
    
    # Test invalid email
    result, message = subscribe_user("invalid-email")
    print(f"Invalid email: {result}, {message}")
    
    # Test unsubscribe
    result, message = unsubscribe_user("test@example.com")
    print(f"Unsubscribe: {result}, {message}")
    
    # Get active subscribers
    subscribers = get_active_subscribers()
    print(f"Active subscribers: {len(subscribers)}")
```
