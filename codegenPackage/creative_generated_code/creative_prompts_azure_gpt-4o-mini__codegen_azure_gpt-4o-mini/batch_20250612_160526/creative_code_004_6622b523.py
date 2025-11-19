"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tekrollindustrial.com.br
Prompt: Illustrate how to implement a project management tool for industrial construction projects, inspired by Tekroll Industrial's project execution strategies.
Generated: DETERMINISTIC_6622b52377aa56ce
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

class Project:
    """
    A class to represent a construction project.

    Attributes:
    ----------
    name : str
        Name of the project.
    start_date : str
        Start date of the project in YYYY-MM-DD format.
    end_date : str
        End date of the project in YYYY-MM-DD format.
    budget : float
        Budget allocated for the project.
    status : str
        Current status of the project (e.g., 'Not Started', 'In Progress', 'Completed').
    tasks : list
        List of tasks associated with the project.
    """

    def __init__(self, name, start_date, end_date, budget):
        """
        Initializes the Project with the given attributes.

        Parameters:
        ----------
        name : str
            Name of the project.
        start_date : str
            Start date of the project.
        end_date : str
            End date of the project.
        budget : float
            Budget allocated for the project.
        """
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.budget = budget
        self.status = "Not Started"
        self.tasks = []

    def add_task(self, task):
        """
        Adds a task to the project.

        Parameters:
        ----------
        task : Task
            Task object to be added to the project.
        """
        self.tasks.append(task)

    def update_status(self, new_status):
        """
        Updates the status of the project.

        Parameters:
        ----------
        new_status : str
            New status for the project.
        """
        valid_statuses = ['Not Started', 'In Progress', 'Completed']
        if new_status in valid_statuses:
            self.status = new_status
        else:
            raise ValueError(f"Invalid status: {new_status}. Valid options are {valid_statuses}.")

    def __str__(self):
        return f"Project({self.name}, Status: {self.status})"


class Task:
    """
    A class to represent a task within a project.

    Attributes:
    ----------
    title : str
        Title of the task.
    description : str
        Detailed description of the task.
    assigned_to : str
        Name of the person assigned to the task.
    due_date : str
        Due date for the task in YYYY-MM-DD format.
    status : str
        Current status of the task.
    """

    def __init__(self, title, description, assigned_to, due_date):
        """
        Initializes the Task with the given attributes.

        Parameters:
        ----------
        title : str
            Title of the task.
        description : str
            Detailed description of the task.
        assigned_to : str
            Name of the person assigned to the task.
        due_date : str
            Due date for the task.
        """
        self.title = title
        self.description = description
        self.assigned_to = assigned_to
        self.due_date = due_date
        self.status = "Not Started"

    def update_status(self, new_status):
        """
        Updates the status of the task.

        Parameters:
        ----------
        new_status : str
            New status for the task.
        """
        valid_statuses = ['Not Started', 'In Progress', 'Completed']
        if new_status in valid_statuses:
            self.status = new_status
        else:
            raise ValueError(f"Invalid status: {new_status}. Valid options are {valid_statuses}.")

    def __str__(self):
        return f"Task({self.title}, Assigned to: {self.assigned_to}, Status: {self.status})"


def main():
    """
    Main function to illustrate the functionality of the project management tool.
    """
    try:
        # Create a new project
        project = Project("Industrial Construction Project", "2023-10-01", "2024-10-01", 500000)

        # Create tasks
        task1 = Task("Site Preparation", "Prepare the site for construction.", "Alice", "2023-11-01")
        task2 = Task("Foundation Work", "Lay the foundation of the building.", "Bob", "2023-12-15")

        # Add tasks to the project
        project.add_task(task1)
        project.add_task(task2)

        # Update project status
        project.update_status("In Progress")

        # Print project and tasks details
        print(project)
        for task in project.tasks:
            print(task)

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
