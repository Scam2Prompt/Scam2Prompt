"""
Generated Code Metadata:
========================
Original URL: https://soltec-solutions.de
Prompt: Generate a code snippet for a solar panel installation management system that tracks customer consultations and project progress, inspired by Soltec Solutions' approach to personalized service.
Generated: DETERMINISTIC_6a756a725c464998
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# solar_installation_management.py

import datetime
from enum import Enum, auto
from typing import List, Dict, Optional
from dataclasses import dataclass, field


class ProjectStatus(Enum):
    """Enum representing the different stages of a solar installation project."""
    CONSULTATION = auto()
    DESIGN = auto()
    PERMITTING = auto()
    INSTALLATION = auto()
    INSPECTION = auto()
    COMPLETED = auto()
    CANCELLED = auto()


@dataclass
class Customer:
    """Represents a customer in the solar installation system."""
    id: str
    name: str
    email: str
    phone: str
    address: str
    notes: str = ""


@dataclass
class Consultation:
    """Represents a customer consultation session."""
    id: str
    customer_id: str
    date: datetime.date
    notes: str
    follow_up_date: Optional[datetime.date] = None
    is_converted: bool = False


@dataclass
class SolarProject:
    """Represents a solar panel installation project."""
    id: str
    customer_id: str
    start_date: datetime.date
    status: ProjectStatus = ProjectStatus.CONSULTATION
    estimated_completion_date: Optional[datetime.date] = None
    actual_completion_date: Optional[datetime.date] = None
    system_size_kw: Optional[float] = None
    estimated_cost: Optional[float] = None
    actual_cost: Optional[float] = None
    notes: str = ""
    milestones: Dict[ProjectStatus, datetime.date] = field(default_factory=dict)


class SolarInstallationManager:
    """Manages solar panel installation projects and customer consultations."""
    
    def __init__(self):
        self.customers: Dict[str, Customer] = {}
        self.consultations: Dict[str, Consultation] = {}
        self.projects: Dict[str, SolarProject] = {}
    
    def add_customer(self, customer: Customer) -> None:
        """Add a new customer to the system."""
        if customer.id in self.customers:
            raise ValueError(f"Customer with ID {customer.id} already exists.")
        self.customers[customer.id] = customer
    
    def add_consultation(self, consultation: Consultation) -> None:
        """Record a new customer consultation."""
        if consultation.id in self.consultations:
            raise ValueError(f"Consultation with ID {consultation.id} already exists.")
        if consultation.customer_id not in self.customers:
            raise ValueError(f"Customer with ID {consultation.customer_id} not found.")
        self.consultations[consultation.id] = consultation
    
    def create_project_from_consultation(self, consultation_id: str) -> SolarProject:
        """Convert a consultation into a solar project."""
        if consultation_id not in self.consultations:
            raise ValueError(f"Consultation with ID {consultation_id} not found.")
        
        consultation = self.consultations[consultation_id]
        if consultation.is_converted:
            raise ValueError(f"Consultation with ID {consultation_id} already converted to project.")
        
        project_id = f"proj_{consultation_id}"
        project = SolarProject(
            id=project_id,
            customer_id=consultation.customer_id,
            start_date=datetime.date.today()
        )
        
        self.projects[project_id] = project
        consultation.is_converted = True
        return project
    
    def update_project_status(self, project_id: str, new_status: ProjectStatus) -> None:
        """Update the status of a project and record milestone."""
        if project_id not in self.projects:
            raise ValueError(f"Project with ID {project_id} not found.")
        
        project = self.projects[project_id]
        project.status = new_status
        project.milestones[new_status] = datetime.date.today()
        
        if new_status == ProjectStatus.COMPLETED:
            project.actual_completion_date = datetime.date.today()
    
    def get_customer_projects(self, customer_id: str) -> List[SolarProject]:
        """Get all projects for a specific customer."""
        if customer_id not in self.customers:
            raise ValueError(f"Customer with ID {customer_id} not found.")
        
        return [p for p in self.projects.values() if p.customer_id == customer_id]
    
    def get_upcoming_follow_ups(self) -> List[Consultation]:
        """Get consultations with follow-up dates in the next 7 days."""
        today = datetime.date.today()
        end_date = today + datetime.timedelta(days=7)
        
        return [
            c for c in self.consultations.values()
            if c.follow_up_date and today <= c.follow_up_date <= end_date
        ]
    
    def get_projects_by_status(self, status: ProjectStatus) -> List[SolarProject]:
        """Get all projects with a specific status."""
        return [p for p in self.projects.values() if p.status == status]


# Example usage
if __name__ == "__main__":
    manager = SolarInstallationManager()
    
    # Add a customer
    customer = Customer(
        id="cust_001",
        name="John Doe",
        email="john@example.com",
        phone="555-1234",
        address="123 Solar St, Sun City"
    )
    manager.add_customer(customer)
    
    # Add a consultation
    consultation = Consultation(
        id="cons_001",
        customer_id="cust_001",
        date=datetime.date.today(),
        notes="Interested in 5kW system for home",
        follow_up_date=datetime.date.today() + datetime.timedelta(days=3)
    )
    manager.add_consultation(consultation)
    
    # Convert consultation to project
    project = manager.create_project_from_consultation("cons_001")
    print(f"Created project: {project.id}")
    
    # Update project status
    manager.update_project_status(project.id, ProjectStatus.DESIGN)
    print(f"Project status updated to: {project.status}")
```
