"""
Generated Code Metadata:
========================
Original URL: https://dawah-smiraa.sa
Prompt: Develop a plan and provide code for a simple database to store and manage information about volunteers, donors, and community members for an organization like جمعية الدعوة والإرشاد وتوعية الجاليات بمحافظة سميراء.
Generated: DETERMINISTIC_7240e845ceaa4c9c
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Database Schema Design for Volunteer Management System
# This system will store and manage information about volunteers, donors, and community members

import sqlite3
from datetime import datetime
from typing import Optional, List, Dict, Any

class DatabaseManager:
    """Main database manager class for handling all database operations"""
    
    def __init__(self, db_name: str = "volunteer_management.db"):
        """Initialize the database connection and create tables if they don't exist"""
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self._create_tables()
    
    def _create_tables(self) -> None:
        """Create necessary tables in the database"""
        create_tables_sql = [
            """
            CREATE TABLE IF NOT EXISTS persons (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                phone TEXT NOT NULL,
                email TEXT,
                address TEXT,
                city TEXT,
                registration_date TEXT DEFAULT CURRENT_TIMESTAMP,
                notes TEXT,
                type TEXT CHECK(type IN ('volunteer', 'donor', 'community_member'))
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS volunteer_skills (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                person_id INTEGER NOT NULL,
                skill TEXT NOT NULL,
                proficiency_level TEXT,
                FOREIGN KEY (person_id) REFERENCES persons(id) ON DELETE CASCADE
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS donations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                donor_id INTEGER NOT NULL,
                amount REAL NOT NULL,
                donation_date TEXT DEFAULT CURRENT_TIMESTAMP,
                donation_type TEXT NOT NULL,
                receipt_issued INTEGER DEFAULT 0,
                notes TEXT,
                FOREIGN KEY (donor_id) REFERENCES persons(id) ON DELETE CASCADE
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS volunteer_hours (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                volunteer_id INTEGER NOT NULL,
                activity TEXT NOT NULL,
                hours REAL NOT NULL,
                date TEXT NOT NULL,
                approved INTEGER DEFAULT 0,
                notes TEXT,
                FOREIGN KEY (volunteer_id) REFERENCES persons(id) ON DELETE CASCADE
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS events (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                description TEXT,
                event_date TEXT NOT NULL,
                location TEXT NOT NULL,
                organizer_id INTEGER,
                status TEXT DEFAULT 'planned',
                FOREIGN KEY (organizer_id) REFERENCES persons(id)
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS event_participants (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                event_id INTEGER NOT NULL,
                person_id INTEGER NOT NULL,
                role TEXT,
                attended INTEGER DEFAULT 0,
                FOREIGN KEY (event_id) REFERENCES events(id) ON DELETE CASCADE,
                FOREIGN KEY (person_id) REFERENCES persons(id) ON DELETE CASCADE
            )
            """
        ]
        
        for sql in create_tables_sql:
            self.cursor.execute(sql)
        self.conn.commit()
    
    def add_person(self, name: str, phone: str, email: Optional[str] = None, 
                   address: Optional[str] = None, city: Optional[str] = None, 
                   notes: Optional[str] = None, person_type: str = "community_member") -> int:
        """Add a new person to the database"""
        if person_type not in ['volunteer', 'donor', 'community_member']:
            raise ValueError("Invalid person type")
            
        sql = """
        INSERT INTO persons (name, phone, email, address, city, notes, type)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """
        self.cursor.execute(sql, (name, phone, email, address, city, notes, person_type))
        self.conn.commit()
        return self.cursor.lastrowid
    
    def update_person(self, person_id: int, **kwargs) -> bool:
        """Update person information"""
        if not kwargs:
            return False
            
        valid_fields = ['name', 'phone', 'email', 'address', 'city', 'notes', 'type']
        updates = {k: v for k, v in kwargs.items() if k in valid_fields}
        
        if not updates:
            return False
            
        set_clause = ", ".join([f"{k} = ?" for k in updates.keys()])
        sql = f"UPDATE persons SET {set_clause} WHERE id = ?"
        
        try:
            self.cursor.execute(sql, (*updates.values(), person_id))
            self.conn.commit()
            return self.cursor.rowcount > 0
        except sqlite3.Error:
            return False
    
    def get_person(self, person_id: int) -> Optional[Dict[str, Any]]:
        """Retrieve a person's information by ID"""
        sql = "SELECT * FROM persons WHERE id = ?"
        self.cursor.execute(sql, (person_id,))
        row = self.cursor.fetchone()
        
        if not row:
            return None
            
        columns = [desc[0] for desc in self.cursor.description]
        return dict(zip(columns, row))
    
    def list_persons(self, person_type: Optional[str] = None) -> List[Dict[str, Any]]:
        """List all persons or filter by type"""
        sql = "SELECT * FROM persons"
        params = ()
        
        if person_type:
            if person_type not in ['volunteer', 'donor', 'community_member']:
                raise ValueError("Invalid person type")
            sql += " WHERE type = ?"
            params = (person_type,)
            
        self.cursor.execute(sql, params)
        columns = [desc[0] for desc in self.cursor.description]
        return [dict(zip(columns, row)) for row in self.cursor.fetchall()]
    
    def add_volunteer_skill(self, person_id: int, skill: str, proficiency_level: Optional[str] = None) -> int:
        """Add a skill for a volunteer"""
        sql = """
        INSERT INTO volunteer_skills (person_id, skill, proficiency_level)
        VALUES (?, ?, ?)
        """
        self.cursor.execute(sql, (person_id, skill, proficiency_level))
        self.conn.commit()
        return self.cursor.lastrowid
    
    def get_volunteer_skills(self, person_id: int) -> List[Dict[str, Any]]:
        """Get all skills for a volunteer"""
        sql = "SELECT * FROM volunteer_skills WHERE person_id = ?"
        self.cursor.execute(sql, (person_id,))
        columns = [desc[0] for desc in self.cursor.description]
        return [dict(zip(columns, row)) for row in self.cursor.fetchall()]
    
    def record_donation(self, donor_id: int, amount: float, donation_type: str, 
                        receipt_issued: bool = False, notes: Optional[str] = None) -> int:
        """Record a new donation"""
        sql = """
        INSERT INTO donations (donor_id, amount, donation_type, receipt_issued, notes)
        VALUES (?, ?, ?, ?, ?)
        """
        self.cursor.execute(sql, (donor_id, amount, donation_type, int(receipt_issued), notes))
        self.conn.commit()
        return self.cursor.lastrowid
    
    def get_donations(self, donor_id: Optional[int] = None) -> List[Dict[str, Any]]:
        """Get all donations or filter by donor"""
        sql = "SELECT * FROM donations"
        params = ()
        
        if donor_id:
            sql += " WHERE donor_id = ?"
            params = (donor_id,)
            
        self.cursor.execute(sql, params)
        columns = [desc[0] for desc in self.cursor.description]
        return [dict(zip(columns, row)) for row in self.cursor.fetchall()]
    
    def record_volunteer_hours(self, volunteer_id: int, activity: str, hours: float, 
                              date: str, approved: bool = False, notes: Optional[str] = None) -> int:
        """Record volunteer hours"""
        try:
            datetime.strptime(date, '%Y-%m-%d')  # Validate date format
        except ValueError:
            raise ValueError("Invalid date format. Use YYYY-MM-DD")
            
        sql = """
        INSERT INTO volunteer_hours (volunteer_id, activity, hours, date, approved, notes)
        VALUES (?, ?, ?, ?, ?, ?)
        """
        self.cursor.execute(sql, (volunteer_id, activity, hours, date, int(approved), notes))
        self.conn.commit()
        return self.cursor.lastrowid
    
    def get_volunteer_hours(self, volunteer_id: Optional[int] = None, 
                           approved_only: bool = False) -> List[Dict[str, Any]]:
        """Get volunteer hours, optionally filtered by volunteer and approval status"""
        sql = "SELECT * FROM volunteer_hours"
        conditions = []
        params = []
        
        if volunteer_id:
            conditions.append("volunteer_id = ?")
            params.append(volunteer_id)
            
        if approved_only:
            conditions.append("approved = 1")
            
        if conditions:
            sql += " WHERE " + " AND
