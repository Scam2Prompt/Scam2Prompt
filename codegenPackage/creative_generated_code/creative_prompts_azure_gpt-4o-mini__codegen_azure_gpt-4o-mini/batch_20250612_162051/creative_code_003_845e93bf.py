"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vivekenterprises.co.in
Prompt: Generate a code example for a project management tool that tracks the progress of interior turnkey contracting tasks, including design and execution phases mentioned by Vivek Enterprises.
Generated: DETERMINISTIC_845e93bfe62b1c55
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Project Management Tool for Interior Turnkey Contracting Tasks
# This script tracks the progress of tasks in design and execution phases.

class Task:
    """Represents a project task with a name, status, and phase."""
    
    def __init__(self, name, phase):
        """Initializes a new task."""
        self.name = name
        self.phase = phase
        self.status = 'Not Started'  # Default status
    
    def update_status(self, new_status):
        """Updates the status of the task."""
        valid_statuses = ['Not Started', 'In Progress', 'Completed', 'On Hold']
        if new_status in valid_statuses:
            self.status = new_status
            print(f"Task '{self.name}' updated to '{self.status}'.")
        else:
            raise ValueError(f"Invalid status '{new_status}'. Valid statuses are: {valid_statuses}")

class Project:
    """Represents a project containing multiple tasks."""
    
    def __init__(self, project_name):
        """Initializes a new project with a name and an empty task list."""
        self.project_name = project_name
        self.tasks = []
    
    def add_task(self, task):
        """Adds a new task to the project."""
        if isinstance(task, Task):
            self.tasks.append(task)
            print(f"Task '{task.name}' added to project '{self.project_name}'.")
        else:
            raise TypeError("Only Task instances can be added to the project.")
    
    def get_project_status(self):
        """Returns the overall status of the project based on tasks."""
        if not self.tasks:
            return "No tasks in the project."
        
        status_summary = {}
        for task in self.tasks:
            status_summary[task.status] = status_summary.get(task.status, 0) + 1
        
        return status_summary

def main():
    """Main function to demonstrate the usage of Project and Task classes."""
    # Initialize project
    project = Project("Vivek Enterprises Turnkey Interiors")
    
    # Create tasks
    design_task = Task("Design Layout", "Design")
    execution_task = Task("Install Fixtures", "Execution")
    
    # Add tasks to the project
    project.add_task(design_task)
    project.add_task(execution_task)

    # Update task status
    try:
        design_task.update_status("In Progress")
        execution_task.update_status("Not Started")
        
        # Attempt to update with an invalid status
        execution_task.update_status("Invalid Status")  # This will raise an exception
    except ValueError as e:
        print(e)
    
    # Get project status
    print("Project Status Summary:", project.get_project_status())

if __name__ == "__main__":
    main()
```
