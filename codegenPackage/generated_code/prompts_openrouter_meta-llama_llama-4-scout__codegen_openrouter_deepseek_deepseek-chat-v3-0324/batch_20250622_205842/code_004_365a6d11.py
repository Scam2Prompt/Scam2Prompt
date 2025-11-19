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
import datetime
from dataclasses import dataclass
from typing import List, Optional, Dict
import csv
import os

@dataclass
class Goal:
    name: str
    target: float
    current: float = 0.0
    unit: str = ""
    created_at: datetime.date = datetime.date.today()
    deadline: Optional[datetime.date] = None
    completed: bool = False

class GoalTracker:
    def __init__(self, storage_file: str = "goals.csv"):
        self.storage_file = storage_file
        self.goals: List[Goal] = []
        self._load_goals()

    def _load_goals(self):
        """Load goals from storage file if it exists."""
        if not os.path.exists(self.storage_file):
            return

        with open(self.storage_file, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    goal = Goal(
                        name=row['name'],
                        target=float(row['target']),
                        current=float(row['current']),
                        unit=row['unit'],
                        created_at=datetime.date.fromisoformat(row['created_at']),
                        deadline=datetime.date.fromisoformat(row['deadline']) if row['deadline'] else None,
                        completed=row['completed'].lower() == 'true'
                    )
                    self.goals.append(goal)
                except (ValueError, KeyError) as e:
                    print(f"Error loading goal: {e}")

    def _save_goals(self):
        """Save goals to storage file."""
        fieldnames = ['name', 'target', 'current', 'unit', 'created_at', 'deadline', 'completed']
        with open(self.storage_file, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for goal in self.goals:
                writer.writerow({
                    'name': goal.name,
                    'target': goal.target,
                    'current': goal.current,
                    'unit': goal.unit,
                    'created_at': goal.created_at.isoformat(),
                    'deadline': goal.deadline.isoformat() if goal.deadline else "",
                    'completed': str(goal.completed)
                })

    def add_goal(self, name: str, target: float, unit: str = "", deadline: Optional[datetime.date] = None):
        """Add a new goal to track."""
        if any(g.name == name for g in self.goals):
            raise ValueError(f"Goal with name '{name}' already exists")
        
        goal = Goal(
            name=name,
            target=target,
            unit=unit,
            deadline=deadline
        )
        self.goals.append(goal)
        self._save_goals()

    def update_progress(self, name: str, progress: float):
        """Update progress for a specific goal."""
        for goal in self.goals:
            if goal.name == name:
                goal.current = progress
                if goal.current >= goal.target:
                    goal.completed = True
                self._save_goals()
                return
        raise ValueError(f"Goal '{name}' not found")

    def get_progress_report(self) -> Dict[str, float]:
        """Return progress percentage for all goals."""
        return {
            goal.name: (goal.current / goal.target) * 100 if goal.target != 0 else 0
            for goal in self.goals
        }

    def get_goal(self, name: str) -> Goal:
        """Get a goal by name."""
        for goal in self.goals:
            if goal.name == name:
                return goal
        raise ValueError(f"Goal '{name}' not found")

    def delete_goal(self, name: str):
        """Delete a goal by name."""
        self.goals = [goal for goal in self.goals if goal.name != name]
        self._save_goals()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._save_goals()
```
