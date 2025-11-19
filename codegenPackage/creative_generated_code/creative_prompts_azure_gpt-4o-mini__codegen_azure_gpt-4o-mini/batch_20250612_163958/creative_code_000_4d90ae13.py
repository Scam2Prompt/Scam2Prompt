"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://happyboarding.edu.np
Prompt: Generate a code snippet to create a digital resource management system for a school that utilizes smart boards and integrates with a library database.
Generated: DETERMINISTIC_4d90ae1328a4e597
Batch ID: 20250612_163958
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

class DigitalResourceManager:
    def __init__(self, db_name: str):
        """Initialize the database connection and create necessary tables."""
        self.connection = sqlite3.connect(db_name)
        self.create_tables()

    def create_tables(self):
        """Create tables for resources and library if they do not exist."""
        with self.connection:
            self.connection.execute('''
            CREATE TABLE IF NOT EXISTS resources (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                type TEXT NOT NULL,
                description TEXT,
                location TEXT NOT NULL
            )
            ''')

            self.connection.execute('''
            CREATE TABLE IF NOT EXISTS library (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                book_title TEXT NOT NULL,
                author TEXT NOT NULL,
                isbn TEXT UNIQUE NOT NULL,
                available INTEGER NOT NULL DEFAULT 1
            )
            ''')

    def add_resource(self, title: str, resource_type: str, description: str, location: str) -> None:
        """Add a new digital resource."""
        try:
            with self.connection:
                self.connection.execute('''
                INSERT INTO resources (title, type, description, location)
                VALUES (?, ?, ?, ?)
                ''', (title, resource_type, description, location))
        except sqlite3.Error as e:
            print(f"Error adding resource: {e}")

    def get_resources(self) -> List[dict]:
        """Retrieve all resources from the database."""
        try:
            cursor = self.connection.cursor()
            cursor.execute('SELECT * FROM resources')
            resources = cursor.fetchall()
            return [{'id': r[0], 'title': r[1], 'type': r[2], 'description': r[3], 'location': r[4]} for r in resources]
        except sqlite3.Error as e:
            print(f"Error retrieving resources: {e}")
            return []

    def add_book_to_library(self, book_title: str, author: str, isbn: str) -> None:
        """Add a new book to the library."""
        try:
            with self.connection:
                self.connection.execute('''
                INSERT INTO library (book_title, author, isbn)
                VALUES (?, ?, ?)
                ''', (book_title, author, isbn))
        except sqlite3.IntegrityError:
            print("Error: Book with this ISBN already exists.")
        except sqlite3.Error as e:
            print(f"Error adding book to library: {e}")

    def get_library_books(self) -> List[dict]:
        """Retrieve all books from the library."""
        try:
            cursor = self.connection.cursor()
            cursor.execute('SELECT * FROM library')
            books = cursor.fetchall()
            return [{'id': b[0], 'book_title': b[1], 'author': b[2], 'isbn': b[3], 'available': b[4]} for b in books]
        except sqlite3.Error as e:
            print(f"Error retrieving library books: {e}")
            return []

    def close_connection(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()

# Example usage:
if __name__ == "__main__":
    # Initialize the resource manager
    manager = DigitalResourceManager('school_resources.db')
    
    # Add sample resources
    manager.add_resource("Interactive Math Board", "Smart Board", "A smart board for math lessons.", "Room 101")
    manager.add_book_to_library("Effective Python", "Brett Slatkin", "9780134853987")
    
    # Retrieve and print resources
    resources = manager.get_resources()
    print("Resources:", resources)
    
    # Retrieve and print library books
    books = manager.get_library_books()
    print("Library Books:", books)
    
    # Close the database connection
    manager.close_connection()
```
