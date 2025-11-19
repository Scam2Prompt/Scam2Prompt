"""
Generated Code Metadata:
========================
Original URL: https://mgel.com.br
Prompt: Generate a code template for creating a construction project management system with features similar to those described on the MGEL website.
Generated: DETERMINISTIC_40f1963d98465b1b
Batch ID: 20250622_205348
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Construction Project Management System
Inspired by MGEL's project management features
"""

from datetime import datetime
from typing import List, Dict, Optional
import sqlite3
from enum import Enum, auto

# Database configuration
DB_NAME = "construction_management.db"

class ProjectStatus(Enum):
    PLANNING = auto()
    IN_PROGRESS = auto()
    ON_HOLD = auto()
    COMPLETED = auto()
    CANCELLED = auto()

class TaskPriority(Enum):
    LOW = auto()
    MEDIUM = auto()
    HIGH = auto()
    CRITICAL = auto()

class DocumentType(Enum):
    BLUEPRINT = auto()
    PERMIT = auto()
    CONTRACT = auto()
    REPORT = auto()
    PHOTO = auto()

class DatabaseManager:
    """Handles all database operations"""
    
    def __init__(self):
        self.connection = sqlite3.connect(DB_NAME)
        self._initialize_database()
    
    def _initialize_database(self):
        """Create tables if they don't exist"""
        cursor = self.connection.cursor()
        
        # Projects table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS projects (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT,
            location TEXT,
            start_date TEXT,
            end_date TEXT,
            budget REAL,
            status TEXT,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
        """)
        
        # Tasks table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            project_id INTEGER,
            name TEXT NOT NULL,
            description TEXT,
            assigned_to TEXT,
            start_date TEXT,
            end_date TEXT,
            priority TEXT,
            status TEXT,
            FOREIGN KEY (project_id) REFERENCES projects (id)
        )
        """)
        
        # Documents table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS documents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            project_id INTEGER,
            name TEXT NOT NULL,
            type TEXT,
            file_path TEXT NOT NULL,
            upload_date TEXT DEFAULT CURRENT_TIMESTAMP,
            uploaded_by TEXT,
            FOREIGN KEY (project_id) REFERENCES projects (id)
        )
        """)
        
        # Team members table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS team_members (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            role TEXT,
            email TEXT,
            phone TEXT,
            specialization TEXT
        )
        """)
        
        # Project team mapping
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS project_team (
            project_id INTEGER,
            member_id INTEGER,
            role TEXT,
            PRIMARY KEY (project_id, member_id),
            FOREIGN KEY (project_id) REFERENCES projects (id),
            FOREIGN KEY (member_id) REFERENCES team_members (id)
        )
        """)
        
        self.connection.commit()
    
    def execute_query(self, query: str, params: tuple = ()) -> sqlite3.Cursor:
        """Execute a SQL query with parameters"""
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, params)
            self.connection.commit()
            return cursor
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            raise
    
    def close(self):
        """Close the database connection"""
        self.connection.close()

class Project:
    """Represents a construction project"""
    
    def __init__(self, db_manager: DatabaseManager):
        self.db = db_manager
        self.id = None
        self.name = ""
        self.description = ""
        self.location = ""
        self.start_date = None
        self.end_date = None
        self.budget = 0.0
        self.status = ProjectStatus.PLANNING.name
        self.created_at = datetime.now().isoformat()
    
    def save(self):
        """Save project to database"""
        query = """
        INSERT INTO projects (name, description, location, start_date, end_date, budget, status, created_at)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """
        params = (
            self.name,
            self.description,
            self.location,
            self.start_date,
            self.end_date,
            self.budget,
            self.status,
            self.created_at
        )
        cursor = self.db.execute_query(query, params)
        self.id = cursor.lastrowid
    
    def update(self):
        """Update project in database"""
        if not self.id:
            raise ValueError("Project ID is required for update")
        
        query = """
        UPDATE projects SET
            name = ?,
            description = ?,
            location = ?,
            start_date = ?,
            end_date = ?,
            budget = ?,
            status = ?
        WHERE id = ?
        """
        params = (
            self.name,
            self.description,
            self.location,
            self.start_date,
            self.end_date,
            self.budget,
            self.status,
            self.id
        )
        self.db.execute_query(query, params)
    
    def add_task(self, task_data: Dict):
        """Add a task to the project"""
        task = Task(self.db)
        task.project_id = self.id
        task.name = task_data.get("name", "")
        task.description = task_data.get("description", "")
        task.assigned_to = task_data.get("assigned_to", "")
        task.start_date = task_data.get("start_date", "")
        task.end_date = task_data.get("end_date", "")
        task.priority = task_data.get("priority", TaskPriority.MEDIUM.name)
        task.status = task_data.get("status", "Not Started")
        task.save()
    
    def get_tasks(self) -> List[Dict]:
        """Get all tasks for this project"""
        query = "SELECT * FROM tasks WHERE project_id = ?"
        cursor = self.db.execute_query(query, (self.id,))
        return [dict(row) for row in cursor.fetchall()]
    
    def add_document(self, document_data: Dict):
        """Add a document to the project"""
        document = Document(self.db)
        document.project_id = self.id
        document.name = document_data.get("name", "")
        document.type = document_data.get("type", DocumentType.REPORT.name)
        document.file_path = document_data.get("file_path", "")
        document.uploaded_by = document_data.get("uploaded_by", "")
        document.save()
    
    def get_documents(self) -> List[Dict]:
        """Get all documents for this project"""
        query = "SELECT * FROM documents WHERE project_id = ?"
        cursor = self.db.execute_query(query, (self.id,))
        return [dict(row) for row in cursor.fetchall()]
    
    def add_team_member(self, member_id: int, role: str):
        """Add a team member to the project"""
        query = "INSERT INTO project_team (project_id, member_id, role) VALUES (?, ?, ?)"
        self.db.execute_query(query, (self.id, member_id, role))
    
    def get_team(self) -> List[Dict]:
        """Get all team members for this project"""
        query = """
        SELECT tm.id, tm.name, tm.role, tm.email, tm.phone, pt.role as project_role
        FROM team_members tm
        JOIN project_team pt ON tm.id = pt.member_id
        WHERE pt.project_id = ?
        """
        cursor = self.db.execute_query(query, (self.id,))
        return [dict(row) for row in cursor.fetchall()]

class Task:
    """Represents a project task"""
    
    def __init__(self, db_manager: DatabaseManager):
        self.db = db_manager
        self.id = None
        self.project_id = None
        self.name = ""
        self.description = ""
        self.assigned_to = ""
        self.start_date = None
        self.end_date = None
        self.priority = TaskPriority.MEDIUM.name
        self.status = "Not Started"
    
    def save(self):
        """Save task to database"""
        query = """
        INSERT INTO tasks (
            project_id, name, description, assigned_to, 
            start_date, end_date, priority, status
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """
        params = (
            self.project_id,
            self.name,
            self.description,
            self.assigned_to,
            self.start_date,
            self.end_date,
            self.priority,
            self.status
        )
        cursor = self.db.execute_query(query, params)
        self.id = cursor.lastrowid
    
    def update(self):
        """Update task in database"""
        if not self.id:
            raise ValueError("Task ID is required for update")
        
        query = """
        UPDATE tasks SET
            name = ?,
            description = ?,
            assigned_to = ?,
            start_date = ?,
            end_date = ?,
            priority = ?,
            status = ?
        WHERE id = ?
        """
        params = (
            self.name,
            self.description,
            self.assigned_to,
            self.start_date,
            self.end_date,
            self.priority,
            self.status,
            self.id
        )
        self.db.execute_query(query, params)

class Document:
    """Represents a project document"""
    
    def __init__(self, db_manager: DatabaseManager):
        self.db
