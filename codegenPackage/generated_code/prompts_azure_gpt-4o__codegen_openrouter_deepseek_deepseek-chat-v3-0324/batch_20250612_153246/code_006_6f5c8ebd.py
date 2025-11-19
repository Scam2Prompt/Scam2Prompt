"""
Generated Code Metadata:
========================
Original URL: https://pahubel.com
Prompt: Recommend software solutions for tracking the progress of turnkey construction projects, focusing on healthcare facilities like dental clinics, as described by Pahubel Ibérica S.L.
Generated: DETERMINISTIC_6f5c8ebd7d7604fd
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Software Solution for Tracking Turnkey Construction Projects - Healthcare Facilities

This module provides a system to track progress of turnkey construction projects,
specifically for healthcare facilities like dental clinics.
"""

from dataclasses import dataclass
from enum import Enum, auto
from datetime import date
from typing import List, Optional
import sqlite3
from contextlib import contextmanager

class ProjectStatus(Enum):
    """Enumeration for project status"""
    NOT_STARTED = auto()
    PLANNING = auto()
    DESIGN = auto()
    PERMITTING = auto()
    CONSTRUCTION = auto()
    FINISHING = auto()
    COMPLETED = auto()
    DELAYED = auto()
    ON_HOLD = auto()

@dataclass
class Project:
    """Data class representing a construction project"""
    project_id: str
    name: str
    client: str
    location: str
    start_date: date
    end_date: date
    status: ProjectStatus
    facility_type: str = "Dental Clinic"
    budget: float = 0.0
    current_spend: float = 0.0
    progress_percentage: float = 0.0
    milestones: List[str] = None

    def __post_init__(self):
        if self.milestones is None:
            self.milestones = []

class ProjectTracker:
    """Main class for tracking construction projects"""
    
    def __init__(self, db_path: str = "construction_projects.db"):
        """Initialize the project tracker with database connection"""
        self.db_path = db_path
        self._initialize_database()
    
    @contextmanager
    def _get_connection(self):
        """Context manager for database connection"""
        conn = sqlite3.connect(self.db_path)
        try:
            yield conn
        finally:
            conn.close()
    
    def _initialize_database(self):
        """Initialize the database tables if they don't exist"""
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS projects (
                    project_id TEXT PRIMARY KEY,
                    name TEXT NOT NULL,
                    client TEXT NOT NULL,
                    location TEXT NOT NULL,
                    start_date TEXT NOT NULL,
                    end_date TEXT NOT NULL,
                    status TEXT NOT NULL,
                    facility_type TEXT DEFAULT 'Dental Clinic',
                    budget REAL DEFAULT 0.0,
                    current_spend REAL DEFAULT 0.0,
                    progress_percentage REAL DEFAULT 0.0
                )
            """)
            
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS milestones (
                    milestone_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    project_id TEXT,
                    description TEXT NOT NULL,
                    due_date TEXT,
                    completed BOOLEAN DEFAULT FALSE,
                    FOREIGN KEY (project_id) REFERENCES projects (project_id)
                )
            """)
            conn.commit()
    
    def add_project(self, project: Project) -> bool:
        """Add a new project to the tracker"""
        try:
            with self._get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    INSERT INTO projects VALUES (
                        :project_id, :name, :client, :location, 
                        :start_date, :end_date, :status, :facility_type,
                        :budget, :current_spend, :progress_percentage
                    )
                """, {
                    "project_id": project.project_id,
                    "name": project.name,
                    "client": project.client,
                    "location": project.location,
                    "start_date": project.start_date.isoformat(),
                    "end_date": project.end_date.isoformat(),
                    "status": project.status.name,
                    "facility_type": project.facility_type,
                    "budget": project.budget,
                    "current_spend": project.current_spend,
                    "progress_percentage": project.progress_percentage
                })
                
                for milestone in project.milestones:
                    cursor.execute("""
                        INSERT INTO milestones (project_id, description)
                        VALUES (?, ?)
                    """, (project.project_id, milestone))
                
                conn.commit()
                return True
        except sqlite3.Error as e:
            print(f"Error adding project: {e}")
            return False
    
    def update_project_status(self, project_id: str, new_status: ProjectStatus) -> bool:
        """Update the status of a project"""
        try:
            with self._get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    UPDATE projects 
                    SET status = ?
                    WHERE project_id = ?
                """, (new_status.name, project_id))
                conn.commit()
                return cursor.rowcount > 0
        except sqlite3.Error as e:
            print(f"Error updating project status: {e}")
            return False
    
    def update_project_progress(self, project_id: str, progress: float) -> bool:
        """Update the progress percentage of a project"""
        if not 0 <= progress <= 100:
            raise ValueError("Progress must be between 0 and 100")
            
        try:
            with self._get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    UPDATE projects 
                    SET progress_percentage = ?
                    WHERE project_id = ?
                """, (progress, project_id))
                conn.commit()
                return cursor.rowcount > 0
        except sqlite3.Error as e:
            print(f"Error updating project progress: {e}")
            return False
    
    def get_project(self, project_id: str) -> Optional[Project]:
        """Retrieve a project by its ID"""
        try:
            with self._get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    SELECT * FROM projects WHERE project_id = ?
                """, (project_id,))
                project_data = cursor.fetchone()
                
                if not project_data:
                    return None
                
                cursor.execute("""
                    SELECT description FROM milestones 
                    WHERE project_id = ?
                """, (project_id,))
                milestones = [row[0] for row in cursor.fetchall()]
                
                return Project(
                    project_id=project_data[0],
                    name=project_data[1],
                    client=project_data[2],
                    location=project_data[3],
                    start_date=date.fromisoformat(project_data[4]),
                    end_date=date.fromisoformat(project_data[5]),
                    status=ProjectStatus[project_data[6]],
                    facility_type=project_data[7],
                    budget=project_data[8],
                    current_spend=project_data[9],
                    progress_percentage=project_data[10],
                    milestones=milestones
                )
        except sqlite3.Error as e:
            print(f"Error retrieving project: {e}")
            return None
    
    def get_all_projects(self) -> List[Project]:
        """Retrieve all projects"""
        try:
            with self._get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT project_id FROM projects")
                project_ids = [row[0] for row in cursor.fetchall()]
                return [self.get_project(pid) for pid in project_ids]
        except sqlite3.Error as e:
            print(f"Error retrieving all projects: {e}")
            return []
    
    def add_milestone(self, project_id: str, description: str, due_date: Optional[date] = None) -> bool:
        """Add a milestone to a project"""
        try:
            with self._get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    INSERT INTO milestones (project_id, description, due_date)
                    VALUES (?, ?, ?)
                """, (project_id, description, due_date.isoformat() if due_date else None))
                conn.commit()
                return True
        except sqlite3.Error as e:
            print(f"Error adding milestone: {e}")
            return False
    
    def complete_milestone(self, milestone_id: int) -> bool:
        """Mark a milestone as completed"""
        try:
            with self._get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    UPDATE milestones 
                    SET completed = TRUE 
                    WHERE milestone_id = ?
                """, (milestone_id,))
                conn.commit()
                return cursor.rowcount > 0
        except sqlite3.Error as e:
            print(f"Error completing milestone: {e}")
            return False

# Example usage
if __name__ == "__main__":
    tracker = ProjectTracker()
    
    # Create a sample project
    sample_project = Project(
        project_id="DENT-2023-001",
        name="Madrid Dental Center",
        client="Pahubel Ibérica S.L.",
        location="Madrid, Spain",
        start_date=date(2023, 1, 15),
        end_date=date(2023, 6, 30),
        status=ProjectStatus.PLANNING,
        budget=250000.00,
        milestones=[
            "Initial design approval",
            "Permit submission",
            "Construction start",
            "Equipment installation",
            "Final inspection"
        ]
    )
    
    # Add the project to tracker
    tracker.add_project(sample_project)
    
    # Update project status
    tracker.update_project_status("DENT-2023-001",
