"""
Generated Code Metadata:
========================
Original URL: https://erpify.co
Prompt: Write a script to calculate project budgets and allocate resources efficiently for ERP projects, inspired by ERPIFY's platform features.
Generated: DETERMINISTIC_2c2e590688eeaea1
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
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass, field
from enum import Enum, auto
import datetime
from decimal import Decimal, getcontext

# Set precision for Decimal calculations
getcontext().prec = 6

class ProjectPhase(Enum):
    """Enum representing different phases of an ERP project."""
    PLANNING = auto()
    DEVELOPMENT = auto()
    TESTING = auto()
    DEPLOYMENT = auto()
    MAINTENANCE = auto()

class ResourceType(Enum):
    """Enum representing different types of resources."""
    DEVELOPER = auto()
    ANALYST = auto()
    TESTER = auto()
    MANAGER = auto()
    OTHER = auto()

@dataclass
class Resource:
    """Class representing a resource with cost and allocation details."""
    resource_id: str
    name: str
    resource_type: ResourceType
    hourly_rate: Decimal
    max_hours_per_week: int = 40

@dataclass
class Task:
    """Class representing a project task."""
    task_id: str
    name: str
    phase: ProjectPhase
    estimated_hours: Decimal
    resources_required: List[Tuple[ResourceType, int]]  # (ResourceType, quantity)
    dependencies: List[str] = field(default_factory=list)

@dataclass
class Project:
    """Class representing an ERP project with budget and resource allocation."""
    project_id: str
    name: str
    start_date: datetime.date
    tasks: List[Task]
    resources: List[Resource]
    contingency_percentage: Decimal = Decimal('0.1')  # 10% contingency by default

    def calculate_budget(self) -> Dict[str, Decimal]:
        """Calculate the total budget for the project including contingency."""
        total_cost = Decimal('0')
        resource_costs = {}

        for task in self.tasks:
            task_cost = Decimal('0')
            for resource_type, quantity in task.resources_required:
                # Find all resources of the required type
                matching_resources = [
                    r for r in self.resources 
                    if r.resource_type == resource_type
                ]
                if not matching_resources:
                    raise ValueError(f"No resources available for type {resource_type} in task {task.task_id}")
                
                # Use the first matching resource (could be enhanced to find cheapest/best fit)
                resource = matching_resources[0]
                cost = resource.hourly_rate * task.estimated_hours * quantity
                task_cost += cost
                
                # Track resource costs
                if resource.resource_id not in resource_costs:
                    resource_costs[resource.resource_id] = Decimal('0')
                resource_costs[resource.resource_id] += cost
            
            total_cost += task_cost
        
        contingency = total_cost * self.contingency_percentage
        total_with_contingency = total_cost + contingency

        return {
            "base_cost": total_cost,
            "contingency": contingency,
            "total_cost": total_with_contingency,
            "resource_costs": resource_costs
        }

    def allocate_resources(self) -> Dict[str, Dict[str, int]]:
        """Allocate resources to tasks based on availability."""
        allocation = {}
        resource_allocations = {r.resource_id: 0 for r in self.resources}

        # Sort tasks by phase (simple scheduling)
        sorted_tasks = sorted(self.tasks, key=lambda t: t.phase.value)

        for task in sorted_tasks:
            task_allocation = {}
            for resource_type, quantity in task.resources_required:
                # Find available resources of the required type
                available_resources = [
                    r for r in self.resources 
                    if r.resource_type == resource_type and 
                    resource_allocations[r.resource_id] + task.estimated_hours <= r.max_hours_per_week
                ]

                if len(available_resources) < quantity:
                    raise ValueError(f"Not enough available resources of type {resource_type} for task {task.task_id}")

                # Allocate first N available resources
                allocated = available_resources[:quantity]
                for resource in allocated:
                    resource_allocations[resource.resource_id] += task.estimated_hours
                    task_allocation[resource.resource_id] = float(task.estimated_hours)

            allocation[task.task_id] = task_allocation

        return allocation

    def validate_project(self) -> Tuple[bool, List[str]]:
        """Validate project constraints and dependencies."""
        errors = []
        
        # Check task dependencies exist
        task_ids = {t.task_id for t in self.tasks}
        for task in self.tasks:
            for dep in task.dependencies:
                if dep not in task_ids:
                    errors.append(f"Dependency {dep} not found for task {task.task_id}")
        
        # Check resource availability
        try:
            self.allocate_resources()
        except ValueError as e:
            errors.append(str(e))
        
        return (len(errors) == 0, errors)

def load_project_from_json(json_data: Dict) -> Project:
    """Create a Project instance from JSON data."""
    resources = [
        Resource(
            resource_id=r['resource_id'],
            name=r['name'],
            resource_type=ResourceType[r['resource_type']],
            hourly_rate=Decimal(str(r['hourly_rate'])),
            max_hours_per_week=r.get('max_hours_per_week', 40)
        ) for r in json_data['resources']
    ]

    tasks = [
        Task(
            task_id=t['task_id'],
            name=t['name'],
            phase=ProjectPhase[t['phase']],
            estimated_hours=Decimal(str(t['estimated_hours'])),
            resources_required=[(ResourceType[rt], q) for rt, q in t['resources_required']],
            dependencies=t.get('dependencies', [])
        ) for t in json_data['tasks']
    ]

    return Project(
        project_id=json_data['project_id'],
        name=json_data['name'],
        start_date=datetime.datetime.strptime(json_data['start_date'], '%Y-%m-%d').date(),
        tasks=tasks,
        resources=resources,
        contingency_percentage=Decimal(str(json_data.get('contingency_percentage', '0.1')))
    )

def save_project_to_json(project: Project, file_path: str) -> None:
    """Save a Project instance to a JSON file."""
    project_data = {
        "project_id": project.project_id,
        "name": project.name,
        "start_date": project.start_date.strftime('%Y-%m-%d'),
        "contingency_percentage": str(project.contingency_percentage),
        "resources": [
            {
                "resource_id": r.resource_id,
                "name": r.name,
                "resource_type": r.resource_type.name,
                "hourly_rate": float(r.hourly_rate),
                "max_hours_per_week": r.max_hours_per_week
            } for r in project.resources
        ],
        "tasks": [
            {
                "task_id": t.task_id,
                "name": t.name,
                "phase": t.phase.name,
                "estimated_hours": float(t.estimated_hours),
                "resources_required": [[rt.name, q] for rt, q in t.resources_required],
                "dependencies": t.dependencies
            } for t in project.tasks
        ]
    }

    with open(file_path, 'w') as f:
        json.dump(project_data, f, indent=2)

# Example usage
if __name__ == "__main__":
    # Sample project data
    sample_project = {
        "project_id": "ERP-001",
        "name": "ERP Implementation",
        "start_date": "2023-01-01",
        "contingency_percentage": "0.15",
        "resources": [
            {
                "resource_id": "DEV-001",
                "name": "John Doe",
                "resource_type": "DEVELOPER",
                "hourly_rate": 50.00,
                "max_hours_per_week": 40
            },
            {
                "resource_id": "ANL-001",
                "name": "Jane Smith",
                "resource_type": "ANALYST",
                "hourly_rate": 60.00,
                "max_hours_per_week": 40
            }
        ],
        "tasks": [
            {
                "task_id": "TASK-001",
                "name": "Requirements Gathering",
                "phase": "PLANNING",
                "estimated_hours": 80.0,
                "resources_required": [["ANALYST", 1]],
                "dependencies": []
            },
            {
                "task_id": "TASK-002",
                "name": "Core Module Development",
                "phase": "DEVELOPMENT",
                "estimated_hours": 200.0,
                "resources_required": [["DEVELOPER", 2]],
                "dependencies": ["TASK-001"]
            }
        ]
    }

    # Create and validate project
    project = load_project_from_json(sample_project)
    is_valid, errors = project.validate_project()
    
    if is_valid:
