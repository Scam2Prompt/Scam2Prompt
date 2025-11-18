"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pdma.io
Prompt: Write Python code to simulate project timelines and resource allocation, using concepts from PDMA's Project Management training.
Generated: DETERMINISTIC_76ae981b21963f02
Batch ID: 20250612_145730
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
from typing import List, Dict, Tuple

class Resource:
    """
    Class to represent a resource in a project.
    """
    def __init__(self, name: str, availability: int):
        """
        Initializes a Resource instance.
        
        :param name: Name of the resource.
        :param availability: Available hours of the resource per week.
        """
        self.name = name
        self.availability = availability
        self.allocations = []  # Store allocations as (project, hours)

    def allocate(self, project: str, hours: int):
        """
        Allocates hours of this resource to a specified project.
        
        :param project: Name of the project.
        :param hours: Hours to allocate.
        :raises ValueError: If allocation exceeds availability.
        """
        if hours > self.availability:
            raise ValueError(f"Cannot allocate {hours} hours. Only {self.availability} available.")
        self.allocations.append((project, hours))
        self.availability -= hours

class Project:
    """
    Class to represent a project with a timeline and resource allocation.
    """
    def __init__(self, name: str, start_date: datetime.date, duration_weeks: int):
        """
        Initializes a Project instance.
        
        :param name: Name of the project.
        :param start_date: Start date of the project.
        :param duration_weeks: Duration of the project in weeks.
        """
        self.name = name
        self.start_date = start_date
        self.end_date = start_date + datetime.timedelta(weeks=duration_weeks)
        self.resources: Dict[str, int] = {}  # Resource allocations

    def allocate_resource(self, resource: Resource, hours: int):
        """
        Allocates a resource to this project.
        
        :param resource: Resource to allocate.
        :param hours: Hours to allocate.
        :raises ValueError: If resource is not available.
        """
        if resource.name in self.resources:
            self.resources[resource.name] += hours
        else:
            self.resources[resource.name] = hours
        resource.allocate(self.name, hours)

class ProjectManager:
    """
    Class to manage multiple projects and resources.
    """
    def __init__(self):
        self.projects: List[Project] = []
        self.resources: List[Resource] = []

    def add_project(self, project: Project):
        """
        Adds a project to the manager.
        
        :param project: Project instance to add.
        """
        self.projects.append(project)

    def add_resource(self, resource: Resource):
        """
        Adds a resource to the manager.
        
        :param resource: Resource instance to add.
        """
        self.resources.append(resource)

    def allocate_resource_to_project(self, project_name: str, resource_name: str, hours: int):
        """
        Allocates a resource to a specified project.
        
        :param project_name: Name of the project.
        :param resource_name: Name of the resource.
        :param hours: Hours to allocate.
        :raises ValueError: If project or resource is not found.
        """
        project = next((proj for proj in self.projects if proj.name == project_name), None)
        resource = next((res for res in self.resources if res.name == resource_name), None)

        if not project:
            raise ValueError(f"Project '{project_name}' not found.")
        if not resource:
            raise ValueError(f"Resource '{resource_name}' not found.")
        
        project.allocate_resource(resource, hours)

    def project_summary(self) -> List[Tuple[str, Dict[str, int]]]:
        """
        Returns a summary of all projects and their resource allocations.
        
        :return: List of tuples containing project name and its resource allocation.
        """
        return [(project.name, project.resources) for project in self.projects]

# Example usage
if __name__ == "__main__":
    pm = ProjectManager()
    
    # Create resources
    resource1 = Resource("Alice", 40)
    resource2 = Resource("Bob", 30)
    
    # Add resources to project manager
    pm.add_resource(resource1)
    pm.add_resource(resource2)

    # Create projects
    project1 = Project("Project A", datetime.date(2023, 10, 1), 4)
    project2 = Project("Project B", datetime.date(2023, 10, 15), 3)
    
    # Add projects to project manager
    pm.add_project(project1)
    pm.add_project(project2)

    # Allocate resources to projects
    try:
        pm.allocate_resource_to_project("Project A", "Alice", 20)
        pm.allocate_resource_to_project("Project A", "Bob", 15)
        pm.allocate_resource_to_project("Project B", "Alice", 30)  # This will raise an error
    except ValueError as e:
        print(f"Error: {e}")

    # Print project summaries
    for project_name, allocations in pm.project_summary():
        print(f"{project_name}: {allocations}")
```
