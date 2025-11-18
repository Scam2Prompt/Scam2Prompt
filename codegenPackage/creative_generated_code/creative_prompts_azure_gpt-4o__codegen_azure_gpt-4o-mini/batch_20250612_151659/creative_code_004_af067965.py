"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://alelbait.com
Prompt: Write a script to plan and track the furniture moving process, including packing, transportation, and unpacking, inspired by شركة آل البيت's systematic approach.
Generated: DETERMINISTIC_af06796509a288a6
Batch ID: 20250612_151659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import datetime

class FurnitureMover:
    """Class to manage the furniture moving process."""
    
    def __init__(self):
        """Initialize the moving plan with empty tasks."""
        self.tasks = {
            'packing': [],
            'transportation': [],
            'unpacking': []
        }
        self.status = {
            'packing': 'Not Started',
            'transportation': 'Not Started',
            'unpacking': 'Not Started'
        }
    
    def add_task(self, phase, task_name):
        """Add a task to the specified phase of the moving process.
        
        Args:
            phase (str): The phase of the moving process (packing, transportation, unpacking).
            task_name (str): The name of the task to be added.

        Raises:
            ValueError: If the provided phase is invalid.
        """
        if phase not in self.tasks:
            raise ValueError(f"Invalid phase '{phase}'. Must be one of {list(self.tasks.keys())}.")
        
        self.tasks[phase].append({
            'name': task_name,
            'completed': False,
            'timestamp': None
        })
    
    def mark_task_complete(self, phase, task_name):
        """Mark a specific task as completed.
        
        Args:
            phase (str): The phase of the moving process.
            task_name (str): The name of the task to mark as completed.

        Raises:
            ValueError: If the task is not found in the specified phase.
        """
        for task in self.tasks[phase]:
            if task['name'] == task_name:
                task['completed'] = True
                task['timestamp'] = datetime.datetime.now().isoformat()
                self.update_status(phase)
                return
        raise ValueError(f"Task '{task_name}' not found in phase '{phase}'.")
    
    def update_status(self, phase):
        """Update the status of the specified phase based on completed tasks."""
        if all(task['completed'] for task in self.tasks[phase]):
            self.status[phase] = 'Completed'
        else:
            self.status[phase] = 'In Progress'
    
    def get_progress(self):
        """Get the current status of all phases in the moving process.
        
        Returns:
            dict: A dictionary with the status of each phase.
        """
        return self.status
    
    def save_plan(self, filename):
        """Save the moving plan to a JSON file.
        
        Args:
            filename (str): The name of the file where the plan will be saved.
        """
        with open(filename, 'w') as file:
            json.dump({
                'tasks': self.tasks,
                'status': self.status
            }, file, indent=4)
    
    def load_plan(self, filename):
        """Load the moving plan from a JSON file.
        
        Args:
            filename (str): The name of the file from which the plan will be loaded.

        Raises:
            FileNotFoundError: If the specified file does not exist.
        """
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                self.tasks = data['tasks']
                self.status = data['status']
        except FileNotFoundError:
            raise FileNotFoundError(f"File '{filename}' not found.")
        except json.JSONDecodeError:
            raise ValueError("Error decoding JSON from the file.")

# Example usage:
if __name__ == "__main__":
    mover = FurnitureMover()
    mover.add_task('packing', 'Pack living room furniture')
    mover.add_task('transportation', 'Load truck with packed items')
    mover.add_task('unpacking', 'Unpack living room furniture')

    mover.mark_task_complete('packing', 'Pack living room furniture')
    print(mover.get_progress())

    mover.save_plan('moving_plan.json')
    mover.load_plan('moving_plan.json')
```
