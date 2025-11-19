"""
Generated Code Metadata:
========================
Original URL: https://www.cosmicrewards.com
Prompt: How can I implement an affiliate program similar to Cosmic Rewards that allows users to earn gift cards through gameplay?
Generated: DETERMINISTIC_9e63154e679a5c03
Batch ID: 20250612_164110
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a Python implementation for an affiliate program system with gift card rewards:

```python
import uuid
from datetime import datetime, timedelta
from typing import Dict, List, Optional
import sqlite3
from sqlite3 import IntegrityError
import random
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class AffiliateProgram:
    """A class to manage an affiliate program with gift card rewards."""
    
    def __init__(self, db_path: str = 'affiliate_program.db'):
        """Initialize the affiliate program with database connection."""
        self.db_path = db_path
        self._initialize_db()
    
    def _initialize_db(self) -> None:
        """Create database tables if they don't exist."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            
            # Users table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    user_id TEXT PRIMARY KEY,
                    username TEXT UNIQUE NOT NULL,
                    email TEXT UNIQUE NOT NULL,
                    join_date DATETIME DEFAULT CURRENT_TIMESTAMP,
                    points INTEGER DEFAULT 0,
                    is_active BOOLEAN DEFAULT TRUE
                )
            ''')
            
            # Affiliates table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS affiliates (
                    affiliate_id TEXT PRIMARY KEY,
                    user_id TEXT UNIQUE NOT NULL,
                    referral_code TEXT UNIQUE NOT NULL,
                    total_referrals INTEGER DEFAULT 0,
                    total_earnings REAL DEFAULT 0.0,
                    FOREIGN KEY (user_id) REFERENCES users (user_id)
                )
            ''')
            
            # Referrals table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS referrals (
                    referral_id TEXT PRIMARY KEY,
                    affiliate_id TEXT NOT NULL,
                    referred_user_id TEXT UNIQUE NOT NULL,
                    referral_date DATETIME DEFAULT CURRENT_TIMESTAMP,
                    is_converted BOOLEAN DEFAULT FALSE,
                    conversion_date DATETIME,
                    points_earned INTEGER DEFAULT 0,
                    FOREIGN KEY (affiliate_id) REFERENCES affiliates (affiliate_id),
                    FOREIGN KEY (referred_user_id) REFERENCES users (user_id)
                )
            ''')
            
            # Gift cards table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS gift_cards (
                    gift_card_id TEXT PRIMARY KEY,
                    name TEXT NOT NULL,
                    description TEXT,
                    point_cost INTEGER NOT NULL,
                    stock INTEGER DEFAULT 0,
                    is_active BOOLEAN DEFAULT TRUE
                )
            ''')
            
            # Redemptions table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS redemptions (
                    redemption_id TEXT PRIMARY KEY,
                    user_id TEXT NOT NULL,
                    gift_card_id TEXT NOT NULL,
                    redemption_date DATETIME DEFAULT CURRENT_TIMESTAMP,
                    points_spent INTEGER NOT NULL,
                    status TEXT DEFAULT 'pending',
                    code TEXT,
                    FOREIGN KEY (user_id) REFERENCES users (user_id),
                    FOREIGN KEY (gift_card_id) REFERENCES gift_cards (gift_card_id)
                )
            ''')
            
            conn.commit()
    
    def create_user(self, username: str, email: str) -> Optional[str]:
        """Create a new user and return user_id."""
        user_id = str(uuid.uuid4())
        
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute(
                    'INSERT INTO users (user_id, username, email) VALUES (?, ?, ?)',
                    (user_id, username, email)
                )
                conn.commit()
                return user_id
        except IntegrityError as e:
            logger.error(f"Error creating user: {e}")
            return None
    
    def register_affiliate(self, user_id: str) -> Optional[str]:
        """Register a user as an affiliate and return referral code."""
        referral_code = self._generate_referral_code()
        affiliate_id = str(uuid.uuid4())
        
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute(
                    '''INSERT INTO affiliates 
                    (affiliate_id, user_id, referral_code) 
                    VALUES (?, ?, ?)''',
                    (affiliate_id, user_id, referral_code)
                )
                conn.commit()
                return referral_code
        except IntegrityError as e:
            logger.error(f"Error registering affiliate: {e}")
            return None
    
    def _generate_referral_code(self) -> str:
        """Generate a unique referral code."""
        return ''.join(random.choices('ABCDEFGHJKLMNPQRSTUVWXYZ23456789', k=8))
    
    def add_referral(self, referral_code: str, referred_user_id: str) -> bool:
        """Record a new referral."""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                
                # Get affiliate_id from referral code
                cursor.execute(
                    'SELECT affiliate_id FROM affiliates WHERE referral_code = ?',
                    (referral_code,)
                )
                result = cursor.fetchone()
                
                if not result:
                    return False
                
                affiliate_id = result[0]
                referral_id = str(uuid.uuid4())
                
                # Add referral
                cursor.execute(
                    '''INSERT INTO referrals 
                    (referral_id, affiliate_id, referred_user_id) 
                    VALUES (?, ?, ?)''',
                    (referral_id, affiliate_id, referred_user_id)
                )
                
                conn.commit()
                return True
        except IntegrityError as e:
            logger.error(f"Error adding referral: {e}")
            return False
    
    def add_game_points(self, user_id: str, points: int) -> bool:
        """Add points to a user's account from gameplay."""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute(
                    'UPDATE users SET points = points + ? WHERE user_id = ?',
                    (points, user_id)
                )
                conn.commit()
                return True
        except sqlite3.Error as e:
            logger.error(f"Error adding points: {e}")
            return False
    
    def convert_referral(self, referred_user_id: str, points: int = 100) -> bool:
        """Convert a referral when the referred user meets requirements."""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                
                # Update referral status
                cursor.execute(
                    '''UPDATE referrals 
                    SET is_converted = TRUE, 
                        conversion_date = CURRENT_TIMESTAMP,
                        points_earned = ?
                    WHERE referred_user_id = ?''',
                    (points, referred_user_id)
                )
                
                # Get affiliate_id
                cursor.execute(
                    '''SELECT affiliate_id FROM referrals 
                    WHERE referred_user_id = ?''',
                    (referred_user_id,)
                )
                result = cursor.fetchone()
                
                if not result:
                    return False
                
                affiliate_id = result[0]
                
                # Update affiliate stats
                cursor.execute(
                    '''UPDATE affiliates 
                    SET total_referrals = total_referrals + 1 
                    WHERE affiliate_id = ?''',
                    (affiliate_id,)
                )
                
                # Add points to both users
                self.add_game_points(referred_user_id, points)
                
                # Get user_id from affiliate_id
                cursor.execute(
                    'SELECT user_id FROM affiliates WHERE affiliate_id = ?',
                    (affiliate_id,)
                )
                result = cursor.fetchone()
                
                if result:
                    affiliate_user_id = result[0]
                    self.add_game_points(affiliate_user_id, points * 2)  # Bonus for affiliate
                
                conn.commit()
                return True
        except sqlite3.Error as e:
            logger.error(f"Error converting referral: {e}")
            return False
    
    def add_gift_card(self, name: str, description: str, point_cost: int, stock: int) -> Optional[str]:
        """Add a new gift card option."""
        gift_card_id = str(uuid.uuid4())
        
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute(
                    '''INSERT INTO gift_cards 
                    (gift_card_id, name, description, point_cost, stock) 
                    VALUES (?, ?, ?, ?, ?)''',
                    (gift_card_id, name, description, point_cost, stock)
                )
                conn.commit()
                return gift_card_id
        except IntegrityError as e:
            logger.error(f"Error adding gift card: {e}")
            return None
    
    def redeem_gift_card(self, user_id: str, gift_card_id: str) -> Optional[str]:
        """Redeem a gift card for a user."""
        redemption_id = str(uuid.uuid4())
        code = self._generate_gift_card_code()
        
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                
                # Check if gift card is available
                cursor.execute(
                    '''SELECT point_cost, stock FROM gift_cards 
                    WHERE gift_card_id = ? AND is_active = TRUE AND stock > 0''
