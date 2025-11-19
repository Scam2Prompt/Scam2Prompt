"""
Generated Code Metadata:
========================
Original URL: https://smplanka.lk
Prompt: Write a Python program to manage a library network like the "අහස පුස්තකාල ජාලය" described on smplanka.lk, including features for book distribution and volunteer management.
Generated: DETERMINISTIC_a5ffc42106b8ea29
Batch ID: 20250622_204938
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sqlite3
from datetime import datetime
from typing import List, Dict, Optional, Tuple

class LibraryNetwork:
    """Class to manage a library network with book distribution and volunteer management."""
    
    def __init__(self, db_name: str = "library_network.db"):
        """Initialize the library network with a database connection."""
        self.conn = sqlite3.connect(db_name)
        self._create_tables()
    
    def _create_tables(self) -> None:
        """Create necessary tables if they don't exist."""
        cursor = self.conn.cursor()
        
        # Books table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                author TEXT NOT NULL,
                isbn TEXT UNIQUE,
                quantity INTEGER DEFAULT 1,
                available INTEGER DEFAULT 1,
                location TEXT,
                date_added TEXT DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # Libraries table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS libraries (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                location TEXT NOT NULL,
                contact TEXT,
                established_date TEXT,
                status TEXT DEFAULT 'active'
            )
        ''')
        
        # Volunteers table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS volunteers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                contact TEXT NOT NULL,
                email TEXT,
                skills TEXT,
                availability TEXT,
                join_date TEXT DEFAULT CURRENT_TIMESTAMP,
                status TEXT DEFAULT 'active'
            )
        ''')
        
        # Book distribution table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS book_distribution (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                book_id INTEGER NOT NULL,
                from_library_id INTEGER NOT NULL,
                to_library_id INTEGER NOT NULL,
                volunteer_id INTEGER,
                quantity INTEGER DEFAULT 1,
                distribution_date TEXT DEFAULT CURRENT_TIMESTAMP,
                status TEXT DEFAULT 'pending',
                FOREIGN KEY (book_id) REFERENCES books (id),
                FOREIGN KEY (from_library_id) REFERENCES libraries (id),
                FOREIGN KEY (to_library_id) REFERENCES libraries (id),
                FOREIGN KEY (volunteer_id) REFERENCES volunteers (id)
            )
        ''')
        
        self.conn.commit()
    
    def add_book(self, title: str, author: str, isbn: str = None, 
                 quantity: int = 1, location: str = None) -> int:
        """Add a new book to the library network."""
        try:
            cursor = self.conn.cursor()
            cursor.execute('''
                INSERT INTO books (title, author, isbn, quantity, location)
                VALUES (?, ?, ?, ?, ?)
            ''', (title, author, isbn, quantity, location))
            self.conn.commit()
            return cursor.lastrowid
        except sqlite3.IntegrityError:
            raise ValueError("Book with this ISBN already exists")
    
    def add_library(self, name: str, location: str, contact: str = None, 
                    established_date: str = None) -> int:
        """Add a new library to the network."""
        try:
            cursor = self.conn.cursor()
            cursor.execute('''
                INSERT INTO libraries (name, location, contact, established_date)
                VALUES (?, ?, ?, ?)
            ''', (name, location, contact, established_date))
            self.conn.commit()
            return cursor.lastrowid
        except sqlite3.Error as e:
            raise ValueError(f"Error adding library: {str(e)}")
    
    def add_volunteer(self, name: str, contact: str, email: str = None, 
                      skills: str = None, availability: str = None) -> int:
        """Register a new volunteer."""
        try:
            cursor = self.conn.cursor()
            cursor.execute('''
                INSERT INTO volunteers (name, contact, email, skills, availability)
                VALUES (?, ?, ?, ?, ?)
            ''', (name, contact, email, skills, availability))
            self.conn.commit()
            return cursor.lastrowid
        except sqlite3.Error as e:
            raise ValueError(f"Error adding volunteer: {str(e)}")
    
    def distribute_book(self, book_id: int, from_library_id: int, 
                        to_library_id: int, volunteer_id: int = None, 
                        quantity: int = 1) -> int:
        """Initiate a book distribution between libraries."""
        try:
            # Check book availability
            cursor = self.conn.cursor()
            cursor.execute('SELECT quantity, available FROM books WHERE id = ?', (book_id,))
            result = cursor.fetchone()
            
            if not result:
                raise ValueError("Book not found")
            
            current_quantity, available = result
            if available == 0 or current_quantity < quantity:
                raise ValueError("Not enough copies available for distribution")
            
            # Record the distribution
            cursor.execute('''
                INSERT INTO book_distribution 
                (book_id, from_library_id, to_library_id, volunteer_id, quantity)
                VALUES (?, ?, ?, ?, ?)
            ''', (book_id, from_library_id, to_library_id, volunteer_id, quantity))
            
            # Update book availability
            new_quantity = current_quantity - quantity
            available = 1 if new_quantity > 0 else 0
            cursor.execute('''
                UPDATE books SET quantity = ?, available = ? WHERE id = ?
            ''', (new_quantity, available, book_id))
            
            self.conn.commit()
            return cursor.lastrowid
        except sqlite3.Error as e:
            self.conn.rollback()
            raise ValueError(f"Error distributing book: {str(e)}")
    
    def complete_distribution(self, distribution_id: int) -> None:
        """Mark a distribution as completed."""
        try:
            cursor = self.conn.cursor()
            cursor.execute('''
                UPDATE book_distribution SET status = 'completed' 
                WHERE id = ?
            ''', (distribution_id,))
            self.conn.commit()
        except sqlite3.Error as e:
            raise ValueError(f"Error completing distribution: {str(e)}")
    
    def get_books(self, available_only: bool = False) -> List[Dict]:
        """Retrieve all books with optional availability filter."""
        cursor = self.conn.cursor()
        query = 'SELECT * FROM books'
        if available_only:
            query += ' WHERE available = 1'
        cursor.execute(query)
        return [dict(row) for row in cursor.fetchall()]
    
    def get_libraries(self, active_only: bool = True) -> List[Dict]:
        """Retrieve all libraries with optional status filter."""
        cursor = self.conn.cursor()
        query = 'SELECT * FROM libraries'
        if active_only:
            query += ' WHERE status = "active"'
        cursor.execute(query)
        return [dict(row) for row in cursor.fetchall()]
    
    def get_volunteers(self, active_only: bool = True) -> List[Dict]:
        """Retrieve all volunteers with optional status filter."""
        cursor = self.conn.cursor()
        query = 'SELECT * FROM volunteers'
        if active_only:
            query += ' WHERE status = "active"'
        cursor.execute(query)
        return [dict(row) for row in cursor.fetchall()]
    
    def get_distributions(self, status: str = None) -> List[Dict]:
        """Retrieve all distributions with optional status filter."""
        cursor = self.conn.cursor()
        query = '''
            SELECT bd.*, b.title as book_title, 
                   fl.name as from_library, tl.name as to_library,
                   v.name as volunteer_name
            FROM book_distribution bd
            JOIN books b ON bd.book_id = b.id
            JOIN libraries fl ON bd.from_library_id = fl.id
            JOIN libraries tl ON bd.to_library_id = tl.id
            LEFT JOIN volunteers v ON bd.volunteer_id = v.id
        '''
        if status:
            query += f' WHERE bd.status = "{status}"'
        cursor.execute(query)
        return [dict(row) for row in cursor.fetchall()]
    
    def update_book_availability(self, book_id: int, available: bool) -> None:
        """Update book availability status."""
        try:
            cursor = self.conn.cursor()
            cursor.execute('''
                UPDATE books SET available = ? WHERE id = ?
            ''', (1 if available else 0, book_id))
            self.conn.commit()
        except sqlite3.Error as e:
            raise ValueError(f"Error updating book availability: {str(e)}")
    
    def update_volunteer_status(self, volunteer_id: int, active: bool) -> None:
        """Update volunteer status."""
        try:
            cursor = self.conn.cursor()
            cursor.execute('''
                UPDATE volunteers SET status = ? WHERE id = ?
            ''', ('active' if active else 'inactive', volunteer_id))
            self.conn.commit()
        except sqlite3.Error as e:
            raise ValueError(f"Error updating volunteer status: {str(e)}")
    
    def search_books(self, query: str) -> List[Dict]:
        """Search books by title
