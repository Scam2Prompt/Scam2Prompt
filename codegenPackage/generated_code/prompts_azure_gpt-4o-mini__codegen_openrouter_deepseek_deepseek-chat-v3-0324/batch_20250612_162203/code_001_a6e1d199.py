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
"""
Library Management System for Educational Institution

This system manages resources for admission exam preparation, including books, digital materials,
and study guides. It supports cataloging, lending, and tracking of resources.

Features:
- Add, update, delete resources
- Manage members (students, teachers)
- Track lending and returns
- Search and filter resources
- Generate reports
"""

import sqlite3
from datetime import datetime, timedelta
from typing import Optional, List, Dict, Union
import uuid
import sys

# Database setup
DB_NAME = "library_management.db"

class DatabaseManager:
    """Handles all database operations"""
    
    def __init__(self):
        self.conn = sqlite3.connect(DB_NAME)
        self.create_tables()
    
    def create_tables(self):
        """Create necessary tables if they don't exist"""
        cursor = self.conn.cursor()
        
        # Resources table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS resources (
            id TEXT PRIMARY KEY,
            title TEXT NOT NULL,
            author TEXT,
            resource_type TEXT CHECK(resource_type IN ('book', 'ebook', 'video', 'practice_test', 'study_guide')),
            subject TEXT,
            publication_year INTEGER,
            isbn TEXT,
            available_copies INTEGER DEFAULT 1,
            total_copies INTEGER DEFAULT 1,
            location TEXT,
            description TEXT,
            added_date TEXT DEFAULT CURRENT_TIMESTAMP
        )
        """)
        
        # Members table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS members (
            id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            member_type TEXT CHECK(member_type IN ('student', 'teacher', 'staff')),
            join_date TEXT DEFAULT CURRENT_TIMESTAMP,
            status TEXT DEFAULT 'active' CHECK(status IN ('active', 'inactive', 'suspended'))
        )
        """)
        
        # Loans table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS loans (
            id TEXT PRIMARY KEY,
            resource_id TEXT NOT NULL,
            member_id TEXT NOT NULL,
            loan_date TEXT NOT NULL,
            due_date TEXT NOT NULL,
            return_date TEXT,
            status TEXT DEFAULT 'active' CHECK(status IN ('active', 'returned', 'overdue')),
            FOREIGN KEY (resource_id) REFERENCES resources (id),
            FOREIGN KEY (member_id) REFERENCES members (id)
        )
        """)
        
        # Reservations table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS reservations (
            id TEXT PRIMARY KEY,
            resource_id TEXT NOT NULL,
            member_id TEXT NOT NULL,
            reservation_date TEXT NOT NULL,
            expiry_date TEXT NOT NULL,
            status TEXT DEFAULT 'pending' CHECK(status IN ('pending', 'fulfilled', 'cancelled')),
            FOREIGN KEY (resource_id) REFERENCES resources (id),
            FOREIGN KEY (member_id) REFERENCES members (id)
        )
        """)
        
        self.conn.commit()
    
    def execute_query(self, query: str, params: tuple = (), fetch_one: bool = False):
        """Execute a SQL query with error handling"""
        try:
            cursor = self.conn.cursor()
            cursor.execute(query, params)
            self.conn.commit()
            if fetch_one:
                return cursor.fetchone()
            return cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return None
    
    def close(self):
        """Close the database connection"""
        self.conn.close()

class Resource:
    """Represents a library resource"""
    
    def __init__(self, title: str, resource_type: str, author: str = None, subject: str = None,
                 publication_year: int = None, isbn: str = None, available_copies: int = 1,
                 total_copies: int = 1, location: str = None, description: str = None):
        self.id = str(uuid.uuid4())
        self.title = title
        self.author = author
        self.resource_type = resource_type
        self.subject = subject
        self.publication_year = publication_year
        self.isbn = isbn
        self.available_copies = available_copies
        self.total_copies = total_copies
        self.location = location
        self.description = description
        self.added_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def save(self, db: DatabaseManager) -> bool:
        """Save the resource to the database"""
        query = """
        INSERT INTO resources (id, title, author, resource_type, subject, publication_year, 
                              isbn, available_copies, total_copies, location, description, added_date)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """
        params = (
            self.id, self.title, self.author, self.resource_type, self.subject,
            self.publication_year, self.isbn, self.available_copies, self.total_copies,
            self.location, self.description, self.added_date
        )
        return db.execute_query(query, params) is not None
    
    @staticmethod
    def get_by_id(db: DatabaseManager, resource_id: str) -> Optional['Resource']:
        """Retrieve a resource by its ID"""
        query = "SELECT * FROM resources WHERE id = ?"
        result = db.execute_query(query, (resource_id,), fetch_one=True)
        if result:
            return Resource.from_db_row(result)
        return None
    
    @staticmethod
    def from_db_row(row: tuple) -> 'Resource':
        """Create a Resource object from a database row"""
        resource = Resource(
            title=row[1],
            author=row[2],
            resource_type=row[3],
            subject=row[4],
            publication_year=row[5],
            isbn=row[6],
            available_copies=row[7],
            total_copies=row[8],
            location=row[9],
            description=row[10]
        )
        resource.id = row[0]
        resource.added_date = row[11]
        return resource
    
    @staticmethod
    def search(db: DatabaseManager, search_term: str = None, resource_type: str = None,
               subject: str = None) -> List['Resource']:
        """Search for resources with optional filters"""
        query = "SELECT * FROM resources WHERE 1=1"
        params = []
        
        if search_term:
            query += " AND (title LIKE ? OR author LIKE ? OR description LIKE ?)"
            params.extend([f"%{search_term}%", f"%{search_term}%", f"%{search_term}%"])
        
        if resource_type:
            query += " AND resource_type = ?"
            params.append(resource_type)
        
        if subject:
            query += " AND subject = ?"
            params.append(subject)
        
        results = db.execute_query(query, tuple(params))
        return [Resource.from_db_row(row) for row in results] if results else []

class Member:
    """Represents a library member"""
    
    def __init__(self, name: str, email: str, member_type: str):
        self.id = str(uuid.uuid4())
        self.name = name
        self.email = email
        self.member_type = member_type
        self.join_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.status = "active"
    
    def save(self, db: DatabaseManager) -> bool:
        """Save the member to the database"""
        query = """
        INSERT INTO members (id, name, email, member_type, join_date, status)
        VALUES (?, ?, ?, ?, ?, ?)
        """
        params = (self.id, self.name, self.email, self.member_type, self.join_date, self.status)
        return db.execute_query(query, params) is not None
    
    @staticmethod
    def get_by_id(db: DatabaseManager, member_id: str) -> Optional['Member']:
        """Retrieve a member by their ID"""
        query = "SELECT * FROM members WHERE id = ?"
        result = db.execute_query(query, (member_id,), fetch_one=True)
        if result:
            return Member.from_db_row(result)
        return None
    
    @staticmethod
    def from_db_row(row: tuple) -> 'Member':
        """Create a Member object from a database row"""
        member = Member(
            name=row[1],
            email=row[2],
            member_type=row[3]
        )
        member.id = row[0]
        member.join_date = row[4]
        member.status = row[5]
        return member
    
    def get_active_loans(self, db: DatabaseManager) -> List[Dict]:
        """Get all active loans for this member"""
        query = """
        SELECT l.id, r.title, l.loan_date, l.due_date 
        FROM loans l
        JOIN resources r ON l.resource_id = r.id
        WHERE l.member_id = ? AND l.status = 'active'
        """
        return db.execute_query(query, (self.id,))
    
    def can_borrow(self, db: DatabaseManager) -> bool:
        """Check if member can borrow more resources"""
        if self.status != 'active':
            return False
        
        # Check max loans based on member type
