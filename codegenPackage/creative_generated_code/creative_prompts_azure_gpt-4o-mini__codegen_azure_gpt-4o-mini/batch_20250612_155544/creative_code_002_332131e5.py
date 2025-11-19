"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://haseebbaig.me
Prompt: Create a project management strategy for a web development project using Agile methodologies, inspired by the project management expertise highlighted by Enorness.
Generated: DETERMINISTIC_332131e5728b43da
Batch ID: 20250612_155544
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# project_management.py

class AgileProjectManager:
    """
    A class to manage a web development project using Agile methodologies.
    """

    def __init__(self, project_name, team_members):
        """
        Initializes the AgileProjectManager.

        :param project_name: Name of the project
        :param team_members: List of team members involved in the project
        """
        self.project_name = project_name
        self.team_members = team_members
        self.sprints = []
        self.backlog = []
        self.completed_tasks = []

    def add_backlog_item(self, item):
        """
        Adds an item to the project backlog.

        :param item: A dictionary containing details of the backlog item
        :raises ValueError: If the item is not a dictionary
        """
        if not isinstance(item, dict):
            raise ValueError("Backlog item must be a dictionary")
        self.backlog.append(item)

    def create_sprint(self, sprint_name, duration):
        """
        Creates a new sprint.

        :param sprint_name: Name of the sprint
        :param duration: Duration of the sprint in days
        """
        sprint = {
            'name': sprint_name,
            'duration': duration,
            'tasks': [],
            'completed': False
        }
        self.sprints.append(sprint)

    def add_task_to_sprint(self, sprint_name, task):
        """
        Adds a task to a specified sprint.

        :param sprint_name: Name of the sprint to which the task is added
        :param task: A dictionary containing details of the task
        :raises ValueError: If the task is not a dictionary or sprint not found
        """
        if not isinstance(task, dict):
            raise ValueError("Task must be a dictionary")
        
        sprint = self._find_sprint(sprint_name)
        if sprint is None:
            raise ValueError(f"Sprint '{sprint_name}' not found")
        
        sprint['tasks'].append(task)

    def complete_task(self, sprint_name, task_name):
        """
        Marks a task as completed in a specified sprint.

        :param sprint_name: Name of the sprint containing the task
        :param task_name: Name of the task to mark as completed
        :raises ValueError: If the task or sprint is not found
        """
        sprint = self._find_sprint(sprint_name)
        if sprint is None:
            raise ValueError(f"Sprint '{sprint_name}' not found")
        
        task = self._find_task(sprint, task_name)
        if task is None:
            raise ValueError(f"Task '{task_name}' not found in sprint '{sprint_name}'")

        sprint['tasks'].remove(task)
        self.completed_tasks.append(task)

    def _find_sprint(self, sprint_name):
        """
        Finds a sprint by its name.

        :param sprint_name: Name of the sprint to find
        :return: Sprint dictionary or None if not found
        """
        for sprint in self.sprints:
            if sprint['name'] == sprint_name:
                return sprint
        return None

    def _find_task(self, sprint, task_name):
        """
        Finds a task in a given sprint.

        :param sprint: Sprint dictionary to search within
        :param task_name: Name of the task to find
        :return: Task dictionary or None if not found
        """
        for task in sprint['tasks']:
            if task['name'] == task_name:
                return task
        return None

    def display_project_status(self):
        """
        Displays the current status of the project, including sprints and backlog items.
        """
        print(f"Project: {self.project_name}")
        print("Backlog:")
        for item in self.backlog:
            print(f" - {item['name']} (Priority: {item['priority']})")

        print("\nSprints:")
        for sprint in self.sprints:
            print(f" - Sprint: {sprint['name']} (Duration: {sprint['duration']} days, Completed: {sprint['completed']})")
            for task in sprint['tasks']:
                print(f"   - Task: {task['name']} (Status: {task.get('status', 'Not started')})")

        print("\nCompleted Tasks:")
        for task in self.completed_tasks:
            print(f" - {task['name']}")


# Example usage
if __name__ == "__main__":
    try:
        project_manager = AgileProjectManager("Web Development Project", ["Alice", "Bob", "Charlie"])

        # Adding backlog items
        project_manager.add_backlog_item({"name": "Design UI", "priority": "High"})
        project_manager.add_backlog_item({"name": "Set up Database", "priority": "Medium"})

        # Creating a sprint
        project_manager.create_sprint("Sprint 1", 14)

        # Adding tasks to the sprint
        project_manager.add_task_to_sprint("Sprint 1", {"name": "Create Landing Page", "status": "In Progress"})
        project_manager.add_task_to_sprint("Sprint 1", {"name": "API Development", "status": "Not started"})

        # Completing a task
        project_manager.complete_task("Sprint 1", "Create Landing Page")

        # Displaying project status
        project_manager.display_project_status()

    except Exception as e:
        print(f"An error occurred: {e}")
```
