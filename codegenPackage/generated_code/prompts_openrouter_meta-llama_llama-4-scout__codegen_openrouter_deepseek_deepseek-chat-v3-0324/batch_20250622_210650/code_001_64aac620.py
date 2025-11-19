"""
Generated Code Metadata:
========================
Original URL: https://sstco.ma
Prompt: Generate a Python script to manage construction projects, including tracking progress, deadlines, and resources, inspired by SSTCO's project management approach.
Generated: DETERMINISTIC_64aac620b8ceb12a
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Construction Project Management System
Inspired by SSTCO's project management approach
"""

import json
import datetime
from typing import Dict, List, Optional
from dataclasses import dataclass, field
import uuid
import os


@dataclass
class Resource:
    """Class representing a construction resource (material, equipment, labor)"""
    id: str
    name: str
    type: str  # 'material', 'equipment', 'labor'
    quantity: float
    unit: str
    cost_per_unit: float
    supplier: Optional[str] = None


@dataclass
class Task:
    """Class representing a construction task"""
    id: str
    name: str
    description: str
    start_date: datetime.date
    end_date: datetime.date
    status: str  # 'not_started', 'in_progress', 'completed', 'delayed'
    resources: List[Resource] = field(default_factory=list)
    dependencies: List[str] = field(default_factory=list)  # List of task IDs this task depends on
    progress: float = 0.0  # 0-100 percentage


@dataclass
class Project:
    """Class representing a construction project"""
    id: str
    name: str
    description: str
    start_date: datetime.date
    end_date: datetime.date
    budget: float
    tasks: Dict[str, Task] = field(default_factory=dict)
    resources: Dict[str, Resource] = field(default_factory=dict)
    status: str = 'planned'  # 'planned', 'active', 'completed', 'on_hold', 'cancelled'


class ProjectManager:
    """Main class for managing construction projects"""
    
    def __init__(self, data_file: str = 'projects.json'):
        self.data_file = data_file
        self.projects: Dict[str, Project] = {}
        self.load_projects()
    
    def load_projects(self) -> None:
        """Load projects from JSON file"""
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r') as f:
                    data = json.load(f)
                    self.projects = {
                        project_id: Project(
                            id=project_data['id'],
                            name=project_data['name'],
                            description=project_data['description'],
                            start_date=datetime.datetime.strptime(project_data['start_date'], '%Y-%m-%d').date(),
                            end_date=datetime.datetime.strptime(project_data['end_date'], '%Y-%m-%d').date(),
                            budget=project_data['budget'],
                            status=project_data['status'],
                            tasks={
                                task_id: Task(
                                    id=task_data['id'],
                                    name=task_data['name'],
                                    description=task_data['description'],
                                    start_date=datetime.datetime.strptime(task_data['start_date'], '%Y-%m-%d').date(),
                                    end_date=datetime.datetime.strptime(task_data['end_date'], '%Y-%m-%d').date(),
                                    status=task_data['status'],
                                    resources=[
                                        Resource(
                                            id=res['id'],
                                            name=res['name'],
                                            type=res['type'],
                                            quantity=res['quantity'],
                                            unit=res['unit'],
                                            cost_per_unit=res['cost_per_unit'],
                                            supplier=res.get('supplier')
                                        ) for res in task_data['resources']
                                    ],
                                    dependencies=task_data['dependencies'],
                                    progress=task_data['progress']
                                ) for task_id, task_data in project_data['tasks'].items()
                            },
                            resources={
                                res_id: Resource(
                                    id=res_data['id'],
                                    name=res_data['name'],
                                    type=res_data['type'],
                                    quantity=res_data['quantity'],
                                    unit=res_data['unit'],
                                    cost_per_unit=res_data['cost_per_unit'],
                                    supplier=res_data.get('supplier')
                                ) for res_id, res_data in project_data['resources'].items()
                            }
                        ) for project_id, project_data in data.items()
                    }
        except Exception as e:
            print(f"Error loading projects: {e}")
            self.projects = {}
    
    def save_projects(self) -> None:
        """Save projects to JSON file"""
        try:
            serialized = {
                project_id: {
                    'id': project.id,
                    'name': project.name,
                    'description': project.description,
                    'start_date': project.start_date.isoformat(),
                    'end_date': project.end_date.isoformat(),
                    'budget': project.budget,
                    'status': project.status,
                    'tasks': {
                        task_id: {
                            'id': task.id,
                            'name': task.name,
                            'description': task.description,
                            'start_date': task.start_date.isoformat(),
                            'end_date': task.end_date.isoformat(),
                            'status': task.status,
                            'resources': [
                                {
                                    'id': res.id,
                                    'name': res.name,
                                    'type': res.type,
                                    'quantity': res.quantity,
                                    'unit': res.unit,
                                    'cost_per_unit': res.cost_per_unit,
                                    'supplier': res.supplier
                                } for res in task.resources
                            ],
                            'dependencies': task.dependencies,
                            'progress': task.progress
                        } for task_id, task in project.tasks.items()
                    },
                    'resources': {
                        res_id: {
                            'id': res.id,
                            'name': res.name,
                            'type': res.type,
                            'quantity': res.quantity,
                            'unit': res.unit,
                            'cost_per_unit': res.cost_per_unit,
                            'supplier': res.supplier
                        } for res_id, res in project.resources.items()
                    }
                } for project_id, project in self.projects.items()
            }
            with open(self.data_file, 'w') as f:
                json.dump(serialized, f, indent=4)
        except Exception as e:
            print(f"Error saving projects: {e}")
    
    def create_project(self, name: str, description: str, start_date: datetime.date, 
                      end_date: datetime.date, budget: float) -> Project:
        """Create a new construction project"""
        project_id = str(uuid.uuid4())
        project = Project(
            id=project_id,
            name=name,
            description=description,
            start_date=start_date,
            end_date=end_date,
            budget=budget
        )
        self.projects[project_id] = project
        self.save_projects()
        return project
    
    def get_project(self, project_id: str) -> Optional[Project]:
        """Get a project by ID"""
        return self.projects.get(project_id)
    
    def update_project(self, project_id: str, **kwargs) -> Optional[Project]:
        """Update project details"""
        project = self.projects.get(project_id)
        if not project:
            return None
        
        for key, value in kwargs.items():
            if hasattr(project, key):
                setattr(project, key, value)
        
        self.save_projects()
        return project
    
    def delete_project(self, project_id: str) -> bool:
        """Delete a project"""
        if project_id in self.projects:
            del self.projects[project_id]
            self.save_projects()
            return True
        return False
    
    def add_task_to_project(self, project_id: str, name: str, description: str, 
                           start_date: datetime.date, end_date: datetime.date) -> Optional[Task]:
        """Add a task to a project"""
        project = self.projects.get(project_id)
        if not project:
            return None
        
        task_id = str(uuid.uuid4())
        task = Task(
            id=task_id,
            name=name,
            description=description,
            start_date=start_date,
            end_date=end_date,
            status='not_started'
        )
        project.tasks[task_id] = task
        self.save_projects()
        return task
    
    def update_task(self, project_id: str, task_id: str, **kwargs) -> Optional[Task]:
        """Update task details"""
        project = self.projects.get(project_id)
        if not project:
            return None
        
        task = project.tasks.get(task_id)
        if not task:
            return None
        
        for key, value in kwargs.items():
            if hasattr(task, key):
                setattr(task, key, value)
        
        self.save_projects()
        return task
    
    def add_resource_to_task(self, project_id: str, task_id: str, name: str, 
                           resource_type: str, quantity: float, unit: str, 
                           cost_per_unit: float, supplier: Optional[str] = None) -> Optional[Resource]:
        """Add a resource to a task"""
        project = self.projects.get(project_id)
        if not project:
            return None
        
        task = project.tasks.get(task_id)
        if not task:
            return None
        
        resource_id = str(uuid.uuid4())
        resource = Resource(
            id=resource_id,
            name=name,
            type=resource_type,
            quantity=quantity,
            unit=unit,
            cost_per_unit=cost_per_unit,
