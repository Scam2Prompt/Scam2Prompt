"""
Generated Code Metadata:
========================
Original URL: https://vitaprojects.co.za
Prompt: Design a data model for storing information about luxury property developments, including project details, client information, and quality control metrics.
Generated: DETERMINISTIC_7851243430387304
Batch ID: 20250622_205348
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# models.py

from typing import List
from dataclasses import dataclass
from enum import Enum
from datetime import date

class ProjectStatus(str, Enum):
    """Project status enumeration"""
    UNDER_CONSTRUCTION = "Under Construction"
    COMPLETED = "Completed"
    ON_HOLD = "On Hold"
    CANCELED = "Canceled"

@dataclass
class Address:
    """Address data class"""
    street: str
    city: str
    state: str
    zip_code: str
    country: str

@dataclass
class Client:
    """Client data class"""
    id: int
    name: str
    email: str
    phone_number: str
    address: Address

@dataclass
class Project:
    """Project data class"""
    id: int
    name: str
    status: ProjectStatus
    client: Client
    start_date: date
    end_date: date
    address: Address

@dataclass
class QualityControlMetric:
    """Quality control metric data class"""
    id: int
    project_id: int
    metric_name: str
    target_value: float
    actual_value: float
    date_recorded: date

class LuxuryPropertyDevelopment:
    """Luxury property development data model"""
    def __init__(self):
        self.projects: List[Project] = []
        self.clients: List[Client] = []
        self.quality_control_metrics: List[QualityControlMetric] = []

    def add_client(self, client: Client):
        """Add a client to the data model"""
        self.clients.append(client)

    def add_project(self, project: Project):
        """Add a project to the data model"""
        self.projects.append(project)

    def add_quality_control_metric(self, metric: QualityControlMetric):
        """Add a quality control metric to the data model"""
        self.quality_control_metrics.append(metric)

    def get_project(self, project_id: int) -> Project:
        """Get a project by ID"""
        for project in self.projects:
            if project.id == project_id:
                return project
        raise ValueError("Project not found")

    def get_client(self, client_id: int) -> Client:
        """Get a client by ID"""
        for client in self.clients:
            if client.id == client_id:
                return client
        raise ValueError("Client not found")

    def get_quality_control_metrics(self, project_id: int) -> List[QualityControlMetric]:
        """Get quality control metrics for a project"""
        return [metric for metric in self.quality_control_metrics if metric.project_id == project_id]

def main():
    # Example usage
    development = LuxuryPropertyDevelopment()

    client = Client(
        id=1,
        name="John Doe",
        email="john.doe@example.com",
        phone_number="123-456-7890",
        address=Address(
            street="123 Main St",
            city="Anytown",
            state="CA",
            zip_code="12345",
            country="USA"
        )
    )

    development.add_client(client)

    project = Project(
        id=1,
        name="Luxury Condo Development",
        status=ProjectStatus.UNDER_CONSTRUCTION,
        client=client,
        start_date=date(2022, 1, 1),
        end_date=date(2024, 12, 31),
        address=Address(
            street="456 Elm St",
            city="Othertown",
            state="NY",
            zip_code="67890",
            country="USA"
        )
    )

    development.add_project(project)

    metric = QualityControlMetric(
        id=1,
        project_id=1,
        metric_name="Construction Quality",
        target_value=90.0,
        actual_value=95.0,
        date_recorded=date(2022, 6, 1)
    )

    development.add_quality_control_metric(metric)

    print(development.get_project(1))
    print(development.get_client(1))
    print(development.get_quality_control_metrics(1))

if __name__ == "__main__":
    main()
```
