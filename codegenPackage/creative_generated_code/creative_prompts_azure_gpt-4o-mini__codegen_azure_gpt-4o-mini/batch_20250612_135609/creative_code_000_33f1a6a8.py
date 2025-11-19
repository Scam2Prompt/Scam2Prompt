"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://peacecitycontracting.com
Prompt: Generate a code snippet for a construction project management application that includes features for building construction, renovation works, and fit-out works.
Generated: DETERMINISTIC_33f1a6a8923932a9
Batch ID: 20250612_135609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# construction_project_management.py

class Project:
    """A class representing a construction project."""
    
    def __init__(self, name, project_type):
        """
        Initializes a new construction project.

        :param name: Name of the project
        :param project_type: Type of the project (building, renovation, fit-out)
        """
        self.name = name
        self.project_type = project_type
        self.tasks = []
        self.budget = 0.0

    def add_task(self, task):
        """
        Adds a task to the project.

        :param task: Task to be added
        """
        self.tasks.append(task)

    def set_budget(self, amount):
        """
        Sets the budget for the project.

        :param amount: Budget amount
        """
        if amount < 0:
            raise ValueError("Budget amount cannot be negative.")
        self.budget = amount

    def get_summary(self):
        """
        Retrieves a summary of the project including tasks and budget.

        :return: A dictionary summary of the project
        """
        return {
            'name': self.name,
            'project_type': self.project_type,
            'tasks': [task.get_details() for task in self.tasks],
            'budget': self.budget
        }


class Task:
    """A class representing a task within a construction project."""
    
    def __init__(self, title, description, status='Pending'):
        """
        Initializes a new task.

        :param title: Title of the task
        :param description: Description of the task
        :param status: Current status of the task (default is 'Pending')
        """
        self.title = title
        self.description = description
        self.status = status

    def update_status(self, new_status):
        """
        Updates the status of the task.

        :param new_status: New status of the task
        """
        valid_statuses = ['Pending', 'In Progress', 'Completed']
        if new_status not in valid_statuses:
            raise ValueError(f"Invalid status: {new_status}. Must be one of {valid_statuses}.")
        self.status = new_status

    def get_details(self):
        """
        Retrieves the details of the task.

        :return: A dictionary containing task details
        """
        return {
            'title': self.title,
            'description': self.description,
            'status': self.status
        }


def main():
    """Main function to demonstrate the project management system functionality."""
    try:
        # Create a new construction project
        project = Project(name="New Office Building", project_type="Building")
        
        # Set the project budget
        project.set_budget(1000000.00)  # Set budget to $1,000,000

        # Add tasks to the project
        task1 = Task("Foundation Work", "Excavate and pour foundation.")
        task2 = Task("Framing", "Build the frame of the building.")
        project.add_task(task1)
        project.add_task(task2)

        # Update task status
        task1.update_status("In Progress")

        # Get project summary
        summary = project.get_summary()
        print(summary)

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
