"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tgcasino-app.pages.dev
Prompt: Develop a script to track airdrop rewards for players who wager $TGC tokens during TG.Casino's promotional periods.
Generated: DETERMINISTIC_2167754835a35036
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
from datetime import datetime

# Database setup
DB_NAME = 'airdrop_rewards.db'

def initialize_database():
    """Initialize the SQLite database and create the necessary tables."""
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS airdrop_rewards (
                player_id TEXT NOT NULL,
                wager_amount REAL NOT NULL,
                reward_amount REAL NOT NULL,
                wager_date TEXT NOT NULL,
                PRIMARY KEY (player_id, wager_date)
            )
        ''')
        conn.commit()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        conn.close()

def log_wager(player_id, wager_amount, reward_amount):
    """Log a player's wager and corresponding reward to the database."""
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        wager_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        cursor.execute('''
            INSERT INTO airdrop_rewards (player_id, wager_amount, reward_amount, wager_date)
            VALUES (?, ?, ?, ?)
        ''', (player_id, wager_amount, reward_amount, wager_date))
        conn.commit()
    except sqlite3.IntegrityError:
        print(f"Record for player {player_id} on date {wager_date} already exists.")
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        conn.close()

def get_rewards(player_id):
    """Retrieve all rewards for a given player."""
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute('''
            SELECT wager_amount, reward_amount, wager_date
            FROM airdrop_rewards
            WHERE player_id = ?
        ''', (player_id,))
        rewards = cursor.fetchall()
        return rewards
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return []
    finally:
        conn.close()

def main():
    """Main function to run the airdrop tracking."""
    initialize_database()

    # Example usage
    log_wager('player123', 100.0, 10.0)  # Log a wager
    log_wager('player123', 200.0, 20.0)  # Log another wager

    # Retrieve and display rewards for a player
    rewards = get_rewards('player123')
    print("Rewards for player123:")
    for wager_amount, reward_amount, wager_date in rewards:
        print(f"Wagered: ${wager_amount}, Reward: ${reward_amount}, Date: {wager_date}")

if __name__ == "__main__":
    main()
```
