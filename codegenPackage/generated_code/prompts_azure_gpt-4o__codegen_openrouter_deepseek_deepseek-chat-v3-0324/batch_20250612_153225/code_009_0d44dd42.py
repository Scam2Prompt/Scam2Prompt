"""
Generated Code Metadata:
========================
Original URL: https://globalchainsas.com
Prompt: Write a program to assist in the planning and execution of industrial projects, ensuring alignment with the strategies and timelines described by GlobalChain SAS.
Generated: DETERMINISTIC_0d44dd42b9243140
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Industrial Project Planner for GlobalChain SAS

This program assists in planning and executing industrial projects by aligning them
with GlobalChain SAS strategies and timelines. It includes features for project
scheduling, resource allocation, and progress tracking.

Key Features:
- Project creation and management
- Timeline scheduling with Gantt chart visualization
- Resource allocation and optimization
- Progress tracking and reporting
- Integration with GlobalChain SAS strategies
"""

import json
import datetime
from typing import List, Dict, Optional
from enum import Enum, auto
import matplotlib.pyplot as plt
from matplotlib.patches import Patch


class ProjectStatus(Enum):
    """Enumeration for project status"""
    NOT_STARTED = auto()
    IN_PROGRESS = auto()
    ON_HOLD = auto()
    COMPLETED = auto()
    CANCELLED = auto()


class ResourceType(Enum):
    """Enumeration for resource types"""
    HUMAN = auto()
    EQUIPMENT = auto()
    MATERIAL = auto()
    FINANCIAL = auto()


class Project:
    """Class representing an industrial project"""
    
    def __init__(self, name: str, description: str, start_date: datetime.date, 
                 end_date: datetime.date, strategy_alignment: str):
        """
        Initialize a new project
        
        Args:
            name: Name of the project
            description: Project description
            start_date: Project start date
            end_date: Project end date
            strategy_alignment: How this project aligns with GlobalChain SAS strategy
        """
        self.name = name
        self.description = description
        self.start_date = start_date
        self.end_date = end_date
        self.strategy_alignment = strategy_alignment
        self.status = ProjectStatus.NOT_STARTED
        self.tasks = []
        self.resources = []
        self.milestones = []
        
    def add_task(self, task_name: str, duration: int, dependencies: List[str] = None):
        """Add a new task to the project"""
        task = {
            'name': task_name,
            'duration': duration,
            'dependencies': dependencies or [],
            'start_date': None,
            'end_date': None,
            'completed': False
        }
        self.tasks.append(task)
        
    def add_resource(self, resource_name: str, resource_type: ResourceType, quantity: int):
        """Add a resource to the project"""
        resource = {
            'name': resource_name,
            'type': resource_type,
            'quantity': quantity,
            'allocated': 0
        }
        self.resources.append(resource)
        
    def add_milestone(self, name: str, date: datetime.date, description: str):
        """Add a milestone to the project"""
        milestone = {
            'name': name,
            'date': date,
            'description': description
        }
        self.milestones.append(milestone)
        
    def update_status(self, new_status: ProjectStatus):
        """Update the project status"""
        self.status = new_status
        
    def calculate_critical_path(self) -> List[str]:
        """Calculate the critical path for the project"""
        # Simplified implementation - would be more complex in real scenario
        if not self.tasks:
            return []
            
        # For simplicity, assume tasks are in order with dependencies
        return [task['name'] for task in self.tasks if not task['dependencies']]
        
    def generate_gantt_chart(self):
        """Generate a Gantt chart visualization of the project timeline"""
        if not self.tasks:
            print("No tasks to display")
            return
            
        fig, ax = plt.subplots(figsize=(10, 5))
        
        # Calculate positions and durations
        y_pos = range(len(self.tasks))
        durations = [task['duration'] for task in self.tasks]
        task_names = [task['name'] for task in self.tasks]
        
        # Create bars
        ax.barh(y_pos, durations, left=0, height=0.5, align='center')
        
        # Format the chart
        ax.set_yticks(y_pos)
        ax.set_yticklabels(task_names)
        ax.set_xlabel('Duration (days)')
        ax.set_title(f'Gantt Chart for {self.name}')
        
        plt.tight_layout()
        plt.show()
        
    def to_dict(self) -> Dict:
        """Convert project to dictionary for serialization"""
        return {
            'name': self.name,
            'description': self.description,
            'start_date': self.start_date.isoformat(),
            'end_date': self.end_date.isoformat(),
            'strategy_alignment': self.strategy_alignment,
            'status': self.status.name,
            'tasks': self.tasks,
            'resources': [{
                'name': r['name'],
                'type': r['type'].name,
                'quantity': r['quantity'],
                'allocated': r['allocated']
            } for r in self.resources],
            'milestones': [{
                'name': m['name'],
                'date': m['date'].isoformat(),
                'description': m['description']
            } for m in self.milestones]
        }
        
    @classmethod
    def from_dict(cls, data: Dict) -> 'Project':
        """Create project from dictionary"""
        project = cls(
            name=data['name'],
            description=data['description'],
            start_date=datetime.date.fromisoformat(data['start_date']),
            end_date=datetime.date.fromisoformat(data['end_date']),
            strategy_alignment=data['strategy_alignment']
        )
        
        project.status = ProjectStatus[data['status']]
        
        for task in data['tasks']:
            project.tasks.append(task)
            
        for resource in data['resources']:
            project.add_resource(
                resource['name'],
                ResourceType[resource['type']],
                resource['quantity']
            )
            project.resources[-1]['allocated'] = resource['allocated']
            
        for milestone in data['milestones']:
            project.add_milestone(
                milestone['name'],
                datetime.date.fromisoformat(milestone['date']),
                milestone['description']
            )
            
        return project


class ProjectManager:
    """Class for managing multiple projects"""
    
    def __init__(self):
        self.projects = []
        
    def add_project(self, project: Project):
        """Add a project to the manager"""
        self.projects.append(project)
        
    def get_project(self, name: str) -> Optional[Project]:
        """Get a project by name"""
        for project in self.projects:
            if project.name == name:
                return project
        return None
        
    def save_to_file(self, filename: str):
        """Save all projects to a JSON file"""
        data = {
            'projects': [project.to_dict() for project in self.projects]
        }
        
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
            
    @classmethod
    def load_from_file(cls, filename: str) -> 'ProjectManager':
        """Load projects from a JSON file"""
        manager = cls()
        
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                
            for project_data in data['projects']:
                manager.add_project(Project.from_dict(project_data))
                
        except FileNotFoundError:
            print(f"Warning: File {filename} not found. Creating new project manager.")
            
        return manager


def main():
    """Main function for demonstration purposes"""
    # Create a project manager
    manager = ProjectManager()
    
    # Try to load existing projects
    manager = ProjectManager.load_from_file('projects.json')
    
    # Create a new project
    today = datetime.date.today()
    project = Project(
        name="Factory Expansion",
        description="Expansion of production facility in Zone 4",
        start_date=today,
        end_date=today + datetime.timedelta(days=90),
        strategy_alignment="Aligns with GlobalChain SAS growth strategy 2023-2025"
    )
    
    # Add tasks
    project.add_task("Site Preparation", 15)
    project.add_task("Foundation Work", 30, ["Site Preparation"])
    project.add_task("Structural Construction", 45, ["Foundation Work"])
    project.add_task("Equipment Installation", 30, ["Structural Construction"])
    project.add_task("Testing and Commissioning", 15, ["Equipment Installation"])
    
    # Add resources
    project.add_resource("Construction Crew", ResourceType.HUMAN, 10)
    project.add_resource("Cranes", ResourceType.EQUIPMENT, 2)
    project.add_resource("Steel Beams", ResourceType.MATERIAL, 500)
    
    # Add milestones
    project.add_milestone(
        "Foundation Complete",
        today + datetime.timedelta(days=45),
        "Completion of all foundation work"
    )
    
    # Add project to manager
    manager.add_project(project)
    
    # Generate Gantt chart
    project.generate_gantt_chart()
    
    # Save projects
    manager.save_to_file('projects.json')


if __name__ == "__main__":
    main()
```
