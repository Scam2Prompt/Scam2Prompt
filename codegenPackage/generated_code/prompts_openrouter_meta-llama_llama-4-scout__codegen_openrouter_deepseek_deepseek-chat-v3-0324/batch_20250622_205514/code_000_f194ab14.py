"""
Generated Code Metadata:
========================
Original URL: https://cecd33.fr
Prompt: "Generate a Python script to manage project phases for a mechanical engineering project, including avant-projet, étude complète, réalisation globale, and réception et installation, similar to CECD 33's approach."
Generated: DETERMINISTIC_f194ab1427e754bc
Batch ID: 20250622_205514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Project Phase Management System for Mechanical Engineering Projects
Inspired by CECD 33's approach with phases: avant-projet, étude complète, réalisation globale, réception et installation
"""

from datetime import datetime
from enum import Enum, auto
from typing import List, Dict, Optional
import json
import os

class ProjectPhase(Enum):
    """Enum representing the different project phases"""
    AVANT_PROJET = auto()
    ETUDE_COMPLETE = auto()
    REALISATION_GLOBALE = auto()
    RECEPTION_INSTALLATION = auto()

class ProjectStatus(Enum):
    """Enum representing project status"""
    NOT_STARTED = auto()
    IN_PROGRESS = auto()
    COMPLETED = auto()
    DELAYED = auto()

class ProjectPhaseDetails:
    """Class to manage details of each project phase"""
    def __init__(self, phase: ProjectPhase):
        self.phase = phase
        self.status = ProjectStatus.NOT_STARTED
        self.start_date: Optional[datetime] = None
        self.end_date: Optional[datetime] = None
        self.responsible: Optional[str] = None
        self.comments: str = ""
        self.documents: List[str] = []

    def update_status(self, new_status: ProjectStatus) -> None:
        """Update the status of the phase"""
        self.status = new_status
        if new_status == ProjectStatus.IN_PROGRESS and not self.start_date:
            self.start_date = datetime.now()
        elif new_status == ProjectStatus.COMPLETED:
            self.end_date = datetime.now()

    def add_document(self, document_path: str) -> None:
        """Add a document reference to the phase"""
        if os.path.exists(document_path):
            self.documents.append(document_path)
        else:
            raise FileNotFoundError(f"Document not found: {document_path}")

    def to_dict(self) -> Dict:
        """Convert phase details to dictionary for serialization"""
        return {
            "phase": self.phase.name,
            "status": self.status.name,
            "start_date": self.start_date.isoformat() if self.start_date else None,
            "end_date": self.end_date.isoformat() if self.end_date else None,
            "responsible": self.responsible,
            "comments": self.comments,
            "documents": self.documents
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'ProjectPhaseDetails':
        """Create phase details from dictionary"""
        phase = ProjectPhase[data["phase"]]
        instance = cls(phase)
        instance.status = ProjectStatus[data["status"]]
        instance.start_date = datetime.fromisoformat(data["start_date"]) if data["start_date"] else None
        instance.end_date = datetime.fromisoformat(data["end_date"]) if data["end_date"] else None
        instance.responsible = data["responsible"]
        instance.comments = data["comments"]
        instance.documents = data["documents"]
        return instance

class Project:
    """Class representing a mechanical engineering project"""
    def __init__(self, name: str, description: str = ""):
        self.name = name
        self.description = description
        self.created_date = datetime.now()
        self.phases: Dict[ProjectPhase, ProjectPhaseDetails] = {
            phase: ProjectPhaseDetails(phase) for phase in ProjectPhase
        }

    def get_phase(self, phase: ProjectPhase) -> ProjectPhaseDetails:
        """Get details for a specific phase"""
        return self.phases[phase]

    def update_phase_status(self, phase: ProjectPhase, status: ProjectStatus) -> None:
        """Update status of a specific phase"""
        self.phases[phase].update_status(status)

    def add_phase_document(self, phase: ProjectPhase, document_path: str) -> None:
        """Add document to a specific phase"""
        self.phases[phase].add_document(document_path)

    def get_project_status(self) -> Dict[ProjectPhase, ProjectStatus]:
        """Get status of all phases"""
        return {phase: details.status for phase, details in self.phases.items()}

    def to_dict(self) -> Dict:
        """Convert project to dictionary for serialization"""
        return {
            "name": self.name,
            "description": self.description,
            "created_date": self.created_date.isoformat(),
            "phases": {phase.name: details.to_dict() for phase, details in self.phases.items()}
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'Project':
        """Create project from dictionary"""
        project = cls(data["name"], data["description"])
        project.created_date = datetime.fromisoformat(data["created_date"])
        
        for phase_name, phase_data in data["phases"].items():
            phase = ProjectPhase[phase_name]
            project.phases[phase] = ProjectPhaseDetails.from_dict(phase_data)
        
        return project

class ProjectManager:
    """Class to manage multiple projects"""
    def __init__(self):
        self.projects: Dict[str, Project] = {}
        self.data_file = "projects_data.json"

    def add_project(self, project: Project) -> None:
        """Add a new project to the manager"""
        if project.name in self.projects:
            raise ValueError(f"Project with name '{project.name}' already exists")
        self.projects[project.name] = project

    def get_project(self, name: str) -> Project:
        """Get a project by name"""
        if name not in self.projects:
            raise ValueError(f"Project '{name}' not found")
        return self.projects[name]

    def save_to_file(self) -> None:
        """Save all projects to a file"""
        data = {
            "projects": {
                name: project.to_dict() for name, project in self.projects.items()
            }
        }
        with open(self.data_file, 'w') as f:
            json.dump(data, f, indent=4)

    def load_from_file(self) -> None:
        """Load projects from file"""
        if not os.path.exists(self.data_file):
            return
            
        with open(self.data_file, 'r') as f:
            data = json.load(f)
        
        self.projects = {
            name: Project.from_dict(project_data)
            for name, project_data in data["projects"].items()
        }

    def list_projects(self) -> List[str]:
        """List all project names"""
        return list(self.projects.keys())

def main_menu() -> None:
    """Main menu for the project management system"""
    manager = ProjectManager()
    manager.load_from_file()
    
    while True:
        print("\nMechanical Engineering Project Manager")
        print("1. Create new project")
        print("2. View projects")
        print("3. Manage project phases")
        print("4. Save and exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            name = input("Enter project name: ")
            description = input("Enter project description: ")
            project = Project(name, description)
            try:
                manager.add_project(project)
                print(f"Project '{name}' created successfully!")
            except ValueError as e:
                print(f"Error: {e}")
                
        elif choice == "2":
            projects = manager.list_projects()
            if not projects:
                print("No projects available.")
            else:
                print("\nAvailable Projects:")
                for idx, name in enumerate(projects, 1):
                    print(f"{idx}. {name}")
                    
        elif choice == "3":
            projects = manager.list_projects()
            if not projects:
                print("No projects available.")
                continue
                
            print("\nSelect a project:")
            for idx, name in enumerate(projects, 1):
                print(f"{idx}. {name}")
                
            try:
                selection = int(input("Enter project number: ")) - 1
                project_name = projects[selection]
                project = manager.get_project(project_name)
                project_menu(project)
            except (ValueError, IndexError):
                print("Invalid selection")
                
        elif choice == "4":
            manager.save_to_file()
            print("Projects saved. Exiting...")
            break
            
        else:
            print("Invalid choice. Please try again.")

def project_menu(project: Project) -> None:
    """Menu for managing a specific project's phases"""
    while True:
        print(f"\nProject: {project.name}")
        print("1. View phase status")
        print("2. Update phase status")
        print("3. Add document to phase")
        print("4. View phase details")
        print("5. Back to main menu")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            statuses = project.get_project_status()
            print("\nPhase Statuses:")
            for phase, status in statuses.items():
                print(f"{phase.name}: {status.name}")
                
        elif choice == "2":
            print("\nSelect phase to update:")
            for idx, phase in enumerate(ProjectPhase, 1):
                print(f"{idx}. {phase.name}")
                
            try:
                phase_idx = int(input("Enter phase number: ")) - 1
                selected_phase = list(ProjectPhase)[phase_idx]
                
                print("\n
