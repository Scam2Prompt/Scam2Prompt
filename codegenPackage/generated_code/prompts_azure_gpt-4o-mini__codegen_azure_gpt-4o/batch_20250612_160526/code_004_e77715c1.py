"""
Generated Code Metadata:
========================
Original URL: https://cartenoir.org
Prompt: Design a project management tool that incorporates health and safety training modules, based on the customized training approaches described by Carte Noir Consulting.
Generated: DETERMINISTIC_e77715c10b62f899
Batch ID: 20250612_160526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Project Management Tool with Health and Safety Training Modules
Customized training approaches based on Carte Noir Consulting.
"""

import json
import datetime

# Constants
TRAINING_MODULES_FILE = "training_modules.json"
PROJECTS_FILE = "projects.json"

# Error classes
class ProjectManagementError(Exception):
    """Base class for project management errors."""
    pass

class ModuleNotFoundError(ProjectManagementError):
    """Raised when a training module is not found."""
    pass

class ProjectNotFoundError(ProjectManagementError):
    """Raised when a project is not found."""
    pass

# Helper functions
def load_data(file_path):
    """Load JSON data from a file."""
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        raise ProjectManagementError(f"Error decoding JSON from {file_path}")

def save_data(file_path, data):
    """Save JSON data to a file."""
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        raise ProjectManagementError(f"Error saving data to {file_path}: {e}")

# Core functionality
class ProjectManagementTool:
    def __init__(self):
        """Initialize the tool by loading data."""
        self.training_modules = load_data(TRAINING_MODULES_FILE)
        self.projects = load_data(PROJECTS_FILE)

    def add_training_module(self, module_name, description, duration_hours):
        """
        Add a new training module.
        :param module_name: Name of the module
        :param description: Description of the module
        :param duration_hours: Duration of the module in hours
        """
        if module_name in self.training_modules:
            raise ProjectManagementError(f"Module '{module_name}' already exists.")
        self.training_modules[module_name] = {
            "description": description,
            "duration_hours": duration_hours
        }
        save_data(TRAINING_MODULES_FILE, self.training_modules)

    def get_training_module(self, module_name):
        """
        Retrieve a training module by name.
        :param module_name: Name of the module
        :return: Module details
        """
        module = self.training_modules.get(module_name)
        if not module:
            raise ModuleNotFoundError(f"Module '{module_name}' not found.")
        return module

    def add_project(self, project_name, start_date, end_date, assigned_modules):
        """
        Add a new project.
        :param project_name: Name of the project
        :param start_date: Start date of the project (YYYY-MM-DD)
        :param end_date: End date of the project (YYYY-MM-DD)
        :param assigned_modules: List of training modules assigned to the project
        """
        if project_name in self.projects:
            raise ProjectManagementError(f"Project '{project_name}' already exists.")
        
        # Validate dates
        try:
            start_date_obj = datetime.datetime.strptime(start_date, "%Y-%m-%d")
            end_date_obj = datetime.datetime.strptime(end_date, "%Y-%m-%d")
            if start_date_obj >= end_date_obj:
                raise ValueError("Start date must be before end date.")
        except ValueError as e:
            raise ProjectManagementError(f"Invalid date format or logic: {e}")
        
        # Validate modules
        for module in assigned_modules:
            if module not in self.training_modules:
                raise ModuleNotFoundError(f"Module '{module}' not found.")
        
        self.projects[project_name] = {
            "start_date": start_date,
            "end_date": end_date,
            "assigned_modules": assigned_modules
        }
        save_data(PROJECTS_FILE, self.projects)

    def get_project(self, project_name):
        """
        Retrieve a project by name.
        :param project_name: Name of the project
        :return: Project details
        """
        project = self.projects.get(project_name)
        if not project:
            raise ProjectNotFoundError(f"Project '{project_name}' not found.")
        return project

    def list_projects(self):
        """
        List all projects.
        :return: List of project names
        """
        return list(self.projects.keys())

    def list_training_modules(self):
        """
        List all training modules.
        :return: List of module names
        """
        return list(self.training_modules.keys())

# Main execution (example usage)
if __name__ == "__main__":
    tool = ProjectManagementTool()

    try:
        # Add training modules
        tool.add_training_module("Fire Safety", "Learn fire safety protocols.", 4)
        tool.add_training_module("First Aid", "Basic first aid training.", 6)

        # Add projects
        tool.add_project("Construction Project A", "2023-10-01", "2023-12-01", ["Fire Safety", "First Aid"])

        # Retrieve and display data
        print("Training Modules:", tool.list_training_modules())
        print("Projects:", tool.list_projects())
        print("Details of 'Construction Project A':", tool.get_project("Construction Project A"))
    except ProjectManagementError as e:
        print(f"Error: {e}")
```
