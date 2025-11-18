"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mini-externalpoint.pages.dev
Prompt: Create a program to track and analyze quests from leading Web3 projects, as described in the "Join Quests" section of the webpage.
Generated: DETERMINISTIC_387459401503b986
Batch ID: 20250612_150226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import requests
import sqlite3
from sqlite3 import Error

# Define the QuestTracker class to handle quest tracking and analysis
class QuestTracker:
    def __init__(self, database):
        """Initialize the QuestTracker with a SQLite database."""
        self.connection = self.create_connection(database)
        self.create_table()

    def create_connection(self, db_file):
        """Create a database connection to an SQLite database."""
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            print("Database connection established.")
        except Error as e:
            print(f"Error connecting to database: {e}")
        return conn

    def create_table(self):
        """Create the quests table if it does not exist."""
        try:
            sql_create_quests_table = """CREATE TABLE IF NOT EXISTS quests (
                                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                                            project_name TEXT NOT NULL,
                                            quest_name TEXT NOT NULL,
                                            status TEXT NOT NULL,
                                            reward TEXT NOT NULL,
                                            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                                        );"""
            cursor = self.connection.cursor()
            cursor.execute(sql_create_quests_table)
            print("Quests table created successfully.")
        except Error as e:
            print(f"Error creating table: {e}")

    def add_quest(self, project_name, quest_name, status, reward):
        """Add a new quest to the database."""
        sql = '''INSERT INTO quests(project_name, quest_name, status, reward)
                 VALUES(?,?,?,?)'''
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql, (project_name, quest_name, status, reward))
            self.connection.commit()
            print(f"Quest '{quest_name}' added successfully.")
        except Error as e:
            print(f"Error adding quest: {e}")

    def fetch_quests(self):
        """Fetch all quests from the database."""
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM quests")
        quests = cursor.fetchall()
        return quests

    def analyze_quests(self):
        """Analyze quests and return summary statistics."""
        cursor = self.connection.cursor()
        cursor.execute("SELECT status, COUNT(*) FROM quests GROUP BY status")
        analysis = cursor.fetchall()
        return {status: count for status, count in analysis}

    def close_connection(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()
            print("Database connection closed.")

# Example usage
if __name__ == "__main__":
    tracker = QuestTracker("quests.db")

    # Example quests to add
    tracker.add_quest("Project A", "Complete Task 1", "active", "10 Tokens")
    tracker.add_quest("Project B", "Join Discord", "completed", "5 Tokens")
    
    # Fetch and print all quests
    quests = tracker.fetch_quests()
    print("All Quests:")
    for quest in quests:
        print(quest)

    # Analyze and print quest statistics
    analysis = tracker.analyze_quests()
    print("Quest Analysis:")
    for status, count in analysis.items():
        print(f"{status}: {count}")

    # Close the database connection
    tracker.close_connection()
```
