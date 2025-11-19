"""
Generated Code Metadata:
========================
Original URL: https://kiberahamlets.org
Prompt: What are some potential software solutions or tools that can be used to manage and track the progress of community conservation projects like Kibera Hamlets' Environment Conservation program?
Generated: DETERMINISTIC_6fc007bba014ba69
Batch ID: 20250622_210914
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Community Conservation Project Management Tool
This script provides a framework for managing and tracking community conservation projects.
It includes functionality for project tracking, volunteer management, and reporting.
"""

import sqlite3
from datetime import datetime
from typing import List, Dict, Optional

class ConservationProjectManager:
    """
    A class to manage community conservation projects with features for tracking progress,
    managing volunteers, and generating reports.
    """
    
    def __init__(self, db_name: str = "conservation_projects.db"):
        """
        Initialize the project manager with a SQLite database connection.
        
        Args:
            db_name: Name of the SQLite database file
        """
        self.conn = sqlite3.connect(db_name)
        self._create_tables()
    
    def _create_tables(self) -> None:
        """Create necessary database tables if they don't exist."""
        cursor = self.conn.cursor()
        
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS projects (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT,
            start_date TEXT,
            target_end_date TEXT,
            status TEXT CHECK(status IN ('planned', 'active', 'completed', 'cancelled')),
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
        """)
        
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS milestones (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            project_id INTEGER,
            name TEXT NOT NULL,
            description TEXT,
            target_date TEXT,
            completed BOOLEAN DEFAULT 0,
            completion_date TEXT,
            FOREIGN KEY (project_id) REFERENCES projects(id)
        )
        """)
        
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS volunteers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE,
            phone TEXT,
            skills TEXT,
            join_date TEXT DEFAULT CURRENT_TIMESTAMP
        )
        """)
        
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS project_volunteers (
            project_id INTEGER,
            volunteer_id INTEGER,
            role TEXT,
            hours_contributed REAL DEFAULT 0,
            PRIMARY KEY (project_id, volunteer_id),
            FOREIGN KEY (project_id) REFERENCES projects(id),
            FOREIGN KEY (volunteer_id) REFERENCES volunteers(id)
        )
        """)
        
        self.conn.commit()
    
    def add_project(self, name: str, description: str, start_date: str, 
                   target_end_date: str, status: str = "planned") -> int:
        """
        Add a new conservation project to the database.
        
        Args:
            name: Project name
            description: Project description
            start_date: Project start date (YYYY-MM-DD)
            target_end_date: Project target end date (YYYY-MM-DD)
            status: Initial project status
            
        Returns:
            The ID of the newly created project
        """
        try:
            cursor = self.conn.cursor()
            cursor.execute("""
            INSERT INTO projects (name, description, start_date, target_end_date, status)
            VALUES (?, ?, ?, ?, ?)
            """, (name, description, start_date, target_end_date, status))
            self.conn.commit()
            return cursor.lastrowid
        except sqlite3.Error as e:
            self.conn.rollback()
            raise Exception(f"Error adding project: {str(e)}")
    
    def add_milestone(self, project_id: int, name: str, description: str, 
                     target_date: str) -> int:
        """
        Add a milestone to a project.
        
        Args:
            project_id: ID of the project
            name: Milestone name
            description: Milestone description
            target_date: Target completion date (YYYY-MM-DD)
            
        Returns:
            The ID of the newly created milestone
        """
        try:
            cursor = self.conn.cursor()
            cursor.execute("""
            INSERT INTO milestones (project_id, name, description, target_date)
            VALUES (?, ?, ?, ?)
            """, (project_id, name, description, target_date))
            self.conn.commit()
            return cursor.lastrowid
        except sqlite3.Error as e:
            self.conn.rollback()
            raise Exception(f"Error adding milestone: {str(e)}")
    
    def complete_milestone(self, milestone_id: int) -> None:
        """
        Mark a milestone as completed.
        
        Args:
            milestone_id: ID of the milestone to mark as completed
        """
        try:
            cursor = self.conn.cursor()
            cursor.execute("""
            UPDATE milestones 
            SET completed = 1, completion_date = ?
            WHERE id = ?
            """, (datetime.now().strftime("%Y-%m-%d"), milestone_id))
            self.conn.commit()
        except sqlite3.Error as e:
            self.conn.rollback()
            raise Exception(f"Error completing milestone: {str(e)}")
    
    def add_volunteer(self, name: str, email: str, phone: str = None, 
                     skills: str = None) -> int:
        """
        Add a new volunteer to the database.
        
        Args:
            name: Volunteer name
            email: Volunteer email (must be unique)
            phone: Volunteer phone number
            skills: Volunteer skills/comma-separated list
            
        Returns:
            The ID of the newly created volunteer
        """
        try:
            cursor = self.conn.cursor()
            cursor.execute("""
            INSERT INTO volunteers (name, email, phone, skills)
            VALUES (?, ?, ?, ?)
            """, (name, email, phone, skills))
            self.conn.commit()
            return cursor.lastrowid
        except sqlite3.Error as e:
            self.conn.rollback()
            raise Exception(f"Error adding volunteer: {str(e)}")
    
    def assign_volunteer(self, project_id: int, volunteer_id: int, 
                        role: str = "volunteer") -> None:
        """
        Assign a volunteer to a project.
        
        Args:
            project_id: ID of the project
            volunteer_id: ID of the volunteer
            role: Role of the volunteer in the project
        """
        try:
            cursor = self.conn.cursor()
            cursor.execute("""
            INSERT INTO project_volunteers (project_id, volunteer_id, role)
            VALUES (?, ?, ?)
            """, (project_id, volunteer_id, role))
            self.conn.commit()
        except sqlite3.Error as e:
            self.conn.rollback()
            raise Exception(f"Error assigning volunteer: {str(e)}")
    
    def log_volunteer_hours(self, project_id: int, volunteer_id: int, 
                           hours: float) -> None:
        """
        Log hours contributed by a volunteer to a project.
        
        Args:
            project_id: ID of the project
            volunteer_id: ID of the volunteer
            hours: Number of hours to add
        """
        try:
            cursor = self.conn.cursor()
            cursor.execute("""
            UPDATE project_volunteers
            SET hours_contributed = hours_contributed + ?
            WHERE project_id = ? AND volunteer_id = ?
            """, (hours, project_id, volunteer_id))
            self.conn.commit()
        except sqlite3.Error as e:
            self.conn.rollback()
            raise Exception(f"Error logging volunteer hours: {str(e)}")
    
    def get_project_progress(self, project_id: int) -> Dict:
        """
        Get progress information for a project.
        
        Args:
            project_id: ID of the project
            
        Returns:
            Dictionary containing project progress information
        """
        try:
            cursor = self.conn.cursor()
            
            # Get project details
            cursor.execute("SELECT * FROM projects WHERE id = ?", (project_id,))
            project = cursor.fetchone()
            
            if not project:
                raise Exception("Project not found")
            
            # Get milestones
            cursor.execute("""
            SELECT COUNT(*) as total_milestones,
                   SUM(CASE WHEN completed = 1 THEN 1 ELSE 0 END) as completed_milestones
            FROM milestones
            WHERE project_id = ?
            """, (project_id,))
            milestones = cursor.fetchone()
            
            # Get volunteer stats
            cursor.execute("""
            SELECT COUNT(*) as total_volunteers,
                   SUM(hours_contributed) as total_hours
            FROM project_volunteers
            WHERE project_id = ?
            """, (project_id,))
            volunteers = cursor.fetchone()
            
            return {
                "project": dict(zip([col[0] for col in cursor.description], project)),
                "milestones": {
                    "total": milestones[0],
                    "completed": milestones[1],
                    "completion_percentage": round((milestones[1] / milestones[0]) * 100, 2) 
                                             if milestones[0] > 0 else 0
                },
                "volunteers": {
                    "total": volunteers[0],
                    "total_hours": volunteers[1]
                }
            }
        except sqlite3.Error as e:
            raise Exception(f"Error getting project progress: {str(e)}")
    
    def generate_project_report(self, project_id: int) -> Dict:
        """
        Generate a comprehensive report
