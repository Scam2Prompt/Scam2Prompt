"""
Generated Code Metadata:
========================
Original URL: https://rakhshandamemorial.org
Prompt: Write code to implement a volunteer management system for RM, including features for registration, task assignment, and tracking hours contributed.
Generated: DETERMINISTIC_e7aedb137e0b7e95
Batch ID: 20250612_152240
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
    """A volunteer management system for RM with registration, task assignment, and hour tracking."""
    
    def __init__(self, db_name: str = "volunteer_management.db"):
        """Initialize the system with a SQLite database connection."""
        self.conn = sqlite3.connect(db_name)
        self._create_tables()
    
    def _create_tables(self) -> None:
        """Create necessary tables if they don't exist."""
        cursor = self.conn.cursor()
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS volunteers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                phone TEXT,
                skills TEXT,
                registration_date TEXT NOT NULL,
                status TEXT DEFAULT 'active'
            )
        """)
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT,
                required_skills TEXT,
                start_date TEXT,
                end_date TEXT,
                status TEXT DEFAULT 'pending'
            )
        """)
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS assignments (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                volunteer_id INTEGER NOT NULL,
                task_id INTEGER NOT NULL,
                assignment_date TEXT NOT NULL,
                completion_date TEXT,
                status TEXT DEFAULT 'assigned',
                FOREIGN KEY (volunteer_id) REFERENCES volunteers (id),
                FOREIGN KEY (task_id) REFERENCES tasks (id)
            )
        """)
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS hours (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                volunteer_id INTEGER NOT NULL,
                task_id INTEGER NOT NULL,
                date TEXT NOT NULL,
                hours REAL NOT NULL,
                description TEXT,
                FOREIGN KEY (volunteer_id) REFERENCES volunteers (id),
                FOREIGN KEY (task_id) REFERENCES tasks (id)
            )
        """)
        
        self.conn.commit()
    
    def register_volunteer(
        self,
        name: str,
        email: str,
        phone: Optional[str] = None,
        skills: Optional[str] = None
    ) -> int:
        """Register a new volunteer and return their ID."""
        try:
            cursor = self.conn.cursor()
            registration_date = datetime.now().isoformat()
            cursor.execute(
                """
                INSERT INTO volunteers (name, email, phone, skills, registration_date)
                VALUES (?, ?, ?, ?, ?)
                """,
                (name, email, phone, skills, registration_date)
            )
            self.conn.commit()
            return cursor.lastrowid
        except sqlite3.IntegrityError:
            raise ValueError("A volunteer with this email already exists.")
    
    def update_volunteer(
        self,
        volunteer_id: int,
        name: Optional[str] = None,
        email: Optional[str] = None,
        phone: Optional[str] = None,
        skills: Optional[str] = None,
        status: Optional[str] = None
    ) -> None:
        """Update volunteer information."""
        updates = []
        params = []
        
        if name:
            updates.append("name = ?")
            params.append(name)
        if email:
            updates.append("email = ?")
            params.append(email)
        if phone:
            updates.append("phone = ?")
            params.append(phone)
        if skills:
            updates.append("skills = ?")
            params.append(skills)
        if status:
            updates.append("status = ?")
            params.append(status)
        
        if not updates:
            return
        
        params.append(volunteer_id)
        query = f"UPDATE volunteers SET {', '.join(updates)} WHERE id = ?"
        
        cursor = self.conn.cursor()
        cursor.execute(query, params)
        self.conn.commit()
    
    def get_volunteer(self, volunteer_id: int) -> Dict:
        """Retrieve a volunteer's details by ID."""
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM volunteers WHERE id = ?", (volunteer_id,))
        result = cursor.fetchone()
        
        if not result:
            raise ValueError("Volunteer not found.")
        
        columns = [desc[0] for desc in cursor.description]
        return dict(zip(columns, result))
    
    def list_volunteers(self, status: Optional[str] = None) -> List[Dict]:
        """List all volunteers, optionally filtered by status."""
        cursor = self.conn.cursor()
        
        if status:
            cursor.execute("SELECT * FROM volunteers WHERE status = ?", (status,))
        else:
            cursor.execute("SELECT * FROM volunteers")
        
        columns = [desc[0] for desc in cursor.description]
        return [dict(zip(columns, row)) for row in cursor.fetchall()]
    
    def create_task(
        self,
        title: str,
        description: Optional[str] = None,
        required_skills: Optional[str] = None,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None
    ) -> int:
        """Create a new task and return its ID."""
        cursor = self.conn.cursor()
        cursor.execute(
            """
            INSERT INTO tasks (title, description, required_skills, start_date, end_date)
            VALUES (?, ?, ?, ?, ?)
            """,
            (title, description, required_skills, start_date, end_date)
        )
        self.conn.commit()
        return cursor.lastrowid
    
    def update_task(
        self,
        task_id: int,
        title: Optional[str] = None,
        description: Optional[str] = None,
        required_skills: Optional[str] = None,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
        status: Optional[str] = None
    ) -> None:
        """Update task information."""
        updates = []
        params = []
        
        if title:
            updates.append("title = ?")
            params.append(title)
        if description:
            updates.append("description = ?")
            params.append(description)
        if required_skills:
            updates.append("required_skills = ?")
            params.append(required_skills)
        if start_date:
            updates.append("start_date = ?")
            params.append(start_date)
        if end_date:
            updates.append("end_date = ?")
            params.append(end_date)
        if status:
            updates.append("status = ?")
            params.append(status)
        
        if not updates:
            return
        
        params.append(task_id)
        query = f"UPDATE tasks SET {', '.join(updates)} WHERE id = ?"
        
        cursor = self.conn.cursor()
        cursor.execute(query, params)
        self.conn.commit()
    
    def get_task(self, task_id: int) -> Dict:
        """Retrieve a task's details by ID."""
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM tasks WHERE id = ?", (task_id,))
        result = cursor.fetchone()
        
        if not result:
            raise ValueError("Task not found.")
        
        columns = [desc[0] for desc in cursor.description]
        return dict(zip(columns, result))
    
    def list_tasks(self, status: Optional[str] = None) -> List[Dict]:
        """List all tasks, optionally filtered by status."""
        cursor = self.conn.cursor()
        
        if status:
            cursor.execute("SELECT * FROM tasks WHERE status = ?", (status,))
        else:
            cursor.execute("SELECT * FROM tasks")
        
        columns = [desc[0] for desc in cursor.description]
        return [dict(zip(columns, row)) for row in cursor.fetchall()]
    
    def assign_task(self, volunteer_id: int, task_id: int) -> int:
        """Assign a task to a volunteer and return the assignment ID."""
        try:
            cursor = self.conn.cursor()
            assignment_date = datetime.now().isoformat()
            cursor.execute(
                """
                INSERT INTO assignments (volunteer_id, task_id, assignment_date)
                VALUES (?, ?, ?)
                """,
                (volunteer_id, task_id, assignment_date)
            )
            self.conn.commit()
            return cursor.lastrowid
        except sqlite3.IntegrityError:
            raise ValueError("Invalid volunteer or task ID.")
    
    def complete_task(self, assignment_id: int) -> None:
        """Mark a task assignment as completed."""
        cursor = self.conn.cursor()
        completion_date = datetime.now().isoformat()
        cursor.execute(
            """
            UPDATE assignments
            SET status = 'completed', completion_date = ?
            WHERE id = ?
            """,
            (completion_date, assignment_id)
        )
        self.conn.commit()
    
    def get_assignment(self, assignment_id: int) -> Dict:
        """Retrieve an assignment's details by ID."""
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM assignments WHERE id = ?", (assignment_id,))
        result = cursor.fetchone()
        
        if not result:
            raise ValueError("Assignment not found.")
        
        columns = [desc[0] for desc in cursor.description]
        return dict(zip(columns, result))
    
    def list
