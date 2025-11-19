"""
Generated Code Metadata:
========================
Original URL: https://sunsystems.hk
Prompt: Design a customized implementation plan for Infor SunSystems in a small business setting in Hong Kong.
Generated: DETERMINISTIC_8ebb560215ddcc10
Batch ID: 20250622_211520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import json
from datetime import datetime
from typing import Dict, List, Optional

class SunSystemsImplementationPlan:
    """
    A class to manage the implementation plan for Infor SunSystems in a small business setting in Hong Kong.
    This includes project phases, tasks, timelines, and resource allocation.
    """

    def __init__(self, business_name: str, start_date: str):
        """
        Initialize the implementation plan with business details and start date.
        
        Args:
            business_name (str): Name of the business implementing SunSystems.
            start_date (str): Project start date in 'YYYY-MM-DD' format.
        """
        self.business_name = business_name
        self.start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
        self.phases: List[Dict] = []
        self.resources: List[Dict] = []

    def add_phase(self, name: str, description: str, duration_days: int) -> None:
        """
        Add a phase to the implementation plan.
        
        Args:
            name (str): Name of the phase (e.g., 'Planning', 'Configuration').
            description (str): Description of the phase.
            duration_days (int): Duration of the phase in days.
        """
        self.phases.append({
            'name': name,
            'description': description,
            'duration_days': duration_days,
            'tasks': []
        })

    def add_task(self, phase_name: str, task_name: str, task_description: str, assigned_to: str) -> None:
        """
        Add a task to a specific phase.
        
        Args:
            phase_name (str): Name of the phase to which the task belongs.
            task_name (str): Name of the task.
            task_description (str): Description of the task.
            assigned_to (str): Resource assigned to the task.
        
        Raises:
            ValueError: If the specified phase does not exist.
        """
        phase = next((p for p in self.phases if p['name'] == phase_name), None)
        if not phase:
            raise ValueError(f"Phase '{phase_name}' not found.")
        
        phase['tasks'].append({
            'task_name': task_name,
            'task_description': task_description,
            'assigned_to': assigned_to,
            'status': 'Not Started'
        })

    def add_resource(self, name: str, role: str, contact: str) -> None:
        """
        Add a resource (team member) to the implementation plan.
        
        Args:
            name (str): Name of the resource.
            role (str): Role of the resource (e.g., 'Consultant', 'Developer').
            contact (str): Contact information of the resource.
        """
        self.resources.append({
            'name': name,
            'role': role,
            'contact': contact
        })

    def generate_timeline(self) -> Dict:
        """
        Generate a timeline with start and end dates for each phase.
        
        Returns:
            Dict: A dictionary containing the timeline for each phase.
        """
        timeline = {}
        current_date = self.start_date
        
        for phase in self.phases:
            end_date = current_date + datetime.timedelta(days=phase['duration_days'])
            timeline[phase['name']] = {
                'start_date': current_date.strftime('%Y-%m-%d'),
                'end_date': end_date.strftime('%Y-%m-%d'),
                'tasks': phase['tasks']
            }
            current_date = end_date + datetime.timedelta(days=1)  # Start next phase the day after
        
        return timeline

    def save_plan_to_file(self, filename: str) -> None:
        """
        Save the implementation plan to a JSON file.
        
        Args:
            filename (str): Name of the file to save the plan.
        """
        plan_data = {
            'business_name': self.business_name,
            'start_date': self.start_date.strftime('%Y-%m-%d'),
            'phases': self.phases,
            'resources': self.resources
        }
        
        with open(filename, 'w') as f:
            json.dump(plan_data, f, indent=4)

    @classmethod
    def load_plan_from_file(cls, filename: str) -> 'SunSystemsImplementationPlan':
        """
        Load an implementation plan from a JSON file.
        
        Args:
            filename (str): Name of the file to load the plan from.
        
        Returns:
            SunSystemsImplementationPlan: An instance of the class with the loaded plan.
        
        Raises:
            FileNotFoundError: If the specified file does not exist.
            ValueError: If the file content is not valid JSON or missing required fields.
        """
        try:
            with open(filename, 'r') as f:
                plan_data = json.load(f)
            
            plan = cls(plan_data['business_name'], plan_data['start_date'])
            plan.phases = plan_data.get('phases', [])
            plan.resources = plan_data.get('resources', [])
            
            return plan
        except FileNotFoundError:
            raise FileNotFoundError(f"File '{filename}' not found.")
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON file.")
        except KeyError as e:
            raise ValueError(f"Missing required field: {e}")

# Example usage
if __name__ == "__main__":
    try:
        # Create a new implementation plan
        plan = SunSystemsImplementationPlan("ABC Trading Co.", "2023-11-01")
        
        # Add phases
        plan.add_phase("Planning", "Initial planning and requirements gathering", 10)
        plan.add_phase("Configuration", "System configuration and setup", 15)
        plan.add_phase("Testing", "System testing and validation", 10)
        plan.add_phase("Deployment", "Go-live and post-deployment support", 5)
        
        # Add resources
        plan.add_resource("John Lee", "Project Manager", "john.lee@example.com")
        plan.add_resource("Mary Wong", "SunSystems Consultant", "mary.wong@example.com")
        plan.add_resource("David Chan", "IT Support", "david.chan@example.com")
        
        # Add tasks
        plan.add_task("Planning", "Gather business requirements", "Document all business processes", "John Lee")
        plan.add_task("Configuration", "Set up chart of accounts", "Configure COA based on HK accounting standards", "Mary Wong")
        plan.add_task("Testing", "Test general ledger", "Validate GL entries and reports", "Mary Wong")
        plan.add_task("Deployment", "Go-live support", "Provide on-site support during go-live", "David Chan")
        
        # Generate and print timeline
        timeline = plan.generate_timeline()
        print(json.dumps(timeline, indent=4))
        
        # Save plan to file
        plan.save_plan_to_file("sun_systems_implementation_plan.json")
        
    except Exception as e:
        print(f"Error: {e}")
```
