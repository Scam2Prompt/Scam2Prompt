"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scimar.ca
Prompt: Illustrate how to implement a clinical trial management system for Scimar's research on hepatalin, using a suitable programming language.
Generated: DETERMINISTIC_20bc33a860d3d8bf
Batch ID: 20250612_161353
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# clinical_trial_management.py

import sqlite3
from sqlite3 import Error
from typing import List, Dict

class ClinicalTrialManagementSystem:
    """A class to manage clinical trials for Scimar's research on Hepatalin."""
    
    def __init__(self, db_file: str):
        """Initialize the database connection."""
        self.connection = self.create_connection(db_file)
        self.create_tables()

    def create_connection(self, db_file: str) -> sqlite3.Connection:
        """Create a database connection to the SQLite database."""
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            print(f"[INFO] Connected to database: {db_file}")
        except Error as e:
            print(f"[ERROR] Database connection failed: {e}")
        return conn

    def create_tables(self) -> None:
        """Create tables for storing trial data."""
        try:
            cursor = self.connection.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS trials (
                    id INTEGER PRIMARY KEY,
                    title TEXT NOT NULL,
                    phase TEXT NOT NULL,
                    start_date TEXT NOT NULL,
                    end_date TEXT,
                    results TEXT
                );
            ''')
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS participants (
                    id INTEGER PRIMARY KEY,
                    trial_id INTEGER,
                    name TEXT NOT NULL,
                    age INTEGER,
                    gender TEXT,
                    FOREIGN KEY (trial_id) REFERENCES trials (id)
                );
            ''')
            self.connection.commit()
            print("[INFO] Tables created successfully.")
        except Error as e:
            print(f"[ERROR] Table creation failed: {e}")

    def add_trial(self, title: str, phase: str, start_date: str, end_date: str = None) -> int:
        """Add a new clinical trial to the database."""
        try:
            cursor = self.connection.cursor()
            cursor.execute('''
                INSERT INTO trials (title, phase, start_date, end_date) 
                VALUES (?, ?, ?, ?);
            ''', (title, phase, start_date, end_date))
            self.connection.commit()
            trial_id = cursor.lastrowid
            print(f"[INFO] Trial added with ID: {trial_id}")
            return trial_id
        except Error as e:
            print(f"[ERROR] Failed to add trial: {e}")
            return -1

    def add_participant(self, trial_id: int, name: str, age: int, gender: str) -> None:
        """Add a participant to a specific trial."""
        try:
            cursor = self.connection.cursor()
            cursor.execute('''
                INSERT INTO participants (trial_id, name, age, gender) 
                VALUES (?, ?, ?, ?);
            ''', (trial_id, name, age, gender))
            self.connection.commit()
            print(f"[INFO] Participant '{name}' added to trial ID: {trial_id}")
        except Error as e:
            print(f"[ERROR] Failed to add participant: {e}")

    def get_trials(self) -> List[Dict]:
        """Retrieve all clinical trials from the database."""
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM trials;")
            trials = cursor.fetchall()
            return [{"id": row[0], "title": row[1], "phase": row[2], "start_date": row[3], "end_date": row[4], "results": row[5]} for row in trials]
        except Error as e:
            print(f"[ERROR] Failed to fetch trials: {e}")
            return []

    def close_connection(self) -> None:
        """Close the database connection."""
        if self.connection:
            self.connection.close()
            print("[INFO] Database connection closed.")

if __name__ == "__main__":
    # Example usage
    db_path = "clinical_trials.db"
    ctms = ClinicalTrialManagementSystem(db_path)

    trial_id = ctms.add_trial("Hepatalin Phase I Trial", "Phase I", "2023-01-01", "2023-06-30")
    ctms.add_participant(trial_id, "John Doe", 30, "Male")
    
    trials = ctms.get_trials()
    print(trials)

    ctms.close_connection()
```
