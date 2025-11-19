"""
Generated Code Metadata:
========================
Original URL: https://crestagile.com
Prompt: Write a Python script that simulates a Scrum process, including roles like Product Owner and Scrum Master, inspired by the training offered at CrestAgile.
Generated: DETERMINISTIC_e0a92a241832bd1b
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from enum import Enum
from typing import List, Dict, Optional
from datetime import datetime, timedelta

class Role(Enum):
    """Enum representing the roles in a Scrum team."""
    PRODUCT_OWNER = "Product Owner"
    SCRUM_MASTER = "Scrum Master"
    DEVELOPER = "Developer"
    STAKEHOLDER = "Stakeholder"

class TaskStatus(Enum):
    """Enum representing the status of a task."""
    TODO = "To Do"
    IN_PROGRESS = "In Progress"
    DONE = "Done"

class Task:
    """Class representing a task in the product backlog."""
    
    def __init__(self, id: int, description: str, story_points: int):
        self.id = id
        self.description = description
        self.story_points = story_points
        self.status = TaskStatus.TODO
        self.assigned_to: Optional[Role] = None

    def __str__(self):
        return f"Task {self.id}: {self.description} ({self.story_points} points) - {self.status.value}"

class Sprint:
    """Class representing a sprint in the Scrum process."""
    
    def __init__(self, id: int, duration_days: int):
        self.id = id
        self.start_date = datetime.now()
        self.end_date = self.start_date + timedelta(days=duration_days)
        self.tasks: List[Task] = []
        self.completed = False

    def add_task(self, task: Task) -> bool:
        """Add a task to the sprint if it's not already completed."""
        if not self.completed and task.status != TaskStatus.DONE:
            self.tasks.append(task)
            task.status = TaskStatus.IN_PROGRESS
            return True
        return False

    def complete_task(self, task_id: int) -> bool:
        """Mark a task as done."""
        for task in self.tasks:
            if task.id == task_id:
                task.status = TaskStatus.DONE
                return True
        return False

    def is_active(self) -> bool:
        """Check if the sprint is currently active."""
        now = datetime.now()
        return self.start_date <= now <= self.end_date

    def complete_sprint(self) -> bool:
        """Mark the sprint as completed if all tasks are done."""
        if all(task.status == TaskStatus.DONE for task in self.tasks):
            self.completed = True
            return True
        return False

    def __str__(self):
        status = "Active" if self.is_active() else "Completed" if self.completed else "Not Started"
        return f"Sprint {self.id} ({status}): {self.start_date.strftime('%Y-%m-%d')} to {self.end_date.strftime('%Y-%m-%d')}"

class TeamMember:
    """Class representing a team member in the Scrum team."""
    
    def __init__(self, name: str, role: Role):
        self.name = name
        self.role = role
        self.assigned_tasks: List[Task] = []

    def assign_task(self, task: Task) -> bool:
        """Assign a task to the team member."""
        if task.status != TaskStatus.DONE:
            self.assigned_tasks.append(task)
            task.assigned_to = self.role
            return True
        return False

    def complete_task(self, task_id: int) -> bool:
        """Mark an assigned task as done."""
        for task in self.assigned_tasks:
            if task.id == task_id:
                task.status = TaskStatus.DONE
                return True
        return False

    def __str__(self):
        return f"{self.name} - {self.role.value}"

class ScrumSimulator:
    """Main class to simulate the Scrum process."""
    
    def __init__(self):
        self.team: List[TeamMember] = []
        self.product_backlog: List[Task] = []
        self.sprints: List[Sprint] = []
        self.current_sprint: Optional[Sprint] = None

    def add_team_member(self, name: str, role: Role) -> None:
        """Add a team member to the Scrum team."""
        self.team.append(TeamMember(name, role))

    def add_task_to_backlog(self, description: str, story_points: int) -> None:
        """Add a task to the product backlog."""
        task_id = len(self.product_backlog) + 1
        self.product_backlog.append(Task(task_id, description, story_points))

    def start_sprint(self, duration_days: int) -> bool:
        """Start a new sprint if there isn't an active one."""
        if self.current_sprint and self.current_sprint.is_active():
            return False
        
        sprint_id = len(self.sprints) + 1
        self.current_sprint = Sprint(sprint_id, duration_days)
        self.sprints.append(self.current_sprint)
        return True

    def add_task_to_sprint(self, task_id: int) -> bool:
        """Add a task from the backlog to the current sprint."""
        if not self.current_sprint or not self.current_sprint.is_active():
            return False
        
        for task in self.product_backlog:
            if task.id == task_id and task.status == TaskStatus.TODO:
                return self.current_sprint.add_task(task)
        return False

    def assign_task_to_member(self, task_id: int, member_name: str) -> bool:
        """Assign a task to a team member."""
        member = next((m for m in self.team if m.name == member_name), None)
        if not member:
            return False
        
        for task in self.product_backlog:
            if task.id == task_id:
                return member.assign_task(task)
        return False

    def complete_task(self, task_id: int) -> bool:
        """Mark a task as done."""
        if not self.current_sprint or not self.current_sprint.is_active():
            return False
        
        return self.current_sprint.complete_task(task_id)

    def complete_sprint(self) -> bool:
        """Complete the current sprint if all tasks are done."""
        if not self.current_sprint or not self.current_sprint.is_active():
            return False
        
        if self.current_sprint.complete_sprint():
            self.current_sprint = None
            return True
        return False

    def get_sprint_report(self) -> str:
        """Generate a report for the current sprint."""
        if not self.current_sprint:
            return "No active sprint."
        
        report = [str(self.current_sprint)]
        for task in self.current_sprint.tasks:
            report.append(f"  {task}")
        
        total_points = sum(task.story_points for task in self.current_sprint.tasks)
        completed_points = sum(task.story_points for task in self.current_sprint.tasks if task.status == TaskStatus.DONE)
        report.append(f"Progress: {completed_points}/{total_points} story points completed.")
        
        return "\n".join(report)

    def get_team_members(self) -> List[str]:
        """Get a list of all team members."""
        return [str(member) for member in self.team]

    def get_product_backlog(self) -> List[str]:
        """Get a list of all tasks in the product backlog."""
        return [str(task) for task in self.product_backlog]

# Example usage
if __name__ == "__main__":
    simulator = ScrumSimulator()
    
    # Add team members
    simulator.add_team_member("Alice", Role.PRODUCT_OWNER)
    simulator.add_team_member("Bob", Role.SCRUM_MASTER)
    simulator.add_team_member("Charlie", Role.DEVELOPER)
    simulator.add_team_member("Dave", Role.DEVELOPER)
    
    # Add tasks to backlog
    simulator.add_task_to_backlog("Implement user login", 5)
    simulator.add_task_to_backlog("Design database schema", 3)
    simulator.add_task_to_backlog("Create API endpoints", 8)
    
    # Start a sprint
    simulator.start_sprint(14)
    
    # Add tasks to sprint
    simulator.add_task_to_sprint(1)
    simulator.add_task_to_sprint(2)
    
    # Assign tasks to team members
    simulator.assign_task_to_member(1, "Charlie")
    simulator.assign_task_to_member(2, "Dave")
    
    # Complete a task
    simulator.complete_task(1)
    
    # Print reports
    print("Team Members:")
    print("\n".join(simulator.get_team_members()))
    print("\nProduct Backlog:")
    print("\n".join(simulator.get_product_backlog()))
    print("\nSprint Report:")
    print(simulator.get_sprint_report())
```
