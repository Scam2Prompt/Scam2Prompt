"""
Generated Code Metadata:
========================
Original URL: https://rewards-memeficlub.pages.dev
Prompt: Generate code for a simple idle game with leaderboard functionality, similar to MemeFi Club's game mechanics.
Generated: DETERMINISTIC_9a52fa917a984cc0
Batch ID: 20250622_211444
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import random
import time
from typing import Dict, List, Optional
import sqlite3
from dataclasses import dataclass
from datetime import datetime
import hashlib
import uuid

# Database setup constants
DB_NAME = "idle_game.db"

@dataclass
class Player:
    id: str
    name: str
    coins: int
    coins_per_second: int
    last_active: float
    upgrades: Dict[str, int]

@dataclass
class LeaderboardEntry:
    player_id: str
    player_name: str
    total_coins: int
    last_active: datetime

class IdleGame:
    def __init__(self):
        self._initialize_database()
        self.upgrade_costs = {
            "click_power": lambda level: 10 + (level * 5),
            "auto_clicker": lambda level: 50 + (level * 20),
            "mega_clicker": lambda level: 200 + (level * 100)
        }
        self.upgrade_effects = {
            "click_power": lambda level: 1 + level,
            "auto_clicker": lambda level: level,
            "mega_clicker": lambda level: level * 5
        }

    def _initialize_database(self):
        """Initialize the SQLite database with required tables."""
        with sqlite3.connect(DB_NAME) as conn:
            cursor = conn.cursor()
            
            # Players table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS players (
                    id TEXT PRIMARY KEY,
                    name TEXT NOT NULL,
                    coins INTEGER NOT NULL,
                    coins_per_second INTEGER NOT NULL,
                    last_active REAL NOT NULL,
                    upgrades TEXT NOT NULL
                )
            """)
            
            # Leaderboard table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS leaderboard (
                    player_id TEXT PRIMARY KEY,
                    player_name TEXT NOT NULL,
                    total_coins INTEGER NOT NULL,
                    last_active TEXT NOT NULL,
                    FOREIGN KEY(player_id) REFERENCES players(id)
                )
            """)
            conn.commit()

    def _get_db_connection(self):
        """Get a database connection with row factory set."""
        conn = sqlite3.connect(DB_NAME)
        conn.row_factory = sqlite3.Row
        return conn

    def create_player(self, name: str) -> Player:
        """Create a new player with initial values."""
        player_id = str(uuid.uuid4())
        now = time.time()
        initial_upgrades = {"click_power": 0, "auto_clicker": 0, "mega_clicker": 0}
        
        player = Player(
            id=player_id,
            name=name,
            coins=0,
            coins_per_second=0,
            last_active=now,
            upgrades=initial_upgrades
        )
        
        with self._get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO players VALUES (?, ?, ?, ?, ?, ?)",
                (
                    player.id,
                    player.name,
                    player.coins,
                    player.coins_per_second,
                    player.last_active,
                    json.dumps(player.upgrades)
                )
            )
            conn.commit()
        
        return player

    def get_player(self, player_id: str) -> Optional[Player]:
        """Retrieve a player by their ID."""
        with self._get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM players WHERE id = ?", (player_id,))
            row = cursor.fetchone()
            
            if not row:
                return None
                
            return Player(
                id=row["id"],
                name=row["name"],
                coins=row["coins"],
                coins_per_second=row["coins_per_second"],
                last_active=row["last_active"],
                upgrades=json.loads(row["upgrades"])
            )

    def update_player(self, player: Player) -> bool:
        """Update player data in the database."""
        with self._get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                UPDATE players 
                SET name = ?, coins = ?, coins_per_second = ?, last_active = ?, upgrades = ?
                WHERE id = ?
                """,
                (
                    player.name,
                    player.coins,
                    player.coins_per_second,
                    player.last_active,
                    json.dumps(player.upgrades),
                    player.id
                )
            )
            conn.commit()
            return cursor.rowcount > 0

    def click(self, player_id: str) -> Optional[Player]:
        """Handle a player click action."""
        player = self.get_player(player_id)
        if not player:
            return None
            
        click_power = self.upgrade_effects["click_power"](player.upgrades["click_power"])
        player.coins += click_power
        player.last_active = time.time()
        
        self.update_player(player)
        return player

    def calculate_offline_earnings(self, player_id: str) -> Optional[Player]:
        """Calculate coins earned while offline."""
        player = self.get_player(player_id)
        if not player:
            return None
            
        now = time.time()
        time_diff = now - player.last_active
        coins_earned = int(time_diff * player.coins_per_second)
        
        player.coins += coins_earned
        player.last_active = now
        
        self.update_player(player)
        return player

    def purchase_upgrade(self, player_id: str, upgrade_type: str) -> Optional[Player]:
        """Purchase an upgrade for the player."""
        player = self.get_player(player_id)
        if not player:
            return None
            
        if upgrade_type not in self.upgrade_costs:
            return None
            
        current_level = player.upgrades[upgrade_type]
        cost = self.upgrade_costs[upgrade_type](current_level)
        
        if player.coins < cost:
            return None
            
        player.coins -= cost
        player.upgrades[upgrade_type] += 1
        
        # Recalculate coins per second
        auto_clicker = self.upgrade_effects["auto_clicker"](player.upgrades["auto_clicker"])
        mega_clicker = self.upgrade_effects["mega_clicker"](player.upgrades["mega_clicker"])
        player.coins_per_second = auto_clicker + mega_clicker
        
        player.last_active = time.time()
        self.update_player(player)
        return player

    def update_leaderboard(self, player_id: str) -> bool:
        """Update the leaderboard with player's current stats."""
        player = self.get_player(player_id)
        if not player:
            return False
            
        now = datetime.now().isoformat()
        
        with self._get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                INSERT OR REPLACE INTO leaderboard 
                VALUES (?, ?, ?, ?)
                """,
                (
                    player.id,
                    player.name,
                    player.coins,
                    now
                )
            )
            conn.commit()
            return cursor.rowcount > 0

    def get_leaderboard(self, limit: int = 10) -> List[LeaderboardEntry]:
        """Retrieve the top players from the leaderboard."""
        with self._get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                SELECT player_id, player_name, total_coins, last_active 
                FROM leaderboard 
                ORDER BY total_coins DESC 
                LIMIT ?
                """,
                (limit,)
            )
            
            return [
                LeaderboardEntry(
                    player_id=row["player_id"],
                    player_name=row["player_name"],
                    total_coins=row["total_coins"],
                    last_active=datetime.fromisoformat(row["last_active"])
                )
                for row in cursor.fetchall()
            ]

# Example usage
if __name__ == "__main__":
    game = IdleGame()
    
    # Create a new player
    player = game.create_player("TestPlayer")
    print(f"Created player: {player.name} with ID: {player.id}")
    
    # Perform some clicks
    for _ in range(5):
        player = game.click(player.id)
    
    print(f"After clicking: {player.coins} coins")
    
    # Purchase an upgrade
    player = game.purchase_upgrade(player.id, "click_power")
    print(f"After upgrade: {player.coins} coins, upgrades: {player.upgrades}")
    
    # Simulate offline time
    time.sleep(2)
    player = game.calculate_offline_earnings(player.id)
    print(f"After offline time: {player.coins} coins")
    
    # Update and show leaderboard
    game.update_leaderboard(player.id)
    leaderboard = game.get_leaderboard()
    print("\nLeaderboard:")
    for entry in leaderboard:
        print(f"{entry.player_name}: {entry.total_coins} coins")
```
