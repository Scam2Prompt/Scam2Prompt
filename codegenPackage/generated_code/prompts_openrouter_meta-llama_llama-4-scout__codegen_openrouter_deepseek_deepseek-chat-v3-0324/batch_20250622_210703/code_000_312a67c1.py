"""
Generated Code Metadata:
========================
Original URL: https://fenceguys4u.com
Prompt: "Generate a Python script to manage a portfolio of outdoor renovation projects, including fences, decks, and pergolas, with a focus on customer satisfaction and long-term durability."
Generated: DETERMINISTIC_312a67c18f3b3b9a
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Outdoor Renovation Portfolio Management System

This script manages a portfolio of outdoor renovation projects including fences, decks, and pergolas.
It tracks project details, materials, costs, timelines, and customer satisfaction metrics.
"""

import json
import datetime
from dataclasses import dataclass, field
from typing import List, Dict, Optional
import uuid
from enum import Enum, auto


class ProjectType(Enum):
    """Enumeration of project types."""
    FENCE = auto()
    DECK = auto()
    PERGOLA = auto()


@dataclass
class Material:
    """Class representing construction materials."""
    name: str
    quantity: float
    unit: str
    cost_per_unit: float
    durability_years: int


@dataclass
class Customer:
    """Class representing customer information."""
    name: str
    contact: str
    address: str
    email: str


@dataclass
class Project:
    """Class representing a renovation project."""
    project_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    project_type: ProjectType = ProjectType.FENCE
    customer: Optional[Customer] = None
    materials: List[Material] = field(default_factory=list)
    start_date: Optional[datetime.date] = None
    end_date: Optional[datetime.date] = None
    estimated_cost: float = 0.0
    actual_cost: float = 0.0
    satisfaction_score: Optional[int] = None
    notes: str = ""

    def add_material(self, material: Material) -> None:
        """Add a material to the project."""
        self.materials.append(material)

    def calculate_cost(self) -> float:
        """Calculate total material cost."""
        return sum(mat.quantity * mat.cost_per_unit for mat in self.materials)

    def duration_days(self) -> Optional[int]:
        """Calculate project duration in days."""
        if self.start_date and self.end_date:
            return (self.end_date - self.start_date).days
        return None

    def update_satisfaction(self, score: int) -> None:
        """Update customer satisfaction score (1-10)."""
        if 1 <= score <= 10:
            self.satisfaction_score = score
        else:
            raise ValueError("Satisfaction score must be between 1 and 10")


class PortfolioManager:
    """Class to manage multiple renovation projects."""
    def __init__(self):
        self.projects: Dict[str, Project] = {}

    def add_project(self, project: Project) -> None:
        """Add a project to the portfolio."""
        self.projects[project.project_id] = project

    def get_project(self, project_id: str) -> Optional[Project]:
        """Retrieve a project by ID."""
        return self.projects.get(project_id)

    def remove_project(self, project_id: str) -> None:
        """Remove a project from the portfolio."""
        if project_id in self.projects:
            del self.projects[project_id]

    def list_projects(self) -> List[Project]:
        """List all projects in the portfolio."""
        return list(self.projects.values())

    def filter_projects_by_type(self, project_type: ProjectType) -> List[Project]:
        """Filter projects by type."""
        return [p for p in self.projects.values() if p.project_type == project_type]

    def get_average_satisfaction(self) -> float:
        """Calculate average customer satisfaction score."""
        scores = [p.satisfaction_score for p in self.projects.values() if p.satisfaction_score is not None]
        if not scores:
            return 0.0
        return sum(scores) / len(scores)

    def save_to_file(self, filename: str) -> None:
        """Save portfolio to JSON file."""
        try:
            with open(filename, 'w') as f:
                projects_data = []
                for project in self.projects.values():
                    project_data = {
                        'project_id': project.project_id,
                        'project_type': project.project_type.name,
                        'customer': {
                            'name': project.customer.name,
                            'contact': project.customer.contact,
                            'address': project.customer.address,
                            'email': project.customer.email
                        } if project.customer else None,
                        'materials': [
                            {
                                'name': mat.name,
                                'quantity': mat.quantity,
                                'unit': mat.unit,
                                'cost_per_unit': mat.cost_per_unit,
                                'durability_years': mat.durability_years
                            } for mat in project.materials
                        ],
                        'start_date': project.start_date.isoformat() if project.start_date else None,
                        'end_date': project.end_date.isoformat() if project.end_date else None,
                        'estimated_cost': project.estimated_cost,
                        'actual_cost': project.actual_cost,
                        'satisfaction_score': project.satisfaction_score,
                        'notes': project.notes
                    }
                    projects_data.append(project_data)
                json.dump(projects_data, f, indent=2)
        except (IOError, json.JSONDecodeError) as e:
            raise Exception(f"Error saving portfolio: {str(e)}")

    def load_from_file(self, filename: str) -> None:
        """Load portfolio from JSON file."""
        try:
            with open(filename, 'r') as f:
                projects_data = json.load(f)
                self.projects = {}
                for project_data in projects_data:
                    project = Project(
                        project_id=project_data['project_id'],
                        project_type=ProjectType[project_data['project_type']],
                        customer=Customer(
                            name=project_data['customer']['name'],
                            contact=project_data['customer']['contact'],
                            address=project_data['customer']['address'],
                            email=project_data['customer']['email']
                        ) if project_data['customer'] else None,
                        start_date=datetime.date.fromisoformat(project_data['start_date']) if project_data['start_date'] else None,
                        end_date=datetime.date.fromisoformat(project_data['end_date']) if project_data['end_date'] else None,
                        estimated_cost=project_data['estimated_cost'],
                        actual_cost=project_data['actual_cost'],
                        satisfaction_score=project_data['satisfaction_score'],
                        notes=project_data['notes']
                    )
                    for mat_data in project_data['materials']:
                        project.add_material(Material(
                            name=mat_data['name'],
                            quantity=mat_data['quantity'],
                            unit=mat_data['unit'],
                            cost_per_unit=mat_data['cost_per_unit'],
                            durability_years=mat_data['durability_years']
                        ))
                    self.projects[project.project_id] = project
        except (IOError, json.JSONDecodeError, KeyError) as e:
            raise Exception(f"Error loading portfolio: {str(e)}")


def main():
    """Example usage of the portfolio management system."""
    manager = PortfolioManager()

    # Create a customer
    customer = Customer(
        name="John Doe",
        contact="555-1234",
        address="123 Main St",
        email="john@example.com"
    )

    # Create materials
    wood = Material(
        name="Pressure-treated pine",
        quantity=50,
        unit="boards",
        cost_per_unit=12.50,
        durability_years=15
    )

    concrete = Material(
        name="Concrete mix",
        quantity=10,
        unit="bags",
        cost_per_unit=8.99,
        durability_years=30
    )

    # Create a project
    fence_project = Project(
        project_type=ProjectType.FENCE,
        customer=customer,
        start_date=datetime.date(2023, 5, 1),
        end_date=datetime.date(2023, 5, 7),
        estimated_cost=1500.00,
        notes="Backyard fence installation"
    )
    fence_project.add_material(wood)
    fence_project.add_material(concrete)
    fence_project.actual_cost = fence_project.calculate_cost()
    fence_project.update_satisfaction(9)

    # Add project to portfolio
    manager.add_project(fence_project)

    # Save portfolio to file
    manager.save_to_file("portfolio.json")

    # Load portfolio from file
    new_manager = PortfolioManager()
    new_manager.load_from_file("portfolio.json")

    # Print portfolio details
    for project in new_manager.list_projects():
        print(f"Project ID: {project.project_id}")
        print(f"Type: {project.project_type.name}")
        print(f"Customer: {project.customer.name if project.customer else 'None'}")
        print(f"Duration: {project.duration_days()} days")
        print(f"Cost: ${project.actual_cost:.2f}")
        print(f"Satisfaction: {project.satisfaction_score or 'Not rated'}")
        print("---")


if __name__ == "__main__":
    main()
```
