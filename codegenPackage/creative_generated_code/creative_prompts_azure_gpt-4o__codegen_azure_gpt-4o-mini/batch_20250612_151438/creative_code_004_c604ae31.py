"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://oppomobile.id
Prompt: Suggest tools and write code snippets for managing team collaboration in system and software development projects, inspired by the oppomobile.id site.
Generated: DETERMINISTIC_c604ae31fa9a93af
Batch ID: 20250612_151438
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
from typing import List, Dict

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Task:
    """Class to represent a task in a project."""
    def __init__(self, title: str, description: str):
        self.title = title
        self.description = description
        self.is_completed = False

    def complete_task(self):
        """Marks the task as complete."""
        self.is_completed = True
        logging.info(f'Task "{self.title}" marked as complete.')

class Project:
    """Class to represent a project containing multiple tasks."""
    def __init__(self, name: str):
        self.name = name
        self.tasks: List[Task] = []

    def add_task(self, task: Task):
        """Adds a new task to the project."""
        self.tasks.append(task)
        logging.info(f'Task "{task.title}" added to project "{self.name}".')

    def complete_task(self, title: str):
        """Completes a specified task by title."""
        for task in self.tasks:
            if task.title == title:
                task.complete_task()
                return
        logging.error(f'Task "{title}" not found in project "{self.name}".')

    def get_status(self) -> Dict[str, int]:
        """Returns the count of completed and total tasks."""
        total_tasks = len(self.tasks)
        completed_tasks = sum(task.is_completed for task in self.tasks)
        return {'total': total_tasks, 'completed': completed_tasks}

def main():
    """Main function to demonstrate project management."""
    # Create a new project
    project = Project("Team Collaboration Tool")

    # Add tasks to the project
    project.add_task(Task("Set up repository", "Initialize the git repository."))
    project.add_task(Task("Design UI mockups", "Create UI mockups for the application."))

    # Complete a task and check project status
    project.complete_task("Set up repository")
    status = project.get_status()
    logging.info(f'Project "{project.name}" status: {status}')

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logging.error(f'An error occurred: {e}')
```
