"""
Generated Code Metadata:
========================
Original URL: https://pdma.io
Prompt: Write Python code to simulate project timelines and resource allocation, using concepts from PDMA's Project Management training.
Generated: DETERMINISTIC_76ae981b21963f02
Batch ID: 20250612_145730
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from typing import List, Dict, Optional
from datetime import datetime, timedelta
from enum import Enum, auto


class TaskStatus(Enum):
    """Enum representing the status of a task."""
    NOT_STARTED = auto()
    IN_PROGRESS = auto()
    COMPLETED = auto()
    BLOCKED = auto()


class ResourceType(Enum):
    """Enum representing types of resources."""
    HUMAN = auto()
    EQUIPMENT = auto()
    MATERIAL = auto()
    FINANCIAL = auto()


class Task:
    """Class representing a project task."""
    
    def __init__(
        self,
        name: str,
        duration: int,
        dependencies: List['Task'] = None,
        required_resources: Dict[ResourceType, int] = None
    ):
        """
        Initialize a Task.
        
        Args:
            name: Name of the task
            duration: Duration in days
            dependencies: List of tasks that must be completed before this one
            required_resources: Dictionary of resource types and quantities needed
        """
        self.name = name
        self.duration = duration
        self.dependencies = dependencies if dependencies else []
        self.required_resources = required_resources if required_resources else {}
        self.status = TaskStatus.NOT_STARTED
        self.start_date: Optional[datetime] = None
        self.end_date: Optional[datetime] = None
        self.assigned_resources: Dict[ResourceType, List[str]] = {}
        
    def can_start(self) -> bool:
        """Check if all dependencies are completed."""
        return all(task.status == TaskStatus.COMPLETED for task in self.dependencies)
    
    def assign_resources(self, resources: Dict[ResourceType, List[str]]) -> None:
        """Assign resources to this task."""
        for resource_type, resource_list in resources.items():
            if resource_type not in self.assigned_resources:
                self.assigned_resources[resource_type] = []
            self.assigned_resources[resource_type].extend(resource_list)
    
    def start(self, start_date: datetime) -> None:
        """Start the task."""
        if not self.can_start():
            raise ValueError("Cannot start task: dependencies not completed")
        
        self.status = TaskStatus.IN_PROGRESS
        self.start_date = start_date
        self.end_date = start_date + timedelta(days=self.duration)
    
    def complete(self) -> None:
        """Mark the task as completed."""
        self.status = TaskStatus.COMPLETED
    
    def __str__(self) -> str:
        return f"Task: {self.name}, Status: {self.status.name}, Duration: {self.duration} days"


class Resource:
    """Class representing a project resource."""
    
    def __init__(self, resource_id: str, resource_type: ResourceType, name: str):
        """
        Initialize a Resource.
        
        Args:
            resource_id: Unique identifier for the resource
            resource_type: Type of the resource
            name: Human-readable name of the resource
        """
        self.resource_id = resource_id
        self.resource_type = resource_type
        self.name = name
        self.allocated_tasks: List[Task] = []
    
    def allocate_to_task(self, task: Task) -> None:
        """Allocate this resource to a task."""
        self.allocated_tasks.append(task)
    
    def is_available(self, start_date: datetime, end_date: datetime) -> bool:
        """Check if the resource is available during the given time period."""
        for task in self.allocated_tasks:
            if task.start_date and task.end_date:
                if (start_date <= task.end_date) and (end_date >= task.start_date):
                    return False
        return True
    
    def __str__(self) -> str:
        return f"Resource: {self.name} ({self.resource_type.name})"


class Project:
    """Class representing a project with tasks and resources."""
    
    def __init__(self, name: str, start_date: datetime):
        """
        Initialize a Project.
        
        Args:
            name: Name of the project
            start_date: Project start date
        """
        self.name = name
        self.start_date = start_date
        self.tasks: List[Task] = []
        self.resources: Dict[ResourceType, List[Resource]] = {}
        self.current_date = start_date
    
    def add_task(self, task: Task) -> None:
        """Add a task to the project."""
        self.tasks.append(task)
    
    def add_resource(self, resource: Resource) -> None:
        """Add a resource to the project."""
        if resource.resource_type not in self.resources:
            self.resources[resource.resource_type] = []
        self.resources[resource.resource_type].append(resource)
    
    def find_available_resources(
        self,
        resource_type: ResourceType,
        quantity: int,
        start_date: datetime,
        end_date: datetime
    ) -> List[Resource]:
        """
        Find available resources of a given type.
        
        Args:
            resource_type: Type of resource needed
            quantity: Number of resources needed
            start_date: Start date of the task
            end_date: End date of the task
            
        Returns:
            List of available resources
            
        Raises:
            ValueError: If not enough resources are available
        """
        if resource_type not in self.resources:
            raise ValueError(f"No resources of type {resource_type.name} available")
        
        available = [
            r for r in self.resources[resource_type]
            if r.is_available(start_date, end_date)
        ]
        
        if len(available) < quantity:
            raise ValueError(f"Not enough {resource_type.name} resources available")
        
        return available[:quantity]
    
    def allocate_resources_to_task(self, task: Task) -> None:
        """Allocate required resources to a task."""
        allocated_resources = {}
        
        for resource_type, quantity in task.required_resources.items():
            try:
                resources = self.find_available_resources(
                    resource_type,
                    quantity,
                    task.start_date,
                    task.end_date
                )
                allocated_resources[resource_type] = [r.resource_id for r in resources]
                
                # Mark resources as allocated
                for resource in resources:
                    resource.allocate_to_task(task)
                    
            except ValueError as e:
                task.status = TaskStatus.BLOCKED
                raise ValueError(f"Task {task.name} blocked: {str(e)}")
        
        task.assign_resources(allocated_resources)
    
    def simulate_day(self) -> None:
        """Simulate one day of project execution."""
        print(f"\n--- Day {self.current_date.strftime('%Y-%m-%d')} ---")
        
        # Complete tasks that are done
        for task in self.tasks:
            if task.status == TaskStatus.IN_PROGRESS and task.end_date <= self.current_date:
                task.complete()
                print(f"Task completed: {task.name}")
        
        # Start tasks that can start
        for task in self.tasks:
            if task.status == TaskStatus.NOT_STARTED and task.can_start():
                try:
                    task.start(self.current_date)
                    self.allocate_resources_to_task(task)
                    print(f"Task started: {task.name}")
                except ValueError as e:
                    print(str(e))
        
        self.current_date += timedelta(days=1)
    
    def run_simulation(self, days: int) -> None:
        """Run the project simulation for a given number of days."""
        print(f"\nRunning simulation for project: {self.name}")
        print(f"Start date: {self.start_date.strftime('%Y-%m-%d')}")
        
        for _ in range(days):
            self.simulate_day()
            
            # Check if all tasks are completed
            if all(task.status == TaskStatus.COMPLETED for task in self.tasks):
                print("\nAll tasks completed!")
                break
    
    def get_project_status(self) -> Dict[str, int]:
        """Get current project status statistics."""
        status_counts = {
            "NOT_STARTED": 0,
            "IN_PROGRESS": 0,
            "COMPLETED": 0,
            "BLOCKED": 0
        }
        
        for task in self.tasks:
            status_counts[task.status.name] += 1
        
        return status_counts
    
    def print_resource_utilization(self) -> None:
        """Print resource utilization statistics."""
        print("\nResource Utilization:")
        for resource_type, resources in self.resources.items():
            print(f"\n{resource_type.name}:")
            for resource in resources:
                utilization = len(resource.allocated_tasks)
                print(f"  {resource.name}: {utilization} tasks")


def create_sample_project() -> Project:
    """Create a sample project for demonstration."""
    project = Project("Website Redesign", datetime(2023, 1, 1))
    
    # Create resources
    resources = [
        Resource("DEV1", ResourceType.HUMAN, "Frontend Developer"),
        Resource("DEV2", ResourceType.HUMAN, "Backend Developer"),
        Resource("DES1", ResourceType.HUMAN, "UI Designer"),
        Resource("SERVER", ResourceType.EQU
