"""
Generated Code Metadata:
========================
Original URL: https://travelobay.com
Prompt: Design a system to implement a VIP program for R7 Casino, using a combination of Python, SQL, and data analysis to track player activity and reward loyalty.
Generated: DETERMINISTIC_c24133a132790dcb
Batch ID: 20250622_205412
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# VIP Program System for R7 Casino
# This system tracks player activity, calculates loyalty points, and manages VIP tiers

import sqlite3
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple
import logging
from dataclasses import dataclass

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Database configuration
DB_NAME = 'r7_casino_vip.db'

@dataclass
class Player:
    """Represents a casino player with VIP information"""
    player_id: int
    name: str
    email: str
    current_tier: str
    loyalty_points: int
    last_activity_date: str
    total_wagered: float

@dataclass
class VIPTier:
    """Represents a VIP tier with requirements and benefits"""
    tier_name: str
    min_points: int
    benefits: List[str]

class VIPProgram:
    """Main class for managing the VIP program"""
    
    def __init__(self):
        self.conn = self._create_connection()
        self._initialize_database()
        self.vip_tiers = self._load_vip_tiers()
        
    def _create_connection(self) -> sqlite3.Connection:
        """Create and return a database connection"""
        try:
            conn = sqlite3.connect(DB_NAME)
            conn.row_factory = sqlite3.Row
            return conn
        except sqlite3.Error as e:
            logger.error(f"Database connection error: {e}")
            raise
            
    def _initialize_database(self):
        """Initialize database tables if they don't exist"""
        try:
            cursor = self.conn.cursor()
            
            # Players table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS players (
                    player_id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    email TEXT UNIQUE NOT NULL,
                    current_tier TEXT DEFAULT 'Bronze',
                    loyalty_points INTEGER DEFAULT 0,
                    last_activity_date TEXT,
                    total_wagered REAL DEFAULT 0
                )
            ''')
            
            # Activity log table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS player_activity (
                    activity_id INTEGER PRIMARY KEY,
                    player_id INTEGER,
                    activity_type TEXT,
                    amount REAL,
                    points_earned INTEGER,
                    activity_date TEXT,
                    FOREIGN KEY(player_id) REFERENCES players(player_id)
                )
            ''')
            
            # VIP tiers table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS vip_tiers (
                    tier_name TEXT PRIMARY KEY,
                    min_points INTEGER,
                    benefits TEXT
                )
            ''')
            
            # Insert default tiers if empty
            cursor.execute('SELECT COUNT(*) FROM vip_tiers')
            if cursor.fetchone()[0] == 0:
                default_tiers = [
                    ('Bronze', 0, 'Basic rewards, email support'),
                    ('Silver', 1000, 'Faster withdrawals, birthday bonus'),
                    ('Gold', 5000, 'Personal account manager, exclusive events'),
                    ('Platinum', 15000, 'Higher withdrawal limits, luxury gifts'),
                    ('Diamond', 30000, 'VIP trips, high roller bonuses')
                ]
                cursor.executemany(
                    'INSERT INTO vip_tiers VALUES (?, ?, ?)',
                    default_tiers
                )
            
            self.conn.commit()
        except sqlite3.Error as e:
            logger.error(f"Database initialization error: {e}")
            self.conn.rollback()
            raise
    
    def _load_vip_tiers(self) -> Dict[str, VIPTier]:
        """Load VIP tiers from database into memory"""
        tiers = {}
        try:
            cursor = self.conn.cursor()
            cursor.execute('SELECT * FROM vip_tiers ORDER BY min_points')
            for row in cursor:
                benefits = row['benefits'].split(', ')
                tiers[row['tier_name']] = VIPTier(
                    tier_name=row['tier_name'],
                    min_points=row['min_points'],
                    benefits=benefits
                )
            return tiers
        except sqlite3.Error as e:
            logger.error(f"Error loading VIP tiers: {e}")
            raise
    
    def register_player(self, name: str, email: str) -> int:
        """Register a new player in the system"""
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                'INSERT INTO players (name, email, last_activity_date) VALUES (?, ?, ?)',
                (name, email, datetime.now().isoformat())
            )
            self.conn.commit()
            return cursor.lastrowid
        except sqlite3.IntegrityError:
            logger.warning(f"Player with email {email} already exists")
            raise ValueError("Email already registered")
        except sqlite3.Error as e:
            logger.error(f"Error registering player: {e}")
            self.conn.rollback()
            raise
    
    def record_activity(self, player_id: int, activity_type: str, amount: float) -> int:
        """
        Record player activity and update loyalty points
        Returns the points earned from this activity
        """
        try:
            points_earned = self._calculate_points(activity_type, amount)
            current_date = datetime.now().isoformat()
            
            cursor = self.conn.cursor()
            
            # Record activity
            cursor.execute(
                '''INSERT INTO player_activity 
                (player_id, activity_type, amount, points_earned, activity_date)
                VALUES (?, ?, ?, ?, ?)''',
                (player_id, activity_type, amount, points_earned, current_date)
            )
            
            # Update player's points and wagered amount
            cursor.execute(
                '''UPDATE players 
                SET loyalty_points = loyalty_points + ?,
                    total_wagered = total_wagered + ?,
                    last_activity_date = ?
                WHERE player_id = ?''',
                (points_earned, amount, current_date, player_id)
            )
            
            # Check for tier promotion
            self._check_tier_promotion(player_id)
            
            self.conn.commit()
            return points_earned
        except sqlite3.Error as e:
            logger.error(f"Error recording activity: {e}")
            self.conn.rollback()
            raise
    
    def _calculate_points(self, activity_type: str, amount: float) -> int:
        """Calculate points based on activity type and amount"""
        point_rates = {
            'slot': 1,      # 1 point per $1 wagered
            'table': 2,     # 2 points per $1 wagered
            'poker': 3,     # 3 points per $1 wagered
            'deposit': 5,   # 5 points per $100 deposited
            'daily_login': 10  # 10 points for daily login
        }
        
        if activity_type not in point_rates:
            raise ValueError(f"Invalid activity type: {activity_type}")
            
        if activity_type == 'deposit':
            return int((amount / 100) * point_rates[activity_type])
        elif activity_type == 'daily_login':
            return point_rates[activity_type]
        else:
            return int(amount * point_rates[activity_type])
    
    def _check_tier_promotion(self, player_id: int):
        """Check if player qualifies for a higher VIP tier"""
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                'SELECT loyalty_points, current_tier FROM players WHERE player_id = ?',
                (player_id,)
            )
            result = cursor.fetchone()
            if not result:
                raise ValueError("Player not found")
                
            current_points = result['loyalty_points']
            current_tier = result['current_tier']
            
            # Find the highest tier the player qualifies for
            new_tier = current_tier
            for tier_name, tier in self.vip_tiers.items():
                if current_points >= tier.min_points:
                    new_tier = tier_name
            
            if new_tier != current_tier:
                cursor.execute(
                    'UPDATE players SET current_tier = ? WHERE player_id = ?',
                    (new_tier, player_id)
                )
                logger.info(f"Player {player_id} promoted to {new_tier} tier")
        except sqlite3.Error as e:
            logger.error(f"Error checking tier promotion: {e}")
            raise
    
    def get_player(self, player_id: int) -> Optional[Player]:
        """Retrieve player information"""
        try:
            cursor = self.conn.cursor()
            cursor.execute('SELECT * FROM players WHERE player_id = ?', (player_id,))
            row = cursor.fetchone()
            if row:
                return Player(
                    player_id=row['player_id'],
                    name=row['name'],
                    email=row['email'],
                    current_tier=row['current_tier'],
                    loyalty_points=row['loyalty_points'],
                    last_activity_date=row['last_activity_date'],
                    total_wagered=row['total_wagered']
                )
            return None
        except sqlite3.Error as e
