"""
Generated Code Metadata:
========================
Original URL: https://pgngaya.in
Prompt: Generate a code snippet for a school management system that includes features like student admission, transport management, and library cataloging, inspired by the offerings of Param Gyan Niketan.
Generated: DETERMINISTIC_bb092fb3398c2f8b
Batch ID: 20250612_162511
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# School Management System for Param Gyan Niketan
# Features: Student Admission, Transport Management, Library Cataloging

import sqlite3
from datetime import datetime
from typing import List, Dict, Optional, Tuple

class DatabaseManager:
    """Handles database connections and operations."""
    
    def __init__(self, db_name: str = "school_management.db"):
        """Initialize database connection."""
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self._create_tables()
    
    def _create_tables(self) -> None:
        """Create necessary tables if they don't exist."""
        try:
            # Students table
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS students (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    dob TEXT NOT NULL,
                    grade TEXT NOT NULL,
                    parent_name TEXT NOT NULL,
                    contact TEXT NOT NULL,
                    address TEXT NOT NULL,
                    admission_date TEXT NOT NULL,
                    status TEXT DEFAULT 'Active'
                )
            """)
            
            # Transport table
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS transport (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    route_name TEXT NOT NULL,
                    vehicle_number TEXT NOT NULL,
                    driver_name TEXT NOT NULL,
                    contact TEXT NOT NULL,
                    stops TEXT NOT NULL,  # JSON array of stops
                    capacity INTEGER NOT NULL,
                    current_students INTEGER DEFAULT 0
                )
            """)
            
            # Library books table
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS library_books (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    author TEXT NOT NULL,
                    isbn TEXT UNIQUE NOT NULL,
                    category TEXT NOT NULL,
                    quantity INTEGER NOT NULL,
                    available INTEGER NOT NULL,
                    location TEXT NOT NULL
                )
            """)
            
            # Book issues table
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS book_issues (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    book_id INTEGER NOT NULL,
                    student_id INTEGER NOT NULL,
                    issue_date TEXT NOT NULL,
                    return_date TEXT,
                    status TEXT DEFAULT 'Issued',
                    FOREIGN KEY (book_id) REFERENCES library_books(id),
                    FOREIGN KEY (student_id) REFERENCES students(id)
                )
            """)
            
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Database error: {e}")
    
    def execute_query(self, query: str, params: Tuple = ()) -> Optional[sqlite3.Cursor]:
        """Execute a SQL query with parameters."""
        try:
            self.cursor.execute(query, params)
            self.conn.commit()
            return self.cursor
        except sqlite3.Error as e:
            print(f"Query execution error: {e}")
            return None
    
    def close(self) -> None:
        """Close database connection."""
        self.conn.close()

class StudentManager:
    """Handles student admission and management."""
    
    def __init__(self, db_manager: DatabaseManager):
        self.db = db_manager
    
    def admit_student(self, name: str, dob: str, grade: str, parent_name: str, 
                     contact: str, address: str) -> bool:
        """Admit a new student to the school."""
        admission_date = datetime.now().strftime("%Y-%m-%d")
        query = """
            INSERT INTO students 
            (name, dob, grade, parent_name, contact, address, admission_date)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """
        params = (name, dob, grade, parent_name, contact, address, admission_date)
        result = self.db.execute_query(query, params)
        return result is not None
    
    def get_student(self, student_id: int) -> Optional[Dict]:
        """Retrieve student details by ID."""
        query = "SELECT * FROM students WHERE id = ?"
        cursor = self.db.execute_query(query, (student_id,))
        if cursor:
            row = cursor.fetchone()
            if row:
                columns = [desc[0] for desc in cursor.description]
                return dict(zip(columns, row))
        return None
    
    def update_student_status(self, student_id: int, status: str) -> bool:
        """Update student status (Active/Inactive)."""
        valid_statuses = ['Active', 'Inactive']
        if status not in valid_statuses:
            return False
        query = "UPDATE students SET status = ? WHERE id = ?"
        result = self.db.execute_query(query, (status, student_id))
        return result is not None

class TransportManager:
    """Handles school transport management."""
    
    def __init__(self, db_manager: DatabaseManager):
        self.db = db_manager
    
    def add_route(self, route_name: str, vehicle_number: str, driver_name: str, 
                 contact: str, stops: List[str], capacity: int) -> bool:
        """Add a new transport route."""
        stops_json = ",".join(stops)
        query = """
            INSERT INTO transport 
            (route_name, vehicle_number, driver_name, contact, stops, capacity)
            VALUES (?, ?, ?, ?, ?, ?)
        """
        params = (route_name, vehicle_number, driver_name, contact, stops_json, capacity)
        result = self.db.execute_query(query, params)
        return result is not None
    
    def assign_student_to_route(self, student_id: int, route_id: int) -> bool:
        """Assign a student to a transport route."""
        # Check capacity
        query = "SELECT capacity, current_students FROM transport WHERE id = ?"
        cursor = self.db.execute_query(query, (route_id,))
        if cursor:
            row = cursor.fetchone()
            if row and row[1] < row[0]:
                # Update count
                update_query = "UPDATE transport SET current_students = current_students + 1 WHERE id = ?"
                self.db.execute_query(update_query, (route_id,))
                return True
        return False
    
    def get_route_details(self, route_id: int) -> Optional[Dict]:
        """Get details of a transport route."""
        query = "SELECT * FROM transport WHERE id = ?"
        cursor = self.db.execute_query(query, (route_id,))
        if cursor:
            row = cursor.fetchone()
            if row:
                columns = [desc[0] for desc in cursor.description]
                return dict(zip(columns, row))
        return None

class LibraryManager:
    """Handles library cataloging and book management."""
    
    def __init__(self, db_manager: DatabaseManager):
        self.db = db_manager
    
    def add_book(self, title: str, author: str, isbn: str, category: str, 
                quantity: int, location: str) -> bool:
        """Add a new book to the library catalog."""
        query = """
            INSERT INTO library_books 
            (title, author, isbn, category, quantity, available, location)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """
        params = (title, author, isbn, category, quantity, quantity, location)
        result = self.db.execute_query(query, params)
        return result is not None
    
    def issue_book(self, book_id: int, student_id: int) -> bool:
        """Issue a book to a student."""
        # Check book availability
        query = "SELECT available FROM library_books WHERE id = ?"
        cursor = self.db.execute_query(query, (book_id,))
        if cursor:
            row = cursor.fetchone()
            if row and row[0] > 0:
                # Update availability
                update_query = "UPDATE library_books SET available = available - 1 WHERE id = ?"
                self.db.execute_query(update_query, (book_id,))
                
                # Record issue
                issue_date = datetime.now().strftime("%Y-%m-%d")
                issue_query = """
                    INSERT INTO book_issues 
                    (book_id, student_id, issue_date, status)
                    VALUES (?, ?, ?, ?)
                """
                self.db.execute_query(issue_query, (book_id, student_id, issue_date, "Issued"))
                return True
        return False
    
    def return_book(self, issue_id: int) -> bool:
        """Return a book to the library."""
        # Get issue details
        query = "SELECT book_id FROM book_issues WHERE id = ? AND status = 'Issued'"
        cursor = self.db.execute_query(query, (issue_id,))
        if cursor:
            row = cursor.fetchone()
            if row:
                book_id = row[0]
                # Update book availability
                update_book_query = "UPDATE library_books SET available = available + 1 WHERE id = ?"
                self.db.execute_query(update_book_query, (book_id,))
                
                # Update issue record
                return_date = datetime.now().strftime("%Y-%m-%d")
                update_issue_query = """
                    UPDATE book_issues 
                    SET return_date = ?, status = 'Returned' 
                    WHERE id = ?
                """
                self.db.execute_query(update_issue_query, (return_date, issue_id))
                return True
        return False
    
    def search_books
