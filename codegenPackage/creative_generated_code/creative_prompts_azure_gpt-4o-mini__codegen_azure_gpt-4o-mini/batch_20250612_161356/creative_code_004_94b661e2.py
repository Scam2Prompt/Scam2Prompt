"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gitcoin-dr-manager.vercel.app
Prompt: What libraries or APIs are recommended for developing a round management system similar to Gitcoin's?
Generated: DETERMINISTIC_94b661e2459b069e
Batch ID: 20250612_161356
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# round_management_system.py

"""
Round Management System

This script provides a basic structure for a round management system similar to Gitcoin's,
allowing the management of funding rounds, projects, and contributors.
"""

import sqlite3
from sqlite3 import Error

class RoundManagementSystem:
    """A class to manage funding rounds, projects, and contributors."""

    def __init__(self, db_file):
        """Initialize the RoundManagementSystem with a database connection."""
        self.connection = self.create_connection(db_file)
        self.create_tables()

    def create_connection(self, db_file):
        """Create a database connection to the SQLite database."""
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            print(f"Connected to database: {db_file}")
            return conn
        except Error as e:
            print(f"Error connecting to database: {e}")
            return None

    def create_tables(self):
        """Create tables for rounds, projects, and contributors."""
        try:
            cursor = self.connection.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS rounds (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    start_date TEXT NOT NULL,
                    end_date TEXT NOT NULL,
                    status TEXT NOT NULL
                );
            ''')

            cursor.execute('''
                CREATE TABLE IF NOT EXISTS projects (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    round_id INTEGER,
                    title TEXT NOT NULL,
                    description TEXT NOT NULL,
                    FOREIGN KEY (round_id) REFERENCES rounds (id)
                );
            ''')

            cursor.execute('''
                CREATE TABLE IF NOT EXISTS contributors (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    project_id INTEGER,
                    name TEXT NOT NULL,
                    contribution_amount REAL NOT NULL,
                    FOREIGN KEY (project_id) REFERENCES projects (id)
                );
            ''')
            self.connection.commit()
            print("Tables created successfully.")
        except Error as e:
            print(f"Error creating tables: {e}")

    def add_round(self, title, start_date, end_date, status):
        """Add a new funding round."""
        try:
            cursor = self.connection.cursor()
            cursor.execute('''
                INSERT INTO rounds (title, start_date, end_date, status)
                VALUES (?, ?, ?, ?);
            ''', (title, start_date, end_date, status))
            self.connection.commit()
            print(f"Round '{title}' added successfully.")
        except Error as e:
            print(f"Error adding round: {e}")

    def add_project(self, round_id, title, description):
        """Add a new project to a specific round."""
        try:
            cursor = self.connection.cursor()
            cursor.execute('''
                INSERT INTO projects (round_id, title, description)
                VALUES (?, ?, ?);
            ''', (round_id, title, description))
            self.connection.commit()
            print(f"Project '{title}' added to round ID {round_id}.")
        except Error as e:
            print(f"Error adding project: {e}")

    def add_contributor(self, project_id, name, contribution_amount):
        """Add a contributor for a specific project."""
        try:
            cursor = self.connection.cursor()
            cursor.execute('''
                INSERT INTO contributors (project_id, name, contribution_amount)
                VALUES (?, ?, ?);
            ''', (project_id, name, contribution_amount))
            self.connection.commit()
            print(f"Contributor '{name}' added to project ID {project_id}.")
        except Error as e:
            print(f"Error adding contributor: {e}")

    def close_connection(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()
            print("Database connection closed.")

# Example usage
if __name__ == "__main__":
    db_path = "round_management.db"
    rms = RoundManagementSystem(db_path)

    # Adding a sample round, project, and contributor
    rms.add_round("Funding Round 1", "2023-01-01", "2023-01-31", "active")
    rms.add_project(1, "Project Alpha", "Description of Project Alpha")
    rms.add_contributor(1, "Alice", 100.0)

    rms.close_connection()
```
