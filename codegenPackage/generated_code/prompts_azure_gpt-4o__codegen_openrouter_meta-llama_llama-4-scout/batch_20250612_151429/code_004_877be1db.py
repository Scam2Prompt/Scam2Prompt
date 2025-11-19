"""
Generated Code Metadata:
========================
Original URL: https://dbcop.org
Prompt: Suggest software tools for e-library management in pharmaceutical education, based on DBCOP's e-library facilities.
Generated: DETERMINISTIC_877be1db571d45b8
Batch ID: 20250612_151429
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# e-library management system for pharmaceutical education

import sqlite3
from typing import Dict, List

class ELibraryManagementSystem:
    """
    A class representing an e-library management system.

    Attributes:
    db_name (str): The name of the SQLite database file.
    conn (sqlite3.Connection): The connection to the SQLite database.
    cursor (sqlite3.Cursor): The cursor object to execute SQL queries.
    """

    def __init__(self, db_name: str = "e-library.db"):
        """
        Initializes the e-library management system.

        Args:
        db_name (str): The name of the SQLite database file. Defaults to "e-library.db".
        """
        self.db_name = db_name
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        """
        Creates the necessary tables in the SQLite database.
        """
        # Create table for books
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY,
                title TEXT NOT NULL,
                author TEXT NOT NULL,
                publication_year INTEGER NOT NULL,
                category TEXT NOT NULL
            )
        ''')

        # Create table for users
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                username TEXT NOT NULL,
                email TEXT NOT NULL,
                role TEXT NOT NULL
            )
        ''')

        # Create table for borrowings
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS borrowings (
                id INTEGER PRIMARY KEY,
                book_id INTEGER NOT NULL,
                user_id INTEGER NOT NULL,
                borrow_date DATE NOT NULL,
                return_date DATE,
                FOREIGN KEY (book_id) REFERENCES books (id),
                FOREIGN KEY (user_id) REFERENCES users (id)
            )
        ''')

        self.conn.commit()

    def add_book(self, book: Dict):
        """
        Adds a book to the e-library.

        Args:
        book (Dict): A dictionary containing the book's details.
        """
        try:
            self.cursor.execute('''
                INSERT INTO books (title, author, publication_year, category)
                VALUES (?, ?, ?, ?)
            ''', (book['title'], book['author'], book['publication_year'], book['category']))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error adding book: {e}")

    def add_user(self, user: Dict):
        """
        Adds a user to the e-library system.

        Args:
        user (Dict): A dictionary containing the user's details.
        """
        try:
            self.cursor.execute('''
                INSERT INTO users (username, email, role)
                VALUES (?, ?, ?)
            ''', (user['username'], user['email'], user['role']))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error adding user: {e}")

    def borrow_book(self, book_id: int, user_id: int):
        """
        Borrows a book from the e-library.

        Args:
        book_id (int): The ID of the book to borrow.
        user_id (int): The ID of the user borrowing the book.
        """
        try:
            self.cursor.execute('''
                INSERT INTO borrowings (book_id, user_id, borrow_date)
                VALUES (?, ?, DATE('now'))
            ''', (book_id, user_id))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error borrowing book: {e}")

    def return_book(self, book_id: int):
        """
        Returns a borrowed book to the e-library.

        Args:
        book_id (int): The ID of the book to return.
        """
        try:
            self.cursor.execute('''
                UPDATE borrowings
                SET return_date = DATE('now')
                WHERE book_id = ? AND return_date IS NULL
            ''', (book_id,))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error returning book: {e}")

    def get_borrowed_books(self, user_id: int) -> List[Dict]:
        """
        Retrieves the books borrowed by a user.

        Args:
        user_id (int): The ID of the user.

        Returns:
        List[Dict]: A list of dictionaries containing the borrowed books' details.
        """
        try:
            self.cursor.execute('''
                SELECT b.title, b.author, bo.borrow_date, bo.return_date
                FROM borrowings bo
                JOIN books b ON bo.book_id = b.id
                WHERE bo.user_id = ?
            ''', (user_id,))
            rows = self.cursor.fetchall()
            borrowed_books = []
            for row in rows:
                borrowed_books.append({
                    'title': row[0],
                    'author': row[1],
                    'borrow_date': row[2],
                    'return_date': row[3]
                })
            return borrowed_books
        except sqlite3.Error as e:
            print(f"Error retrieving borrowed books: {e}")
            return []

def main():
    # Example usage:
    e_library = ELibraryManagementSystem()

    # Add books
    book1 = {'title': 'Pharmacology', 'author': 'John Doe', 'publication_year': 2020, 'category': 'Pharmacy'}
    book2 = {'title': 'Toxicology', 'author': 'Jane Smith', 'publication_year': 2019, 'category': 'Pharmacy'}
    e_library.add_book(book1)
    e_library.add_book(book2)

    # Add users
    user1 = {'username': 'john', 'email': 'john@example.com', 'role': 'student'}
    user2 = {'username': 'jane', 'email': 'jane@example.com', 'role': 'lecturer'}
    e_library.add_user(user1)
    e_library.add_user(user2)

    # Borrow books
    e_library.borrow_book(1, 1)
    e_library.borrow_book(2, 2)

    # Retrieve borrowed books
    borrowed_books = e_library.get_borrowed_books(1)
    print("Borrowed books:")
    for book in borrowed_books:
        print(book)

if __name__ == "__main__":
    main()
```
