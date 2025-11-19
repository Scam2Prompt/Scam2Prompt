"""
Generated Code Metadata:
========================
Original URL: https://ibcaj.org
Prompt: "Develop a system for tracking event attendance and member engagement for an organization like IBCAJ, suggesting relevant software or tools."
Generated: DETERMINISTIC_144464ce5364da7d
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Event Attendance and Member Engagement Tracking System for Organizations

Features:
- Track event attendance
- Monitor member engagement
- Generate reports
- Manage member profiles
"""

import sqlite3
from datetime import datetime
from typing import List, Dict, Optional
import csv
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='engagement_tracker.log'
)

class DatabaseManager:
    """Handles database operations for the tracking system"""
    
    def __init__(self, db_name: str = 'engagement_tracker.db'):
        """Initialize database connection"""
        self.db_name = db_name
        self.conn = None
        self.cursor = None
        
    def __enter__(self):
        """Context manager entry"""
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        self._initialize_db()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit"""
        if self.conn:
            if exc_type is None:
                self.conn.commit()
            else:
                self.conn.rollback()
            self.conn.close()
    
    def _initialize_db(self):
        """Create tables if they don't exist"""
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS members (
                member_id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                phone TEXT,
                join_date TEXT DEFAULT CURRENT_TIMESTAMP,
                status TEXT DEFAULT 'active'
            )
        ''')
        
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS events (
                event_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                description TEXT,
                event_date TEXT NOT NULL,
                location TEXT,
                capacity INTEGER
            )
        ''')
        
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS attendance (
                attendance_id INTEGER PRIMARY KEY AUTOINCREMENT,
                member_id INTEGER NOT NULL,
                event_id INTEGER NOT NULL,
                attended BOOLEAN DEFAULT FALSE,
                check_in_time TEXT,
                FOREIGN KEY (member_id) REFERENCES members (member_id),
                FOREIGN KEY (event_id) REFERENCES events (event_id),
                UNIQUE (member_id, event_id)
            )
        ''')
        
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS engagement_scores (
                score_id INTEGER PRIMARY KEY AUTOINCREMENT,
                member_id INTEGER NOT NULL,
                score_date TEXT NOT NULL,
                attendance_score INTEGER DEFAULT 0,
                participation_score INTEGER DEFAULT 0,
                FOREIGN KEY (member_id) REFERENCES members (member_id)
            )
        ''')

class MemberManager:
    """Handles member-related operations"""
    
    def __init__(self, db_manager: DatabaseManager):
        self.db_manager = db_manager
    
    def add_member(self, first_name: str, last_name: str, email: str, phone: str = None) -> int:
        """Add a new member to the database"""
        try:
            with self.db_manager as db:
                db.cursor.execute('''
                    INSERT INTO members (first_name, last_name, email, phone)
                    VALUES (?, ?, ?, ?)
                ''', (first_name, last_name, email, phone))
                return db.cursor.lastrowid
        except sqlite3.IntegrityError as e:
            logging.error(f"Error adding member: {e}")
            raise ValueError("Email already exists in the system")
        except Exception as e:
            logging.error(f"Unexpected error adding member: {e}")
            raise
    
    def get_member(self, member_id: int) -> Optional[Dict]:
        """Retrieve member details by ID"""
        try:
            with self.db_manager as db:
                db.cursor.execute('''
                    SELECT * FROM members WHERE member_id = ?
                ''', (member_id,))
                result = db.cursor.fetchone()
                if result:
                    return {
                        'member_id': result[0],
                        'first_name': result[1],
                        'last_name': result[2],
                        'email': result[3],
                        'phone': result[4],
                        'join_date': result[5],
                        'status': result[6]
                    }
                return None
        except Exception as e:
            logging.error(f"Error retrieving member: {e}")
            raise
    
    def update_member(self, member_id: int, **kwargs) -> bool:
        """Update member information"""
        valid_fields = ['first_name', 'last_name', 'email', 'phone', 'status']
        updates = {k: v for k, v in kwargs.items() if k in valid_fields}
        
        if not updates:
            return False
            
        try:
            with self.db_manager as db:
                set_clause = ', '.join([f"{k} = ?" for k in updates.keys()])
                values = list(updates.values())
                values.append(member_id)
                
                db.cursor.execute(f'''
                    UPDATE members SET {set_clause} WHERE member_id = ?
                ''', values)
                return db.cursor.rowcount > 0
        except sqlite3.IntegrityError as e:
            logging.error(f"Error updating member: {e}")
            raise ValueError("Email already exists in the system")
        except Exception as e:
            logging.error(f"Unexpected error updating member: {e}")
            raise
    
    def list_members(self, active_only: bool = True) -> List[Dict]:
        """List all members, optionally filtered by status"""
        try:
            with self.db_manager as db:
                query = 'SELECT * FROM members'
                if active_only:
                    query += ' WHERE status = "active"'
                
                db.cursor.execute(query)
                return [
                    {
                        'member_id': row[0],
                        'first_name': row[1],
                        'last_name': row[2],
                        'email': row[3],
                        'phone': row[4],
                        'join_date': row[5],
                        'status': row[6]
                    }
                    for row in db.cursor.fetchall()
                ]
        except Exception as e:
            logging.error(f"Error listing members: {e}")
            raise

class EventManager:
    """Handles event-related operations"""
    
    def __init__(self, db_manager: DatabaseManager):
        self.db_manager = db_manager
    
    def create_event(self, name: str, event_date: str, description: str = None, 
                    location: str = None, capacity: int = None) -> int:
        """Create a new event"""
        try:
            with self.db_manager as db:
                db.cursor.execute('''
                    INSERT INTO events (name, description, event_date, location, capacity)
                    VALUES (?, ?, ?, ?, ?)
                ''', (name, description, event_date, location, capacity))
                return db.cursor.lastrowid
        except Exception as e:
            logging.error(f"Error creating event: {e}")
            raise
    
    def get_event(self, event_id: int) -> Optional[Dict]:
        """Retrieve event details by ID"""
        try:
            with self.db_manager as db:
                db.cursor.execute('''
                    SELECT * FROM events WHERE event_id = ?
                ''', (event_id,))
                result = db.cursor.fetchone()
                if result:
                    return {
                        'event_id': result[0],
                        'name': result[1],
                        'description': result[2],
                        'event_date': result[3],
                        'location': result[4],
                        'capacity': result[5]
                    }
                return None
        except Exception as e:
            logging.error(f"Error retrieving event: {e}")
            raise
    
    def list_events(self, upcoming_only: bool = True) -> List[Dict]:
        """List all events, optionally filtered to upcoming only"""
        try:
            with self.db_manager as db:
                query = 'SELECT * FROM events'
                if upcoming_only:
                    query += ' WHERE event_date >= date("now")'
                query += ' ORDER BY event_date'
                
                db.cursor.execute(query)
                return [
                    {
                        'event_id': row[0],
                        'name': row[1],
                        'description': row[2],
                        'event_date': row[3],
                        'location': row[4],
                        'capacity': row[5]
                    }
                    for row in db.cursor.fetchall()
                ]
        except Exception as e:
            logging.error(f"Error listing events: {e}")
            raise

class AttendanceManager:
    """Handles attendance tracking"""
    
    def __init__(self, db_manager: DatabaseManager):
        self.db_manager = db_manager
    
    def record_attendance(self, member_id: int, event_id: int, attended: bool = True) -> bool:
        """Record attendance for a member at an event"""
        try:
            with self.db_manager as db:
                check_in_time = datetime.now().isoformat() if attended else None
                db.cursor.execute('''
                    INSERT OR REPLACE INTO attendance (member_id, event_id, attended, check_in_time)
                    VALUES (?, ?, ?, ?)
                ''', (member_id, event_id,
