"""
Generated Code Metadata:
========================
Original URL: https://stockyardrefacing.com
Prompt: "Write a Python script to manage a cabinet refacing project's timeline and costs, considering factors like material sourcing and labor hours, as discussed on stockyardrefacing.com."
Generated: DETERMINISTIC_5b77402dc8ee6bb0
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import json
import os
from typing import Dict, List, Optional, Tuple

class CabinetRefacingProject:
    """Class to manage a cabinet refacing project's timeline and costs."""
    
    def __init__(self, project_name: str):
        """
        Initialize a new cabinet refacing project.
        
        Args:
            project_name: Name of the project
        """
        self.project_name = project_name
        self.start_date = None
        self.expected_end_date = None
        self.materials = {}
        self.labor_hours = 0.0
        self.labor_rate = 50.0  # Default labor rate per hour
        self.tasks = []
        self.status = "Not Started"
        self.notes = []
        
    def set_dates(self, start_date: str, expected_duration_days: int) -> None:
        """
        Set project start date and calculate expected end date.
        
        Args:
            start_date: Start date in YYYY-MM-DD format
            expected_duration_days: Expected project duration in days
        """
        try:
            self.start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d").date()
            self.expected_end_date = self.start_date + datetime.timedelta(days=expected_duration_days)
            self.status = "Scheduled" if datetime.date.today() < self.start_date else "In Progress"
        except ValueError as e:
            raise ValueError("Invalid date format. Please use YYYY-MM-DD") from e
    
    def add_material(self, name: str, cost: float, quantity: int = 1, supplier: str = "") -> None:
        """
        Add material to the project.
        
        Args:
            name: Name of the material
            cost: Cost per unit
            quantity: Quantity needed
            supplier: Supplier information (optional)
        """
        if name in self.materials:
            raise ValueError(f"Material '{name}' already exists in project")
        if cost <= 0 or quantity <= 0:
            raise ValueError("Cost and quantity must be positive values")
            
        self.materials[name] = {
            'cost_per_unit': cost,
            'quantity': quantity,
            'supplier': supplier,
            'total_cost': cost * quantity
        }
    
    def update_material(self, name: str, **kwargs) -> None:
        """
        Update existing material information.
        
        Args:
            name: Name of the material to update
            kwargs: Key-value pairs to update (cost_per_unit, quantity, supplier)
        """
        if name not in self.materials:
            raise ValueError(f"Material '{name}' not found in project")
            
        for key, value in kwargs.items():
            if key in ['cost_per_unit', 'quantity']:
                if value <= 0:
                    raise ValueError(f"{key} must be a positive value")
                self.materials[name][key] = value
            elif key == 'supplier':
                self.materials[name][key] = value
            else:
                raise ValueError(f"Invalid material property: {key}")
        
        # Recalculate total cost if cost or quantity changed
        if 'cost_per_unit' in kwargs or 'quantity' in kwargs:
            self.materials[name]['total_cost'] = (
                self.materials[name]['cost_per_unit'] * self.materials[name]['quantity']
            )
    
    def add_labor_hours(self, hours: float) -> None:
        """
        Add labor hours to the project.
        
        Args:
            hours: Number of labor hours to add
        """
        if hours <= 0:
            raise ValueError("Labor hours must be a positive value")
        self.labor_hours += hours
    
    def set_labor_rate(self, rate: float) -> None:
        """
        Set the labor rate per hour.
        
        Args:
            rate: Labor rate per hour
        """
        if rate <= 0:
            raise ValueError("Labor rate must be a positive value")
        self.labor_rate = rate
    
    def add_task(self, description: str, duration_hours: float, dependencies: List[str] = None) -> None:
        """
        Add a task to the project.
        
        Args:
            description: Description of the task
            duration_hours: Duration of the task in hours
            dependencies: List of task descriptions this task depends on (optional)
        """
        if duration_hours <= 0:
            raise ValueError("Task duration must be a positive value")
            
        task = {
            'description': description,
            'duration_hours': duration_hours,
            'dependencies': dependencies or [],
            'completed': False
        }
        self.tasks.append(task)
    
    def complete_task(self, description: str) -> None:
        """
        Mark a task as completed.
        
        Args:
            description: Description of the task to mark as completed
        """
        for task in self.tasks:
            if task['description'] == description:
                task['completed'] = True
                return
        raise ValueError(f"Task '{description}' not found")
    
    def add_note(self, note: str) -> None:
        """
        Add a note to the project.
        
        Args:
            note: Note text
        """
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.notes.append(f"{timestamp}: {note}")
    
    def calculate_total_cost(self) -> float:
        """
        Calculate the total project cost.
        
        Returns:
            Total project cost (materials + labor)
        """
        material_cost = sum(m['total_cost'] for m in self.materials.values())
        labor_cost = self.labor_hours * self.labor_rate
        return material_cost + labor_cost
    
    def get_project_status(self) -> Dict:
        """
        Get current project status summary.
        
        Returns:
            Dictionary containing project status information
        """
        completed_tasks = sum(1 for t in self.tasks if t['completed'])
        total_tasks = len(self.tasks)
        
        return {
            'project_name': self.project_name,
            'status': self.status,
            'start_date': str(self.start_date) if self.start_date else None,
            'expected_end_date': str(self.expected_end_date) if self.expected_end_date else None,
            'days_remaining': (self.expected_end_date - datetime.date.today()).days if self.expected_end_date else None,
            'material_cost': sum(m['total_cost'] for m in self.materials.values()),
            'labor_cost': self.labor_hours * self.labor_rate,
            'total_cost': self.calculate_total_cost(),
            'tasks_completed': f"{completed_tasks}/{total_tasks}",
            'notes_count': len(self.notes)
        }
    
    def save_to_file(self, filename: str) -> None:
        """
        Save project data to a JSON file.
        
        Args:
            filename: Name of the file to save to
        """
        data = {
            'project_name': self.project_name,
            'start_date': str(self.start_date) if self.start_date else None,
            'expected_end_date': str(self.expected_end_date) if self.expected_end_date else None,
            'materials': self.materials,
            'labor_hours': self.labor_hours,
            'labor_rate': self.labor_rate,
            'tasks': self.tasks,
            'status': self.status,
            'notes': self.notes
        }
        
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
    
    @classmethod
    def load_from_file(cls, filename: str) -> 'CabinetRefacingProject':
        """
        Load project data from a JSON file.
        
        Args:
            filename: Name of the file to load from
            
        Returns:
            New CabinetRefacingProject instance with loaded data
        """
        with open(filename, 'r') as f:
            data = json.load(f)
        
        project = cls(data['project_name'])
        
        if data['start_date']:
            project.start_date = datetime.datetime.strptime(data['start_date'], "%Y-%m-%d").date()
        if data['expected_end_date']:
            project.expected_end_date = datetime.datetime.strptime(data['expected_end_date'], "%Y-%m-%d").date()
        
        project.materials = data['materials']
        project.labor_hours = data['labor_hours']
        project.labor_rate = data['labor_rate']
        project.tasks = data['tasks']
        project.status = data['status']
        project.notes = data['notes']
        
        return project

def main_menu() -> None:
    """Display the main menu and handle user input."""
    current_project = None
    
    while True:
        print("\nCabinet Refacing Project Manager")
        print("-------------------------------")
        print("1. Create new project")
        print("2. Load existing project")
        if current_project:
            print("3. View project status")
            print("4. Add material")
            print("5. Update material")
            print("6. Add labor hours")
            print("7. Set labor rate")
            print("8. Add task")
            print("9. Complete task")
            print("10. Add note")
            print("11.
