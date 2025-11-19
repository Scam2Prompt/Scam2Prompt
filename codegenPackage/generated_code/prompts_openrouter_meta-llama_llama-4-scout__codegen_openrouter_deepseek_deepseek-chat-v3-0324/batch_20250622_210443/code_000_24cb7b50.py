"""
Generated Code Metadata:
========================
Original URL: https://uaeinterior.com
Prompt: Write a Python script to manage interior design projects, including client information, project spaces, and budget planning, inspired by the services offered by Amazing Interior in Abu Dhabi.
Generated: DETERMINISTIC_24cb7b501633dd92
Batch ID: 20250622_210443
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
from typing import Dict, List, Optional

class Client:
    """Represents a client for interior design projects."""
    
    def __init__(self, client_id: str, name: str, email: str, phone: str, address: str):
        """
        Initialize a new client.
        
        Args:
            client_id: Unique identifier for the client
            name: Client's full name
            email: Client's email address
            phone: Client's phone number
            address: Client's physical address
        """
        self.client_id = client_id
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address
    
    def to_dict(self) -> Dict:
        """Convert client data to dictionary for serialization."""
        return {
            'client_id': self.client_id,
            'name': self.name,
            'email': self.email,
            'phone': self.phone,
            'address': self.address
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'Client':
        """Create Client instance from dictionary."""
        return cls(
            client_id=data['client_id'],
            name=data['name'],
            email=data['email'],
            phone=data['phone'],
            address=data['address']
        )

class ProjectSpace:
    """Represents a space within an interior design project."""
    
    def __init__(self, space_id: str, name: str, area: float, description: str):
        """
        Initialize a new project space.
        
        Args:
            space_id: Unique identifier for the space
            name: Name of the space (e.g., 'Living Room')
            area: Area in square meters
            description: Description of the space
        """
        self.space_id = space_id
        self.name = name
        self.area = area
        self.description = description
    
    def to_dict(self) -> Dict:
        """Convert space data to dictionary for serialization."""
        return {
            'space_id': self.space_id,
            'name': self.name,
            'area': self.area,
            'description': self.description
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'ProjectSpace':
        """Create ProjectSpace instance from dictionary."""
        return cls(
            space_id=data['space_id'],
            name=data['name'],
            area=data['area'],
            description=data['description']
        )

class BudgetItem:
    """Represents a budget item for a project."""
    
    def __init__(self, item_id: str, name: str, category: str, estimated_cost: float, actual_cost: float = 0.0):
        """
        Initialize a new budget item.
        
        Args:
            item_id: Unique identifier for the item
            name: Name of the item
            category: Category (e.g., 'Furniture', 'Lighting')
            estimated_cost: Estimated cost
            actual_cost: Actual cost (defaults to 0)
        """
        self.item_id = item_id
        self.name = name
        self.category = category
        self.estimated_cost = estimated_cost
        self.actual_cost = actual_cost
    
    def to_dict(self) -> Dict:
        """Convert budget item data to dictionary for serialization."""
        return {
            'item_id': self.item_id,
            'name': self.name,
            'category': self.category,
            'estimated_cost': self.estimated_cost,
            'actual_cost': self.actual_cost
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'BudgetItem':
        """Create BudgetItem instance from dictionary."""
        return cls(
            item_id=data['item_id'],
            name=data['name'],
            category=data['category'],
            estimated_cost=data['estimated_cost'],
            actual_cost=data.get('actual_cost', 0.0)
        )

class InteriorProject:
    """Represents an interior design project."""
    
    def __init__(self, project_id: str, name: str, client: Client, start_date: str, end_date: str):
        """
        Initialize a new interior design project.
        
        Args:
            project_id: Unique identifier for the project
            name: Project name
            client: Client associated with the project
            start_date: Project start date (YYYY-MM-DD)
            end_date: Project end date (YYYY-MM-DD)
        """
        self.project_id = project_id
        self.name = name
        self.client = client
        self.start_date = start_date
        self.end_date = end_date
        self.spaces: List[ProjectSpace] = []
        self.budget_items: List[BudgetItem] = []
    
    def add_space(self, space: ProjectSpace) -> None:
        """Add a space to the project."""
        self.spaces.append(space)
    
    def add_budget_item(self, item: BudgetItem) -> None:
        """Add a budget item to the project."""
        self.budget_items.append(item)
    
    def get_total_estimated_cost(self) -> float:
        """Calculate total estimated cost of all budget items."""
        return sum(item.estimated_cost for item in self.budget_items)
    
    def get_total_actual_cost(self) -> float:
        """Calculate total actual cost of all budget items."""
        return sum(item.actual_cost for item in self.budget_items)
    
    def to_dict(self) -> Dict:
        """Convert project data to dictionary for serialization."""
        return {
            'project_id': self.project_id,
            'name': self.name,
            'client': self.client.to_dict(),
            'start_date': self.start_date,
            'end_date': self.end_date,
            'spaces': [space.to_dict() for space in self.spaces],
            'budget_items': [item.to_dict() for item in self.budget_items]
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'InteriorProject':
        """Create InteriorProject instance from dictionary."""
        project = cls(
            project_id=data['project_id'],
            name=data['name'],
            client=Client.from_dict(data['client']),
            start_date=data['start_date'],
            end_date=data['end_date']
        )
        project.spaces = [ProjectSpace.from_dict(space) for space in data.get('spaces', [])]
        project.budget_items = [BudgetItem.from_dict(item) for item in data.get('budget_items', [])]
        return project

class ProjectManager:
    """Manages interior design projects with persistence."""
    
    def __init__(self, data_file: str = 'projects.json'):
        """
        Initialize the project manager.
        
        Args:
            data_file: Path to JSON file for data persistence
        """
        self.data_file = data_file
        self.projects: Dict[str, InteriorProject] = {}
        self.load_projects()
    
    def add_project(self, project: InteriorProject) -> None:
        """Add a new project."""
        if project.project_id in self.projects:
            raise ValueError(f"Project with ID {project.project_id} already exists")
        self.projects[project.project_id] = project
        self.save_projects()
    
    def get_project(self, project_id: str) -> Optional[InteriorProject]:
        """Retrieve a project by ID."""
        return self.projects.get(project_id)
    
    def update_project(self, project: InteriorProject) -> None:
        """Update an existing project."""
        if project.project_id not in self.projects:
            raise ValueError(f"Project with ID {project.project_id} not found")
        self.projects[project.project_id] = project
        self.save_projects()
    
    def delete_project(self, project_id: str) -> None:
        """Delete a project."""
        if project_id not in self.projects:
            raise ValueError(f"Project with ID {project_id} not found")
        del self.projects[project_id]
        self.save_projects()
    
    def list_projects(self) -> List[InteriorProject]:
        """List all projects."""
        return list(self.projects.values())
    
    def save_projects(self) -> None:
        """Save projects to JSON file."""
        data = {
            'projects': [project.to_dict() for project in self.projects.values()]
        }
        with open(self.data_file, 'w') as f:
            json.dump(data, f, indent=2)
    
    def load_projects(self) -> None:
        """Load projects from JSON file."""
        if not os.path.exists(self.data_file):
            return
        
        with open(self.data_file, 'r') as f:
            try:
                data = json.load(f)
                self.projects = {
                    project['project_id']: InteriorProject.from_dict(project)
                    for project in data.get('projects', [])
                }
            except json.JSONDecodeError:
                raise ValueError("Invalid JSON data in projects file")

def generate_id(prefix: str = '') -> str:
    """Generate a unique ID with optional prefix."""
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    return f"{prefix}{timestamp}"

def main_menu(manager: ProjectManager) -> None:
    """Display the main menu and handle user input."""
    while True:
        print("\nInterior Design Project Management")
