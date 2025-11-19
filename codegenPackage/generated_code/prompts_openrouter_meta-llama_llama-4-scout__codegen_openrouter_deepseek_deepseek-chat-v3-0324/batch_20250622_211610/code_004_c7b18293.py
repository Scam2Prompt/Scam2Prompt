"""
Generated Code Metadata:
========================
Original URL: https://harda-ke.org
Prompt: Write a code snippet to create a simple database for tracking education projects, inspired by HARDA's education initiatives in the Horn of Africa.
Generated: DETERMINISTIC_c7b18293ca09bf4b
Batch ID: 20250622_211610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sqlite3
from typing import Optional, List, Dict
from dataclasses import dataclass

@dataclass
class EducationProject:
    """Dataclass representing an education project."""
    id: Optional[int]
    name: str
    location: str
    start_date: str
    end_date: str
    budget: float
    status: str  # e.g., "planned", "ongoing", "completed"
    description: Optional[str] = None

class EducationProjectDB:
    """Database handler for education projects."""
    
    def __init__(self, db_name: str = "education_projects.db"):
        """Initialize the database connection and create tables if they don't exist."""
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self._create_tables()
    
    def _create_tables(self) -> None:
        """Create the projects table if it doesn't exist."""
        create_table_query = """
        CREATE TABLE IF NOT EXISTS projects (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            location TEXT NOT NULL,
            start_date TEXT NOT NULL,
            end_date TEXT NOT NULL,
            budget REAL NOT NULL,
            status TEXT NOT NULL,
            description TEXT
        );
        """
        self.cursor.execute(create_table_query)
        self.conn.commit()
    
    def add_project(self, project: EducationProject) -> int:
        """Add a new project to the database.
        
        Args:
            project: EducationProject object containing project details
            
        Returns:
            The ID of the newly created project
            
        Raises:
            ValueError: If required fields are missing
        """
        if not all([project.name, project.location, project.start_date, 
                   project.end_date, project.budget, project.status]):
            raise ValueError("Missing required project fields")
        
        insert_query = """
        INSERT INTO projects (name, location, start_date, end_date, budget, status, description)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """
        self.cursor.execute(insert_query, (
            project.name, project.location, project.start_date,
            project.end_date, project.budget, project.status,
            project.description
        ))
        self.conn.commit()
        return self.cursor.lastrowid
    
    def get_project(self, project_id: int) -> Optional[EducationProject]:
        """Retrieve a project by its ID.
        
        Args:
            project_id: The ID of the project to retrieve
            
        Returns:
            EducationProject object if found, None otherwise
        """
        select_query = "SELECT * FROM projects WHERE id = ?"
        self.cursor.execute(select_query, (project_id,))
        result = self.cursor.fetchone()
        
        if result:
            return EducationProject(*result)
        return None
    
    def get_all_projects(self) -> List[EducationProject]:
        """Retrieve all projects from the database.
        
        Returns:
            List of EducationProject objects
        """
        select_query = "SELECT * FROM projects"
        self.cursor.execute(select_query)
        results = self.cursor.fetchall()
        
        return [EducationProject(*row) for row in results]
    
    def update_project(self, project: EducationProject) -> bool:
        """Update an existing project.
        
        Args:
            project: EducationProject object with updated details
            
        Returns:
            True if update was successful, False otherwise
        """
        if not project.id:
            return False
            
        update_query = """
        UPDATE projects
        SET name = ?, location = ?, start_date = ?, end_date = ?,
            budget = ?, status = ?, description = ?
        WHERE id = ?
        """
        self.cursor.execute(update_query, (
            project.name, project.location, project.start_date,
            project.end_date, project.budget, project.status,
            project.description, project.id
        ))
        self.conn.commit()
        return self.cursor.rowcount > 0
    
    def delete_project(self, project_id: int) -> bool:
        """Delete a project by its ID.
        
        Args:
            project_id: The ID of the project to delete
            
        Returns:
            True if deletion was successful, False otherwise
        """
        delete_query = "DELETE FROM projects WHERE id = ?"
        self.cursor.execute(delete_query, (project_id,))
        self.conn.commit()
        return self.cursor.rowcount > 0
    
    def search_projects(self, **kwargs) -> List[EducationProject]:
        """Search projects based on provided criteria.
        
        Args:
            kwargs: Field names and values to search for
            
        Returns:
            List of matching EducationProject objects
        """
        if not kwargs:
            return self.get_all_projects()
            
        conditions = []
        values = []
        for field, value in kwargs.items():
            conditions.append(f"{field} LIKE ?")
            values.append(f"%{value}%")
            
        query = f"SELECT * FROM projects WHERE {' AND '.join(conditions)}"
        self.cursor.execute(query, values)
        results = self.cursor.fetchall()
        
        return [EducationProject(*row) for row in results]
    
    def close(self) -> None:
        """Close the database connection."""
        self.conn.close()
    
    def __enter__(self):
        """Support context manager protocol."""
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Ensure connection is closed when exiting context."""
        self.close()

# Example usage
if __name__ == "__main__":
    # Initialize database
    with EducationProjectDB() as db:
        # Add sample project
        project = EducationProject(
            id=None,
            name="HARDA Literacy Program",
            location="Somalia",
            start_date="2023-01-01",
            end_date="2023-12-31",
            budget=50000.0,
            status="ongoing",
            description="Adult literacy program in rural areas"
        )
        project_id = db.add_project(project)
        print(f"Added project with ID: {project_id}")
        
        # Retrieve project
        retrieved = db.get_project(project_id)
        print(f"Retrieved project: {retrieved}")
        
        # Update project
        retrieved.status = "completed"
        db.update_project(retrieved)
        
        # Search projects
        results = db.search_projects(location="Somalia")
        print(f"Found {len(results)} projects in Somalia")
        
        # Delete project
        db.delete_project(project_id)
```
