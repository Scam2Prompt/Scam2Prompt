"""
Generated Code Metadata:
========================
Original URL: https://harda-ke.org
Prompt: Design an algorithm for resource allocation in agriculture and food security projects, taking into account HARDA's experience in the Horn of Africa.
Generated: DETERMINISTIC_93866e7edb5b38ab
Batch ID: 20250622_211610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
from typing import List, Dict, Tuple
from enum import Enum

class ResourceType(Enum):
    """Enumeration of different types of agricultural resources"""
    SEEDS = 1
    FERTILIZER = 2
    IRRIGATION = 3
    LIVESTOCK = 4
    EQUIPMENT = 5
    TRAINING = 6

class Project:
    """Class representing an agricultural project"""
    def __init__(self, name: str, priority: int, required_resources: Dict[ResourceType, float]):
        self.name = name
        self.priority = priority
        self.required_resources = required_resources
        self.allocated_resources = {rtype: 0.0 for rtype in ResourceType}

class ResourceAllocator:
    """Algorithm for allocating resources to agricultural projects"""
    
    def __init__(self, available_resources: Dict[ResourceType, float]):
        self.available_resources = available_resources.copy()
        self.projects: List[Project] = []
    
    def add_project(self, project: Project) -> None:
        """Add a project to the allocation system"""
        self.projects.append(project)
    
    def allocate_resources(self) -> Dict[str, Dict[ResourceType, float]]:
        """
        Allocate resources to projects based on priority and available resources
        Returns a dictionary of allocation results
        """
        if not self.projects:
            raise ValueError("No projects to allocate resources to")
        
        # Sort projects by priority (higher priority first)
        sorted_projects = sorted(self.projects, key=lambda p: p.priority, reverse=True)
        
        allocation_results = {}
        
        for project in sorted_projects:
            allocation = {}
            for rtype, amount in project.required_resources.items():
                if rtype not in self.available_resources:
                    raise ValueError(f"Resource type {rtype} not available in allocator")
                
                # Allocate as much as possible without exceeding available resources
                allocated = min(amount, self.available_resources[rtype])
                allocation[rtype] = allocated
                self.available_resources[rtype] -= allocated
                project.allocated_resources[rtype] = allocated
            
            allocation_results[project.name] = allocation
        
        return allocation_results
    
    def get_remaining_resources(self) -> Dict[ResourceType, float]:
        """Return the remaining available resources after allocation"""
        return self.available_resources.copy()

# Example usage
if __name__ == "__main__":
    try:
        # Initialize available resources (example values)
        available_resources = {
            ResourceType.SEEDS: 1000.0,      # kg
            ResourceType.FERTILIZER: 500.0,  # kg
            ResourceType.IRRIGATION: 200.0,  # liters
            ResourceType.LIVESTOCK: 50.0,    # animals
            ResourceType.EQUIPMENT: 20.0,    # units
            ResourceType.TRAINING: 10.0      # sessions
        }
        
        allocator = ResourceAllocator(available_resources)
        
        # Add projects (example projects)
        project1 = Project(
            "Drought-resistant crops",
            priority=3,
            required_resources={
                ResourceType.SEEDS: 400.0,
                ResourceType.FERTILIZER: 200.0,
                ResourceType.IRRIGATION: 100.0,
                ResourceType.TRAINING: 4.0
            }
        )
        
        project2 = Project(
            "Livestock development",
            priority=2,
            required_resources={
                ResourceType.LIVESTOCK: 30.0,
                ResourceType.EQUIPMENT: 10.0,
                ResourceType.TRAINING: 3.0
            }
        )
        
        project3 = Project(
            "Community irrigation",
            priority=1,
            required_resources={
                ResourceType.IRRIGATION: 150.0,
                ResourceType.EQUIPMENT: 15.0
            }
        )
        
        allocator.add_project(project1)
        allocator.add_project(project2)
        allocator.add_project(project3)
        
        # Perform allocation
        results = allocator.allocate_resources()
        
        # Print results
        print("Resource Allocation Results:")
        for project_name, allocation in results.items():
            print(f"\nProject: {project_name}")
            for rtype, amount in allocation.items():
                print(f"  {rtype.name}: {amount}")
        
        print("\nRemaining Resources:")
        remaining = allocator.get_remaining_resources()
        for rtype, amount in remaining.items():
            print(f"  {rtype.name}: {amount}")
            
    except ValueError as e:
        print(f"Error in resource allocation: {e}")
```
