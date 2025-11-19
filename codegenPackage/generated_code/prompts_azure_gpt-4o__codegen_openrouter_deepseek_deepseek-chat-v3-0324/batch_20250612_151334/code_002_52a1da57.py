"""
Generated Code Metadata:
========================
Original URL: https://usdtclaim.com
Prompt: Generate code to implement a referral tracking system for a cryptocurrency faucet platform, adhering to the rules outlined by USDT Claim regarding referral limits and inactivity.
Generated: DETERMINISTIC_52a1da570d828859
Batch ID: 20250612_151334
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sqlite3
from datetime import datetime, timedelta
from typing import Optional, Tuple

class ReferralTracker:
    """
    A referral tracking system for a cryptocurrency faucet platform.
    Handles referral limits and inactivity as per USDT Claim rules.
    """
    
    def __init__(self, db_path: str = "referrals.db"):
        """
        Initialize the referral tracker with a SQLite database.
        
        Args:
            db_path: Path to the SQLite database file
        """
        self.conn = sqlite3.connect(db_path)
        self._create_tables()
    
    def _create_tables(self) -> None:
        """
        Create necessary database tables if they don't exist.
        """
        cursor = self.conn.cursor()
        
        # Users table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id TEXT PRIMARY KEY,
            registration_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            is_active BOOLEAN DEFAULT TRUE,
            last_activity TIMESTAMP
        )
        """)
        
        # Referrals table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS referrals (
            referral_id INTEGER PRIMARY KEY AUTOINCREMENT,
            referrer_id TEXT NOT NULL,
            referee_id TEXT NOT NULL,
            referral_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            is_valid BOOLEAN DEFAULT TRUE,
            FOREIGN KEY (referrer_id) REFERENCES users (user_id),
            FOREIGN KEY (referee_id) REFERENCES users (user_id),
            UNIQUE (referrer_id, referee_id)
        )
        """)
        
        # Activity log table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS activity_log (
            log_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id TEXT NOT NULL,
            activity_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            activity_type TEXT NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users (user_id)
        )
        """)
        
        self.conn.commit()
    
    def register_user(self, user_id: str) -> bool:
        """
        Register a new user in the system.
        
        Args:
            user_id: Unique identifier for the user
            
        Returns:
            bool: True if registration was successful, False if user already exists
        """
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                "INSERT INTO users (user_id) VALUES (?)",
                (user_id,)
            )
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False
    
    def record_activity(self, user_id: str, activity_type: str) -> bool:
        """
        Record user activity and update their last activity timestamp.
        
        Args:
            user_id: ID of the user performing the activity
            activity_type: Type of activity (e.g., 'claim', 'login')
            
        Returns:
            bool: True if activity was recorded successfully
        """
        try:
            cursor = self.conn.cursor()
            
            # Record the activity in the log
            cursor.execute(
                "INSERT INTO activity_log (user_id, activity_type) VALUES (?, ?)",
                (user_id, activity_type)
            )
            
            # Update last activity timestamp
            cursor.execute(
                "UPDATE users SET last_activity = CURRENT_TIMESTAMP WHERE user_id = ?",
                (user_id,)
            )
            
            # Mark user as active
            cursor.execute(
                "UPDATE users SET is_active = TRUE WHERE user_id = ?",
                (user_id,)
            )
            
            self.conn.commit()
            return True
        except sqlite3.Error:
            return False
    
    def add_referral(self, referrer_id: str, referee_id: str) -> Tuple[bool, str]:
        """
        Add a new referral relationship between users.
        
        Args:
            referrer_id: ID of the referring user
            referee_id: ID of the referred user
            
        Returns:
            Tuple[bool, str]: (success status, message)
        """
        try:
            cursor = self.conn.cursor()
            
            # Check if referee exists
            cursor.execute("SELECT 1 FROM users WHERE user_id = ?", (referee_id,))
            if not cursor.fetchone():
                return (False, "Referee does not exist")
            
            # Check if referrer exists
            cursor.execute("SELECT 1 FROM users WHERE user_id = ?", (referrer_id,))
            if not cursor.fetchone():
                return (False, "Referrer does not exist")
            
            # Check if referral already exists
            cursor.execute(
                "SELECT 1 FROM referrals WHERE referrer_id = ? AND referee_id = ?",
                (referrer_id, referee_id)
            )
            if cursor.fetchone():
                return (False, "Referral already exists")
            
            # Check referrer's activity status
            cursor.execute(
                "SELECT is_active FROM users WHERE user_id = ?",
                (referrer_id,)
            )
            result = cursor.fetchone()
            if not result or not result[0]:
                return (False, "Referrer is inactive")
            
            # Check referrer's referral count (limit to 10)
            cursor.execute(
                "SELECT COUNT(*) FROM referrals WHERE referrer_id = ? AND is_valid = TRUE",
                (referrer_id,)
            )
            count = cursor.fetchone()[0]
            if count >= 10:
                return (False, "Referral limit reached (max 10)")
            
            # Add the referral
            cursor.execute(
                "INSERT INTO referrals (referrer_id, referee_id) VALUES (?, ?)",
                (referrer_id, referee_id)
            )
            
            self.conn.commit()
            return (True, "Referral added successfully")
            
        except sqlite3.Error as e:
            return (False, f"Database error: {str(e)}")
    
    def check_inactive_users(self, inactivity_days: int = 30) -> None:
        """
        Mark users as inactive if they haven't been active for specified days.
        
        Args:
            inactivity_days: Number of days to consider a user inactive (default 30)
        """
        try:
            cursor = self.conn.cursor()
            cutoff_date = datetime.now() - timedelta(days=inactivity_days)
            
            # Mark inactive users
            cursor.execute(
                "UPDATE users SET is_active = FALSE WHERE last_activity < ?",
                (cutoff_date,)
            )
            
            # Invalidate referrals from inactive users
            cursor.execute("""
            UPDATE referrals SET is_valid = FALSE 
            WHERE referrer_id IN (
                SELECT user_id FROM users WHERE is_active = FALSE
            )
            """)
            
            self.conn.commit()
        except sqlite3.Error:
            # Log error in production
            pass
    
    def get_referral_stats(self, user_id: str) -> dict:
        """
        Get referral statistics for a user.
        
        Args:
            user_id: ID of the user to get stats for
            
        Returns:
            dict: Dictionary containing referral statistics
        """
        stats = {
            'total_referrals': 0,
            'active_referrals': 0,
            'inactive_referrals': 0,
            'is_active': False
        }
        
        try:
            cursor = self.conn.cursor()
            
            # Check if user is active
            cursor.execute(
                "SELECT is_active FROM users WHERE user_id = ?",
                (user_id,)
            )
            result = cursor.fetchone()
            if result:
                stats['is_active'] = bool(result[0])
            
            # Get total referrals
            cursor.execute(
                "SELECT COUNT(*) FROM referrals WHERE referrer_id = ?",
                (user_id,)
            )
            stats['total_referrals'] = cursor.fetchone()[0]
            
            # Get active referrals
            cursor.execute(
                """
                SELECT COUNT(*) FROM referrals 
                WHERE referrer_id = ? AND is_valid = TRUE
                """,
                (user_id,)
            )
            stats['active_referrals'] = cursor.fetchone()[0]
            
            # Get inactive referrals
            stats['inactive_referrals'] = (
                stats['total_referrals'] - stats['active_referrals']
            )
            
        except sqlite3.Error:
            pass
        
        return stats
    
    def close(self) -> None:
        """Close the database connection."""
        self.conn.close()
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
```
