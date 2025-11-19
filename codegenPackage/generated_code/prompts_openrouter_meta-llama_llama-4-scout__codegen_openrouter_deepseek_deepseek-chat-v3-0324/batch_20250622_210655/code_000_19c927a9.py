"""
Generated Code Metadata:
========================
Original URL: https://bismillah-traders.com
Prompt: "Write a Python script to manage construction projects using design-build and turnkey construction methods, considering factors like client requirements and project planning."
Generated: DETERMINISTIC_19c927a9e5d7458c
Batch ID: 20250622_210655
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

This script manages construction projects using design-build and turnkey methods.
It handles client requirements, project planning, scheduling, and resource allocation.
"""

from datetime import datetime
from enum import Enum
import json
from typing import Dict, List, Optional


class ConstructionMethod(Enum):
    DESIGN_BUILD = "Design-Build"
    TURNKEY = "Turnkey"


class ProjectStatus(Enum):
    PLANNING = "Planning"
    DESIGN = "Design"
    CONSTRUCTION = "Construction"
    COMPLETED = "Completed"
    CANCELLED = "Cancelled"


class ConstructionProject:
    """Class representing a construction project."""

    def __init__(
        self,
        name: str,
        client: str,
        method: ConstructionMethod,
        requirements: Dict[str, str],
        start_date: str,
        budget: float,
    ):
        """Initialize a construction project.

        Args:
            name: Project name
            client: Client name
            method: Construction method (Design-Build or Turnkey)
            requirements: Dictionary of client requirements
            start_date: Project start date (YYYY-MM-DD)
            budget: Project budget
        """
        self.name = name
        self.client = client
        self.method = method
        self.requirements = requirements
        self.start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
        self.budget = budget
        self.status = ProjectStatus.PLANNING
        self.phases: List[Dict[str, str]] = []
        self.resources: Dict[str, List[str]] = {"materials": [], "labor": []}
        self.completion_date: Optional[str] = None

    def add_phase(self, name: str, duration: int, cost: float) -> None:
        """Add a phase to the project.

        Args:
            name: Phase name
            duration: Duration in days
            cost: Estimated cost for the phase
        """
        self.phases.append(
            {
                "name": name,
                "duration": duration,
                "cost": cost,
                "status": "Pending",
                "start_date": None,
                "end_date": None,
            }
        )

    def allocate_resources(self, resource_type: str, resources: List[str]) -> None:
        """Allocate resources to the project.

        Args:
            resource_type: Type of resource ('materials' or 'labor')
            resources: List of resources to allocate
        """
        if resource_type not in self.resources:
            raise ValueError("Invalid resource type. Must be 'materials' or 'labor'")
        self.resources[resource_type].extend(resources)

    def update_status(self, status: ProjectStatus) -> None:
        """Update project status.

        Args:
            status: New project status
        """
        self.status = status
        if status == ProjectStatus.COMPLETED:
            self.completion_date = datetime.now().strftime("%Y-%m-%d")

    def calculate_remaining_budget(self) -> float:
        """Calculate remaining budget based on completed phases."""
        spent = sum(phase["cost"] for phase in self.phases if phase["status"] == "Completed")
        return self.budget - spent

    def to_dict(self) -> Dict:
        """Convert project to dictionary for serialization."""
        return {
            "name": self.name,
            "client": self.client,
            "method": self.method.value,
            "requirements": self.requirements,
            "start_date": self.start_date.strftime("%Y-%m-%d"),
            "budget": self.budget,
            "status": self.status.value,
            "phases": self.phases,
            "resources": self.resources,
            "completion_date": self.completion_date,
        }


class ProjectManager:
    """Class for managing multiple construction projects."""

    def __init__(self):
        self.projects: Dict[str, ConstructionProject] = {}

    def add_project(self, project: ConstructionProject) -> None:
        """Add a project to the manager.

        Args:
            project: ConstructionProject instance
        """
        if project.name in self.projects:
            raise ValueError("Project with this name already exists")
        self.projects[project.name] = project

    def get_project(self, name: str) -> ConstructionProject:
        """Get a project by name.

        Args:
            name: Project name

        Returns:
            ConstructionProject instance
        """
        if name not in self.projects:
            raise ValueError("Project not found")
        return self.projects[name]

    def save_projects(self, filename: str) -> None:
        """Save projects to JSON file.

        Args:
            filename: Name of the file to save to
        """
        with open(filename, "w") as f:
            json.dump(
                {name: project.to_dict() for name, project in self.projects.items()},
                f,
                indent=2,
            )

    def load_projects(self, filename: str) -> None:
        """Load projects from JSON file.

        Args:
            filename: Name of the file to load from
        """
        try:
            with open(filename, "r") as f:
                data = json.load(f)
                self.projects = {}
                for name, project_data in data.items():
                    method = (
                        ConstructionMethod.DESIGN_BUILD
                        if project_data["method"] == "Design-Build"
                        else ConstructionMethod.TURNKEY
                    )
                    project = ConstructionProject(
                        name=project_data["name"],
                        client=project_data["client"],
                        method=method,
                        requirements=project_data["requirements"],
                        start_date=project_data["start_date"],
                        budget=project_data["budget"],
                    )
                    project.phases = project_data["phases"]
                    project.resources = project_data["resources"]
                    project.status = ProjectStatus(project_data["status"])
                    project.completion_date = project_data["completion_date"]
                    self.projects[name] = project
        except FileNotFoundError:
            raise FileNotFoundError("Project file not found")
        except json.JSONDecodeError:
            raise ValueError("Invalid project file format")


def main_menu() -> None:
    """Display main menu and handle user input."""
    manager = ProjectManager()
    
    while True:
        print("\nConstruction Project Management System")
        print("1. Create New Project")
        print("2. View Project Details")
        print("3. Add Project Phase")
        print("4. Allocate Resources")
        print("5. Update Project Status")
        print("6. Save Projects")
        print("7. Load Projects")
        print("8. Exit")
        
        choice = input("Enter your choice (1-8): ")
        
        try:
            if choice == "1":
                create_project(manager)
            elif choice == "2":
                view_project(manager)
            elif choice == "3":
                add_phase(manager)
            elif choice == "4":
                allocate_resources(manager)
            elif choice == "5":
                update_status(manager)
            elif choice == "6":
                save_projects(manager)
            elif choice == "7":
                load_projects(manager)
            elif choice == "8":
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")
        except Exception as e:
            print(f"Error: {str(e)}")


def create_project(manager: ProjectManager) -> None:
    """Create a new construction project."""
    print("\nCreate New Project")
    name = input("Project Name: ")
    client = input("Client Name: ")
    
    print("\nConstruction Method:")
    print("1. Design-Build")
    print("2. Turnkey")
    method_choice = input("Select method (1-2): ")
    method = ConstructionMethod.DESIGN_BUILD if method_choice == "1" else ConstructionMethod.TURNKEY
    
    requirements = {}
    print("\nEnter Client Requirements (enter 'done' when finished):")
    while True:
        key = input("Requirement key (e.g., 'size', 'materials'): ")
        if key.lower() == 'done':
            break
        value = input(f"{key} value: ")
        requirements[key] = value
    
    start_date = input("Start Date (YYYY-MM-DD): ")
    budget = float(input("Budget: "))
    
    project = ConstructionProject(name, client, method, requirements, start_date, budget)
    manager.add_project(project)
    print(f"Project '{name}' created successfully!")


def view_project(manager: ProjectManager) -> None:
    """View project details."""
    name = input("Enter project name: ")
    project = manager.get_project(name)
    
    print(f"\nProject: {project.name}")
    print(f"Client: {project.client}")
    print(f"Method: {project.method.value}")
    print(f"Status: {project.status.value}")
    print(f"Start Date: {project.start_date}")
    print(f"Budget: ${project.budget:,.2f}")
    print(f"Remaining Budget: ${project.calculate_remaining_budget():,.2f}")
    
    print("\nRequirements:")
    for key, value in project.requirements.items():
        print(f"- {key}: {value}")
    
    print("\nPhases:")
    for phase in project.phases:
