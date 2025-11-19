"""
Generated Code Metadata:
========================
Original URL: https://longtradegroup.com
Prompt: Write a Python script that implements a referral program for a cryptocurrency staking platform, allowing users to earn up to 0.50% on referral deposits.
Generated: DETERMINISTIC_d0dd7820b4dbe6fd
Batch ID: 20250612_160309
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sqlite3
from typing import Optional, Tuple
from decimal import Decimal, getcontext

# Configure Decimal precision
getcontext().prec = 6

class ReferralProgram:
    """
    A referral program implementation for a cryptocurrency staking platform.
    Users can earn up to 0.50% on referral deposits.
    """
    
    def __init__(self, db_path: str = 'referral_program.db'):
        """
        Initialize the referral program with a SQLite database.
        
        Args:
            db_path: Path to the SQLite database file
        """
        self.db_path = db_path
        self._initialize_database()
    
    def _initialize_database(self) -> None:
        """
        Create database tables if they don't exist.
        """
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            
            # Users table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    user_id TEXT PRIMARY KEY,
                    referral_code TEXT UNIQUE,
                    referrer_id TEXT,
                    total_earned DECIMAL(18, 8) DEFAULT 0,
                    FOREIGN KEY (referrer_id) REFERENCES users(user_id)
                )
            ''')
            
            # Deposits table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS deposits (
                    deposit_id TEXT PRIMARY KEY,
                    user_id TEXT,
                    amount DECIMAL(18, 8),
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                    referral_bonus_applied BOOLEAN DEFAULT FALSE,
                    FOREIGN KEY (user_id) REFERENCES users(user_id)
                )
            ''')
            
            # Referral earnings table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS referral_earnings (
                    earning_id TEXT PRIMARY KEY,
                    referrer_id TEXT,
                    deposit_id TEXT,
                    amount DECIMAL(18, 8),
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (referrer_id) REFERENCES users(user_id),
                    FOREIGN KEY (deposit_id) REFERENCES deposits(deposit_id)
                )
            ''')
            
            conn.commit()
    
    def register_user(self, user_id: str, referral_code: str, referrer_id: Optional[str] = None) -> bool:
        """
        Register a new user with an optional referrer.
        
        Args:
            user_id: Unique identifier for the user
            referral_code: Unique referral code for the user
            referrer_id: ID of the referring user (optional)
            
        Returns:
            bool: True if registration was successful, False otherwise
        """
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                
                # Check if referrer exists
                if referrer_id:
                    cursor.execute('SELECT 1 FROM users WHERE user_id = ?', (referrer_id,))
                    if not cursor.fetchone():
                        return False
                
                # Insert new user
                cursor.execute('''
                    INSERT INTO users (user_id, referral_code, referrer_id)
                    VALUES (?, ?, ?)
                ''', (user_id, referral_code, referrer_id))
                
                conn.commit()
                return True
        except sqlite3.IntegrityError:
            return False
    
    def record_deposit(self, deposit_id: str, user_id: str, amount: Decimal) -> bool:
        """
        Record a new deposit and apply referral bonus if applicable.
        
        Args:
            deposit_id: Unique identifier for the deposit
            user_id: ID of the user making the deposit
            amount: Deposit amount
            
        Returns:
            bool: True if deposit was recorded successfully, False otherwise
        """
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                
                # Check if user exists
                cursor.execute('SELECT 1 FROM users WHERE user_id = ?', (user_id,))
                if not cursor.fetchone():
                    return False
                
                # Record deposit
                cursor.execute('''
                    INSERT INTO deposits (deposit_id, user_id, amount)
                    VALUES (?, ?, ?)
                ''', (deposit_id, user_id, str(amount)))
                
                # Apply referral bonus
                self._apply_referral_bonus(deposit_id, user_id, amount)
                
                conn.commit()
                return True
        except sqlite3.Error:
            return False
    
    def _apply_referral_bonus(self, deposit_id: str, user_id: str, amount: Decimal) -> None:
        """
        Apply referral bonus to the referrer if applicable.
        
        Args:
            deposit_id: ID of the deposit
            user_id: ID of the user making the deposit
            amount: Deposit amount
        """
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            
            # Get referrer if exists
            cursor.execute('''
                SELECT referrer_id FROM users WHERE user_id = ?
            ''', (user_id,))
            result = cursor.fetchone()
            
            if result and result[0]:
                referrer_id = result[0]
                bonus_percentage = Decimal('0.005')  # 0.50%
                bonus_amount = amount * bonus_percentage
                
                # Record referral earning
                cursor.execute('''
                    INSERT INTO referral_earnings (earning_id, referrer_id, deposit_id, amount)
                    VALUES (?, ?, ?, ?)
                ''', (f'earn_{deposit_id}', referrer_id, deposit_id, str(bonus_amount)))
                
                # Update referrer's total earnings
                cursor.execute('''
                    UPDATE users
                    SET total_earned = total_earned + ?
                    WHERE user_id = ?
                ''', (str(bonus_amount), referrer_id))
                
                # Mark deposit as having referral bonus applied
                cursor.execute('''
                    UPDATE deposits
                    SET referral_bonus_applied = TRUE
                    WHERE deposit_id = ?
                ''', (deposit_id,))
    
    def get_user_earnings(self, user_id: str) -> Optional[Decimal]:
        """
        Get total referral earnings for a user.
        
        Args:
            user_id: ID of the user
            
        Returns:
            Decimal: Total referral earnings, or None if user doesn't exist
        """
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            
            cursor.execute('''
                SELECT total_earned FROM users WHERE user_id = ?
            ''', (user_id,))
            
            result = cursor.fetchone()
            return Decimal(result[0]) if result else None
    
    def get_referral_history(self, user_id: str) -> list[Tuple[str, Decimal, str]]:
        """
        Get referral history for a user.
        
        Args:
            user_id: ID of the user
            
        Returns:
            list: List of tuples containing (deposit_id, amount, timestamp)
        """
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            
            cursor.execute('''
                SELECT re.deposit_id, re.amount, re.timestamp
                FROM referral_earnings re
                WHERE re.referrer_id = ?
                ORDER BY re.timestamp DESC
            ''', (user_id,))
            
            return cursor.fetchall()
```
