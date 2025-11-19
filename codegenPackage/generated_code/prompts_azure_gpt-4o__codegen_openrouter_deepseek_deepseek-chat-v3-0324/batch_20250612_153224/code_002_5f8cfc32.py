"""
Generated Code Metadata:
========================
Original URL: https://thedesignumbrella.in
Prompt: Develop a project management script in Python to track progress through the phases of discovery, design, development, and delivery as described by The Design Umbrella.
Generated: DETERMINISTIC_5f8cfc328b1eab33
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime
from enum import Enum, auto
from typing import Dict, List, Optional


class ProjectPhase(Enum):
    """Enum representing the different phases of a project."""
    DISCOVERY = auto()
    DESIGN = auto()
    DEVELOPMENT = auto()
    DELIVERY = auto()


class ProjectStatus(Enum):
    """Enum representing the status of a project phase."""
    NOT_STARTED = auto()
    IN_PROGRESS = auto()
    COMPLETED = auto()
    BLOCKED = auto()


class Project:
    """Class representing a project with its phases and progress."""
    
    def __init__(self, name: str, description: str = ""):
        """Initialize a new project.
        
        Args:
            name: Name of the project.
            description: Optional description of the project.
        """
        self.name = name
        self.description = description
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.phases: Dict[ProjectPhase, ProjectStatus] = {
            phase: ProjectStatus.NOT_STARTED for phase in ProjectPhase
        }
        self.notes: Dict[ProjectPhase, List[str]] = {
            phase: [] for phase in ProjectPhase
        }
    
    def update_phase_status(self, phase: ProjectPhase, status: ProjectStatus) -> None:
        """Update the status of a project phase.
        
        Args:
            phase: The phase to update.
            status: The new status of the phase.
        """
        if phase not in ProjectPhase:
            raise ValueError(f"Invalid phase: {phase}")
        if status not in ProjectStatus:
            raise ValueError(f"Invalid status: {status}")
        
        self.phases[phase] = status
        self.updated_at = datetime.now()
    
    def add_note(self, phase: ProjectPhase, note: str) -> None:
        """Add a note to a project phase.
        
        Args:
            phase: The phase to add the note to.
            note: The note content.
        """
        if phase not in ProjectPhase:
            raise ValueError(f"Invalid phase: {phase}")
        
        self.notes[phase].append(note)
        self.updated_at = datetime.now()
    
    def get_phase_progress(self) -> Dict[str, str]:
        """Get the current progress of all phases.
        
        Returns:
            A dictionary mapping phase names to their statuses.
        """
        return {
            phase.name: status.name for phase, status in self.phases.items()
        }
    
    def to_dict(self) -> Dict:
        """Convert the project to a dictionary for serialization.
        
        Returns:
            A dictionary representation of the project.
        """
        return {
            "name": self.name,
            "description": self.description,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
            "phases": {phase.name: status.name for phase, status in self.phases.items()},
            "notes": {phase.name: notes for phase, notes in self.notes.items()}
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'Project':
        """Create a Project instance from a dictionary.
        
        Args:
            data: Dictionary containing project data.
            
        Returns:
            A Project instance.
        """
        project = cls(data["name"], data.get("description", ""))
        project.created_at = datetime.fromisoformat(data["created_at"])
        project.updated_at = datetime.fromisoformat(data["updated_at"])
        
        for phase_name, status_name in data["phases"].items():
            phase = ProjectPhase[phase_name]
            status = ProjectStatus[status_name]
            project.phases[phase] = status
        
        for phase_name, notes in data["notes"].items():
            phase = ProjectPhase[phase_name]
            project.notes[phase] = notes
        
        return project


class ProjectManager:
    """Class to manage multiple projects."""
    
    def __init__(self, storage_file: str = "projects.json"):
        """Initialize the project manager.
        
        Args:
            storage_file: Path to the file where projects are stored.
        """
        self.storage_file = storage_file
        self.projects: Dict[str, Project] = {}
        self.load_projects()
    
    def add_project(self, project: Project) -> None:
        """Add a project to the manager.
        
        Args:
            project: The project to add.
        """
        if project.name in self.projects:
            raise ValueError(f"Project '{project.name}' already exists")
        self.projects[project.name] = project
        self.save_projects()
    
    def get_project(self, name: str) -> Optional[Project]:
        """Get a project by name.
        
        Args:
            name: Name of the project to retrieve.
            
        Returns:
            The project if found, None otherwise.
        """
        return self.projects.get(name)
    
    def update_project(self, project: Project) -> None:
        """Update an existing project.
        
        Args:
            project: The updated project.
        """
        if project.name not in self.projects:
            raise ValueError(f"Project '{project.name}' does not exist")
        self.projects[project.name] = project
        self.save_projects()
    
    def delete_project(self, name: str) -> None:
        """Delete a project.
        
        Args:
            name: Name of the project to delete.
        """
        if name not in self.projects:
            raise ValueError(f"Project '{name}' does not exist")
        del self.projects[name]
        self.save_projects()
    
    def save_projects(self) -> None:
        """Save all projects to the storage file."""
        data = {
            "projects": [project.to_dict() for project in self.projects.values()]
        }
        with open(self.storage_file, "w") as f:
            json.dump(data, f, indent=2)
    
    def load_projects(self) -> None:
        """Load projects from the storage file."""
        try:
            with open(self.storage_file, "r") as f:
                data = json.load(f)
                for project_data in data["projects"]:
                    project = Project.from_dict(project_data)
                    self.projects[project.name] = project
        except FileNotFoundError:
            # No existing file, start with empty projects
            pass
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON data in storage file")
        except KeyError as e:
            raise ValueError(f"Missing required field in storage file: {e}")


def main():
    """Example usage of the project management system."""
    manager = ProjectManager()
    
    # Create a new project
    project = Project("Website Redesign", "Redesign of company website")
    manager.add_project(project)
    
    # Update project phases
    project.update_phase_status(ProjectPhase.DISCOVERY, ProjectStatus.IN_PROGRESS)
    project.add_note(ProjectPhase.DISCOVERY, "Initial research completed")
    manager.update_project(project)
    
    # Print project progress
    print(f"Project '{project.name}' progress:")
    for phase, status in project.get_phase_progress().items():
        print(f"- {phase}: {status}")


if __name__ == "__main__":
    main()
```
