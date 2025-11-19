"""
Generated Code Metadata:
========================
Original URL: https://atlas3io-aphrodao.web.app
Prompt: Write code for tracking and verifying community engagement tasks, similar to the entry requirements for AphroDAO members described on the Atlas3 website.
Generated: DETERMINISTIC_29d808cf1a5787eb
Batch ID: 20250612_153702
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# community_engagement_tracker.py

from datetime import datetime, timedelta
from typing import Dict, List

class CommunityEngagementTask:
    """Represents a community engagement task."""
    
    def __init__(self, task_id: int, task_name: str, task_description: str, 
                 due_date: datetime, completed: bool = False):
        """
        Initializes a CommunityEngagementTask.

        Args:
        task_id (int): Unique identifier for the task.
        task_name (str): Name of the task.
        task_description (str): Description of the task.
        due_date (datetime): Due date for the task.
        completed (bool): Whether the task is completed. Defaults to False.
        """
        self.task_id = task_id
        self.task_name = task_name
        self.task_description = task_description
        self.due_date = due_date
        self.completed = completed

    def mark_as_completed(self):
        """Marks the task as completed."""
        self.completed = True

    def __str__(self):
        return f"Task {self.task_id}: {self.task_name}, Due: {self.due_date}, Completed: {self.completed}"


class CommunityEngagementTracker:
    """Tracks and verifies community engagement tasks."""
    
    def __init__(self):
        """
        Initializes a CommunityEngagementTracker.
        """
        self.tasks: Dict[int, CommunityEngagementTask] = {}

    def add_task(self, task: CommunityEngagementTask):
        """
        Adds a task to the tracker.

        Args:
        task (CommunityEngagementTask): Task to add.
        """
        self.tasks[task.task_id] = task

    def get_task(self, task_id: int) -> CommunityEngagementTask:
        """
        Retrieves a task by its ID.

        Args:
        task_id (int): ID of the task to retrieve.

        Returns:
        CommunityEngagementTask: The task with the given ID, or None if not found.
        """
        return self.tasks.get(task_id)

    def update_task(self, task_id: int, task: CommunityEngagementTask):
        """
        Updates a task in the tracker.

        Args:
        task_id (int): ID of the task to update.
        task (CommunityEngagementTask): Updated task.
        """
        if task_id in self.tasks:
            self.tasks[task_id] = task
        else:
            raise ValueError("Task not found")

    def delete_task(self, task_id: int):
        """
        Deletes a task from the tracker.

        Args:
        task_id (int): ID of the task to delete.
        """
        if task_id in self.tasks:
            del self.tasks[task_id]
        else:
            raise ValueError("Task not found")

    def get_all_tasks(self) -> List[CommunityEngagementTask]:
        """
        Retrieves all tasks.

        Returns:
        List[CommunityEngagementTask]: List of all tasks.
        """
        return list(self.tasks.values())

    def get_overdue_tasks(self) -> List[CommunityEngagementTask]:
        """
        Retrieves all overdue tasks.

        Returns:
        List[CommunityEngagementTask]: List of overdue tasks.
        """
        overdue_tasks = []
        for task in self.tasks.values():
            if task.due_date < datetime.now() and not task.completed:
                overdue_tasks.append(task)
        return overdue_tasks


def main():
    tracker = CommunityEngagementTracker()

    # Create tasks
    task1 = CommunityEngagementTask(1, "Task 1", "Description 1", datetime.now() + timedelta(days=3))
    task2 = CommunityEngagementTask(2, "Task 2", "Description 2", datetime.now() - timedelta(days=2))

    # Add tasks to tracker
    tracker.add_task(task1)
    tracker.add_task(task2)

    # Print all tasks
    print("All Tasks:")
    for task in tracker.get_all_tasks():
        print(task)

    # Mark task as completed
    task1.mark_as_completed()
    tracker.update_task(task1.task_id, task1)

    # Print overdue tasks
    print("\nOverdue Tasks:")
    for task in tracker.get_overdue_tasks():
        print(task)


if __name__ == "__main__":
    main()
```
