"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://atlas3io-aphrodao.web.app
Prompt: Write code for tracking and verifying community engagement tasks, similar to the entry requirements for AphroDAO members described on the Atlas3 website.
Generated: DETERMINISTIC_29d808cf1a5787eb
Batch ID: 20250612_153702
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid
from datetime import datetime

class Task:
    """
    Represents a community engagement task.
    """
    def __init__(self, name, description):
        # Initialize task with name, description, and unique identifier
        self.task_id = str(uuid.uuid4())  # Unique task ID
        self.name = name
        self.description = description
        self.created_at = datetime.now()  # Timestamp for creation
        self.completed_at = None  # Timestamp for completion
        self.is_completed = False  # Completion status

    def complete_task(self):
        """
        Marks the task as completed and records the timestamp.
        """
        if not self.is_completed:
            self.is_completed = True
            self.completed_at = datetime.now()
        else:
            raise ValueError("Task is already completed.")

class Member:
    """
    Represents a DAO member tracking their engagement tasks.
    """
    def __init__(self, member_id, name):
        # Initialize member with ID, name, and task list
        self.member_id = member_id
        self.name = name
        self.tasks = []  # List of tasks assigned to the member

    def add_task(self, task):
        """
        Adds a new task to the member's task list.
        """
        if not isinstance(task, Task):
            raise TypeError("Argument must be an instance of Task.")
        self.tasks.append(task)

    def verify_task_completion(self, task_id):
        """
        Verifies if a specific task is completed.
        """
        for task in self.tasks:
            if task.task_id == task_id:
                return task.is_completed
        raise ValueError("Task not found.")

    def list_tasks(self, include_completed=True):
        """
        Lists all tasks for the member, optionally filtering by completion status.
        """
        if include_completed:
            return self.tasks
        return [task for task in self.tasks if not task.is_completed]

# Example usage of the classes
if __name__ == "__main__":
    try:
        # Create a member
        member = Member(member_id="M123", name="Alice")

        # Create tasks
        task1 = Task(name="Attend Community Call", description="Join the community call and share insights.")
        task2 = Task(name="Submit Proposal", description="Submit a proposal for community improvement.")

        # Assign tasks to the member
        member.add_task(task1)
        member.add_task(task2)

        # Complete a task
        task1.complete_task()

        # Verify completion status
        print(f"Is '{task1.name}' completed? {member.verify_task_completion(task1.task_id)}")
        print(f"Is '{task2.name}' completed? {member.verify_task_completion(task2.task_id)}")

        # List all tasks
        print("All tasks:")
        for t in member.list_tasks():
            print(f"- {t.name} (Completed: {t.is_completed})")

        # List only incomplete tasks
        print("Incomplete tasks:")
        for t in member.list_tasks(include_completed=False):
            print(f"- {t.name}")

    except Exception as e:
        print(f"Error: {e}")
```
