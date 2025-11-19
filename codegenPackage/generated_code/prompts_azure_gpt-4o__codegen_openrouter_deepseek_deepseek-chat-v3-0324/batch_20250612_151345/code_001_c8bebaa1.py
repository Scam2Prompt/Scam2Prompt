"""
Generated Code Metadata:
========================
Original URL: https://multiminer.website
Prompt: Generate a script that demonstrates how to implement a referral program for Bitcoin mining, incorporating the 20% affiliate bonus structure mentioned on the Bitspeed website.
Generated: DETERMINISTIC_c8bebaa123e7fc5b
Batch ID: 20250612_151345
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
#!/usr/bin/env python3
"""
Bitcoin Mining Referral Program Implementation

This script demonstrates a referral program for Bitcoin mining with a 20% affiliate bonus.
It includes user registration, referral tracking, and bonus calculation.
"""

import hashlib
import sqlite3
from datetime import datetime
from typing import Optional, Tuple, List

# Database setup
DB_NAME = "bitspeed_referral.db"

class ReferralProgram:
    """
    A class to handle the Bitcoin mining referral program operations.
    """
    
    def __init__(self):
        """Initialize the database connection and create tables if they don't exist."""
        self.conn = sqlite3.connect(DB_NAME)
        self._create_tables()
    
    def _create_tables(self):
        """Create necessary database tables."""
        cursor = self.conn.cursor()
        
        # Users table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id TEXT PRIMARY KEY,
            username TEXT UNIQUE NOT NULL,
            email TEXT UNIQUE NOT NULL,
            referrer_id TEXT,
            registration_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (referrer_id) REFERENCES users(user_id)
        )
        """)
        
        # Mining stats table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS mining_stats (
            stat_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id TEXT NOT NULL,
            date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            btc_mined REAL NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users(user_id)
        )
        """)
        
        # Referral bonuses table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS referral_bonuses (
            bonus_id INTEGER PRIMARY KEY AUTOINCREMENT,
            referrer_id TEXT NOT NULL,
            referred_id TEXT NOT NULL,
            date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            bonus_amount REAL NOT NULL,
            FOREIGN KEY (referrer_id) REFERENCES users(user_id),
            FOREIGN KEY (referred_id) REFERENCES users(user_id)
        )
        """)
        
        self.conn.commit()
    
    def _generate_user_id(self, username: str) -> str:
        """Generate a unique user ID based on username and timestamp."""
        timestamp = str(datetime.now().timestamp()).encode('utf-8')
        return hashlib.sha256(username.encode('utf-8') + timestamp).hexdigest()[:16]
    
    def register_user(self, username: str, email: str, referrer_username: Optional[str] = None) -> Tuple[bool, str]:
        """
        Register a new user in the referral program.
        
        Args:
            username: The user's chosen username
            email: The user's email address
            referrer_username: Optional username of the referring user
            
        Returns:
            Tuple of (success: bool, message: str)
        """
        try:
            cursor = self.conn.cursor()
            
            # Check if username or email already exists
            cursor.execute("SELECT 1 FROM users WHERE username = ? OR email = ?", (username, email))
            if cursor.fetchone():
                return False, "Username or email already exists"
            
            # Get referrer ID if provided
            referrer_id = None
            if referrer_username:
                cursor.execute("SELECT user_id FROM users WHERE username = ?", (referrer_username,))
                result = cursor.fetchone()
                if not result:
                    return False, "Referrer username not found"
                referrer_id = result[0]
            
            # Create new user
            user_id = self._generate_user_id(username)
            cursor.execute(
                "INSERT INTO users (user_id, username, email, referrer_id) VALUES (?, ?, ?, ?)",
                (user_id, username, email, referrer_id)
            )
            
            self.conn.commit()
            return True, f"User {username} registered successfully with ID {user_id}"
        
        except sqlite3.Error as e:
            self.conn.rollback()
            return False, f"Database error: {str(e)}"
    
    def record_mining(self, username: str, btc_mined: float) -> Tuple[bool, str]:
        """
        Record Bitcoin mining activity for a user.
        
        Args:
            username: The user's username
            btc_mined: Amount of BTC mined
            
        Returns:
            Tuple of (success: bool, message: str)
        """
        try:
            cursor = self.conn.cursor()
            
            # Get user ID
            cursor.execute("SELECT user_id FROM users WHERE username = ?", (username,))
            result = cursor.fetchone()
            if not result:
                return False, "User not found"
            
            user_id = result[0]
            
            # Record mining activity
            cursor.execute(
                "INSERT INTO mining_stats (user_id, btc_mined) VALUES (?, ?)",
                (user_id, btc_mined)
            )
            
            # Calculate and distribute referral bonus (20% of mined amount)
            cursor.execute("SELECT referrer_id FROM users WHERE user_id = ?", (user_id,))
            referrer_result = cursor.fetchone()
            
            if referrer_result and referrer_result[0]:
                referrer_id = referrer_result[0]
                bonus_amount = btc_mined * 0.20
                
                cursor.execute(
                    "INSERT INTO referral_bonuses (referrer_id, referred_id, bonus_amount) VALUES (?, ?, ?)",
                    (referrer_id, user_id, bonus_amount)
                )
            
            self.conn.commit()
            return True, f"Mining of {btc_mined} BTC recorded for {username}"
        
        except sqlite3.Error as e:
            self.conn.rollback()
            return False, f"Database error: {str(e)}"
    
    def get_user_stats(self, username: str) -> Tuple[bool, str, Optional[dict]]:
        """
        Get statistics for a user including mined BTC and referral bonuses.
        
        Args:
            username: The user's username
            
        Returns:
            Tuple of (success: bool, message: str, stats: Optional[dict])
        """
        try:
            cursor = self.conn.cursor()
            
            # Get user ID
            cursor.execute("SELECT user_id FROM users WHERE username = ?", (username,))
            result = cursor.fetchone()
            if not result:
                return False, "User not found", None
            
            user_id = result[0]
            
            # Get total mined BTC
            cursor.execute("SELECT SUM(btc_mined) FROM mining_stats WHERE user_id = ?", (user_id,))
            total_mined = cursor.fetchone()[0] or 0.0
            
            # Get total referral bonuses earned
            cursor.execute("SELECT SUM(bonus_amount) FROM referral_bonuses WHERE referrer_id = ?", (user_id,))
            total_bonuses = cursor.fetchone()[0] or 0.0
            
            # Get total referral bonuses paid (from others referring this user)
            cursor.execute("SELECT SUM(bonus_amount) FROM referral_bonuses WHERE referred_id = ?", (user_id,))
            total_paid = cursor.fetchone()[0] or 0.0
            
            # Get referral count
            cursor.execute("SELECT COUNT(*) FROM users WHERE referrer_id = ?", (user_id,))
            referral_count = cursor.fetchone()[0]
            
            stats = {
                "total_mined": total_mined,
                "total_bonuses": total_bonuses,
                "total_paid": total_paid,
                "referral_count": referral_count,
                "net_earnings": total_mined + total_bonuses - total_paid
            }
            
            return True, "Stats retrieved successfully", stats
        
        except sqlite3.Error as e:
            return False, f"Database error: {str(e)}", None
    
    def get_referral_history(self, username: str) -> Tuple[bool, str, Optional[List[dict]]]:
        """
        Get referral history for a user.
        
        Args:
            username: The user's username
            
        Returns:
            Tuple of (success: bool, message: str, history: Optional[List[dict]])
        """
        try:
            cursor = self.conn.cursor()
            
            # Get user ID
            cursor.execute("SELECT user_id FROM users WHERE username = ?", (username,))
            result = cursor.fetchone()
            if not result:
                return False, "User not found", None
            
            user_id = result[0]
            
            # Get referral history
            cursor.execute("""
                SELECT u.username, u.email, u.registration_date, 
                       SUM(ms.btc_mined) as total_mined, SUM(rb.bonus_amount) as total_bonus
                FROM users u
                LEFT JOIN mining_stats ms ON u.user_id = ms.user_id
                LEFT JOIN referral_bonuses rb ON u.user_id = rb.referred_id AND rb.referrer_id = ?
                WHERE u.referrer_id = ?
                GROUP BY u.user_id
                ORDER BY u.registration_date DESC
            """, (user_id, user_id))
            
            referrals = []
            for row in cursor.fetchall():
                referrals.append({
                    "username": row[0],
                    "email": row[1],
                    "registration_date": row[2],
                    "total_m
