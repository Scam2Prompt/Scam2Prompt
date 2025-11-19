"""
Generated Code Metadata:
========================
Original URL: https://teamdga.com
Prompt: Design a mobile app feature that encourages athletes to set personal goals in both sports and life, reflecting the mentorship philosophy of Team DGA.
Generated: DETERMINISTIC_225cb3e80fd5403d
Batch ID: 20250612_162508
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import json
from datetime import datetime
from typing import List, Dict, Optional
from enum import Enum

# Define enums for goal categories and status
class GoalCategory(Enum):
    SPORTS = "Sports"
    LIFE = "Life"
    MENTAL_HEALTH = "Mental Health"
    EDUCATION = "Education"

class GoalStatus(Enum):
    NOT_STARTED = "Not Started"
    IN_PROGRESS = "In Progress"
    COMPLETED = "Completed"
    ABANDONED = "Abandoned"

# Define data models
class Goal:
    def __init__(
        self,
        title: str,
        description: str,
        category: GoalCategory,
        target_date: str,
        status: GoalStatus = GoalStatus.NOT_STARTED,
        milestones: Optional[List[Dict]] = None,
        notes: Optional[List[Dict]] = None
    ):
        self.title = title
        self.description = description
        self.category = category
        self.target_date = target_date
        self.status = status
        self.milestones = milestones if milestones else []
        self.notes = notes if notes else []
        self.created_at = datetime.now().isoformat()
        self.updated_at = datetime.now().isoformat()

    def to_dict(self) -> Dict:
        return {
            "title": self.title,
            "description": self.description,
            "category": self.category.value,
            "target_date": self.target_date,
            "status": self.status.value,
            "milestones": self.milestones,
            "notes": self.notes,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }

# Main app feature class
class GoalTracker:
    def __init__(self, user_id: str):
        self.user_id = user_id
        self.goals: List[Goal] = []
        self.load_goals()

    def add_goal(self, goal: Goal) -> bool:
        try:
            self.goals.append(goal)
            self.save_goals()
            return True
        except Exception as e:
            print(f"Error adding goal: {e}")
            return False

    def update_goal(self, goal_index: int, updated_goal: Goal) -> bool:
        try:
            if 0 <= goal_index < len(self.goals):
                self.goals[goal_index] = updated_goal
                updated_goal.updated_at = datetime.now().isoformat()
                self.save_goals()
                return True
            return False
        except Exception as e:
            print(f"Error updating goal: {e}")
            return False

    def delete_goal(self, goal_index: int) -> bool:
        try:
            if 0 <= goal_index < len(self.goals):
                del self.goals[goal_index]
                self.save_goals()
                return True
            return False
        except Exception as e:
            print(f"Error deleting goal: {e}")
            return False

    def add_milestone(self, goal_index: int, milestone: Dict) -> bool:
        try:
            if 0 <= goal_index < len(self.goals):
                self.goals[goal_index].milestones.append(milestone)
                self.goals[goal_index].updated_at = datetime.now().isoformat()
                self.save_goals()
                return True
            return False
        except Exception as e:
            print(f"Error adding milestone: {e}")
            return False

    def add_note(self, goal_index: int, note: Dict) -> bool:
        try:
            if 0 <= goal_index < len(self.goals):
                self.goals[goal_index].notes.append(note)
                self.goals[goal_index].updated_at = datetime.now().isoformat()
                self.save_goals()
                return True
            return False
        except Exception as e:
            print(f"Error adding note: {e}")
            return False

    def get_goals_by_category(self, category: GoalCategory) -> List[Goal]:
        return [goal for goal in self.goals if goal.category == category]

    def save_goals(self) -> bool:
        try:
            with open(f"{self.user_id}_goals.json", "w") as f:
                json.dump([goal.to_dict() for goal in self.goals], f)
            return True
        except Exception as e:
            print(f"Error saving goals: {e}")
            return False

    def load_goals(self) -> bool:
        try:
            with open(f"{self.user_id}_goals.json", "r") as f:
                data = json.load(f)
                self.goals = [
                    Goal(
                        title=item["title"],
                        description=item["description"],
                        category=GoalCategory(item["category"]),
                        target_date=item["target_date"],
                        status=GoalStatus(item["status"]),
                        milestones=item["milestones"],
                        notes=item["notes"]
                    ) for item in data
                ]
            return True
        except FileNotFoundError:
            return True  # No file yet is okay
        except Exception as e:
            print(f"Error loading goals: {e}")
            return False

# Example usage
if __name__ == "__main__":
    # Initialize goal tracker for a user
    tracker = GoalTracker("athlete123")

    # Create a new goal
    sports_goal = Goal(
        title="Improve Free Throw Percentage",
        description="Increase free throw percentage from 70% to 85%",
        category=GoalCategory.SPORTS,
        target_date="2023-12-31"
    )

    # Add the goal
    tracker.add_goal(sports_goal)

    # Add a life goal
    life_goal = Goal(
        title="Read More Books",
        description="Read 12 books this year",
        category=GoalCategory.LIFE,
        target_date="2023-12-31"
    )
    tracker.add_goal(life_goal)

    # Add a milestone to the sports goal
    tracker.add_milestone(0, {
        "title": "Reach 75%",
        "target_date": "2023-04-30",
        "completed": False
    })

    # Add a note to the life goal
    tracker.add_note(1, {
        "date": datetime.now().isoformat(),
        "content": "Finished 'Atomic Habits' today!"
    })

    # Update goal status
    sports_goal.status = GoalStatus.IN_PROGRESS
    tracker.update_goal(0, sports_goal)

    # Get goals by category
    sports_goals = tracker.get_goals_by_category(GoalCategory.SPORTS)
    print(f"Sports Goals: {[goal.title for goal in sports_goals]}")
```
