"""
Generated Code Metadata:
========================
Original URL: https://beyond-blitz.pages.dev
Prompt: Design a system to distribute airdrops to users based on their engagement metrics on Beyond Blitz.
Generated: DETERMINISTIC_39af21a690eb3dde
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import logging
from typing import Dict, List, Optional
from dataclasses import dataclass
from datetime import datetime
import hashlib
import sqlite3
from sqlite3 import Error

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

@dataclass
class User:
    user_id: str
    wallet_address: str
    engagement_score: float
    last_active: datetime
    airdrop_received: bool = False

@dataclass
class AirdropRules:
    min_engagement: float
    max_users: int
    token_amount: float
    distribution_date: datetime

class AirdropDistributor:
    def __init__(self, db_path: str = 'airdrop.db'):
        self.db_path = db_path
        self._initialize_database()

    def _initialize_database(self) -> None:
        """Initialize the database tables if they don't exist."""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                
                # Users table
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS users (
                        user_id TEXT PRIMARY KEY,
                        wallet_address TEXT NOT NULL,
                        engagement_score REAL NOT NULL,
                        last_active TEXT NOT NULL,
                        airdrop_received INTEGER DEFAULT 0
                    )
                ''')
                
                # Airdrops table
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS airdrops (
                        airdrop_id TEXT PRIMARY KEY,
                        rules_json TEXT NOT NULL,
                        distributed_at TEXT NOT NULL
                    )
                ''')
                
                # Transactions table
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS transactions (
                        transaction_id TEXT PRIMARY KEY,
                        user_id TEXT NOT NULL,
                        airdrop_id TEXT NOT NULL,
                        amount REAL NOT NULL,
                        timestamp TEXT NOT NULL,
                        FOREIGN KEY (user_id) REFERENCES users (user_id),
                        FOREIGN KEY (airdrop_id) REFERENCES airdrops (airdrop_id)
                    )
                ''')
                
                conn.commit()
        except Error as e:
            logger.error(f"Database initialization failed: {e}")
            raise

    def add_user(self, user: User) -> bool:
        """Add a user to the database."""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    INSERT INTO users (user_id, wallet_address, engagement_score, last_active)
                    VALUES (?, ?, ?, ?)
                ''', (
                    user.user_id,
                    user.wallet_address,
                    user.engagement_score,
                    user.last_active.isoformat()
                ))
                conn.commit()
                return True
        except Error as e:
            logger.error(f"Failed to add user {user.user_id}: {e}")
            return False

    def get_eligible_users(self, min_engagement: float, max_users: int) -> List[User]:
        """Get users eligible for airdrop based on engagement score."""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    SELECT user_id, wallet_address, engagement_score, last_active, airdrop_received
                    FROM users
                    WHERE engagement_score >= ? AND airdrop_received = 0
                    ORDER BY engagement_score DESC
                    LIMIT ?
                ''', (min_engagement, max_users))
                
                rows = cursor.fetchall()
                return [
                    User(
                        user_id=row[0],
                        wallet_address=row[1],
                        engagement_score=row[2],
                        last_active=datetime.fromisoformat(row[3]),
                        airdrop_received=bool(row[4])
                    ) for row in rows
                ]
        except Error as e:
            logger.error(f"Failed to get eligible users: {e}")
            return []

    def create_airdrop(self, rules: AirdropRules) -> Optional[str]:
        """Create a new airdrop campaign."""
        airdrop_id = hashlib.sha256(
            f"{rules.min_engagement}{rules.max_users}{rules.distribution_date.isoformat()}".encode()
        ).hexdigest()
        
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    INSERT INTO airdrops (airdrop_id, rules_json, distributed_at)
                    VALUES (?, ?, ?)
                ''', (
                    airdrop_id,
                    json.dumps({
                        'min_engagement': rules.min_engagement,
                        'max_users': rules.max_users,
                        'token_amount': rules.token_amount,
                        'distribution_date': rules.distribution_date.isoformat()
                    }),
                    rules.distribution_date.isoformat()
                ))
                conn.commit()
                return airdrop_id
        except Error as e:
            logger.error(f"Failed to create airdrop: {e}")
            return None

    def distribute_airdrop(self, airdrop_id: str) -> Dict[str, int]:
        """Distribute tokens to eligible users for a specific airdrop."""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                
                # Get airdrop rules
                cursor.execute('''
                    SELECT rules_json FROM airdrops WHERE airdrop_id = ?
                ''', (airdrop_id,))
                row = cursor.fetchone()
                if not row:
                    raise ValueError("Airdrop not found")
                
                rules_data = json.loads(row[0])
                rules = AirdropRules(
                    min_engagement=rules_data['min_engagement'],
                    max_users=rules_data['max_users'],
                    token_amount=rules_data['token_amount'],
                    distribution_date=datetime.fromisoformat(rules_data['distribution_date'])
                )
                
                # Get eligible users
                users = self.get_eligible_users(rules.min_engagement, rules.max_users)
                if not users:
                    logger.info("No eligible users for airdrop")
                    return {'success': 0, 'failed': 0}
                
                # Process distribution
                success = 0
                failed = 0
                distribution_time = datetime.utcnow().isoformat()
                
                for user in users:
                    try:
                        # In a real system, this would call a blockchain transaction
                        transaction_id = hashlib.sha256(
                            f"{user.user_id}{airdrop_id}{distribution_time}".encode()
                        ).hexdigest()
                        
                        cursor.execute('''
                            INSERT INTO transactions (transaction_id, user_id, airdrop_id, amount, timestamp)
                            VALUES (?, ?, ?, ?, ?)
                        ''', (
                            transaction_id,
                            user.user_id,
                            airdrop_id,
                            rules.token_amount,
                            distribution_time
                        ))
                        
                        cursor.execute('''
                            UPDATE users SET airdrop_received = 1 WHERE user_id = ?
                        ''', (user.user_id,))
                        
                        success += 1
                    except Error as e:
                        logger.error(f"Failed to distribute to user {user.user_id}: {e}")
                        failed += 1
                
                conn.commit()
                return {'success': success, 'failed': failed}
        except Error as e:
            logger.error(f"Airdrop distribution failed: {e}")
            return {'success': 0, 'failed': 0}
        except Exception as e:
            logger.error(f"Unexpected error during distribution: {e}")
            return {'success': 0, 'failed': 0}

    def get_user_airdrops(self, user_id: str) -> List[Dict]:
        """Get all airdrops received by a user."""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    SELECT t.amount, a.rules_json, t.timestamp
                    FROM transactions t
                    JOIN airdrops a ON t.airdrop_id = a.airdrop_id
                    WHERE t.user_id = ?
                ''', (user_id,))
                
                rows = cursor.fetchall()
                return [
                    {
                        'amount': row[0],
                        'rules': json.loads(row[1]),
                        'timestamp': row[2]
                    } for row in rows
                ]
        except Error as e:
            logger.error(f"Failed to get user airdrops: {e}")
            return []
```
