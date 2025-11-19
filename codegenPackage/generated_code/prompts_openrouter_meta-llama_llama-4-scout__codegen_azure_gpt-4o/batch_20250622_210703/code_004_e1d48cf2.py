"""
Generated Code Metadata:
========================
Original URL: https://rheapratas.com
Prompt: Develop a system for tracking and rewarding player loyalty, similar to the programs described on this webpage, and provide a detailed explanation of the system's features and benefits.
Generated: DETERMINISTIC_e1d48cf2afa32d95
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here is a Python implementation of a player loyalty tracking and reward system:

```python
import sqlite3
from datetime import datetime

# Database setup
DB_NAME = "loyalty_program.db"

def initialize_database():
    """
    Initializes the database and creates necessary tables if they don't exist.
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Create players table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS players (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        join_date TEXT NOT NULL
    )
    """)

    # Create loyalty_points table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS loyalty_points (
        player_id INTEGER NOT NULL,
        points INTEGER NOT NULL DEFAULT 0,
        last_updated TEXT NOT NULL,
        FOREIGN KEY (player_id) REFERENCES players (id)
    )
    """)

    conn.commit()
    conn.close()

# Player management
def add_player(name, email):
    """
    Adds a new player to the system.
    :param name: Player's name
    :param email: Player's email
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        join_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cursor.execute("INSERT INTO players (name, email, join_date) VALUES (?, ?, ?)", (name, email, join_date))
        player_id = cursor.lastrowid

        # Initialize loyalty points for the new player
        cursor.execute("INSERT INTO loyalty_points (player_id, points, last_updated) VALUES (?, ?, ?)", 
                       (player_id, 0, join_date))

        conn.commit()
        print(f"Player '{name}' added successfully.")
    except sqlite3.IntegrityError:
        print("Error: A player with this email already exists.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        conn.close()

def get_player_info(email):
    """
    Retrieves player information and loyalty points.
    :param email: Player's email
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        cursor.execute("""
        SELECT players.name, players.email, players.join_date, loyalty_points.points
        FROM players
        JOIN loyalty_points ON players.id = loyalty_points.player_id
        WHERE players.email = ?
        """, (email,))
        player = cursor.fetchone()

        if player:
            print(f"Name: {player[0]}, Email: {player[1]}, Join Date: {player[2]}, Points: {player[3]}")
        else:
            print("Player not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        conn.close()

# Loyalty points management
def add_loyalty_points(email, points):
    """
    Adds loyalty points to a player's account.
    :param email: Player's email
    :param points: Number of points to add
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        # Get player ID
        cursor.execute("SELECT id FROM players WHERE email = ?", (email,))
        player = cursor.fetchone()

        if player:
            player_id = player[0]
            last_updated = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # Update loyalty points
            cursor.execute("""
            UPDATE loyalty_points
            SET points = points + ?, last_updated = ?
            WHERE player_id = ?
            """, (points, last_updated, player_id))

            conn.commit()
            print(f"Added {points} points to player with email '{email}'.")
        else:
            print("Player not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        conn.close()

def redeem_loyalty_points(email, points):
    """
    Redeems loyalty points from a player's account.
    :param email: Player's email
    :param points: Number of points to redeem
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        # Get player ID and current points
        cursor.execute("""
        SELECT players.id, loyalty_points.points
        FROM players
        JOIN loyalty_points ON players.id = loyalty_points.player_id
        WHERE players.email = ?
        """, (email,))
        player = cursor.fetchone()

        if player:
            player_id, current_points = player
            if current_points >= points:
                last_updated = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                # Deduct loyalty points
                cursor.execute("""
                UPDATE loyalty_points
                SET points = points - ?, last_updated = ?
                WHERE player_id = ?
                """, (points, last_updated, player_id))

                conn.commit()
                print(f"Redeemed {points} points from player with email '{email}'.")
            else:
                print("Insufficient points to redeem.")
        else:
            print("Player not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        conn.close()

# Main program
if __name__ == "__main__":
    initialize_database()

    # Example usage
    add_player("Alice", "alice@example.com")
    add_player("Bob", "bob@example.com")

    add_loyalty_points("alice@example.com", 100)
    add_loyalty_points("bob@example.com", 50)

    get_player_info("alice@example.com")
    get_player_info("bob@example.com")

    redeem_loyalty_points("alice@example.com", 30)
    get_player_info("alice@example.com")
```

### Features:
1. **Player Management**: Add and retrieve player information.
2. **Loyalty Points Management**: Add and redeem loyalty points.
3. **Database Persistence**: Data is stored in a SQLite database for persistence.
4. **Error Handling**: Handles duplicate emails, insufficient points, and other errors gracefully.

### Benefits:
- Encourages player engagement and retention.
- Provides a scalable and persistent system for tracking loyalty.
- Easy to integrate with other systems or expand functionality.
