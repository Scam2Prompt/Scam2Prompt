"""
Generated Code Metadata:
========================
Original URL: https://pumaipce.com
Prompt: "Generate a project plan for the construction of an industrial plant, including tasks for procurement, construction, and specialized services like fiscalization and consultancy."
Generated: DETERMINISTIC_df0901be90a24cda
Batch ID: 20250622_205306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Industrial Plant Construction Project Plan Generator

This script generates a structured project plan for constructing an industrial plant,
including procurement, construction, and specialized services tasks.
"""

from datetime import datetime, timedelta
import json
from typing import List, Dict, Optional

class ProjectPlanGenerator:
    """
    Generates a comprehensive project plan for industrial plant construction.
    """
    
    def __init__(self, project_name: str, start_date: str, duration_days: int):
        """
        Initialize the project plan generator.
        
        Args:
            project_name: Name of the industrial plant project
            start_date: Project start date (YYYY-MM-DD)
            duration_days: Total project duration in days
        """
        self.project_name = project_name
        self.start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
        self.duration_days = duration_days
        self.tasks = []
        
    def add_task(self, 
                 name: str, 
                 duration: int, 
                 dependencies: Optional[List[int]] = None,
                 task_type: str = "construction",
                 resources: Optional[List[str]] = None):
        """
        Add a task to the project plan.
        
        Args:
            name: Task name/description
            duration: Duration in days
            dependencies: List of task IDs this task depends on
            task_type: Type of task (procurement|construction|specialized)
            resources: List of required resources
        """
        task_id = len(self.tasks) + 1
        task = {
            "id": task_id,
            "name": name,
            "duration": duration,
            "type": task_type,
            "dependencies": dependencies or [],
            "resources": resources or []
        }
        self.tasks.append(task)
        
    def generate_default_plan(self):
        """Generate a default project plan with common tasks."""
        # Procurement tasks
        self.add_task(
            "Site survey and land acquisition",
            30,
            task_type="procurement",
            resources=["Survey team", "Legal team"]
        )
        self.add_task(
            "Raw material procurement",
            45,
            task_type="procurement",
            resources=["Procurement team", "Suppliers"]
        )
        self.add_task(
            "Equipment procurement",
            60,
            task_type="procurement",
            resources=["Procurement team", "Manufacturers"]
        )
        
        # Construction tasks
        self.add_task(
            "Site preparation and foundation",
            60,
            dependencies=[1],
            task_type="construction",
            resources=["Construction crew", "Heavy equipment"]
        )
        self.add_task(
            "Structural construction",
            90,
            dependencies=[4],
            task_type="construction",
            resources=["Construction crew", "Engineers"]
        )
        self.add_task(
            "Mechanical installation",
            60,
            dependencies=[3, 5],
            task_type="construction",
            resources=["Mechanical team", "Equipment"]
        )
        
        # Specialized services
        self.add_task(
            "Environmental compliance consultancy",
            30,
            dependencies=[1],
            task_type="specialized",
            resources=["Environmental consultants"]
        )
        self.add_task(
            "Fiscalization services",
            45,
            dependencies=[6],
            task_type="specialized",
            resources=["Tax consultants", "Legal team"]
        )
        self.add_task(
            "Safety certification",
            15,
            dependencies=[6],
            task_type="specialized",
            resources=["Safety inspectors"]
        )
        
    def calculate_schedule(self) -> List[Dict]:
        """
        Calculate start and end dates for each task based on dependencies.
        
        Returns:
            List of tasks with calculated dates
        """
        scheduled_tasks = []
        
        for task in self.tasks:
            if not task["dependencies"]:
                start_date = self.start_date
            else:
                # Find the latest end date among dependencies
                dep_end_dates = [
                    t["end_date"] for t in scheduled_tasks 
                    if t["id"] in task["dependencies"]
                ]
                start_date = max(dep_end_dates) + timedelta(days=1)
                
            end_date = start_date + timedelta(days=task["duration"] - 1)
            
            scheduled_task = task.copy()
            scheduled_task["start_date"] = start_date.strftime("%Y-%m-%d")
            scheduled_task["end_date"] = end_date.strftime("%Y-%m-%d")
            scheduled_tasks.append(scheduled_task)
            
        return scheduled_tasks
    
    def generate_gantt_data(self) -> Dict:
        """
        Generate data for Gantt chart visualization.
        
        Returns:
            Dictionary containing project information and task data
        """
        scheduled_tasks = self.calculate_schedule()
        
        return {
            "project_name": self.project_name,
            "start_date": self.start_date.strftime("%Y-%m-%d"),
            "duration_days": self.duration_days,
            "tasks": scheduled_tasks
        }
    
    def save_to_json(self, filename: str):
        """
        Save the project plan to a JSON file.
        
        Args:
            filename: Output file path
        """
        data = self.generate_gantt_data()
        
        try:
            with open(filename, 'w') as f:
                json.dump(data, f, indent=2)
        except IOError as e:
            print(f"Error saving file: {e}")
            
    def print_summary(self):
        """Print a summary of the project plan."""
        scheduled_tasks = self.calculate_schedule()
        
        print(f"\nProject: {self.project_name}")
        print(f"Start Date: {self.start_date}")
        print(f"Duration: {self.duration_days} days\n")
        
        print("Tasks:")
        print("{:<5} {:<40} {:<15} {:<12} {:<12} {:<15}".format(
            "ID", "Task", "Type", "Start", "End", "Duration"
        ))
        
        for task in scheduled_tasks:
            print("{:<5} {:<40} {:<15} {:<12} {:<12} {:<15}".format(
                task["id"],
                task["name"],
                task["type"],
                task["start_date"],
                task["end_date"],
                f"{task['duration']} days"
            ))


# Example usage
if __name__ == "__main__":
    try:
        # Initialize project
        project = ProjectPlanGenerator(
            project_name="Greenfield Chemical Plant",
            start_date="2024-01-15",
            duration_days=365
        )
        
        # Add tasks
        project.generate_default_plan()
        
        # Print summary
        project.print_summary()
        
        # Save to file
        project.save_to_json("chemical_plant_project_plan.json")
        print("\nProject plan saved to chemical_plant_project_plan.json")
        
    except Exception as e:
        print(f"Error generating project plan: {e}")
```
