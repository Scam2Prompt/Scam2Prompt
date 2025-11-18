"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://paradigmgroup.co.ug
Prompt: Develop a program to track and evaluate the effectiveness of BTL activations, referencing Paradigm Group's experiential marketing projects.
Generated: DETERMINISTIC_a0cbadf34a8da076
Batch ID: 20250612_154909
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
from datetime import datetime

class BTLActivationTracker:
    """A class to manage BTL activation tracking and evaluation."""

    def __init__(self, db_file):
        """Initialize the tracker with a SQLite database."""
        self.connection = self.create_connection(db_file)
        self.create_table()

    def create_connection(self, db_file):
        """Create a database connection to the SQLite database."""
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            print(f"Connected to database: {db_file}")
        except Error as e:
            print(f"Error occurred while connecting to database: {e}")
        return conn

    def create_table(self):
        """Create a table for BTL activations if it does not exist."""
        try:
            sql_create_table = """
            CREATE TABLE IF NOT EXISTS btl_activations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                date TEXT NOT NULL,
                location TEXT NOT NULL,
                participants INTEGER NOT NULL,
                effectiveness_score REAL NOT NULL CHECK(effectiveness_score >= 0 AND effectiveness_score <= 100)
            );
            """
            cursor = self.connection.cursor()
            cursor.execute(sql_create_table)
            print("BTL Activations table is created or already exists.")
        except Error as e:
            print(f"Error creating table: {e}")

    def add_activation(self, name, date, location, participants, effectiveness_score):
        """Add a new BTL activation to the database."""
        sql_insert_activation = """
        INSERT INTO btl_activations (name, date, location, participants, effectiveness_score)
        VALUES (?, ?, ?, ?, ?);
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql_insert_activation, (name, date, location, participants, effectiveness_score))
            self.connection.commit()
            print(f"Activation '{name}' added successfully.")
        except Error as e:
            print(f"Error adding activation: {e}")

    def evaluate_effectiveness(self):
        """Evaluate the effectiveness of all BTL activations."""
        sql_select_effectiveness = """
        SELECT name, effectiveness_score FROM btl_activations;
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql_select_effectiveness)
            rows = cursor.fetchall()

            print("\nEffectiveness Evaluation of BTL Activations:")
            for row in rows:
                print(f"Activation: {row[0]}, Effectiveness Score: {row[1]}")
        except Error as e:
            print(f"Error fetching effectiveness data: {e}")

    def close_connection(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()
            print("Database connection closed.")

if __name__ == "__main__":
    # Initialize the tracker
    tracker = BTLActivationTracker("btl_activations.db")
    
    # Example usage
    tracker.add_activation("Summer Festival", "2023-06-15", "Central Park", 200, 85.0)
    tracker.add_activation("Winter Wonderland", "2023-12-01", "Downtown", 150, 90.5)
    
    # Evaluate effectiveness of activations
    tracker.evaluate_effectiveness()
    
    # Close the tracker connection when done
    tracker.close_connection()
```
