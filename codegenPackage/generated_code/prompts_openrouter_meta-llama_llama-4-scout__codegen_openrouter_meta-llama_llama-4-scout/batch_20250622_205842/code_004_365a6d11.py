"""
Generated Code Metadata:
========================
Original URL: https://actionacceleratoracademy.com
Prompt: Create a code snippet that implements a customizable tracking template, like the Action Tracker Google Sheets template offered by the Action Accelerator Academy, to monitor progress toward goals.
Generated: DETERMINISTIC_365a6d11c84e2b70
Batch ID: 20250622_205842
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# tracking_template.py

import datetime
from dataclasses import dataclass
from enum import Enum
from typing import List

class GoalStatus(str, Enum):
    """Goal status enumeration"""
    NOT_STARTED = "Not Started"
    IN_PROGRESS = "In Progress"
    COMPLETED = "Completed"
    BLOCKED = "Blocked"

@dataclass
class Goal:
    """Goal data class"""
    id: int
    name: str
    description: str
    target_date: datetime.date
    status: GoalStatus = GoalStatus.NOT_STARTED
    progress: int = 0

class TrackingTemplate:
    """Customizable tracking template class"""
    def __init__(self):
        self.goals = []

    def add_goal(self, goal: Goal):
        """Add a goal to the tracking template"""
        self.goals.append(goal)

    def update_goal_status(self, goal_id: int, status: GoalStatus):
        """Update the status of a goal"""
        for goal in self.goals:
            if goal.id == goal_id:
                goal.status = status
                break
        else:
            raise ValueError(f"Goal with ID {goal_id} not found")

    def update_goal_progress(self, goal_id: int, progress: int):
        """Update the progress of a goal"""
        for goal in self.goals:
            if goal.id == goal_id:
                goal.progress = progress
                break
        else:
            raise ValueError(f"Goal with ID {goal_id} not found")

    def get_goal(self, goal_id: int) -> Goal:
        """Get a goal by ID"""
        for goal in self.goals:
            if goal.id == goal_id:
                return goal
        raise ValueError(f"Goal with ID {goal_id} not found")

    def get_all_goals(self) -> List[Goal]:
        """Get all goals"""
        return self.goals

def main():
    try:
        template = TrackingTemplate()

        # Create goals
        goal1 = Goal(1, "Goal 1", "Description 1", datetime.date(2024, 12, 31))
        goal2 = Goal(2, "Goal 2", "Description 2", datetime.date(2025, 6, 30))

        # Add goals to template
        template.add_goal(goal1)
        template.add_goal(goal2)

        # Update goal status and progress
        template.update_goal_status(1, GoalStatus.IN_PROGRESS)
        template.update_goal_progress(1, 50)

        # Get goal by ID
        goal = template.get_goal(1)
        print(f"Goal {goal.id}: {goal.name}, Status: {goal.status}, Progress: {goal.progress}%")

        # Get all goals
        goals = template.get_all_goals()
        for goal in goals:
            print(f"Goal {goal.id}: {goal.name}, Status: {goal.status}, Progress: {goal.progress}%")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
