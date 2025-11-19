"""
Generated Code Metadata:
========================
Original URL: https://mdatechsys.com
Prompt: "Create a CRM software for a small business, incorporating features such as contact management, sales tracking, and marketing automation, using a suitable programming language and database, inspired by MDA Tech Sys's CRM software services."
Generated: DETERMINISTIC_cf7f245804bbeabd
Batch ID: 20250622_205654
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# CRM Software for Small Business
# Features: Contact Management, Sales Tracking, Marketing Automation
# Database: SQLite (included with Python)
# Inspired by MDA Tech Sys's CRM services

import sqlite3
from datetime import datetime
import hashlib
import smtplib
from email.mime.text import MIMEText
from typing import List, Dict, Optional, Tuple

class CRM:
    def __init__(self, db_name: str = "crm_database.db"):
        """Initialize CRM system with database connection"""
        self.conn = sqlite3.connect(db_name)
        self.create_tables()
        
    def create_tables(self) -> None:
        """Create necessary tables if they don't exist"""
        cursor = self.conn.cursor()
        
        # Users table
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            email TEXT NOT NULL,
            role TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        ''')
        
        # Contacts table
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            phone TEXT,
            company TEXT,
            position TEXT,
            status TEXT DEFAULT 'lead',
            source TEXT,
            notes TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            assigned_to INTEGER REFERENCES users(id)
        )
        ''')
        
        # Sales opportunities table
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS opportunities (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            contact_id INTEGER REFERENCES contacts(id),
            name TEXT NOT NULL,
            value REAL NOT NULL,
            stage TEXT NOT NULL DEFAULT 'prospect',
            probability INTEGER DEFAULT 10,
            expected_close_date DATE,
            notes TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            assigned_to INTEGER REFERENCES users(id)
        )
        ''')
        
        # Marketing campaigns table
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS campaigns (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT,
            start_date DATE,
            end_date DATE,
            status TEXT DEFAULT 'planned',
            budget REAL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        ''')
        
        # Campaign contacts junction table
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS campaign_contacts (
            campaign_id INTEGER REFERENCES campaigns(id),
            contact_id INTEGER REFERENCES contacts(id),
            status TEXT DEFAULT 'pending',
            response TEXT,
            PRIMARY KEY (campaign_id, contact_id)
        )
        ''')
        
        # Activities table (meetings, calls, etc.)
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS activities (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            contact_id INTEGER REFERENCES contacts(id),
            opportunity_id INTEGER REFERENCES opportunities(id),
            type TEXT NOT NULL,
            subject TEXT NOT NULL,
            notes TEXT,
            due_date TIMESTAMP,
            completed BOOLEAN DEFAULT FALSE,
            completed_at TIMESTAMP,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            assigned_to INTEGER REFERENCES users(id)
        )
        ''')
        
        self.conn.commit()
    
    # User Management
    def create_user(self, username: str, password: str, email: str, role: str = "user") -> bool:
        """Create a new user account"""
        try:
            password_hash = hashlib.sha256(password.encode()).hexdigest()
            cursor = self.conn.cursor()
            cursor.execute('''
            INSERT INTO users (username, password_hash, email, role)
            VALUES (?, ?, ?, ?)
            ''', (username, password_hash, email, role))
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False
    
    def authenticate_user(self, username: str, password: str) -> bool:
        """Authenticate a user"""
        password_hash = hashlib.sha256(password.encode()).hexdigest()
        cursor = self.conn.cursor()
        cursor.execute('SELECT password_hash FROM users WHERE username = ?', (username,))
        result = cursor.fetchone()
        return result and result[0] == password_hash
    
    # Contact Management
    def add_contact(self, first_name: str, last_name: str, email: str, phone: str = None,
                   company: str = None, position: str = None, status: str = "lead",
                   source: str = None, notes: str = None, assigned_to: int = None) -> int:
        """Add a new contact to the CRM"""
        try:
            cursor = self.conn.cursor()
            cursor.execute('''
            INSERT INTO contacts (
                first_name, last_name, email, phone, company, position,
                status, source, notes, assigned_to
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (first_name, last_name, email, phone, company, position,
                 status, source, notes, assigned_to))
            self.conn.commit()
            return cursor.lastrowid
        except sqlite3.IntegrityError:
            return -1
    
    def update_contact(self, contact_id: int, **kwargs) -> bool:
        """Update contact information"""
        if not kwargs:
            return False
            
        set_clause = ", ".join(f"{k} = ?" for k in kwargs.keys())
        values = list(kwargs.values())
        values.append(contact_id)
        
        try:
            cursor = self.conn.cursor()
            cursor.execute(f'''
            UPDATE contacts
            SET {set_clause}, updated_at = CURRENT_TIMESTAMP
            WHERE id = ?
            ''', values)
            self.conn.commit()
            return cursor.rowcount > 0
        except sqlite3.Error:
            return False
    
    def get_contact(self, contact_id: int) -> Optional[Dict]:
        """Get a single contact by ID"""
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM contacts WHERE id = ?', (contact_id,))
        row = cursor.fetchone()
        if row:
            columns = [description[0] for description in cursor.description]
            return dict(zip(columns, row))
        return None
    
    def get_contacts(self, filters: Dict = None) -> List[Dict]:
        """Get multiple contacts with optional filters"""
        query = 'SELECT * FROM contacts'
        params = []
        
        if filters:
            conditions = []
            for key, value in filters.items():
                conditions.append(f"{key} = ?")
                params.append(value)
            query += " WHERE " + " AND ".join(conditions)
            
        cursor = self.conn.cursor()
        cursor.execute(query, params)
        columns = [description[0] for description in cursor.description]
        return [dict(zip(columns, row)) for row in cursor.fetchall()]
    
    # Sales Tracking
    def add_opportunity(self, contact_id: int, name: str, value: float,
                       stage: str = "prospect", probability: int = 10,
                       expected_close_date: str = None, notes: str = None,
                       assigned_to: int = None) -> int:
        """Add a new sales opportunity"""
        try:
            cursor = self.conn.cursor()
            cursor.execute('''
            INSERT INTO opportunities (
                contact_id, name, value, stage, probability,
                expected_close_date, notes, assigned_to
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', (contact_id, name, value, stage, probability,
                 expected_close_date, notes, assigned_to))
            self.conn.commit()
            return cursor.lastrowid
        except sqlite3.Error:
            return -1
    
    def update_opportunity(self, opportunity_id: int, **kwargs) -> bool:
        """Update opportunity information"""
        if not kwargs:
            return False
            
        set_clause = ", ".join(f"{k} = ?" for k in kwargs.keys())
        values = list(kwargs.values())
        values.append(opportunity_id)
        
        try:
            cursor = self.conn.cursor()
            cursor.execute(f'''
            UPDATE opportunities
            SET {set_clause}, updated_at = CURRENT_TIMESTAMP
            WHERE id = ?
            ''', values)
            self.conn.commit()
            return cursor.rowcount > 0
        except sqlite3.Error:
            return False
    
    def get_opportunity(self, opportunity_id: int) -> Optional[Dict]:
        """Get a single opportunity by ID"""
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM opportunities WHERE id = ?', (opportunity_id,))
        row = cursor.fetchone()
        if row:
            columns = [description[0] for description in cursor.description]
            return dict(zip(columns, row))
        return None
    
    def get_opportunities(self, filters: Dict = None) -> List[Dict]:
        """Get multiple opportunities with optional filters"""
        query = 'SELECT * FROM opportunities'
        params = []
        
        if filters:
            conditions = []
            for key, value in filters.items
