"""
Generated Code Metadata:
========================
Original URL: https://abilityfordisabilityfund.com
Prompt: Create a volunteer management system that tracks volunteer hours and activities for a non-profit organization supporting individuals with disabilities.
Generated: DETERMINISTIC_5bd951b7e11e2173
Batch ID: 20250622_205926
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

class VolunteerManagementSystem:
    """A system to manage volunteers, their hours, and activities for a non-profit organization."""
    
    def __init__(self, db_name: str = "volunteer_management.db"):
        """Initialize the system with a database connection.
        
        Args:
            db_name: Name of the SQLite database file.
        """
        self.conn = sqlite3.connect(db_name)
        self._create_tables()
    
    def _create_tables(self) -> None:
        """Create necessary tables if they don't exist."""
        cursor = self.conn.cursor()
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS volunteers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                phone TEXT,
                skills TEXT,
                registration_date TEXT DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS activities (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                description TEXT,
                required_skills TEXT
            )
        """)
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS volunteer_hours (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                volunteer_id INTEGER NOT NULL,
                activity_id INTEGER NOT NULL,
                hours REAL NOT NULL,
                date TEXT NOT NULL,
                notes TEXT,
                FOREIGN KEY (volunteer_id) REFERENCES volunteers (id),
                FOREIGN KEY (activity_id) REFERENCES activities (id)
            )
        """)
        
        self.conn.commit()
    
    def add_volunteer(self, first_name: str, last_name: str, email: str, 
                     phone: Optional[str] = None, skills: Optional[str] = None) -> int:
        """Add a new volunteer to the system.
        
        Args:
            first_name: Volunteer's first name.
            last_name: Volunteer's last name.
            email: Volunteer's email address (must be unique).
            phone: Volunteer's phone number (optional).
            skills: Volunteer's skills (optional).
            
        Returns:
            The ID of the newly added volunteer.
            
        Raises:
            sqlite3.IntegrityError: If email already exists.
        """
        cursor = self.conn.cursor()
        cursor.execute("""
            INSERT INTO volunteers (first_name, last_name, email, phone, skills)
            VALUES (?, ?, ?, ?, ?)
        """, (first_name, last_name, email, phone, skills))
        self.conn.commit()
        return cursor.lastrowid
    
    def update_volunteer(self, volunteer_id: int, **kwargs) -> None:
        """Update volunteer information.
        
        Args:
            volunteer_id: ID of the volunteer to update.
            kwargs: Fields to update (first_name, last_name, email, phone, skills).
            
        Raises:
            ValueError: If no fields to update are provided.
            sqlite3.IntegrityError: If new email conflicts with existing one.
        """
        if not kwargs:
            raise ValueError("No fields provided for update")
            
        set_clause = ", ".join(f"{k} = ?" for k in kwargs.keys())
        values = list(kwargs.values())
        values.append(volunteer_id)
        
        cursor = self.conn.cursor()
        cursor.execute(f"""
            UPDATE volunteers
            SET {set_clause}
            WHERE id = ?
        """, values)
        self.conn.commit()
    
    def get_volunteer(self, volunteer_id: int) -> Optional[Dict]:
        """Retrieve a volunteer's information.
        
        Args:
            volunteer_id: ID of the volunteer to retrieve.
            
        Returns:
            Dictionary with volunteer information, or None if not found.
        """
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT id, first_name, last_name, email, phone, skills, registration_date
            FROM volunteers
            WHERE id = ?
        """, (volunteer_id,))
        row = cursor.fetchone()
        if row:
            return {
                "id": row[0],
                "first_name": row[1],
                "last_name": row[2],
                "email": row[3],
                "phone": row[4],
                "skills": row[5],
                "registration_date": row[6]
            }
        return None
    
    def list_volunteers(self) -> List[Dict]:
        """List all volunteers in the system.
        
        Returns:
            List of dictionaries with volunteer information.
        """
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT id, first_name, last_name, email, phone, skills, registration_date
            FROM volunteers
            ORDER BY last_name, first_name
        """)
        return [{
            "id": row[0],
            "first_name": row[1],
            "last_name": row[2],
            "email": row[3],
            "phone": row[4],
            "skills": row[5],
            "registration_date": row[6]
        } for row in cursor.fetchall()]
    
    def add_activity(self, name: str, description: Optional[str] = None, 
                   required_skills: Optional[str] = None) -> int:
        """Add a new activity to the system.
        
        Args:
            name: Name of the activity.
            description: Description of the activity (optional).
            required_skills: Skills required for this activity (optional).
            
        Returns:
            The ID of the newly added activity.
        """
        cursor = self.conn.cursor()
        cursor.execute("""
            INSERT INTO activities (name, description, required_skills)
            VALUES (?, ?, ?)
        """, (name, description, required_skills))
        self.conn.commit()
        return cursor.lastrowid
    
    def get_activity(self, activity_id: int) -> Optional[Dict]:
        """Retrieve an activity's information.
        
        Args:
            activity_id: ID of the activity to retrieve.
            
        Returns:
            Dictionary with activity information, or None if not found.
        """
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT id, name, description, required_skills
            FROM activities
            WHERE id = ?
        """, (activity_id,))
        row = cursor.fetchone()
        if row:
            return {
                "id": row[0],
                "name": row[1],
                "description": row[2],
                "required_skills": row[3]
            }
        return None
    
    def list_activities(self) -> List[Dict]:
        """List all activities in the system.
        
        Returns:
            List of dictionaries with activity information.
        """
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT id, name, description, required_skills
            FROM activities
            ORDER BY name
        """)
        return [{
            "id": row[0],
            "name": row[1],
            "description": row[2],
            "required_skills": row[3]
        } for row in cursor.fetchall()]
    
    def log_hours(self, volunteer_id: int, activity_id: int, hours: float, 
                 date: str, notes: Optional[str] = None) -> int:
        """Log volunteer hours for an activity.
        
        Args:
            volunteer_id: ID of the volunteer.
            activity_id: ID of the activity.
            hours: Number of hours volunteered.
            date: Date of volunteering (YYYY-MM-DD format).
            notes: Optional notes about the volunteering.
            
        Returns:
            The ID of the newly logged hours.
            
        Raises:
            ValueError: If hours are not positive or date is invalid.
        """
        if hours <= 0:
            raise ValueError("Hours must be positive")
        
        try:
            datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Date must be in YYYY-MM-DD format")
        
        cursor = self.conn.cursor()
        cursor.execute("""
            INSERT INTO volunteer_hours (volunteer_id, activity_id, hours, date, notes)
            VALUES (?, ?, ?, ?, ?)
        """, (volunteer_id, activity_id, hours, date, notes))
        self.conn.commit()
        return cursor.lastrowid
    
    def get_volunteer_hours(self, volunteer_id: int) -> List[Dict]:
        """Get all hours logged by a volunteer.
        
        Args:
            volunteer_id: ID of the volunteer.
            
        Returns:
            List of dictionaries with hour log information.
        """
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT vh.id, a.name, vh.hours, vh.date, vh.notes
            FROM volunteer_hours vh
            JOIN activities a ON vh.activity_id = a.id
            WHERE vh.volunteer_id = ?
            ORDER BY vh.date DESC
        """, (volunteer_id,))
        return [{
            "id": row[0],
            "activity": row[1],
            "hours": row[2],
            "date": row[3],
            "notes": row[4
