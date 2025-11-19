"""
Generated Code Metadata:
========================
Original URL: https://braavos.rs
Prompt: Write a Python script to create a simple project management tool for architectural firms like Études, including features for task assignment and resource allocation.
Generated: DETERMINISTIC_7ced2f7da4eabe7e
Batch ID: 20250622_205158
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
from typing import List, Dict, Optional

class Project:
    """Represents an architectural project."""
    
    def __init__(self, name: str, description: str, start_date: str, end_date: str):
        self.name = name
        self.description = description
        self.start_date = start_date
        self.end_date = end_date
        self.tasks: List[Task] = []
        self.resources: List[Resource] = []
    
    def add_task(self, task: 'Task') -> None:
        """Add a task to the project."""
        self.tasks.append(task)
    
    def add_resource(self, resource: 'Resource') -> None:
        """Add a resource to the project."""
        self.resources.append(resource)
    
    def get_project_details(self) -> Dict:
        """Return project details as a dictionary."""
        return {
            'name': self.name,
            'description': self.description,
            'start_date': self.start_date,
            'end_date': self.end_date,
            'tasks': [task.get_task_details() for task in self.tasks],
            'resources': [resource.get_resource_details() for resource in self.resources]
        }

class Task:
    """Represents a task in a project."""
    
    def __init__(self, name: str, description: str, assigned_to: str, deadline: str, status: str = 'Not Started'):
        self.name = name
        self.description = description
        self.assigned_to = assigned_to
        self.deadline = deadline
        self.status = status
    
    def update_status(self, new_status: str) -> None:
        """Update the status of the task."""
        valid_statuses = ['Not Started', 'In Progress', 'Completed', 'Blocked']
        if new_status in valid_statuses:
            self.status = new_status
        else:
            raise ValueError(f"Invalid status. Must be one of: {valid_statuses}")
    
    def get_task_details(self) -> Dict:
        """Return task details as a dictionary."""
        return {
            'name': self.name,
            'description': self.description,
            'assigned_to': self.assigned_to,
            'deadline': self.deadline,
            'status': self.status
        }

class Resource:
    """Represents a resource (person or equipment) in a project."""
    
    def __init__(self, name: str, resource_type: str, availability: str):
        self.name = name
        self.resource_type = resource_type
        self.availability = availability
    
    def get_resource_details(self) -> Dict:
        """Return resource details as a dictionary."""
        return {
            'name': self.name,
            'type': self.resource_type,
            'availability': self.availability
        }

class ProjectManager:
    """Manages multiple architectural projects."""
    
    def __init__(self):
        self.projects: Dict[str, Project] = {}
    
    def create_project(self, name: str, description: str, start_date: str, end_date: str) -> Project:
        """Create and add a new project."""
        if name in self.projects:
            raise ValueError("Project with this name already exists.")
        
        project = Project(name, description, start_date, end_date)
        self.projects[name] = project
        return project
    
    def get_project(self, name: str) -> Optional[Project]:
        """Get a project by name."""
        return self.projects.get(name)
    
    def save_to_file(self, filename: str) -> None:
        """Save all projects to a JSON file."""
        projects_data = {
            'projects': [
                project.get_project_details() 
                for project in self.projects.values()
            ]
        }
        
        with open(filename, 'w') as f:
            json.dump(projects_data, f, indent=4)
    
    def load_from_file(self, filename: str) -> None:
        """Load projects from a JSON file."""
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
            
            for project_data in data['projects']:
                project = Project(
                    project_data['name'],
                    project_data['description'],
                    project_data['start_date'],
                    project_data['end_date']
                )
                
                for task_data in project_data['tasks']:
                    task = Task(
                        task_data['name'],
                        task_data['description'],
                        task_data['assigned_to'],
                        task_data['deadline'],
                        task_data['status']
                    )
                    project.add_task(task)
                
                for resource_data in project_data['resources']:
                    resource = Resource(
                        resource_data['name'],
                        resource_data['type'],
                        resource_data['availability']
                    )
                    project.add_resource(resource)
                
                self.projects[project.name] = project
                
        except FileNotFoundError:
            raise FileNotFoundError("The specified file does not exist.")
        except json.JSONDecodeError:
            raise ValueError("The file contains invalid JSON data.")
        except KeyError as e:
            raise KeyError(f"Missing required field in JSON data: {e}")

def main():
    """Demonstrate the project management tool."""
    manager = ProjectManager()
    
    # Create a project
    try:
        project = manager.create_project(
            "Études Office Building",
            "Design and construction of new office building",
            "2023-01-01",
            "2024-06-30"
        )
        
        # Add tasks
        project.add_task(Task(
            "Initial Design",
            "Create initial architectural drawings",
            "Lead Architect",
            "2023-03-15"
        ))
        
        project.add_task(Task(
            "Permit Approval",
            "Obtain construction permits",
            "Project Manager",
            "2023-04-30"
        ))
        
        # Add resources
        project.add_resource(Resource(
            "Lead Architect",
            "Personnel",
            "Full-time"
        ))
        
        project.add_resource(Resource(
            "3D Modeling Software",
            "Software",
            "Licensed"
        ))
        
        # Save to file
        manager.save_to_file("projects.json")
        print("Project saved successfully.")
        
        # Load from file
        new_manager = ProjectManager()
        new_manager.load_from_file("projects.json")
        loaded_project = new_manager.get_project("Études Office Building")
        
        if loaded_project:
            print("\nLoaded Project Details:")
            print(json.dumps(loaded_project.get_project_details(), indent=4))
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
