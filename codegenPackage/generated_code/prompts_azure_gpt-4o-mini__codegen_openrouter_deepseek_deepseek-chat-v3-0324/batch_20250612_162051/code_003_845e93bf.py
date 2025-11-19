"""
Generated Code Metadata:
========================
Original URL: https://vivekenterprises.co.in
Prompt: Generate a code example for a project management tool that tracks the progress of interior turnkey contracting tasks, including design and execution phases mentioned by Vivek Enterprises.
Generated: DETERMINISTIC_845e93bfe62b1c55
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Project Management Tool for Interior Turnkey Contracting Tasks

This module provides functionality to track the progress of interior turnkey contracting tasks,
including design and execution phases. It allows adding tasks, updating their status, and generating reports.

Author: Vivek Enterprises
"""

from datetime import datetime
from enum import Enum, auto
from typing import List, Dict, Optional


class TaskStatus(Enum):
    """Enum representing the status of a task."""
    NOT_STARTED = auto()
    IN_PROGRESS = auto()
    COMPLETED = auto()
    DELAYED = auto()


class TaskPhase(Enum):
    """Enum representing the phase of a task."""
    DESIGN = auto()
    EXECUTION = auto()


class Task:
    """Class representing a single task in the project."""

    def __init__(self, name: str, description: str, phase: TaskPhase, 
                 assigned_to: str, deadline: datetime):
        """
        Initialize a new task.
        
        Args:
            name: Name of the task
            description: Detailed description of the task
            phase: Design or Execution phase
            assigned_to: Person/team responsible
            deadline: Due date for the task
        """
        self.name = name
        self.description = description
        self.phase = phase
        self.assigned_to = assigned_to
        self.deadline = deadline
        self.status = TaskStatus.NOT_STARTED
        self.created_at = datetime.now()
        self.completed_at: Optional[datetime] = None
        self.comments: List[str] = []

    def update_status(self, new_status: TaskStatus) -> None:
        """
        Update the status of the task.
        
        Args:
            new_status: New status to set
        """
        self.status = new_status
        if new_status == TaskStatus.COMPLETED:
            self.completed_at = datetime.now()

    def add_comment(self, comment: str) -> None:
        """
        Add a comment to the task.
        
        Args:
            comment: Comment to add
        """
        self.comments.append(f"{datetime.now()}: {comment}")

    def __str__(self) -> str:
        """String representation of the task."""
        return (f"Task: {self.name} ({self.phase.name})\n"
                f"Status: {self.status.name}\n"
                f"Assigned to: {self.assigned_to}\n"
                f"Deadline: {self.deadline}\n"
                f"Description: {self.description}")


class Project:
    """Class representing a complete interior turnkey project."""

    def __init__(self, name: str, client: str, start_date: datetime):
        """
        Initialize a new project.
        
        Args:
            name: Name of the project
            client: Client name
            start_date: Project start date
        """
        self.name = name
        self.client = client
        self.start_date = start_date
        self.tasks: List[Task] = []
        self.completed = False

    def add_task(self, task: Task) -> None:
        """Add a new task to the project."""
        self.tasks.append(task)

    def complete_project(self) -> None:
        """Mark the project as completed."""
        if all(task.status == TaskStatus.COMPLETED for task in self.tasks):
            self.completed = True
        else:
            raise ValueError("Cannot complete project with unfinished tasks")

    def get_task_progress(self) -> Dict[TaskPhase, Dict[TaskStatus, int]]:
        """
        Get progress statistics by phase and status.
        
        Returns:
            Dictionary with counts of tasks by phase and status
        """
        progress = {
            phase: {status: 0 for status in TaskStatus}
            for phase in TaskPhase
        }

        for task in self.tasks:
            progress[task.phase][task.status] += 1

        return progress

    def generate_report(self) -> str:
        """Generate a comprehensive project report."""
        progress = self.get_task_progress()
        report = [
            f"Project: {self.name}",
            f"Client: {self.client}",
            f"Start Date: {self.start_date}",
            f"Status: {'COMPLETED' if self.completed else 'IN PROGRESS'}",
            "\nTask Progress:"
        ]

        for phase in TaskPhase:
            report.append(f"\n{phase.name} PHASE:")
            for status in TaskStatus:
                count = progress[phase][status]
                report.append(f"  {status.name}: {count} tasks")

        report.append("\nTask Details:")
        for task in self.tasks:
            report.append("\n" + str(task))
            if task.comments:
                report.append("  Comments:")
                for comment in task.comments:
                    report.append(f"    - {comment}")

        return "\n".join(report)


# Example usage
if __name__ == "__main__":
    # Create a new project
    project = Project(
        name="Luxury Villa Interior",
        client="Mr. Sharma",
        start_date=datetime(2023, 1, 1)
    )

    # Add design phase tasks
    design_task1 = Task(
        name="Concept Design",
        description="Create initial concept for living room",
        phase=TaskPhase.DESIGN,
        assigned_to="Design Team A",
        deadline=datetime(2023, 1, 15)
    )
    project.add_task(design_task1)

    design_task2 = Task(
        name="3D Modeling",
        description="Create 3D models for all rooms",
        phase=TaskPhase.DESIGN,
        assigned_to="Design Team B",
        deadline=datetime(2023, 1, 30)
    )
    project.add_task(design_task2)

    # Add execution phase tasks
    execution_task1 = Task(
        name="Material Procurement",
        description="Purchase all required materials",
        phase=TaskPhase.EXECUTION,
        assigned_to="Procurement Team",
        deadline=datetime(2023, 2, 15)
    )
    project.add_task(execution_task1)

    execution_task2 = Task(
        name="Living Room Construction",
        description="Complete construction of living room",
        phase=TaskPhase.EXECUTION,
        assigned_to="Construction Team A",
        deadline=datetime(2023, 3, 1)
    )
    project.add_task(execution_task2)

    # Update some task statuses
    design_task1.update_status(TaskStatus.COMPLETED)
    design_task1.add_comment("Client approved the initial concept")
    design_task2.update_status(TaskStatus.IN_PROGRESS)
    execution_task1.update_status(TaskStatus.NOT_STARTED)
    execution_task2.update_status(TaskStatus.NOT_STARTED)

    # Generate and print project report
    print(project.generate_report())
```
