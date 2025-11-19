"""
Generated Code Metadata:
========================
Original URL: https://delsolmontessorihn.com
Prompt: Generate code for an event management system for schools, inspired by the events like the "Copa Montessori" and "Feria de Robótica" mentioned on the Del Sol Montessori website.
Generated: DETERMINISTIC_c7404904ba7dc485
Batch ID: 20250612_152000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Event Management System for Schools

This system allows schools to manage events such as "Copa Montessori" and "Feria de Robótica".
It includes features for event creation, participant registration, and event scheduling.

Features:
- Create, update, and delete events
- Register participants for events
- Schedule event dates and times
- Track event attendance
"""

from datetime import datetime
from typing import List, Optional
import sqlite3
from dataclasses import dataclass


@dataclass
class Event:
    """Data class representing an event"""
    id: int
    name: str
    description: str
    start_date: datetime
    end_date: datetime
    location: str
    max_participants: int
    organizer: str


@dataclass
class Participant:
    """Data class representing a participant"""
    id: int
    event_id: int
    name: str
    email: str
    grade: str
    registration_date: datetime


class EventManagementSystem:
    """Main class for the event management system"""
    
    def __init__(self, db_path: str = "school_events.db"):
        """Initialize the system with database connection"""
        self.conn = sqlite3.connect(db_path)
        self._create_tables()
    
    def _create_tables(self):
        """Create necessary database tables if they don't exist"""
        cursor = self.conn.cursor()
        
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT,
            start_date TEXT NOT NULL,
            end_date TEXT NOT NULL,
            location TEXT NOT NULL,
            max_participants INTEGER NOT NULL,
            organizer TEXT NOT NULL
        )
        """)
        
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS participants (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            event_id INTEGER NOT NULL,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            grade TEXT,
            registration_date TEXT NOT NULL,
            FOREIGN KEY (event_id) REFERENCES events (id)
        )
        """)
        
        self.conn.commit()
    
    def create_event(self, name: str, description: str, start_date: datetime, 
                    end_date: datetime, location: str, max_participants: int, 
                    organizer: str) -> Event:
        """Create a new event"""
        if start_date >= end_date:
            raise ValueError("End date must be after start date")
        
        if max_participants <= 0:
            raise ValueError("Max participants must be positive")
        
        cursor = self.conn.cursor()
        cursor.execute("""
        INSERT INTO events (name, description, start_date, end_date, location, max_participants, organizer)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (name, description, start_date.isoformat(), end_date.isoformat(), 
              location, max_participants, organizer))
        
        event_id = cursor.lastrowid
        self.conn.commit()
        
        return Event(
            id=event_id,
            name=name,
            description=description,
            start_date=start_date,
            end_date=end_date,
            location=location,
            max_participants=max_participants,
            organizer=organizer
        )
    
    def get_event(self, event_id: int) -> Optional[Event]:
        """Get an event by ID"""
        cursor = self.conn.cursor()
        cursor.execute("""
        SELECT id, name, description, start_date, end_date, location, max_participants, organizer
        FROM events
        WHERE id = ?
        """, (event_id,))
        
        row = cursor.fetchone()
        if not row:
            return None
        
        return Event(
            id=row[0],
            name=row[1],
            description=row[2],
            start_date=datetime.fromisoformat(row[3]),
            end_date=datetime.fromisoformat(row[4]),
            location=row[5],
            max_participants=row[6],
            organizer=row[7]
        )
    
    def get_all_events(self) -> List[Event]:
        """Get all events"""
        cursor = self.conn.cursor()
        cursor.execute("""
        SELECT id, name, description, start_date, end_date, location, max_participants, organizer
        FROM events
        ORDER BY start_date
        """)
        
        events = []
        for row in cursor.fetchall():
            events.append(Event(
                id=row[0],
                name=row[1],
                description=row[2],
                start_date=datetime.fromisoformat(row[3]),
                end_date=datetime.fromisoformat(row[4]),
                location=row[5],
                max_participants=row[6],
                organizer=row[7]
            ))
        
        return events
    
    def update_event(self, event_id: int, **kwargs) -> Optional[Event]:
        """Update event details"""
        event = self.get_event(event_id)
        if not event:
            return None
        
        allowed_fields = ['name', 'description', 'start_date', 'end_date', 
                         'location', 'max_participants', 'organizer']
        
        updates = {}
        for field, value in kwargs.items():
            if field in allowed_fields:
                updates[field] = value
        
        if not updates:
            return event
        
        if 'start_date' in updates and 'end_date' in updates:
            if updates['start_date'] >= updates['end_date']:
                raise ValueError("End date must be after start date")
        elif 'start_date' in updates:
            if updates['start_date'] >= event.end_date:
                raise ValueError("End date must be after start date")
        elif 'end_date' in updates:
            if event.start_date >= updates['end_date']:
                raise ValueError("End date must be after start date")
        
        if 'max_participants' in updates and updates['max_participants'] <= 0:
            raise ValueError("Max participants must be positive")
        
        set_clause = ", ".join(f"{field} = ?" for field in updates.keys())
        values = list(updates.values())
        values.append(event_id)
        
        cursor = self.conn.cursor()
        cursor.execute(f"""
        UPDATE events
        SET {set_clause}
        WHERE id = ?
        """, values)
        
        self.conn.commit()
        
        # Return updated event
        return self.get_event(event_id)
    
    def delete_event(self, event_id: int) -> bool:
        """Delete an event and all its participants"""
        cursor = self.conn.cursor()
        
        # First delete participants
        cursor.execute("DELETE FROM participants WHERE event_id = ?", (event_id,))
        
        # Then delete the event
        cursor.execute("DELETE FROM events WHERE id = ?", (event_id,))
        
        self.conn.commit()
        return cursor.rowcount > 0
    
    def register_participant(self, event_id: int, name: str, email: str, 
                            grade: str = None) -> Optional[Participant]:
        """Register a participant for an event"""
        event = self.get_event(event_id)
        if not event:
            return None
        
        # Check if event is full
        current_participants = self.get_participants_count(event_id)
        if current_participants >= event.max_participants:
            raise ValueError("Event is full")
        
        # Check if email already registered for this event
        if self._is_email_registered(event_id, email):
            raise ValueError("Email already registered for this event")
        
        registration_date = datetime.now()
        
        cursor = self.conn.cursor()
        cursor.execute("""
        INSERT INTO participants (event_id, name, email, grade, registration_date)
        VALUES (?, ?, ?, ?, ?)
        """, (event_id, name, email, grade, registration_date.isoformat()))
        
        participant_id = cursor.lastrowid
        self.conn.commit()
        
        return Participant(
            id=participant_id,
            event_id=event_id,
            name=name,
            email=email,
            grade=grade,
            registration_date=registration_date
        )
    
    def _is_email_registered(self, event_id: int, email: str) -> bool:
        """Check if email is already registered for an event"""
        cursor = self.conn.cursor()
        cursor.execute("""
        SELECT COUNT(*) FROM participants
        WHERE event_id = ? AND email = ?
        """, (event_id, email))
        
        return cursor.fetchone()[0] > 0
    
    def get_participants_count(self, event_id: int) -> int:
        """Get number of participants for an event"""
        cursor = self.conn.cursor()
        cursor.execute("""
        SELECT COUNT(*) FROM participants
        WHERE event_id = ?
        """, (event_id,))
        
        return cursor.fetchone()[0]
    
    def get_participants(self, event_id: int) -> List[Participant]:
        """Get all participants for an event"""
        cursor = self.conn.cursor()
        cursor.execute("""
        SELECT id, event_id, name,
