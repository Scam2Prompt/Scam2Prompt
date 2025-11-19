"""
Generated Code Metadata:
========================
Original URL: https://educarcomitan.mx
Prompt: How can I implement a library management system for an educational institution that provides resources for admission exam preparation, similar to the "Biblioteca de estudio en casa" mentioned on Educar Comitán?
Generated: DETERMINISTIC_a6e1d199418e6da6
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sqlite3
from sqlite3 import Error

class LibraryManagementSystem:
    def __init__(self, db_file):
        """Initialize the library management system with a database connection."""
        self.connection = self.create_connection(db_file)
        self.create_tables()

    def create_connection(self, db_file):
        """Create a database connection to the SQLite database specified by db_file."""
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            print("Connection to database established.")
        except Error as e:
            print(f"Error connecting to database: {e}")
        return conn

    def create_tables(self):
        """Create tables for books and users if they do not exist."""
        try:
            cursor = self.connection.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT NOT NULL UNIQUE
                );
            ''')
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS books (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    author TEXT NOT NULL,
                    available INTEGER NOT NULL DEFAULT 1
                );
            ''')
            self.connection.commit()
            print("Tables created successfully.")
        except Error as e:
            print(f"Error creating tables: {e}")

    def add_user(self, name, email):
        """Add a new user to the library system."""
        try:
            cursor = self.connection.cursor()
            cursor.execute('INSERT INTO users (name, email) VALUES (?, ?)', (name, email))
            self.connection.commit()
            print(f"User {name} added successfully.")
        except Error as e:
            print(f"Error adding user: {e}")

    def add_book(self, title, author):
        """Add a new book to the library system."""
        try:
            cursor = self.connection.cursor()
            cursor.execute('INSERT INTO books (title, author) VALUES (?, ?)', (title, author))
            self.connection.commit()
            print(f"Book '{title}' by {author} added successfully.")
        except Error as e:
            print(f"Error adding book: {e}")

    def borrow_book(self, book_id):
        """Mark a book as borrowed."""
        try:
            cursor = self.connection.cursor()
            cursor.execute('UPDATE books SET available = 0 WHERE id = ? AND available = 1', (book_id,))
            if cursor.rowcount == 0:
                print("Book is not available for borrowing.")
            else:
                self.connection.commit()
                print("Book borrowed successfully.")
        except Error as e:
            print(f"Error borrowing book: {e}")

    def return_book(self, book_id):
        """Mark a book as returned."""
        try:
            cursor = self.connection.cursor()
            cursor.execute('UPDATE books SET available = 1 WHERE id = ?', (book_id,))
            if cursor.rowcount == 0:
                print("Book was not borrowed or does not exist.")
            else:
                self.connection.commit()
                print("Book returned successfully.")
        except Error as e:
            print(f"Error returning book: {e}")

    def list_books(self):
        """List all books in the library."""
        try:
            cursor = self.connection.cursor()
            cursor.execute('SELECT * FROM books')
            books = cursor.fetchall()
            for book in books:
                status = "Available" if book[2] == 1 else "Borrowed"
                print(f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Status: {status}")
        except Error as e:
            print(f"Error listing books: {e}")

    def close_connection(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()
            print("Database connection closed.")

# Example usage
if __name__ == "__main__":
    library_system = LibraryManagementSystem("library.db")
    library_system.add_user("John Doe", "john@example.com")
    library_system.add_book("Python Programming", "Jane Smith")
    library_system.list_books()
    library_system.borrow_book(1)  # Assuming the book ID is 1
    library_system.return_book(1)   # Assuming the book ID is 1
    library_system.close_connection()
```
