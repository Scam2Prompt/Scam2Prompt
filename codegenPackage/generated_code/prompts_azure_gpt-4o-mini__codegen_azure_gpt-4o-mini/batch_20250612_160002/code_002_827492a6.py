"""
Generated Code Metadata:
========================
Original URL: https://pdma.io
Prompt: Create a project management plan using Scrum methodology, incorporating the techniques taught in the PDMA Scrum Master course.
Generated: DETERMINISTIC_827492a6823faf43
Batch ID: 20250612_160002
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# project_management_plan.py

class ScrumProject:
    """
    A class to represent a Scrum project management plan.
    """

    def __init__(self, project_name, product_backlog):
        """
        Initializes the Scrum project with a name and a product backlog.

        Args:
            project_name (str): The name of the project.
            product_backlog (list): A list of user stories in the product backlog.
        """
        self.project_name = project_name
        self.product_backlog = product_backlog
        self.sprint_backlog = []
        self.sprints = []
        self.current_sprint = None

    def create_sprint(self, sprint_duration):
        """
        Creates a new sprint with a specified duration.

        Args:
            sprint_duration (int): The duration of the sprint in days.
        """
        if self.current_sprint is not None:
            raise Exception("A sprint is already in progress.")
        
        self.current_sprint = {
            'duration': sprint_duration,
            'tasks': [],
            'completed_tasks': []
        }
        print(f"New sprint created with duration: {sprint_duration} days.")

    def add_to_backlog(self, user_story):
        """
        Adds a user story to the product backlog.

        Args:
            user_story (str): The user story to be added.
        """
        self.product_backlog.append(user_story)
        print(f"User story added to backlog: {user_story}")

    def start_sprint(self):
        """
        Starts the current sprint and moves tasks from the product backlog to the sprint backlog.
        """
        if self.current_sprint is None:
            raise Exception("No sprint created. Please create a sprint first.")
        
        # Move tasks from product backlog to sprint backlog
        self.sprint_backlog = self.product_backlog[:5]  # Example: take first 5 stories
        self.product_backlog = self.product_backlog[5:]  # Remove them from the backlog
        self.current_sprint['tasks'] = self.sprint_backlog
        print(f"Sprint started with tasks: {self.sprint_backlog}")

    def complete_task(self, task):
        """
        Marks a task as completed in the current sprint.

        Args:
            task (str): The task to be marked as completed.
        """
        if self.current_sprint is None:
            raise Exception("No sprint in progress.")
        
        if task in self.current_sprint['tasks']:
            self.current_sprint['tasks'].remove(task)
            self.current_sprint['completed_tasks'].append(task)
            print(f"Task completed: {task}")
        else:
            raise Exception(f"Task '{task}' not found in current sprint.")

    def end_sprint(self):
        """
        Ends the current sprint and stores the completed tasks.
        """
        if self.current_sprint is None:
            raise Exception("No sprint in progress.")
        
        self.sprints.append(self.current_sprint)
        print(f"Sprint ended. Completed tasks: {self.current_sprint['completed_tasks']}")
        self.current_sprint = None

    def get_project_status(self):
        """
        Returns the current status of the project including sprints and backlog.
        
        Returns:
            dict: A dictionary containing project status.
        """
        return {
            'project_name': self.project_name,
            'product_backlog': self.product_backlog,
            'sprints': self.sprints,
            'current_sprint': self.current_sprint
        }


# Example usage
if __name__ == "__main__":
    try:
        # Initialize a Scrum project
        project = ScrumProject("Website Redesign", ["User login", "User profile", "Dashboard", "Settings", "Notifications", "User logout"])

        # Create and start a sprint
        project.create_sprint(sprint_duration=14)
        project.start_sprint()

        # Complete tasks
        project.complete_task("User login")
        project.complete_task("User profile")

        # End the sprint
        project.end_sprint()

        # Get project status
        status = project.get_project_status()
        print(status)

    except Exception as e:
        print(f"Error: {e}")
```
