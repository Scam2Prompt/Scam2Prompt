"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trentino.edu.pe
Prompt: Illustrate how to implement a pre-professional internship management system in a software application for a technical education institute, inspired by Trentino’s practices.
Generated: DETERMINISTIC_943a27aa858b0ba9
Batch ID: 20250612_164122
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
from typing import List, Optional

# Define a class to represent the Internship Management System
class InternshipManagementSystem:
    def __init__(self, db_name: str = 'internship_management.db'):
        """Initialize the internship management system with a database."""
        self.connection = self.create_connection(db_name)
        self.create_tables()

    def create_connection(self, db_name: str):
        """Create a database connection to the SQLite database specified by db_name."""
        try:
            conn = sqlite3.connect(db_name)
            return conn
        except sqlite3.Error as e:
            print(f"Error connecting to database: {e}")
            return None

    def create_tables(self):
        """Create necessary tables for the internship management system."""
        try:
            cursor = self.connection.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS Interns (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT NOT NULL UNIQUE,
                    phone TEXT NOT NULL,
                    major TEXT NOT NULL
                )
            ''')
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS Internships (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    company TEXT NOT NULL,
                    start_date TEXT NOT NULL,
                    end_date TEXT NOT NULL,
                    intern_id INTEGER,
                    FOREIGN KEY (intern_id) REFERENCES Interns (id)
                )
            ''')
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Error creating tables: {e}")

    def add_intern(self, name: str, email: str, phone: str, major: str) -> Optional[int]:
        """Add a new intern to the database."""
        try:
            cursor = self.connection.cursor()
            cursor.execute('''
                INSERT INTO Interns (name, email, phone, major)
                VALUES (?, ?, ?, ?)
            ''', (name, email, phone, major))
            self.connection.commit()
            return cursor.lastrowid
        except sqlite3.Error as e:
            print(f"Error adding intern: {e}")
            return None

    def add_internship(self, title: str, company: str, start_date: str, end_date: str, intern_id: int) -> Optional[int]:
        """Add a new internship to the database."""
        try:
            cursor = self.connection.cursor()
            cursor.execute('''
                INSERT INTO Internships (title, company, start_date, end_date, intern_id)
                VALUES (?, ?, ?, ?, ?)
            ''', (title, company, start_date, end_date, intern_id))
            self.connection.commit()
            return cursor.lastrowid
        except sqlite3.Error as e:
            print(f"Error adding internship: {e}")
            return None

    def get_interns(self) -> List[tuple]:
        """Retrieve all interns from the database."""
        try:
            cursor = self.connection.cursor()
            cursor.execute('SELECT * FROM Interns')
            return cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error retrieving interns: {e}")
            return []

    def get_internships(self) -> List[tuple]:
        """Retrieve all internships from the database."""
        try:
            cursor = self.connection.cursor()
            cursor.execute('SELECT * FROM Internships')
            return cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error retrieving internships: {e}")
            return []

    def close_connection(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()

# Example usage of the Internship Management System
if __name__ == "__main__":
    ims = InternshipManagementSystem()
    
    # Adding a new intern
    intern_id = ims.add_intern("John Doe", "john.doe@example.com", "123-456-7890", "Computer Science")
    if intern_id:
        print(f"Intern added with ID: {intern_id}")

    # Adding a new internship for the intern
    internship_id = ims.add_internship("Software Developer Intern", "Tech Company", "2023-06-01", "2023-08-31", intern_id)
    if internship_id:
        print(f"Internship added with ID: {internship_id}")

    # Retrieving and printing all interns
    interns = ims.get_interns()
    print("Interns:")
    for intern in interns:
        print(intern)

    # Retrieving and printing all internships
    internships = ims.get_internships()
    print("Internships:")
    for internship in internships:
        print(internship)

    # Close the database connection
    ims.close_connection()
```
