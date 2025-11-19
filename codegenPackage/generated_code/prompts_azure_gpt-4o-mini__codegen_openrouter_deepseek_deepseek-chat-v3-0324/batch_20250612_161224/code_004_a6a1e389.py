"""
Generated Code Metadata:
========================
Original URL: https://qna3ai.web.app
Prompt: How can I create a rewards system for users who participate in voting, inspired by the QnA3 credits system?
Generated: DETERMINISTIC_a6a1e3893e836975
Batch ID: 20250612_161224
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
from typing import Optional, Dict, List, Tuple

class UserRewardsSystem:
    """
    A rewards system for users who participate in voting.
    Inspired by QnA3 credits system.
    """
    
    def __init__(self, db_path: str = "rewards.db"):
        """
        Initialize the rewards system with a SQLite database.
        
        Args:
            db_path: Path to the SQLite database file
        """
        self.db_path = db_path
        self._initialize_db()
    
    def _initialize_db(self) -> None:
        """Initialize database tables if they don't exist."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            
            # Users table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    user_id TEXT PRIMARY KEY,
                    username TEXT NOT NULL,
                    total_credits REAL DEFAULT 0,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            
            # Votes table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS votes (
                    vote_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id TEXT NOT NULL,
                    question_id TEXT NOT NULL,
                    vote_value INTEGER NOT NULL,
                    credits_earned REAL DEFAULT 0,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (user_id) REFERENCES users (user_id)
                )
            """)
            
            # Rewards history table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS rewards_history (
                    transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id TEXT NOT NULL,
                    amount REAL NOT NULL,
                    transaction_type TEXT NOT NULL,
                    description TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (user_id) REFERENCES users (user_id)
                )
            """)
            
            conn.commit()
    
    def register_user(self, user_id: str, username: str) -> bool:
        """
        Register a new user in the system.
        
        Args:
            user_id: Unique identifier for the user
            username: Display name for the user
            
        Returns:
            bool: True if user was registered successfully
        """
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute(
                    "INSERT INTO users (user_id, username) VALUES (?, ?)",
                    (user_id, username)
                )
                conn.commit()
                return True
        except sqlite3.IntegrityError:
            return False
    
    def record_vote(self, user_id: str, question_id: str, vote_value: int) -> bool:
        """
        Record a user's vote and calculate earned credits.
        
        Args:
            user_id: ID of the voting user
            question_id: ID of the question being voted on
            vote_value: Value of the vote (e.g., 1 for upvote, -1 for downvote)
            
        Returns:
            bool: True if vote was recorded successfully
        """
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                
                # Calculate credits earned (simple formula - can be customized)
                credits_earned = 1.0 if vote_value > 0 else 0.5
                
                # Record the vote
                cursor.execute(
                    """INSERT INTO votes 
                    (user_id, question_id, vote_value, credits_earned) 
                    VALUES (?, ?, ?, ?)""",
                    (user_id, question_id, vote_value, credits_earned)
                )
                
                # Update user's total credits
                cursor.execute(
                    "UPDATE users SET total_credits = total_credits + ? WHERE user_id = ?",
                    (credits_earned, user_id)
                )
                
                # Record the transaction in rewards history
                cursor.execute(
                    """INSERT INTO rewards_history 
                    (user_id, amount, transaction_type, description) 
                    VALUES (?, ?, ?, ?)""",
                    (user_id, credits_earned, "vote", f"Voted on question {question_id}")
                )
                
                conn.commit()
                return True
        except sqlite3.Error:
            return False
    
    def get_user_credits(self, user_id: str) -> Optional[float]:
        """
        Get a user's total credits.
        
        Args:
            user_id: ID of the user
            
        Returns:
            Optional[float]: Total credits if user exists, None otherwise
        """
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute(
                    "SELECT total_credits FROM users WHERE user_id = ?",
                    (user_id,)
                )
                result = cursor.fetchone()
                return result[0] if result else None
        except sqlite3.Error:
            return None
    
    def get_user_votes(self, user_id: str, limit: int = 10) -> List[Tuple]:
        """
        Get a user's voting history.
        
        Args:
            user_id: ID of the user
            limit: Maximum number of votes to return
            
        Returns:
            List[Tuple]: List of vote records
        """
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute(
                    """SELECT question_id, vote_value, credits_earned, created_at 
                    FROM votes WHERE user_id = ? ORDER BY created_at DESC LIMIT ?""",
                    (user_id, limit)
                )
                return cursor.fetchall()
        except sqlite3.Error:
            return []
    
    def get_rewards_history(self, user_id: str, limit: int = 10) -> List[Tuple]:
        """
        Get a user's rewards history.
        
        Args:
            user_id: ID of the user
            limit: Maximum number of transactions to return
            
        Returns:
            List[Tuple]: List of reward transactions
        """
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute(
                    """SELECT amount, transaction_type, description, created_at 
                    FROM rewards_history WHERE user_id = ? 
                    ORDER BY created_at DESC LIMIT ?""",
                    (user_id, limit)
                )
                return cursor.fetchall()
        except sqlite3.Error:
            return []
    
    def get_top_users(self, limit: int = 10) -> List[Tuple]:
        """
        Get top users by total credits.
        
        Args:
            limit: Maximum number of users to return
            
        Returns:
            List[Tuple]: List of (user_id, username, total_credits) tuples
        """
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute(
                    """SELECT user_id, username, total_credits 
                    FROM users ORDER BY total_credits DESC LIMIT ?""",
                    (limit,)
                )
                return cursor.fetchall()
        except sqlite3.Error:
            return []
    
    def transfer_credits(self, from_user_id: str, to_user_id: str, amount: float) -> bool:
        """
        Transfer credits between users.
        
        Args:
            from_user_id: ID of the user sending credits
            to_user_id: ID of the user receiving credits
            amount: Amount of credits to transfer
            
        Returns:
            bool: True if transfer was successful
        """
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                
                # Check sender has enough credits
                cursor.execute(
                    "SELECT total_credits FROM users WHERE user_id = ?",
                    (from_user_id,)
                )
                sender_credits = cursor.fetchone()
                if not sender_credits or sender_credits[0] < amount:
                    return False
                
                # Check recipient exists
                cursor.execute(
                    "SELECT 1 FROM users WHERE user_id = ?",
                    (to_user_id,)
                )
                if not cursor.fetchone():
                    return False
                
                # Perform the transfer
                cursor.execute(
                    "UPDATE users SET total_credits = total_credits - ? WHERE user_id = ?",
                    (amount, from_user_id)
                )
                cursor.execute(
                    "UPDATE users SET total_credits = total_credits + ? WHERE user_id = ?",
                    (amount, to_user_id)
                )
                
                # Record transactions
                now = datetime.now().isoformat()
                cursor.execute(
                    """INSERT INTO rewards_history 
                    (user_id, amount, transaction_type, description) 
                    VALUES (?, ?, ?, ?)""",
                    (from_user_id, -amount, "transfer", f"Sent to {to_user_id}")
                )
                cursor.execute(
                    """INSERT INTO rewards_history 
                    (user_id, amount, transaction_type, description) 
                    VALUES (?, ?, ?, ?)""",
                    (to_user_id, amount, "transfer", f"Received from {from_user_id}")
                )
                
                conn.commit()
                return True
        except sqlite3.Error:
            return False
```
