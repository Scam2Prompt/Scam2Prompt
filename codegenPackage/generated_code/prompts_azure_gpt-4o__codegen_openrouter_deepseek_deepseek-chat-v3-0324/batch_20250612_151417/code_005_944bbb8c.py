"""
Generated Code Metadata:
========================
Original URL: https://excelwithsmart.com
Prompt: Write code to manage referrals for a training program, including tracking enrollments and rewards, similar to the referral system described on SMART Training Resources' website.
Generated: DETERMINISTIC_944bbb8ce05baa02
Batch ID: 20250612_151417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sqlite3
from typing import Optional, List, Dict, Tuple
from dataclasses import dataclass
from datetime import datetime
import hashlib
import uuid

# Database setup constants
DATABASE_NAME = "referral_system.db"

@dataclass
class User:
    """Represents a user in the referral system."""
    id: str
    name: str
    email: str
    join_date: datetime
    is_active: bool = True

@dataclass
class Referral:
    """Represents a referral relationship between users."""
    id: str
    referrer_id: str
    referred_id: str
    referral_date: datetime
    is_completed: bool = False

@dataclass
class Enrollment:
    """Represents a training program enrollment."""
    id: str
    user_id: str
    program_id: str
    enrollment_date: datetime
    completion_date: Optional[datetime] = None
    is_paid: bool = False

@dataclass
class Reward:
    """Represents a reward for successful referrals."""
    id: str
    referral_id: str
    reward_type: str
    amount: float
    issue_date: datetime
    is_claimed: bool = False

class ReferralSystem:
    """Manages the referral program including tracking enrollments and rewards."""
    
    def __init__(self):
        """Initialize the database connection and create tables if they don't exist."""
        self.conn = sqlite3.connect(DATABASE_NAME)
        self._create_tables()
    
    def _create_tables(self) -> None:
        """Create necessary tables in the database."""
        cursor = self.conn.cursor()
        
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            join_date TEXT NOT NULL,
            is_active INTEGER DEFAULT 1
        )
        """)
        
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS referrals (
            id TEXT PRIMARY KEY,
            referrer_id TEXT NOT NULL,
            referred_id TEXT NOT NULL,
            referral_date TEXT NOT NULL,
            is_completed INTEGER DEFAULT 0,
            FOREIGN KEY (referrer_id) REFERENCES users(id),
            FOREIGN KEY (referred_id) REFERENCES users(id)
        )
        """)
        
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS enrollments (
            id TEXT PRIMARY KEY,
            user_id TEXT NOT NULL,
            program_id TEXT NOT NULL,
            enrollment_date TEXT NOT NULL,
            completion_date TEXT,
            is_paid INTEGER DEFAULT 0,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
        """)
        
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS rewards (
            id TEXT PRIMARY KEY,
            referral_id TEXT NOT NULL,
            reward_type TEXT NOT NULL,
            amount REAL NOT NULL,
            issue_date TEXT NOT NULL,
            is_claimed INTEGER DEFAULT 0,
            FOREIGN KEY (referral_id) REFERENCES referrals(id)
        )
        """)
        
        self.conn.commit()
    
    def add_user(self, name: str, email: str) -> User:
        """Add a new user to the system."""
        try:
            user_id = str(uuid.uuid4())
            join_date = datetime.now().isoformat()
            
            cursor = self.conn.cursor()
            cursor.execute(
                "INSERT INTO users (id, name, email, join_date) VALUES (?, ?, ?, ?)",
                (user_id, name, email, join_date)
            )
            self.conn.commit()
            
            return User(user_id, name, email, datetime.fromisoformat(join_date))
        except sqlite3.IntegrityError:
            raise ValueError("Email already exists in the system")
    
    def create_referral(self, referrer_id: str, referred_email: str) -> Referral:
        """Create a new referral relationship."""
        try:
            # Check if referrer exists and is active
            cursor = self.conn.cursor()
            cursor.execute(
                "SELECT id, name, email, join_date, is_active FROM users WHERE id = ?",
                (referrer_id,)
            )
            referrer_data = cursor.fetchone()
            
            if not referrer_data or not referrer_data[4]:
                raise ValueError("Referrer does not exist or is inactive")
            
            # Check if referred user exists
            cursor.execute(
                "SELECT id, name, email, join_date, is_active FROM users WHERE email = ?",
                (referred_email,)
            )
            referred_data = cursor.fetchone()
            
            if not referred_data:
                raise ValueError("Referred email not found in system")
            
            referred_id = referred_data[0]
            
            # Check if referral already exists
            cursor.execute(
                "SELECT id FROM referrals WHERE referrer_id = ? AND referred_id = ?",
                (referrer_id, referred_id)
            )
            if cursor.fetchone():
                raise ValueError("Referral relationship already exists")
            
            # Create new referral
            referral_id = str(uuid.uuid4())
            referral_date = datetime.now().isoformat()
            
            cursor.execute(
                "INSERT INTO referrals (id, referrer_id, referred_id, referral_date) VALUES (?, ?, ?, ?)",
                (referral_id, referrer_id, referred_id, referral_date)
            )
            self.conn.commit()
            
            return Referral(
                referral_id,
                referrer_id,
                referred_id,
                datetime.fromisoformat(referral_date)
            )
        except sqlite3.Error as e:
            raise RuntimeError(f"Database error: {str(e)}")
    
    def add_enrollment(self, user_id: str, program_id: str) -> Enrollment:
        """Add a new enrollment for a user."""
        try:
            # Check if user exists
            cursor = self.conn.cursor()
            cursor.execute(
                "SELECT id FROM users WHERE id = ? AND is_active = 1",
                (user_id,)
            )
            if not cursor.fetchone():
                raise ValueError("User does not exist or is inactive")
            
            enrollment_id = str(uuid.uuid4())
            enrollment_date = datetime.now().isoformat()
            
            cursor.execute(
                "INSERT INTO enrollments (id, user_id, program_id, enrollment_date) VALUES (?, ?, ?, ?)",
                (enrollment_id, user_id, program_id, enrollment_date)
            )
            self.conn.commit()
            
            return Enrollment(
                enrollment_id,
                user_id,
                program_id,
                datetime.fromisoformat(enrollment_date)
            )
        except sqlite3.Error as e:
            raise RuntimeError(f"Database error: {str(e)}")
    
    def complete_enrollment(self, enrollment_id: str, is_paid: bool = True) -> None:
        """Mark an enrollment as completed and optionally paid."""
        try:
            completion_date = datetime.now().isoformat()
            
            cursor = self.conn.cursor()
            cursor.execute(
                "UPDATE enrollments SET completion_date = ?, is_paid = ? WHERE id = ?",
                (completion_date, int(is_paid), enrollment_id)
            )
            
            if cursor.rowcount == 0:
                raise ValueError("Enrollment not found")
            
            self.conn.commit()
            
            # Check if this completes any referrals
            self._check_completed_referrals(enrollment_id)
        except sqlite3.Error as e:
            raise RuntimeError(f"Database error: {str(e)}")
    
    def _check_completed_referrals(self, enrollment_id: str) -> None:
        """Check if any referrals should be marked as completed and issue rewards."""
        try:
            cursor = self.conn.cursor()
            
            # Get the user ID from the enrollment
            cursor.execute(
                "SELECT user_id FROM enrollments WHERE id = ? AND is_paid = 1",
                (enrollment_id,)
            )
            enrollment_data = cursor.fetchone()
            
            if not enrollment_data:
                return
            
            user_id = enrollment_data[0]
            
            # Find referrals for this user that aren't completed yet
            cursor.execute(
                """SELECT r.id, r.referrer_id 
                FROM referrals r 
                WHERE r.referred_id = ? AND r.is_completed = 0""",
                (user_id,)
            )
            referrals = cursor.fetchall()
            
            for referral_id, referrer_id in referrals:
                # Mark referral as completed
                cursor.execute(
                    "UPDATE referrals SET is_completed = 1 WHERE id = ?",
                    (referral_id,)
                )
                
                # Issue reward
                self._issue_reward(referral_id, referrer_id)
            
            self.conn.commit()
        except sqlite3.Error as e:
            raise RuntimeError(f"Database error: {str(e)}")
    
    def _issue_reward(self, referral_id: str, referrer_id: str) -> Reward:
        """Issue a reward for a completed referral."""
        try:
            reward_id = str(uuid.uuid4())
            reward_type = "credit"  # Could be configurable
            amount = 50.00  # Could be configurable
            issue_date = datetime.now().isoformat()
            
            cursor = self.conn.cursor()
            cursor.execute(
                """INSERT INTO rewards 
                (id, referral_id, reward_type, amount, issue
