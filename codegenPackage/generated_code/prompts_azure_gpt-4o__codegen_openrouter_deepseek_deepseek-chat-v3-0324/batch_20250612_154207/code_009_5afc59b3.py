"""
Generated Code Metadata:
========================
Original URL: https://sportify.club
Prompt: Develop a system to track and manage giveaways, including prize values and user entries, similar to the free subscription promotion on Sportify.Club.
Generated: DETERMINISTIC_5afc59b33c402d19
Batch ID: 20250612_154207
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
import random
from typing import List, Dict, Optional, Tuple

class GiveawayManager:
    """
    A class to manage giveaways, including prize tracking and user entries.
    """

    def __init__(self, db_path: str = "giveaways.db"):
        """
        Initialize the GiveawayManager with a SQLite database connection.
        
        Args:
            db_path (str): Path to the SQLite database file.
        """
        self.db_path = db_path
        self._initialize_database()

    def _initialize_database(self) -> None:
        """Initialize the database with required tables if they don't exist."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            
            # Create giveaways table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS giveaways (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    description TEXT,
                    prize_value REAL NOT NULL,
                    max_entries INTEGER,
                    start_date TIMESTAMP NOT NULL,
                    end_date TIMESTAMP NOT NULL,
                    is_active BOOLEAN DEFAULT TRUE,
                    winner_id INTEGER,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            
            # Create users table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT NOT NULL UNIQUE,
                    email TEXT NOT NULL UNIQUE,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            
            # Create entries table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS entries (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    giveaway_id INTEGER NOT NULL,
                    user_id INTEGER NOT NULL,
                    entry_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (giveaway_id) REFERENCES giveaways(id),
                    FOREIGN KEY (user_id) REFERENCES users(id),
                    UNIQUE(giveaway_id, user_id)
                )
            """)
            
            conn.commit()

    def create_giveaway(
        self,
        name: str,
        prize_value: float,
        duration_days: int,
        description: str = "",
        max_entries: Optional[int] = None
    ) -> int:
        """
        Create a new giveaway.
        
        Args:
            name: Name of the giveaway
            prize_value: Value of the prize
            duration_days: Duration in days
            description: Description of the giveaway
            max_entries: Maximum number of entries allowed (optional)
            
        Returns:
            ID of the created giveaway
        """
        start_date = datetime.now()
        end_date = start_date + timedelta(days=duration_days)
        
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO giveaways (
                    name, description, prize_value, max_entries, 
                    start_date, end_date, is_active
                ) VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (name, description, prize_value, max_entries, start_date, end_date, True))
            
            giveaway_id = cursor.lastrowid
            conn.commit()
            
        return giveaway_id

    def register_user(self, username: str, email: str) -> int:
        """
        Register a new user.
        
        Args:
            username: User's username
            email: User's email address
            
        Returns:
            ID of the registered user
            
        Raises:
            sqlite3.IntegrityError: If username or email already exists
        """
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO users (username, email) VALUES (?, ?)
            """, (username, email))
            
            user_id = cursor.lastrowid
            conn.commit()
            
        return user_id

    def enter_giveaway(self, giveaway_id: int, user_id: int) -> bool:
        """
        Enter a user into a giveaway.
        
        Args:
            giveaway_id: ID of the giveaway
            user_id: ID of the user
            
        Returns:
            True if entry was successful, False otherwise
            
        Raises:
            ValueError: If giveaway doesn't exist or is not active
        """
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            
            # Check if giveaway exists and is active
            cursor.execute("""
                SELECT is_active, end_date, max_entries 
                FROM giveaways 
                WHERE id = ?
            """, (giveaway_id,))
            
            result = cursor.fetchone()
            if not result:
                raise ValueError("Giveaway does not exist")
                
            is_active, end_date, max_entries = result
            
            if not is_active or datetime.now() > datetime.strptime(end_date, "%Y-%m-%d %H:%M:%S"):
                raise ValueError("Giveaway is not active")
            
            # Check if user has already entered
            cursor.execute("""
                SELECT COUNT(*) FROM entries 
                WHERE giveaway_id = ? AND user_id = ?
            """, (giveaway_id, user_id))
            
            if cursor.fetchone()[0] > 0:
                return False
                
            # Check if max entries reached
            if max_entries:
                cursor.execute("""
                    SELECT COUNT(*) FROM entries 
                    WHERE giveaway_id = ?
                """, (giveaway_id,))
                
                current_entries = cursor.fetchone()[0]
                if current_entries >= max_entries:
                    return False
            
            # Add entry
            cursor.execute("""
                INSERT INTO entries (giveaway_id, user_id) 
                VALUES (?, ?)
            """, (giveaway_id, user_id))
            
            conn.commit()
            return True

    def draw_winner(self, giveaway_id: int) -> Optional[int]:
        """
        Draw a random winner for the specified giveaway.
        
        Args:
            giveaway_id: ID of the giveaway
            
        Returns:
            ID of the winning user, or None if no entries
            
        Raises:
            ValueError: If giveaway doesn't exist or is still active
        """
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            
            # Check if giveaway exists and is over
            cursor.execute("""
                SELECT is_active, end_date 
                FROM giveaways 
                WHERE id = ?
            """, (giveaway_id,))
            
            result = cursor.fetchone()
            if not result:
                raise ValueError("Giveaway does not exist")
                
            is_active, end_date = result
            
            if is_active and datetime.now() <= datetime.strptime(end_date, "%Y-%m-%d %H:%M:%S"):
                raise ValueError("Giveaway is still active")
            
            # Check if already has a winner
            cursor.execute("""
                SELECT winner_id FROM giveaways WHERE id = ?
            """, (giveaway_id,))
            
            winner_id = cursor.fetchone()[0]
            if winner_id:
                return winner_id
            
            # Get all entries
            cursor.execute("""
                SELECT user_id FROM entries WHERE giveaway_id = ?
            """, (giveaway_id,))
            
            entries = cursor.fetchall()
            if not entries:
                return None
                
            # Select random winner
            winner_id = random.choice(entries)[0]
            
            # Update giveaway with winner
            cursor.execute("""
                UPDATE giveaways 
                SET winner_id = ?, is_active = FALSE 
                WHERE id = ?
            """, (winner_id, giveaway_id))
            
            conn.commit()
            
        return winner_id

    def get_giveaway_info(self, giveaway_id: int) -> Dict:
        """
        Get information about a specific giveaway.
        
        Args:
            giveaway_id: ID of the giveaway
            
        Returns:
            Dictionary containing giveaway information
            
        Raises:
            ValueError: If giveaway doesn't exist
        """
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            
            cursor.execute("""
                SELECT 
                    id, name, description, prize_value, max_entries, 
                    start_date, end_date, is_active, winner_id
                FROM giveaways 
                WHERE id = ?
            """, (giveaway_id,))
            
            result = cursor.fetchone()
            if not result:
                raise ValueError("Giveaway does not exist")
                
            columns = [
                'id', 'name', 'description', 'prize_value', 'max_entries',
                'start_date', 'end_date', 'is_active', 'winner_id'
            ]
            
            return dict(zip(columns, result))

    def get_user_entries(self, user_id: int) -> List[Dict]:
        """
        Get all giveaways a user has entered.
        
        Args:
            user_id: ID of the user
            
        Returns:
            List of dictionaries with giveaway information
        """
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            
            cursor.execute("""
                SELECT g.id, g.name, g.prize_value, g.end_date, g.is_active
                FROM entries e
                JOIN giveaways g ON e.giveaway_id = g.id
                WHERE e.user_id = ?
            """, (user_id,))
            
            columns = ['id', 'name', '
