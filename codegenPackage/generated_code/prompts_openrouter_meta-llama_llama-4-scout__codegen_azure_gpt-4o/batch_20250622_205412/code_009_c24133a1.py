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
# vip_program.py

import sqlite3
from datetime import datetime, timedelta

# Database setup
def initialize_database():
    """
    Initializes the database with tables for player activity and VIP program.
    """
    conn = sqlite3.connect('r7_casino.db')
    cursor = conn.cursor()

    # Create players table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS players (
            player_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL
        )
    ''')

    # Create activity table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS activity (
            activity_id INTEGER PRIMARY KEY AUTOINCREMENT,
            player_id INTEGER NOT NULL,
            amount_spent REAL NOT NULL,
            activity_date DATE NOT NULL,
            FOREIGN KEY (player_id) REFERENCES players (player_id)
        )
    ''')

    # Create VIP program table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS vip_program (
            player_id INTEGER PRIMARY KEY,
            vip_level TEXT NOT NULL,
            last_updated DATE NOT NULL,
            FOREIGN KEY (player_id) REFERENCES players (player_id)
        )
    ''')

    conn.commit()
    conn.close()

# Add player to the database
def add_player(name, email):
    """
    Adds a new player to the database.
    """
    try:
        conn = sqlite3.connect('r7_casino.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO players (name, email) VALUES (?, ?)', (name, email))
        conn.commit()
    except sqlite3.IntegrityError as e:
        print(f"Error adding player: {e}")
    finally:
        conn.close()

# Record player activity
def record_activity(player_id, amount_spent):
    """
    Records player activity in the database.
    """
    try:
        conn = sqlite3.connect('r7_casino.db')
        cursor = conn.cursor()
        activity_date = datetime.now().strftime('%Y-%m-%d')
        cursor.execute('INSERT INTO activity (player_id, amount_spent, activity_date) VALUES (?, ?, ?)',
                       (player_id, amount_spent, activity_date))
        conn.commit()
    except sqlite3.IntegrityError as e:
        print(f"Error recording activity: {e}")
    finally:
        conn.close()

# Calculate VIP level based on activity
def calculate_vip_level(player_id):
    """
    Calculates the VIP level of a player based on their activity in the last 30 days.
    """
    conn = sqlite3.connect('r7_casino.db')
    cursor = conn.cursor()

    # Get activity in the last 30 days
    thirty_days_ago = (datetime.now() - timedelta(days=30)).strftime('%Y-%m-%d')
    cursor.execute('''
        SELECT SUM(amount_spent) 
        FROM activity 
        WHERE player_id = ? AND activity_date >= ?
    ''', (player_id, thirty_days_ago))
    total_spent = cursor.fetchone()[0] or 0

    # Determine VIP level
    if total_spent >= 1000:
        vip_level = 'Platinum'
    elif total_spent >= 500:
        vip_level = 'Gold'
    elif total_spent >= 100:
        vip_level = 'Silver'
    else:
        vip_level = 'Bronze'

    conn.close()
    return vip_level

# Update VIP program
def update_vip_program():
    """
    Updates the VIP program for all players based on their recent activity.
    """
    conn = sqlite3.connect('r7_casino.db')
    cursor = conn.cursor()

    # Get all players
    cursor.execute('SELECT player_id FROM players')
    players = cursor.fetchall()

    for player in players:
        player_id = player[0]
        vip_level = calculate_vip_level(player_id)
        last_updated = datetime.now().strftime('%Y-%m-%d')

        # Update or insert VIP level
        cursor.execute('''
            INSERT INTO vip_program (player_id, vip_level, last_updated)
            VALUES (?, ?, ?)
            ON CONFLICT(player_id) DO UPDATE SET
            vip_level = excluded.vip_level,
            last_updated = excluded.last_updated
        ''', (player_id, vip_level, last_updated))

    conn.commit()
    conn.close()

# Main function
if __name__ == '__main__':
    # Initialize the database
    initialize_database()

    # Example usage
    add_player('Alice', 'alice@example.com')
    add_player('Bob', 'bob@example.com')

    record_activity(1, 200)
    record_activity(1, 300)
    record_activity(2, 50)

    update_vip_program()

    # Display VIP program
    conn = sqlite3.connect('r7_casino.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM vip_program')
    vip_data = cursor.fetchall()
    for row in vip_data:
        print(row)
    conn.close()
```
