"""
Generated Code Metadata:
========================
Original URL: https://thebookcompany.org
Prompt: "Write a Python script to manage book publishing services, including ghostwriting, publishing, and printing, for a company like The Book Company."
Generated: DETERMINISTIC_ba627723830b7fec
Batch ID: 20250622_205919
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


class BookService:
    """Base class for all book services."""

    def __init__(self, service_name: str, base_cost: float):
        """Initialize the book service with name and base cost."""
        self.service_name = service_name
        self.base_cost = base_cost
        self.additional_costs: Dict[str, float] = {}

    def add_additional_cost(self, description: str, cost: float) -> None:
        """Add an additional cost to the service."""
        if cost <= 0:
            raise ValueError("Cost must be positive.")
        self.additional_costs[description] = cost

    def calculate_total_cost(self) -> float:
        """Calculate the total cost including additional costs."""
        return self.base_cost + sum(self.additional_costs.values())

    def __str__(self) -> str:
        """Return a string representation of the service."""
        return f"{self.service_name} (Base: ${self.base_cost:.2f})"


class GhostwritingService(BookService):
    """Service for ghostwriting books."""

    def __init__(self, base_cost: float = 5000.00):
        """Initialize ghostwriting service with default base cost."""
        super().__init__("Ghostwriting", base_cost)


class PublishingService(BookService):
    """Service for publishing books."""

    def __init__(self, base_cost: float = 3000.00):
        """Initialize publishing service with default base cost."""
        super().__init__("Publishing", base_cost)


class PrintingService(BookService):
    """Service for printing books."""

    def __init__(self, base_cost: float = 2000.00):
        """Initialize printing service with default base cost."""
        super().__init__("Printing", base_cost)


class BookProject:
    """Class to manage a book project with multiple services."""

    def __init__(self, project_name: str, client_name: str):
        """Initialize a book project with name and client."""
        self.project_name = project_name
        self.client_name = client_name
        self.services: List[BookService] = []
        self.created_at = datetime.now()
        self.completed = False

    def add_service(self, service: BookService) -> None:
        """Add a service to the project."""
        self.services.append(service)

    def calculate_total_cost(self) -> float:
        """Calculate the total cost of all services in the project."""
        return sum(service.calculate_total_cost() for service in self.services)

    def mark_completed(self) -> None:
        """Mark the project as completed."""
        self.completed = True

    def __str__(self) -> str:
        """Return a string representation of the project."""
        status = "Completed" if self.completed else "In Progress"
        return (
            f"Project: {self.project_name}\n"
            f"Client: {self.client_name}\n"
            f"Status: {status}\n"
            f"Total Cost: ${self.calculate_total_cost():.2f}\n"
            f"Services: {len(self.services)}"
        )


class BookCompanyManager:
    """Manager class to handle multiple book projects."""

    def __init__(self, data_file: str = "book_projects.json"):
        """Initialize the manager with a data file for persistence."""
        self.data_file = data_file
        self.projects: Dict[str, BookProject] = {}
        self._load_projects()

    def _load_projects(self) -> None:
        """Load projects from the data file."""
        if os.path.exists(self.data_file):
            with open(self.data_file, "r") as f:
                data = json.load(f)
                for project_data in data:
                    project = BookProject(
                        project_data["project_name"],
                        project_data["client_name"]
                    )
                    project.created_at = datetime.fromisoformat(
                        project_data["created_at"]
                    )
                    project.completed = project_data["completed"]

                    for service_data in project_data["services"]:
                        service_class = globals()[service_data["type"]]
                        service = service_class(service_data["base_cost"])
                        for desc, cost in service_data["additional_costs"].items():
                            service.add_additional_cost(desc, cost)
                        project.add_service(service)

                    self.projects[project_data["project_name"]] = project

    def _save_projects(self) -> None:
        """Save projects to the data file."""
        data = []
        for project in self.projects.values():
            project_data = {
                "project_name": project.project_name,
                "client_name": project.client_name,
                "created_at": project.created_at.isoformat(),
                "completed": project.completed,
                "services": []
            }
            for service in project.services:
                service_data = {
                    "type": service.__class__.__name__,
                    "base_cost": service.base_cost,
                    "additional_costs": service.additional_costs
                }
                project_data["services"].append(service_data)
            data.append(project_data)

        with open(self.data_file, "w") as f:
            json.dump(data, f, indent=2)

    def create_project(
        self,
        project_name: str,
        client_name: str
    ) -> BookProject:
        """Create a new book project."""
        if project_name in self.projects:
            raise ValueError("Project with this name already exists.")
        project = BookProject(project_name, client_name)
        self.projects[project_name] = project
        self._save_projects()
        return project

    def get_project(self, project_name: str) -> Optional[BookProject]:
        """Get a project by name."""
        return self.projects.get(project_name)

    def add_service_to_project(
        self,
        project_name: str,
        service: BookService
    ) -> None:
        """Add a service to an existing project."""
        project = self.projects.get(project_name)
        if not project:
            raise ValueError("Project not found.")
        project.add_service(service)
        self._save_projects()

    def complete_project(self, project_name: str) -> None:
        """Mark a project as completed."""
        project = self.projects.get(project_name)
        if not project:
            raise ValueError("Project not found.")
        project.mark_completed()
        self._save_projects()

    def list_projects(self) -> List[BookProject]:
        """List all projects."""
        return list(self.projects.values())

    def delete_project(self, project_name: str) -> None:
        """Delete a project."""
        if project_name not in self.projects:
            raise ValueError("Project not found.")
        del self.projects[project_name]
        self._save_projects()


def main():
    """Main function to demonstrate the book company manager."""
    manager = BookCompanyManager()

    # Example usage
    try:
        # Create a new project
        project = manager.create_project(
            "The Great Novel",
            "John Doe"
        )

        # Add services to the project
        ghostwriting = GhostwritingService(6000.00)
        ghostwriting.add_additional_cost("Research", 1000.00)
        manager.add_service_to_project("The Great Novel", ghostwriting)

        publishing = PublishingService(3500.00)
        publishing.add_additional_cost("Cover Design", 500.00)
        manager.add_service_to_project("The Great Novel", publishing)

        printing = PrintingService(2500.00)
        printing.add_additional_cost("Special Paper", 300.00)
        manager.add_service_to_project("The Great Novel", printing)

        # Complete the project
        manager.complete_project("The Great Novel")

        # List all projects
        for p in manager.list_projects():
            print(p)
            print("---")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
