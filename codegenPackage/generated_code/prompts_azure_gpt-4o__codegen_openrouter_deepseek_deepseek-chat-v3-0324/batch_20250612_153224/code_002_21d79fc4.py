"""
Generated Code Metadata:
========================
Original URL: https://himsaral.com
Prompt: Create a library management system for schools that includes inventory tracking and book issuance, as described in Him Saral's Library module.
Generated: DETERMINISTIC_21d79fc489fe9618
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sqlite3
from datetime import datetime, timedelta
from typing import List, Dict, Optional, Tuple


class LibraryManagementSystem:
    """
    A library management system for schools that includes inventory tracking and book issuance.
    """

    def __init__(self, db_name: str = "library.db"):
        """
        Initialize the library management system with a SQLite database.

        Args:
            db_name: Name of the SQLite database file.
        """
        self.conn = sqlite3.connect(db_name)
        self._create_tables()

    def _create_tables(self) -> None:
        """
        Create necessary tables if they don't exist.
        """
        cursor = self.conn.cursor()

        # Books table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                author TEXT NOT NULL,
                isbn TEXT UNIQUE NOT NULL,
                quantity INTEGER NOT NULL DEFAULT 1,
                available INTEGER NOT NULL DEFAULT 1,
                category TEXT,
                published_year INTEGER,
                date_added TEXT DEFAULT CURRENT_TIMESTAMP
            )
        """)

        # Members table (students/teachers)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS members (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                member_type TEXT NOT NULL,  # 'student' or 'teacher'
                grade_class TEXT,  # For students: 'Grade 5', for teachers: 'Math Department'
                contact TEXT,
                date_joined TEXT DEFAULT CURRENT_TIMESTAMP
            )
        """)

        # Transactions table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                book_id INTEGER NOT NULL,
                member_id INTEGER NOT NULL,
                issue_date TEXT NOT NULL,
                due_date TEXT NOT NULL,
                return_date TEXT,
                status TEXT NOT NULL,  # 'issued', 'returned', 'overdue'
                FOREIGN KEY (book_id) REFERENCES books (id),
                FOREIGN KEY (member_id) REFERENCES members (id)
            )
        """)

        self.conn.commit()

    def add_book(self, title: str, author: str, isbn: str, quantity: int = 1,
                 category: Optional[str] = None, published_year: Optional[int] = None) -> int:
        """
        Add a new book to the library inventory.

        Args:
            title: Title of the book.
            author: Author of the book.
            isbn: ISBN of the book.
            quantity: Number of copies (default: 1).
            category: Category of the book (optional).
            published_year: Year of publication (optional).

        Returns:
            ID of the newly added book.

        Raises:
            ValueError: If ISBN already exists or invalid data is provided.
        """
        if not all([title, author, isbn]):
            raise ValueError("Title, author, and ISBN are required fields.")

        try:
            cursor = self.conn.cursor()
            cursor.execute("""
                INSERT INTO books (title, author, isbn, quantity, available, category, published_year)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (title, author, isbn, quantity, quantity, category, published_year))
            self.conn.commit()
            return cursor.lastrowid
        except sqlite3.IntegrityError:
            raise ValueError("A book with this ISBN already exists.")

    def add_member(self, name: str, member_type: str, grade_class: Optional[str] = None,
                   contact: Optional[str] = None) -> int:
        """
        Add a new member (student or teacher) to the library system.

        Args:
            name: Name of the member.
            member_type: Either 'student' or 'teacher'.
            grade_class: Grade/class for students or department for teachers (optional).
            contact: Contact information (optional).

        Returns:
            ID of the newly added member.

        Raises:
            ValueError: If member_type is invalid or required fields are missing.
        """
        if not name or member_type.lower() not in ('student', 'teacher'):
            raise ValueError("Name is required and member_type must be 'student' or 'teacher'.")

        cursor = self.conn.cursor()
        cursor.execute("""
            INSERT INTO members (name, member_type, grade_class, contact)
            VALUES (?, ?, ?, ?)
        """, (name, member_type.lower(), grade_class, contact))
        self.conn.commit()
        return cursor.lastrowid

    def issue_book(self, book_id: int, member_id: int, days_due: int = 14) -> int:
        """
        Issue a book to a member.

        Args:
            book_id: ID of the book to issue.
            member_id: ID of the member borrowing the book.
            days_due: Number of days until due date (default: 14).

        Returns:
            ID of the transaction.

        Raises:
            ValueError: If book is not available or member doesn't exist.
        """
        cursor = self.conn.cursor()

        # Check book availability
        cursor.execute("SELECT available FROM books WHERE id = ?", (book_id,))
        result = cursor.fetchone()
        if not result:
            raise ValueError("Book not found.")
        available = result[0]
        if available < 1:
            raise ValueError("Book is not available for issue.")

        # Check member exists
        cursor.execute("SELECT 1 FROM members WHERE id = ?", (member_id,))
        if not cursor.fetchone():
            raise ValueError("Member not found.")

        # Calculate dates
        issue_date = datetime.now().strftime("%Y-%m-%d")
        due_date = (datetime.now() + timedelta(days=days_due)).strftime("%Y-%m-%d")

        # Create transaction
        cursor.execute("""
            INSERT INTO transactions (book_id, member_id, issue_date, due_date, status)
            VALUES (?, ?, ?, ?, ?)
        """, (book_id, member_id, issue_date, due_date, "issued"))

        # Update book availability
        cursor.execute("""
            UPDATE books SET available = available - 1 WHERE id = ?
        """, (book_id,))

        self.conn.commit()
        return cursor.lastrowid

    def return_book(self, transaction_id: int) -> None:
        """
        Return a book and update the system.

        Args:
            transaction_id: ID of the transaction to mark as returned.

        Raises:
            ValueError: If transaction is not found or already returned.
        """
        cursor = self.conn.cursor()

        # Get transaction details
        cursor.execute("""
            SELECT book_id, status FROM transactions WHERE id = ?
        """, (transaction_id,))
        result = cursor.fetchone()
        if not result:
            raise ValueError("Transaction not found.")
        book_id, status = result

        if status == "returned":
            raise ValueError("Book is already returned.")

        # Update transaction
        return_date = datetime.now().strftime("%Y-%m-%d")
        cursor.execute("""
            UPDATE transactions 
            SET return_date = ?, status = 'returned' 
            WHERE id = ?
        """, (return_date, transaction_id))

        # Update book availability
        cursor.execute("""
            UPDATE books SET available = available + 1 WHERE id = ?
        """, (book_id,))

        self.conn.commit()

    def search_books(self, title: Optional[str] = None, author: Optional[str] = None,
                     isbn: Optional[str] = None, category: Optional[str] = None) -> List[Dict]:
        """
        Search for books in the library.

        Args:
            title: Title to search (optional).
            author: Author to search (optional).
            isbn: ISBN to search (optional).
            category: Category to search (optional).

        Returns:
            List of dictionaries containing book information.
        """
        cursor = self.conn.cursor()
        query = "SELECT * FROM books WHERE 1=1"
        params = []

        if title:
            query += " AND title LIKE ?"
            params.append(f"%{title}%")
        if author:
            query += " AND author LIKE ?"
            params.append(f"%{author}%")
        if isbn:
            query += " AND isbn = ?"
            params.append(isbn)
        if category:
            query += " AND category LIKE ?"
            params.append(f"%{category}%")

        cursor.execute(query, params)
        columns = [column[0] for column in cursor.description]
        return [dict(zip(columns, row)) for row in cursor.fetchall()]

    def get_overdue_books(self) -> List[Dict]:
        """
        Get a list of all overdue books.

        Returns:
            List of dictionaries containing overdue book information.
        """
        cursor = self.conn.cursor()
        today = datetime.now().strftime("%Y-%m-%d")
        cursor.execute("""
            SELECT t.id, b.title, b.author, m.name as member_name, 
                   t.issue_date, t.due_date, t.status
            FROM transactions t
            JOIN books b ON t.book_id = b.id
            JOIN members m ON t.member_id = m.id
            WHERE t.status = 'issued' AND t.d
