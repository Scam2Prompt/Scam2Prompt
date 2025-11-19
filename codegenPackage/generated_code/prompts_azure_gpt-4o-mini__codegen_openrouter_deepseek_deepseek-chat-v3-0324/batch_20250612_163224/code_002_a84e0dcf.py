"""
Generated Code Metadata:
========================
Original URL: https://itmastar.pages.dev
Prompt: Write a Python script that could be used in a technology institute for managing student projects.
Generated: DETERMINISTIC_a84e0dcf46be65ef
Batch ID: 20250612_163224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import os
from datetime import datetime
from typing import Dict, List, Optional, Union

class ProjectManager:
    """
    A class to manage student projects for a technology institute.
    Handles project creation, assignment, updates, and reporting.
    """

    def __init__(self, data_file: str = "projects.json"):
        """
        Initialize the ProjectManager with a data file.
        
        Args:
            data_file: Path to JSON file storing project data.
        """
        self.data_file = data_file
        self.projects = self._load_data()

    def _load_data(self) -> Dict[str, Dict]:
        """
        Load project data from JSON file.
        
        Returns:
            Dictionary containing project data.
            
        Raises:
            FileNotFoundError: If data file doesn't exist.
            json.JSONDecodeError: If data file is corrupted.
        """
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r') as f:
                    return json.load(f)
            return {}
        except json.JSONDecodeError as e:
            raise json.JSONDecodeError(f"Error decoding {self.data_file}: {e}", e.doc, e.pos)
        except Exception as e:
            raise Exception(f"Error loading data: {e}")

    def _save_data(self) -> None:
        """
        Save project data to JSON file.
        
        Raises:
            IOError: If file cannot be written.
        """
        try:
            with open(self.data_file, 'w') as f:
                json.dump(self.projects, f, indent=2)
        except Exception as e:
            raise IOError(f"Error saving data: {e}")

    def create_project(
        self,
        project_id: str,
        title: str,
        description: str,
        supervisor: str,
        max_students: int = 3
    ) -> Dict[str, Union[str, int, List[str]]]:
        """
        Create a new project.
        
        Args:
            project_id: Unique identifier for the project.
            title: Project title.
            description: Project description.
            supervisor: Name of project supervisor.
            max_students: Maximum number of students allowed (default: 3).
            
        Returns:
            Dictionary containing the created project details.
            
        Raises:
            ValueError: If project ID already exists.
        """
        if project_id in self.projects:
            raise ValueError(f"Project ID {project_id} already exists.")
            
        project = {
            "title": title,
            "description": description,
            "supervisor": supervisor,
            "max_students": max_students,
            "students": [],
            "status": "active",
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat()
        }
        
        self.projects[project_id] = project
        self._save_data()
        return project

    def assign_student(self, project_id: str, student_id: str) -> Dict[str, Union[str, int, List[str]]]:
        """
        Assign a student to a project.
        
        Args:
            project_id: ID of the project.
            student_id: ID of the student to assign.
            
        Returns:
            Updated project details.
            
        Raises:
            ValueError: If project doesn't exist, is full, or student is already assigned.
        """
        if project_id not in self.projects:
            raise ValueError(f"Project {project_id} does not exist.")
            
        project = self.projects[project_id]
        
        if student_id in project["students"]:
            raise ValueError(f"Student {student_id} is already assigned to this project.")
            
        if len(project["students"]) >= project["max_students"]:
            raise ValueError(f"Project {project_id} has reached maximum capacity.")
            
        project["students"].append(student_id)
        project["updated_at"] = datetime.now().isoformat()
        self._save_data()
        return project

    def remove_student(self, project_id: str, student_id: str) -> Dict[str, Union[str, int, List[str]]]:
        """
        Remove a student from a project.
        
        Args:
            project_id: ID of the project.
            student_id: ID of the student to remove.
            
        Returns:
            Updated project details.
            
        Raises:
            ValueError: If project doesn't exist or student isn't assigned.
        """
        if project_id not in self.projects:
            raise ValueError(f"Project {project_id} does not exist.")
            
        project = self.projects[project_id]
        
        if student_id not in project["students"]:
            raise ValueError(f"Student {student_id} is not assigned to this project.")
            
        project["students"].remove(student_id)
        project["updated_at"] = datetime.now().isoformat()
        self._save_data()
        return project

    def update_project_status(self, project_id: str, status: str) -> Dict[str, Union[str, int, List[str]]]:
        """
        Update project status.
        
        Args:
            project_id: ID of the project.
            status: New status (e.g., 'active', 'completed', 'archived').
            
        Returns:
            Updated project details.
            
        Raises:
            ValueError: If project doesn't exist or status is invalid.
        """
        valid_statuses = {"active", "completed", "archived"}
        if status.lower() not in valid_statuses:
            raise ValueError(f"Invalid status. Must be one of: {valid_statuses}")
            
        if project_id not in self.projects:
            raise ValueError(f"Project {project_id} does not exist.")
            
        project = self.projects[project_id]
        project["status"] = status.lower()
        project["updated_at"] = datetime.now().isoformat()
        self._save_data()
        return project

    def get_project(self, project_id: str) -> Optional[Dict[str, Union[str, int, List[str]]]]:
        """
        Get project details by ID.
        
        Args:
            project_id: ID of the project.
            
        Returns:
            Project details if found, None otherwise.
        """
        return self.projects.get(project_id)

    def list_projects(self, status: Optional[str] = None) -> List[Dict[str, Union[str, int, List[str]]]]:
        """
        List all projects, optionally filtered by status.
        
        Args:
            status: Filter projects by this status.
            
        Returns:
            List of project details.
        """
        if status:
            return [p for p in self.projects.values() if p["status"] == status.lower()]
        return list(self.projects.values())

    def search_projects(self, query: str) -> List[Dict[str, Union[str, int, List[str]]]]:
        """
        Search projects by title or description.
        
        Args:
            query: Search string.
            
        Returns:
            List of matching projects.
        """
        query = query.lower()
        return [
            p for p in self.projects.values()
            if query in p["title"].lower() or query in p["description"].lower()
        ]


# Example usage
if __name__ == "__main__":
    try:
        manager = ProjectManager()
        
        # Create a project
        project = manager.create_project(
            project_id="p001",
            title="AI Research",
            description="Research on neural networks",
            supervisor="Dr. Smith"
        )
        print(f"Created project: {project['title']}")
        
        # Assign students
        manager.assign_student("p001", "s123")
        manager.assign_student("p001", "s456")
        print(f"Assigned students to project: {manager.get_project('p001')['students']}")
        
        # List active projects
        print("Active projects:")
        for p in manager.list_projects(status="active"):
            print(f"- {p['title']} (ID: {p['title']})")
            
    except Exception as e:
        print(f"Error: {e}")
```
