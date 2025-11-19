"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kayenferno.pages.dev
Prompt: How can I automate the process of tracking and displaying the leading scorers in the KAYEN League using a database?
Generated: DETERMINISTIC_4277fbf918261370
Batch ID: 20250612_155606
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import sqlite3
from typing import List, Tuple

# Database setup
DB_NAME = "kayen_league.db"

def initialize_database():
    """
    Initialize the database by creating the necessary table
    if it doesn't already exist.
    """
    try:
        # Connect to the SQLite database (creates file if it doesn't exist)
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        # Create "players" table to store scorer data
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS players (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                team TEXT NOT NULL,
                goals INTEGER DEFAULT 0
            )
        """)

        # Commit and close the connection
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error initializing database: {e}")
    finally:
        conn.close()

def add_player(name: str, team: str):
    """
    Add a new player to the database.
    :param name: Player's name
    :param team: Player's team
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO players (name, team, goals)
            VALUES (?, ?, ?)
        """, (name, team, 0))

        conn.commit()
    except sqlite3.Error as e:
        print(f"Error adding player: {e}")
    finally:
        conn.close()

def update_goals(player_id: int, goals: int):
    """
    Update the number of goals for a specific player.
    :param player_id: Player's ID
    :param goals: Number of goals to set
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE players
            SET goals = ?
            WHERE id = ?
        """, (goals, player_id))

        conn.commit()
    except sqlite3.Error as e:
        print(f"Error updating goals: {e}")
    finally:
        conn.close()

def get_top_scorers(limit: int = 10) -> List[Tuple]:
    """
    Retrieve the top scorers from the database.
    :param limit: Number of top scorers to retrieve (default is 10)
    :return: List of tuples containing player data
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        cursor.execute("""
            SELECT name, team, goals
            FROM players
            ORDER BY goals DESC
            LIMIT ?
        """, (limit,))

        top_scorers = cursor.fetchall()
        return top_scorers
    except sqlite3.Error as e:
        print(f"Error retrieving top scorers: {e}")
        return []
    finally:
        conn.close()

def display_top_scorers():
    """
    Display the top scorers in a human-readable format.
    """
    top_scorers = get_top_scorers()
    print("Top Scorers in the KAYEN League:")
    print("-" * 40)
    for index, (name, team, goals) in enumerate(top_scorers, start=1):
        print(f"{index}. {name} ({team}) - {goals} goals")

if __name__ == "__main__":
    # Initialize the database
    initialize_database()

    # Example: Add players
    add_player("Alice Johnson", "Golden Eagles")
    add_player("Bob Smith", "Silver Hawks")
    add_player("Charlie Brown", "Copper Bears")

    # Example: Update goal counts
    update_goals(1, 15)
    update_goals(2, 10)
    update_goals(3, 20)

    # Display the current top scorers
    display_top_scorers()
```
