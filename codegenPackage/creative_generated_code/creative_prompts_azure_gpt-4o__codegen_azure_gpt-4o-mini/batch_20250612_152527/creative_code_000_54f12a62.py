"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://iebcatitiribi.edu.co
Prompt: Write Python code to create a database schema for managing educational projects, including fields for project name, description, participants, and associated clubs like "Club de robótica" mentioned on the IEBCA website.
Generated: DETERMINISTIC_54f12a62dc3a3e86
Batch ID: 20250612_152527
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

# Database connection and schema creation for educational projects
class DatabaseManager:
    def __init__(self, db_file):
        """Initialize the DatabaseManager with the given database file."""
        self.connection = self.create_connection(db_file)
        self.create_table()

    def create_connection(self, db_file):
        """Create a database connection to the SQLite database specified by db_file."""
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            print(f"Connected to database: {db_file}")
        except Error as e:
            print(f"Error connecting to database: {e}")
        return conn

    def create_table(self):
        """Create the educational projects table if it doesn't exist."""
        create_table_sql = """
        CREATE TABLE IF NOT EXISTS projects (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT,
            participants TEXT NOT NULL,
            club TEXT NOT NULL
        );
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute(create_table_sql)
            print("Projects table created successfully.")
        except Error as e:
            print(f"Error creating table: {e}")

    def insert_project(self, name, description, participants, club):
        """Insert a new project into the projects table."""
        insert_sql = """
        INSERT INTO projects (name, description, participants, club)
        VALUES (?, ?, ?, ?);
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute(insert_sql, (name, description, participants, club))
            self.connection.commit()
            print(f"Project '{name}' added successfully.")
        except Error as e:
            print(f"Error inserting project: {e}")

    def close_connection(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()
            print("Database connection closed.")

# Example usage
if __name__ == "__main__":
    db_file = "educational_projects.db"
    db_manager = DatabaseManager(db_file)
    
    # Insert a sample project (you can modify these values)
    db_manager.insert_project(
        name="Robotics Workshop",
        description="A workshop to enhance skills in robotics.",
        participants="John Doe, Jane Smith",
        club="Club de robótica"
    )
    
    # Clean up and close the database connection
    db_manager.close_connection()
```
