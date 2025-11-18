"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jobbo.com.au
Prompt: Develop a script to track and display historical tractor pulling data, including team history and event results, as seen on jobbo.com.au.
Generated: DETERMINISTIC_c30b5ace139f64c9
Batch ID: 20250612_150316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
from sqlite3 import Error

# Define a class to handle the Tractor Pulling database
class TractorPullingDB:
    def __init__(self, db_file):
        """Initialize the database connection."""
        self.connection = self.create_connection(db_file)

    def create_connection(self, db_file):
        """Create a database connection to the SQLite database."""
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            return conn
        except Error as e:
            print(f"Error connecting to database: {e}")
        return conn

    def create_table(self):
        """Create tables for teams and events."""
        try:
            cursor = self.connection.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS teams (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    history TEXT
                );
            ''')
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS events (
                    id INTEGER PRIMARY KEY,
                    team_id INTEGER,
                    event_name TEXT NOT NULL,
                    result TEXT,
                    date TEXT NOT NULL,
                    FOREIGN KEY (team_id) REFERENCES teams (id)
                );
            ''')
            self.connection.commit()
        except Error as e:
            print(f"Error creating tables: {e}")

    def add_team(self, name, history):
        """Add a new team to the database."""
        try:
            cursor = self.connection.cursor()
            cursor.execute("INSERT INTO teams (name, history) VALUES (?, ?)", (name, history))
            self.connection.commit()
        except Error as e:
            print(f"Error adding team: {e}")

    def add_event(self, team_id, event_name, result, date):
        """Add a new event to the database."""
        try:
            cursor = self.connection.cursor()
            cursor.execute("INSERT INTO events (team_id, event_name, result, date) VALUES (?, ?, ?, ?)", 
                           (team_id, event_name, result, date))
            self.connection.commit()
        except Error as e:
            print(f"Error adding event: {e}")

    def get_team_history(self, team_id):
        """Retrieve the history of a specified team."""
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM events WHERE team_id=?", (team_id,))
            return cursor.fetchall()
        except Error as e:
            print(f"Error retrieving team history: {e}")
            return []

    def close_connection(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()

# Main execution
if __name__ == '__main__':
    # Initialize database
    db = TractorPullingDB("tractor_pulling.db")
    db.create_table()

    # Example data addition
    db.add_team("Team A", "Established in 2010, known for speed.")
    db.add_event(1, "National Championship", "1st Place", "2023-08-15")

    # Fetch and display team history
    team_history = db.get_team_history(1)
    for event in team_history:
        print(f"Event: {event[2]}, Result: {event[3]}, Date: {event[4]}")

    # Close the database connection
    db.close_connection()
```
