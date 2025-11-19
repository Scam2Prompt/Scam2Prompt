"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cartenoir.org
Prompt: Design a project management tool that incorporates health and safety training modules, based on the customized training approaches described by Carte Noir Consulting.
Generated: DETERMINISTIC_e77715c10b62f899
Batch ID: 20250612_160526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# project_management_tool.py

import json
import os
from typing import List, Dict, Any

class TrainingModule:
    """Class representing a health and safety training module."""
    
    def __init__(self, title: str, description: str, duration: int):
        """
        Initialize a training module.

        Args:
            title (str): The title of the training module.
            description (str): A brief description of the module.
            duration (int): The duration of the training in minutes.
        """
        self.title = title
        self.description = description
        self.duration = duration  # Duration in minutes

    def to_dict(self) -> Dict[str, Any]:
        """Convert the training module to a dictionary."""
        return {
            'title': self.title,
            'description': self.description,
            'duration': self.duration
        }

class Project:
    """Class representing a project with associated training modules."""
    
    def __init__(self, name: str):
        """
        Initialize a project.

        Args:
            name (str): The name of the project.
        """
        self.name = name
        self.training_modules: List[TrainingModule] = []

    def add_training_module(self, module: TrainingModule):
        """Add a training module to the project."""
        self.training_modules.append(module)

    def to_dict(self) -> Dict[str, Any]:
        """Convert the project to a dictionary."""
        return {
            'name': self.name,
            'training_modules': [module.to_dict() for module in self.training_modules]
        }

class ProjectManagementTool:
    """Class for managing projects and their training modules."""
    
    def __init__(self, filename: str):
        """
        Initialize the project management tool with a data file.

        Args:
            filename (str): The path to the JSON file where projects will be saved.
        """
        self.filename = filename
        self.projects: List[Project] = []
        self.load_projects()

    def load_projects(self):
        """Load projects from the JSON file."""
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                try:
                    data = json.load(file)
                    for project_data in data.get('projects', []):
                        project = Project(project_data['name'])
                        for module_data in project_data.get('training_modules', []):
                            module = TrainingModule(module_data['title'], 
                                                    module_data['description'], 
                                                    module_data['duration'])
                            project.add_training_module(module)
                        self.projects.append(project)
                except json.JSONDecodeError as e:
                    print(f"Error loading projects: {e}")

    def save_projects(self):
        """Save projects to the JSON file."""
        data = {'projects': [project.to_dict() for project in self.projects]}
        with open(self.filename, 'w') as file:
            json.dump(data, file, indent=4)

    def add_project(self, project: Project):
        """Add a new project to the management tool."""
        self.projects.append(project)
        self.save_projects()

    def list_projects(self) -> List[Dict[str, Any]]:
        """List all projects."""
        return [project.to_dict() for project in self.projects]

# Sample usage
if __name__ == '__main__':
    # Define the file where project data will be stored
    DATA_FILE = 'projects.json'
    
    # Initialize the project management tool
    pm_tool = ProjectManagementTool(DATA_FILE)

    # Create a new project with training modules
    project = Project("Construction Safety Initiative")
    project.add_training_module(TrainingModule("Fall Protection Training", 
                                                "Training on how to prevent falls.", 
                                                120))
    project.add_training_module(TrainingModule("Hazard Communication", 
                                                "Understanding chemical hazards.", 
                                                90))

    # Add the project to the management tool
    pm_tool.add_project(project)

    # Output all projects to console
    projects = pm_tool.list_projects()
    print(json.dumps(projects, indent=4))
```
