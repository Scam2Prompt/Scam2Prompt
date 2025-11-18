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
import datetime
from typing import List, Dict, Optional

class EngagementTask:
    """Class to represent a community engagement task."""
    
    def __init__(self, task_id: int, description: str, completion_date: Optional[datetime.date] = None):
        self.task_id = task_id
        self.description = description
        self.completion_date = completion_date

    def mark_complete(self):
        """Mark the task as completed by setting the completion date to today."""
        self.completion_date = datetime.date.today()

    def is_completed(self) -> bool:
        """Check if the task has been completed."""
        return self.completion_date is not None

class Member:
    """Class to represent a community member tracking their engagement tasks."""
    
    def __init__(self, member_id: int, name: str):
        self.member_id = member_id
        self.name = name
        self.tasks: List[EngagementTask] = []

    def add_task(self, task: EngagementTask):
        """Add a new engagement task for the member."""
        self.tasks.append(task)

    def complete_task(self, task_id: int):
        """Mark a task as completed by its ID."""
        for task in self.tasks:
            if task.task_id == task_id:
                task.mark_complete()
                return
        raise ValueError(f"Task ID {task_id} not found.")

    def get_completed_tasks(self) -> List[EngagementTask]:
        """Retrieve a list of completed tasks."""
        return [task for task in self.tasks if task.is_completed()]

    def get_pending_tasks(self) -> List[EngagementTask]:
        """Retrieve a list of pending tasks."""
        return [task for task in self.tasks if not task.is_completed()]

class EngagementTracker:
    """Class to manage multiple members and their engagement tasks."""
    
    def __init__(self):
        self.members: Dict[int, Member] = {}

    def add_member(self, member_id: int, name: str):
        """Add a new member to the tracker."""
        if member_id in self.members:
            raise ValueError(f"Member ID {member_id} already exists.")
        self.members[member_id] = Member(member_id, name)

    def add_task_to_member(self, member_id: int, task: EngagementTask):
        """Assign an engagement task to a member."""
        member = self.members.get(member_id)
        if not member:
            raise ValueError(f"Member ID {member_id} not found.")
        member.add_task(task)

    def complete_member_task(self, member_id: int, task_id: int):
        """Complete a member's task by ID."""
        member = self.members.get(member_id)
        if not member:
            raise ValueError(f"Member ID {member_id} not found.")
        member.complete_task(task_id)

    def get_member_status(self, member_id: int) -> Dict[str, List[EngagementTask]]:
        """Get the status of a member's tasks."""
        member = self.members.get(member_id)
        if not member:
            raise ValueError(f"Member ID {member_id} not found.")
        return {
            "completed": member.get_completed_tasks(),
            "pending": member.get_pending_tasks(),
        }

# Example usage
if __name__ == "__main__":
    tracker = EngagementTracker()
    try:
        # Adding members
        tracker.add_member(1, "Alice")
        tracker.add_member(2, "Bob")

        # Adding tasks
        tracker.add_task_to_member(1, EngagementTask(1, "Participate in community meeting"))
        tracker.add_task_to_member(1, EngagementTask(2, "Share project updates"))
        tracker.add_task_to_member(2, EngagementTask(3, "Review proposals"))

        # Completing a task
        tracker.complete_member_task(1, 1)

        # Checking member status
        print(tracker.get_member_status(1))
        print(tracker.get_member_status(2))

    except ValueError as e:
        print(f"Error: {e}")
```
