"""
Generated Code Metadata:
========================
Original URL: https://dalilamedeiros.com
Prompt: How can I implement a workshop registration system for a mentoring program like the one offered by Dalila Medeiros?
Generated: DETERMINISTIC_dc658e3837253c19
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# workshop_registration_system.py
import sqlite3
from datetime import datetime
from typing import Optional, List, Dict, Tuple

class WorkshopRegistrationSystem:
    """
    A workshop registration system for a mentoring program.
    Handles workshop creation, participant registration, and management.
    """

    def __init__(self, db_name: str = "workshop_registration.db"):
        """
        Initialize the system with a SQLite database.
        
        Args:
            db_name: Name of the SQLite database file
        """
        self.conn = sqlite3.connect(db_name)
        self._create_tables()

    def _create_tables(self) -> None:
        """Create necessary database tables if they don't exist."""
        cursor = self.conn.cursor()
        
        # Workshops table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS workshops (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT,
                mentor_name TEXT NOT NULL,
                max_participants INTEGER NOT NULL,
                start_datetime TEXT NOT NULL,
                end_datetime TEXT NOT NULL,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        # Participants table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS participants (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                phone TEXT,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        # Registrations table (junction table)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS registrations (
                workshop_id INTEGER NOT NULL,
                participant_id INTEGER NOT NULL,
                registered_at TEXT DEFAULT CURRENT_TIMESTAMP,
                PRIMARY KEY (workshop_id, participant_id),
                FOREIGN KEY (workshop_id) REFERENCES workshops(id),
                FOREIGN KEY (participant_id) REFERENCES participants(id)
            )
        """)
        
        self.conn.commit()

    def create_workshop(
        self,
        title: str,
        mentor_name: str,
        max_participants: int,
        start_datetime: str,
        end_datetime: str,
        description: Optional[str] = None
    ) -> int:
        """
        Create a new workshop.
        
        Args:
            title: Workshop title
            mentor_name: Name of the mentor
            max_participants: Maximum number of participants
            start_datetime: Start datetime in ISO format
            end_datetime: End datetime in ISO format
            description: Optional workshop description
            
        Returns:
            ID of the created workshop
            
        Raises:
            ValueError: If datetime format is invalid or max_participants <= 0
        """
        try:
            # Validate datetimes
            datetime.fromisoformat(start_datetime)
            datetime.fromisoformat(end_datetime)
            
            if max_participants <= 0:
                raise ValueError("max_participants must be positive")
                
            cursor = self.conn.cursor()
            cursor.execute("""
                INSERT INTO workshops (
                    title, description, mentor_name, max_participants, 
                    start_datetime, end_datetime
                ) VALUES (?, ?, ?, ?, ?, ?)
            """, (title, description, mentor_name, max_participants, start_datetime, end_datetime))
            
            self.conn.commit()
            return cursor.lastrowid
        except ValueError as e:
            raise ValueError(f"Invalid input: {str(e)}")
        except sqlite3.Error as e:
            raise Exception(f"Database error: {str(e)}")

    def register_participant(
        self,
        workshop_id: int,
        name: str,
        email: str,
        phone: Optional[str] = None
    ) -> Tuple[int, bool]:
        """
        Register a participant for a workshop.
        
        Args:
            workshop_id: ID of the workshop to register for
            name: Participant name
            email: Participant email (must be unique)
            phone: Optional participant phone number
            
        Returns:
            Tuple of (participant_id, is_new_participant)
            
        Raises:
            ValueError: If workshop is full or doesn't exist
            Exception: For database errors
        """
        try:
            cursor = self.conn.cursor()
            
            # Check if workshop exists and has space
            cursor.execute("""
                SELECT max_participants, COUNT(participant_id)
                FROM workshops
                LEFT JOIN registrations ON workshops.id = registrations.workshop_id
                WHERE workshops.id = ?
                GROUP BY workshops.id
            """, (workshop_id,))
            
            result = cursor.fetchone()
            if not result:
                raise ValueError("Workshop does not exist")
                
            max_participants, current_participants = result
            if current_participants >= max_participants:
                raise ValueError("Workshop is full")
            
            # Check if participant exists
            cursor.execute("SELECT id FROM participants WHERE email = ?", (email,))
            participant = cursor.fetchone()
            
            if participant:
                participant_id = participant[0]
                is_new = False
            else:
                # Create new participant
                cursor.execute("""
                    INSERT INTO participants (name, email, phone)
                    VALUES (?, ?, ?)
                """, (name, email, phone))
                participant_id = cursor.lastrowid
                is_new = True
            
            # Register participant for workshop
            cursor.execute("""
                INSERT OR IGNORE INTO registrations (workshop_id, participant_id)
                VALUES (?, ?)
            """, (workshop_id, participant_id))
            
            self.conn.commit()
            return (participant_id, is_new)
        except sqlite3.IntegrityError:
            raise ValueError("Participant already registered for this workshop")
        except sqlite3.Error as e:
            raise Exception(f"Database error: {str(e)}")

    def get_workshop_details(self, workshop_id: int) -> Optional[Dict]:
        """
        Get details for a specific workshop.
        
        Args:
            workshop_id: ID of the workshop
            
        Returns:
            Dictionary with workshop details or None if not found
        """
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT 
                id, title, description, mentor_name, 
                max_participants, start_datetime, end_datetime
            FROM workshops
            WHERE id = ?
        """, (workshop_id,))
        
        row = cursor.fetchone()
        if not row:
            return None
            
        return {
            "id": row[0],
            "title": row[1],
            "description": row[2],
            "mentor_name": row[3],
            "max_participants": row[4],
            "start_datetime": row[5],
            "end_datetime": row[6]
        }

    def get_workshop_participants(self, workshop_id: int) -> List[Dict]:
        """
        Get all participants registered for a workshop.
        
        Args:
            workshop_id: ID of the workshop
            
        Returns:
            List of participant dictionaries
        """
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT p.id, p.name, p.email, p.phone, r.registered_at
            FROM participants p
            JOIN registrations r ON p.id = r.participant_id
            WHERE r.workshop_id = ?
            ORDER BY r.registered_at
        """, (workshop_id,))
        
        return [
            {
                "id": row[0],
                "name": row[1],
                "email": row[2],
                "phone": row[3],
                "registered_at": row[4]
            }
            for row in cursor.fetchall()
        ]

    def get_upcoming_workshops(self) -> List[Dict]:
        """
        Get all upcoming workshops.
        
        Returns:
            List of workshop dictionaries with current registration count
        """
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT 
                w.id, w.title, w.description, w.mentor_name, 
                w.max_participants, w.start_datetime, w.end_datetime,
                COUNT(r.participant_id) as registered_count
            FROM workshops w
            LEFT JOIN registrations r ON w.id = r.workshop_id
            WHERE datetime(w.start_datetime) > datetime('now')
            GROUP BY w.id
            ORDER BY w.start_datetime
        """)
        
        return [
            {
                "id": row[0],
                "title": row[1],
                "description": row[2],
                "mentor_name": row[3],
                "max_participants": row[4],
                "start_datetime": row[5],
                "end_datetime": row[6],
                "registered_count": row[7],
                "available_spots": row[4] - row[7]
            }
            for row in cursor.fetchall()
        ]

    def cancel_registration(self, workshop_id: int, participant_id: int) -> bool:
        """
        Cancel a participant's registration for a workshop.
        
        Args:
            workshop_id: ID of the workshop
            participant_id: ID of the participant
            
        Returns:
            True if registration was cancelled, False if it didn't exist
        """
        cursor =
