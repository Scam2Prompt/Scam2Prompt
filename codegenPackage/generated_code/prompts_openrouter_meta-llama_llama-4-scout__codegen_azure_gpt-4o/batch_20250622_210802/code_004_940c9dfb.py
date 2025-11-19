"""
Generated Code Metadata:
========================
Original URL: https://plenatoken.vercel.app
Prompt: "Design a leaderboard system to track participants' progress in a multi-week challenge, such as the $PLENA Road to TGE Quest, using a suitable data storage solution."
Generated: DETERMINISTIC_940c9dfb9bc9aaae
Batch ID: 20250622_210802
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sqlite3
from datetime import datetime

# Database setup
DB_NAME = "leaderboard.db"

def initialize_database():
    """
    Initialize the database and create the necessary tables.
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    # Create participants table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS participants (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL
    )
    """)
    
    # Create progress table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS progress (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        participant_id INTEGER NOT NULL,
        week INTEGER NOT NULL,
        points INTEGER NOT NULL,
        updated_at TIMESTAMP NOT NULL,
        FOREIGN KEY (participant_id) REFERENCES participants (id)
    )
    """)
    
    conn.commit()
    conn.close()

def add_participant(name, email):
    """
    Add a new participant to the leaderboard.
    :param name: Name of the participant
    :param email: Email of the participant
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO participants (name, email) VALUES (?, ?)", (name, email))
        conn.commit()
    except sqlite3.IntegrityError:
        print(f"Error: Participant with email {email} already exists.")
    finally:
        conn.close()

def update_progress(participant_email, week, points):
    """
    Update the progress of a participant for a specific week.
    :param participant_email: Email of the participant
    :param week: Week number
    :param points: Points earned in the week
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        
        # Get participant ID
        cursor.execute("SELECT id FROM participants WHERE email = ?", (participant_email,))
        result = cursor.fetchone()
        if not result:
            print(f"Error: Participant with email {participant_email} not found.")
            return
        
        participant_id = result[0]
        
        # Update or insert progress
        cursor.execute("""
        INSERT INTO progress (participant_id, week, points, updated_at)
        VALUES (?, ?, ?, ?)
        ON CONFLICT(participant_id, week) DO UPDATE SET
        points = excluded.points,
        updated_at = excluded.updated_at
        """, (participant_id, week, points, datetime.now()))
        
        conn.commit()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        conn.close()

def get_leaderboard():
    """
    Retrieve the leaderboard sorted by total points.
    :return: List of participants and their total points
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        
        # Calculate total points for each participant
        cursor.execute("""
        SELECT p.name, p.email, SUM(pr.points) as total_points
        FROM participants p
        LEFT JOIN progress pr ON p.id = pr.participant_id
        GROUP BY p.id
        ORDER BY total_points DESC
        """)
        
        leaderboard = cursor.fetchall()
        return leaderboard
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return []
    finally:
        conn.close()

# Initialize the database
initialize_database()

# Example usage
add_participant("Alice", "alice@example.com")
add_participant("Bob", "bob@example.com")

update_progress("alice@example.com", 1, 50)
update_progress("bob@example.com", 1, 40)
update_progress("alice@example.com", 2, 30)

leaderboard = get_leaderboard()
print("Leaderboard:")
for rank, (name, email, total_points) in enumerate(leaderboard, start=1):
    print(f"{rank}. {name} ({email}) - {total_points} points")
```
