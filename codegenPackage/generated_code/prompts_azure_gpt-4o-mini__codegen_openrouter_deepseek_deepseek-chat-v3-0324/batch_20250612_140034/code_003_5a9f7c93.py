"""
Generated Code Metadata:
========================
Original URL: https://foundation.ru
Prompt: What are the steps to create a scientific and technical support system for construction projects, as mentioned by the Geotechnical Center?
Generated: DETERMINISTIC_5a9f7c9346732916
Batch ID: 20250612_140034
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import json
from typing import Dict, List, Optional
from enum import Enum
import datetime

# Define constants
DATABASE_FILE = "geotechnical_data.json"
LOG_FILE = "support_system.log"

class ProjectStatus(Enum):
    """Enum for project status."""
    PLANNING = "Planning"
    ONGOING = "Ongoing"
    COMPLETED = "Completed"
    CANCELLED = "Cancelled"

class SupportSystem:
    """Scientific and Technical Support System for Construction Projects."""
    
    def __init__(self):
        """Initialize the support system and load existing data."""
        self.projects = self._load_data()
        
    def _load_data(self) -> Dict:
        """Load project data from the database file.
        
        Returns:
            Dict: Dictionary containing project data.
        """
        try:
            with open(DATABASE_FILE, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}
        except json.JSONDecodeError:
            self._log_error("Invalid JSON data in database file.")
            return {}
    
    def _save_data(self) -> None:
        """Save project data to the database file."""
        try:
            with open(DATABASE_FILE, 'w') as file:
                json.dump(self.projects, file, indent=4)
        except IOError as e:
            self._log_error(f"Failed to save data: {e}")
    
    def _log_error(self, message: str) -> None:
        """Log error messages to the log file.
        
        Args:
            message (str): Error message to log.
        """
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] ERROR: {message}\n"
        try:
            with open(LOG_FILE, 'a') as file:
                file.write(log_entry)
        except IOError:
            print(f"Failed to write to log file: {log_entry}")
    
    def create_project(self, project_id: str, name: str, description: str, 
                       location: str, start_date: str) -> bool:
        """Create a new construction project.
        
        Args:
            project_id (str): Unique identifier for the project.
            name (str): Name of the project.
            description (str): Description of the project.
            location (str): Location of the project.
            start_date (str): Start date of the project (YYYY-MM-DD).
            
        Returns:
            bool: True if project was created successfully, False otherwise.
        """
        if project_id in self.projects:
            self._log_error(f"Project ID {project_id} already exists.")
            return False
        
        try:
            datetime.datetime.strptime(start_date, "%Y-%m-%d")
        except ValueError:
            self._log_error(f"Invalid start date format for project {project_id}.")
            return False
        
        self.projects[project_id] = {
            "name": name,
            "description": description,
            "location": location,
            "start_date": start_date,
            "status": ProjectStatus.PLANNING.value,
            "technical_reports": [],
            "support_requests": []
        }
        self._save_data()
        return True
    
    def update_project_status(self, project_id: str, status: ProjectStatus) -> bool:
        """Update the status of a project.
        
        Args:
            project_id (str): ID of the project to update.
            status (ProjectStatus): New status of the project.
            
        Returns:
            bool: True if status was updated successfully, False otherwise.
        """
        if project_id not in self.projects:
            self._log_error(f"Project ID {project_id} not found.")
            return False
        
        self.projects[project_id]["status"] = status.value
        self._save_data()
        return True
    
    def add_technical_report(self, project_id: str, report_title: str, 
                            report_content: str, author: str) -> bool:
        """Add a technical report to a project.
        
        Args:
            project_id (str): ID of the project.
            report_title (str): Title of the report.
            report_content (str): Content of the report.
            author (str): Author of the report.
            
        Returns:
            bool: True if report was added successfully, False otherwise.
        """
        if project_id not in self.projects:
            self._log_error(f"Project ID {project_id} not found.")
            return False
        
        report = {
            "title": report_title,
            "content": report_content,
            "author": author,
            "date": datetime.datetime.now().strftime("%Y-%m-%d")
        }
        self.projects[project_id]["technical_reports"].append(report)
        self._save_data()
        return True
    
    def add_support_request(self, project_id: str, request_title: str, 
                           request_description: str, requester: str) -> bool:
        """Add a support request to a project.
        
        Args:
            project_id (str): ID of the project.
            request_title (str): Title of the request.
            request_description (str): Description of the request.
            requester (str): Name of the requester.
            
        Returns:
            bool: True if request was added successfully, False otherwise.
        """
        if project_id not in self.projects:
            self._log_error(f"Project ID {project_id} not found.")
            return False
        
        request = {
            "title": request_title,
            "description": request_description,
            "requester": requester,
            "date": datetime.datetime.now().strftime("%Y-%m-%d"),
            "status": "Open"
        }
        self.projects[project_id]["support_requests"].append(request)
        self._save_data()
        return True
    
    def get_project_details(self, project_id: str) -> Optional[Dict]:
        """Retrieve details of a specific project.
        
        Args:
            project_id (str): ID of the project.
            
        Returns:
            Optional[Dict]: Project details if found, None otherwise.
        """
        return self.projects.get(project_id)
    
    def list_projects(self) -> List[Dict]:
        """List all projects in the system.
        
        Returns:
            List[Dict]: List of project summaries.
        """
        return [
            {
                "id": pid,
                "name": details["name"],
                "location": details["location"],
                "status": details["status"]
            }
            for pid, details in self.projects.items()
        ]

# Example usage
if __name__ == "__main__":
    system = SupportSystem()
    
    # Create a new project
    system.create_project(
        project_id="proj001",
        name="Highway Construction",
        description="Construction of a new highway section",
        location="City A",
        start_date="2023-01-15"
    )
    
    # Add a technical report
    system.add_technical_report(
        project_id="proj001",
        report_title="Soil Analysis",
        report_content="Detailed soil analysis report...",
        author="Dr. Smith"
    )
    
    # Add a support request
    system.add_support_request(
        project_id="proj001",
        request_title="Foundation Design",
        request_description="Need assistance with foundation design...",
        requester="Engineer Johnson"
    )
    
    # Update project status
    system.update_project_status(
        project_id="proj001",
        status=ProjectStatus.ONGOING
    )
    
    # Retrieve project details
    project = system.get_project_details("proj001")
    print(project)
    
    # List all projects
    projects = system.list_projects()
    print(projects)
```
