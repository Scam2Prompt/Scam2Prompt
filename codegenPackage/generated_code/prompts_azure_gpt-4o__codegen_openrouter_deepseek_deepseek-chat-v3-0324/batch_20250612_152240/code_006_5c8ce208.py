"""
Generated Code Metadata:
========================
Original URL: https://appmemekombatclaim.pages.dev
Prompt: Provide code examples for implementing a leaderboard system for Meme Kombat battles, where players can view rankings based on their betting outcomes and rewards earned.
Generated: DETERMINISTIC_5c8ce2081ffddc05
Batch ID: 20250612_152240
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# leaderboard.py
from typing import List, Dict, Optional
from dataclasses import dataclass
import sqlite3
from datetime import datetime
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

@dataclass
class PlayerStats:
    """Data class to hold player statistics for the leaderboard"""
    player_id: str
    username: str
    total_battles: int
    wins: int
    losses: int
    total_wagered: float
    total_earned: float
    win_rate: float
    last_active: datetime

class LeaderboardSystem:
    """Leaderboard system for Meme Kombat battles"""
    
    def __init__(self, db_path: str = 'meme_kombat.db'):
        """Initialize the leaderboard system with database connection"""
        self.db_path = db_path
        self._initialize_database()
    
    def _initialize_database(self) -> None:
        """Create database tables if they don't exist"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS players (
                        player_id TEXT PRIMARY KEY,
                        username TEXT NOT NULL,
                        total_battles INTEGER DEFAULT 0,
                        wins INTEGER DEFAULT 0,
                        losses INTEGER DEFAULT 0,
                        total_wagered REAL DEFAULT 0,
                        total_earned REAL DEFAULT 0,
                        last_active TIMESTAMP
                    )
                ''')
                conn.commit()
        except sqlite3.Error as e:
            logger.error(f"Database initialization failed: {e}")
            raise
    
    def update_player_stats(
        self,
        player_id: str,
        username: str,
        wagered: float,
        earned: float,
        won: bool
    ) -> None:
        """Update player statistics after a battle"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                
                # Get current stats
                cursor.execute('''
                    SELECT total_battles, wins, losses, total_wagered, total_earned 
                    FROM players WHERE player_id = ?
                ''', (player_id,))
                result = cursor.fetchone()
                
                if result:
                    # Update existing player
                    total_battles, wins, losses, total_wagered, total_earned = result
                    total_battles += 1
                    wins += 1 if won else 0
                    losses += 0 if won else 1
                    total_wagered += wagered
                    total_earned += earned
                    
                    cursor.execute('''
                        UPDATE players SET
                            username = ?,
                            total_battles = ?,
                            wins = ?,
                            losses = ?,
                            total_wagered = ?,
                            total_earned = ?,
                            last_active = CURRENT_TIMESTAMP
                        WHERE player_id = ?
                    ''', (username, total_battles, wins, losses, total_wagered, total_earned, player_id))
                else:
                    # Insert new player
                    wins = 1 if won else 0
                    losses = 0 if won else 1
                    cursor.execute('''
                        INSERT INTO players (
                            player_id, username, total_battles, wins, losses,
                            total_wagered, total_earned, last_active
                        ) VALUES (?, ?, 1, ?, ?, ?, ?, CURRENT_TIMESTAMP)
                    ''', (player_id, username, wins, losses, wagered, earned))
                
                conn.commit()
        except sqlite3.Error as e:
            logger.error(f"Failed to update player stats: {e}")
            raise
    
    def get_leaderboard(
        self,
        limit: int = 10,
        sort_by: str = 'total_earned',
        descending: bool = True
    ) -> List[PlayerStats]:
        """Retrieve leaderboard with specified sorting and limit"""
        valid_sort_columns = {
            'total_earned', 'wins', 'win_rate', 'total_wagered', 'last_active'
        }
        
        if sort_by not in valid_sort_columns:
            raise ValueError(f"Invalid sort column. Must be one of: {valid_sort_columns}")
        
        order = 'DESC' if descending else 'ASC'
        
        try:
            with sqlite3.connect(self.db_path) as conn:
                conn.row_factory = sqlite3.Row
                cursor = conn.cursor()
                
                if sort_by == 'win_rate':
                    query = f'''
                        SELECT 
                            player_id, 
                            username, 
                            total_battles, 
                            wins, 
                            losses, 
                            total_wagered, 
                            total_earned,
                            (wins * 1.0 / CASE WHEN total_battles = 0 THEN 1 ELSE total_battles END) AS win_rate,
                            last_active
                        FROM players
                        WHERE total_battles > 0
                        ORDER BY win_rate {order}
                        LIMIT ?
                    '''
                else:
                    query = f'''
                        SELECT 
                            player_id, 
                            username, 
                            total_battles, 
                            wins, 
                            losses, 
                            total_wagered, 
                            total_earned,
                            (wins * 1.0 / CASE WHEN total_battles = 0 THEN 1 ELSE total_battles END) AS win_rate,
                            last_active
                        FROM players
                        ORDER BY {sort_by} {order}
                        LIMIT ?
                    '''
                
                cursor.execute(query, (limit,))
                rows = cursor.fetchall()
                
                leaderboard = []
                for row in rows:
                    leaderboard.append(PlayerStats(
                        player_id=row['player_id'],
                        username=row['username'],
                        total_battles=row['total_battles'],
                        wins=row['wins'],
                        losses=row['losses'],
                        total_wagered=row['total_wagered'],
                        total_earned=row['total_earned'],
                        win_rate=row['win_rate'],
                        last_active=datetime.strptime(row['last_active'], '%Y-%m-%d %H:%M:%S')
                    ))
                
                return leaderboard
        except sqlite3.Error as e:
            logger.error(f"Failed to retrieve leaderboard: {e}")
            raise
    
    def get_player_stats(self, player_id: str) -> Optional[PlayerStats]:
        """Get statistics for a specific player"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                conn.row_factory = sqlite3.Row
                cursor = conn.cursor()
                
                cursor.execute('''
                    SELECT 
                        player_id, 
                        username, 
                        total_battles, 
                        wins, 
                        losses, 
                        total_wagered, 
                        total_earned,
                        (wins * 1.0 / CASE WHEN total_battles = 0 THEN 1 ELSE total_battles END) AS win_rate,
                        last_active
                    FROM players
                    WHERE player_id = ?
                ''', (player_id,))
                
                row = cursor.fetchone()
                if row:
                    return PlayerStats(
                        player_id=row['player_id'],
                        username=row['username'],
                        total_battles=row['total_battles'],
                        wins=row['wins'],
                        losses=row['losses'],
                        total_wagered=row['total_wagered'],
                        total_earned=row['total_earned'],
                        win_rate=row['win_rate'],
                        last_active=datetime.strptime(row['last_active'], '%Y-%m-%d %H:%M:%S')
                    )
                return None
        except sqlite3.Error as e:
            logger.error(f"Failed to get player stats: {e}")
            raise

# Example usage
if __name__ == "__main__":
    leaderboard = LeaderboardSystem()
    
    # Simulate some battles
    leaderboard.update_player_stats("player1", "MemeLord", 10.0, 15.0, True)
    leaderboard.update_player_stats("player2", "DankMaster", 5.0, 0.0, False)
    leaderboard.update_player_stats("player3", "KombatKing", 20.0, 30.0, True)
    leaderboard.update_player_stats("player1", "MemeLord", 15.0, 5.0, False)
    leaderboard.update_player_stats("player3", "KombatKing", 10.0, 20.0, True)
    
    # Get top 5 by total earned
    top_earners = leaderboard.get_leaderboard(limit=5, sort_by='total_earned')
    print("Top Earners:")
    for idx, player in enumerate(top_earners, 1):
        print(f"{idx}. {player.username}: ${player.total_earned:.2f}")
    
    # Get player stats
    player = leaderboard.get_player_stats("player3")
    if player:
        print(f"\nStats for {player.username}:
